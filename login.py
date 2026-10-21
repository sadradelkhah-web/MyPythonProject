import sys
import hashlib
import hmac
import os
from datetime import date

from PySide6.QtCore import QDateTime, QSettings, QTimer, Qt
from PySide6.QtGui import QAction, QFont
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTabBar,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from ui_login import Ui_login
from db_config import get_connection
from main import MainWindow


# -----------------------------
# هش کردن رمز عبور (PBKDF2-HMAC-SHA256)
# -----------------------------
def _hash_password(plain: str) -> str:
    """ساخت هش PBKDF2-HMAC-SHA256 با فرمت pbkdf2:<iterations>:<salt_hex>:<hash_hex>."""
    iterations = 260000
    salt = os.urandom(16)
    digest = hashlib.pbkdf2_hmac("sha256", plain.encode("utf-8"), salt, iterations)
    return f"pbkdf2:{iterations}:{salt.hex()}:{digest.hex()}"


def _verify_password(plain: str, stored: str) -> bool:
    """بررسی رمز عبور؛ هم فرمت هش‌شده (pbkdf2:...) و هم متن ساده قدیمی پشتیبانی می‌شود."""
    stored = str(stored or "")
    if stored.startswith("pbkdf2:"):
        try:
            _, iterations_hex, salt_hex, hash_hex = stored.split(":", 3)
            iterations = int(iterations_hex)
            salt = bytes.fromhex(salt_hex)
            expected = bytes.fromhex(hash_hex)
            computed = hashlib.pbkdf2_hmac(
                "sha256", plain.encode("utf-8"), salt, iterations
            )
            return hmac.compare_digest(computed, expected)
        except Exception:
            return False
    # رمز عبور قدیمی (متن ساده)
    return plain == stored


# -----------------------------
# تبدیل تاریخ میلادی به شمسی
# -----------------------------
def gregorian_to_jalali(gy, gm, gd):
    g_d_m = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

    gy2 = gy + 1 if gm > 2 else gy
    days = (
        355666
        + 365 * gy
        + (gy2 + 3) // 4
        - (gy2 + 99) // 100
        + (gy2 + 399) // 400
        + gd
        + g_d_m[gm - 1]
    )

    jy = -1595 + 33 * (days // 12053)
    days %= 12053
    jy += 4 * (days // 1461)
    days %= 1461

    if days > 365:
        jy += (days - 1) // 365
        days = (days - 1) % 365

    if days < 186:
        jm = 1 + days // 31
        jd = 1 + days % 31
    else:
        jm = 7 + (days - 186) // 30
        jd = 1 + (days - 186) % 30

    return jy, jm, jd


PERSIAN_WEEKDAYS = {
    1: "دوشنبه",
    2: "سه‌شنبه",
    3: "چهارشنبه",
    4: "پنجشنبه",
    5: "جمعه",
    6: "شنبه",
    7: "یکشنبه",
}


class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_login()
        self.ui.setupUi(self)
        self.setLayoutDirection(Qt.RightToLeft)

        self.current_user = None

        self.settings = QSettings("MyPythonProject", "MyApp")
        saved_username = self.settings.value("last_username", "")
        self.ui.txtUsername.setText(str(saved_username))

        self.ui.btnLogin.clicked.connect(self.login)
        self.ui.btnExit.clicked.connect(self.reject)
        self.ui.txtPassword.returnPressed.connect(self.login)

        if self.ui.txtUsername.text().strip():
            self.ui.txtPassword.setFocus()
        else:
            self.ui.txtUsername.setFocus()

    def login(self):
        username = self.ui.txtUsername.text().strip()
        password = self.ui.txtPassword.text()

        if not username:
            QMessageBox.warning(self, "ورود", "نام کاربری را وارد کنید.")
            self.ui.txtUsername.setFocus()
            return

        if not password:
            QMessageBox.warning(self, "ورود", "رمز عبور را وارد کنید.")
            self.ui.txtPassword.setFocus()
            return

        connection = None
        cursor = None

        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT [userid], [username], [UserLogin], [password],
                       [usersecurity], [Samat], [vahed], [Userlevel]
                FROM [tbluser]
                WHERE [UserLogin] = ?
                """,
                (username,),
            )

            user = cursor.fetchone()

            if user is None or not _verify_password(password, str(user[3] or "")):
                QMessageBox.warning(
                    self,
                    "ورود ناموفق",
                    "نام کاربری یا رمز عبور صحیح نیست.",
                )
                self.ui.txtPassword.clear()
                self.ui.txtPassword.setFocus()
                return

            # ارتقای شفاف: اگر رمز در پایگاه داده همان متن ساده قدیمی است،
            # آن را به هش PBKDF2 تبدیل کن. خطای این مهاجرت مانع ورود نمی‌شود.
            stored = str(user[3] or "")
            if not stored.startswith("pbkdf2:"):
                try:
                    cursor.execute(
                        "UPDATE [tbluser] SET [password] = ? WHERE [UserLogin] = ?",
                        (_hash_password(password), username),
                    )
                    connection.commit()
                except Exception:
                    pass

            self.current_user = {
                "userid": user[0],
                "username": user[1],
                "UserLogin": user[2],
                "usersecurity": user[4],
                "Samat": user[5],
                "vahed": user[6],
                "Userlevel": user[7],
            }

            self.settings.setValue("last_username", username)
            self.accept()

        except Exception as exc:
            QMessageBox.critical(
                self,
                "خطای اتصال",
                f"اتصال به پایگاه داده یا بررسی اطلاعات ورود با خطا مواجه شد:\n\n{exc}",
            )
        finally:
            if cursor is not None:
                try:
                    cursor.close()
                except Exception:
                    pass
            if connection is not None:
                try:
                    connection.close()
                except Exception:
                    pass


def main():
    app = QApplication(sys.argv)
    app.setLayoutDirection(Qt.RightToLeft)

    login = LoginDialog()

    if login.exec() != QDialog.Accepted or login.current_user is None:
        return 0

    main_window = MainWindow(login.current_user)
    main_window.showMaximized()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
