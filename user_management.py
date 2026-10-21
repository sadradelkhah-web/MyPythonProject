
import sys

from PySide6.QtWidgets import (
    QApplication,
    QMessageBox,
    QTableWidgetItem,
)

from db_config import get_connection


# =========================================================
# مدیریت کاربران
# کنترلر متصل به ویجت‌های فرم اصلی
# =========================================================

class UserManagement:

    def __init__(self, parent_window, ui, current_user):

        self.window = parent_window
        self.ui = ui

        # -------------------------------------------------
        # کاربر جاری
        # -------------------------------------------------

        self.current_user = current_user

        # userid انتخاب‌شده برای ویرایش / حذف
        self.selected_userid = None

        # =================================================
        # تشخیص SuperAdmin
        # =================================================

        user_security = str(
            self.current_user.get("usersecurity") or ""
        ).strip()

        self.is_master = (
            user_security.casefold() == "superadmin"
        )

        # =================================================
        # دکمه‌های مدیریت کاربران
        # =================================================

        self.ui.btnSaveUser.clicked.connect(
            self.save_user
        )

        self.ui.btnEditUser.clicked.connect(
            self.edit_user
        )

        self.ui.btnDeleteUser.clicked.connect(
            self.delete_user
        )

        self.ui.btnClear.clicked.connect(
            self.clear_form
        )

        self.ui.btnCancel.clicked.connect(
            self.go_home
        )

        if hasattr(self.ui, "btnCancelPassword"):
            self.ui.btnCancelPassword.clicked.connect(
                self.go_home
            )

        # =================================================
        # جدول کاربران
        # =================================================

        self.ui.tblUsers.cellClicked.connect(
            self.select_user
        )

        # =================================================
        # تغییر رمز
        # =================================================

        self.ui.btnChangePassword.clicked.connect(
            self.change_password
        )

        # =================================================
        # بارگذاری اولیه
        # =================================================

        self.load_combos()

        # برای تب تغییر رمز:
        # SuperAdmin -> همه کاربران
        # کاربر عادی -> فقط خودش
        self.load_change_password_users()

        # فقط SuperAdmin اجازه دیدن جدول مدیریت کاربران را دارد
        if self.is_master:
            self.load_users()
        else:
            self.ui.tblUsers.setRowCount(0)

        self.clear_form()
        self.clear_password_form()

        # اعمال دسترسی
        self.apply_permissions()

    # =====================================================
    # بازگشت به صفحه اصلی
    # =====================================================

    def go_home(self):

        self.clear_form()
        self.clear_password_form()

        if hasattr(self.ui, "tabMain") and hasattr(self.ui, "tabHome"):
            self.ui.tabMain.setCurrentWidget(
                self.ui.tabHome
            )

    # =====================================================
    # اعمال سطح دسترسی
    # =====================================================

    def apply_permissions(self):

        if self.is_master:

            # -------------------------------------------------
            # SuperAdmin
            # -------------------------------------------------

            self.ui.tabUserManagement.setEnabled(True)
            self.ui.tabChangePassword.setEnabled(True)

            self.ui.cmbChangeUser.setEnabled(True)

            self.window.setWindowTitle(
                "سیستم مدیریت درخواست‌های تعمیرات"
            )

        else:

            # -------------------------------------------------
            # کاربر عادی
            # -------------------------------------------------

            # تب مدیریت کاربران غیرفعال
            self.ui.tabUserManagement.setEnabled(False)

            # تب تغییر رمز فعال
            self.ui.tabChangePassword.setEnabled(True)

            # انتخاب کاربر غیرفعال
            self.ui.cmbChangeUser.setEnabled(False)

    # =====================================================
    # ساخت آیتم جدول
    # =====================================================

    @staticmethod
    def make_item(value):

        if value is None:
            value = ""

        return QTableWidgetItem(
            str(value)
        )

    # =====================================================
    # بارگذاری واحدها و سطح دسترسی
    # =====================================================

    def load_combos(self):

        conn = None

        try:

            conn = get_connection()
            cursor = conn.cursor()

            # -------------------------------------------------
            # واحد
            # -------------------------------------------------

            self.ui.cmbUserVahed.clear()

            cursor.execute("""
                SELECT DISTINCT [vahed]
                FROM [tbluser]
                WHERE [vahed] IS NOT NULL
                  AND [vahed] <> ''
                ORDER BY [vahed]
            """)

            for row in cursor.fetchall():

                self.ui.cmbUserVahed.addItem(
                    str(row[0])
                )

            # -------------------------------------------------
            # سطح دسترسی
            # -------------------------------------------------

            self.ui.cmbUserLevel.clear()

            cursor.execute("""
                SELECT DISTINCT [Userlevel]
                FROM [tbluser]
                WHERE [Userlevel] IS NOT NULL
                ORDER BY [Userlevel]
            """)

            for row in cursor.fetchall():

                self.ui.cmbUserLevel.addItem(
                    str(row[0])
                )

        except Exception as e:

            QMessageBox.critical(
                self.window,
                "خطای دیتابیس",
                f"خطا در خواندن اطلاعات:\n\n{e}"
            )

        finally:

            if conn is not None:

                try:
                    conn.close()
                except Exception:
                    pass

    # =====================================================
    # نمایش کاربران در جدول مدیریت
    # =====================================================

    def load_users(self):

        # فقط SuperAdmin
        if not self.is_master:
            return

        conn = None

        try:

            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    [userid],
                    [UserLogin],
                    [username],
                    [vahed],
                    [Userlevel]
                FROM [tbluser]
                ORDER BY [userid]
            """)

            users = cursor.fetchall()

            table = self.ui.tblUsers

            table.setRowCount(0)
            table.setColumnCount(4)

            for row_number, user in enumerate(users):

                table.insertRow(row_number)

                # نام کاربری
                table.setItem(
                    row_number,
                    0,
                    self.make_item(user[1])
                )

                # نام و نام خانوادگی
                table.setItem(
                    row_number,
                    1,
                    self.make_item(user[2])
                )

                # واحد
                table.setItem(
                    row_number,
                    2,
                    self.make_item(user[3])
                )

                # سطح دسترسی
                table.setItem(
                    row_number,
                    3,
                    self.make_item(user[4])
                )

            # شماره ردیف خودکار
            table.setVerticalHeaderLabels(
                [
                    str(i + 1)
                    for i in range(
                        table.rowCount()
                    )
                ]
            )

        except Exception as e:

            QMessageBox.critical(
                self.window,
                "خطای دیتابیس",
                f"خطا در نمایش کاربران:\n\n{e}"
            )

        finally:

            if conn is not None:

                try:
                    conn.close()
                except Exception:
                    pass

    # =====================================================
    # بارگذاری کاربران برای تغییر رمز
    # =====================================================

    def load_change_password_users(self):

        conn = None

        try:

            conn = get_connection()
            cursor = conn.cursor()

            # =================================================
            # SuperAdmin
            # فقط SuperAdmin فهرست همه کاربران را می‌گیرد
            # =================================================

            if self.is_master:

                cursor.execute("""
                    SELECT
                        [userid],
                        [UserLogin],
                        [username]
                    FROM [tbluser]
                    ORDER BY [username]
                """)

            # =================================================
            # کاربر عادی
            # فقط رکورد خودش از بانک خوانده می‌شود
            # =================================================

            else:

                current_userid = (
                    self.current_user.get("userid")
                )

                if current_userid is None:
                    return

                cursor.execute("""
                    SELECT
                        [userid],
                        [UserLogin],
                        [username]
                    FROM [tbluser]
                    WHERE [userid] = ?
                """, (
                    current_userid,
                ))

            users = cursor.fetchall()

            self.ui.cmbChangeUser.clear()

            # -------------------------------------------------
            # پر کردن ComboBox
            # -------------------------------------------------

            for user in users:

                userid = user[0]
                user_login = user[1]
                full_name = user[2]

                if full_name is None:
                    full_name = ""

                if user_login is None:
                    user_login = ""

                display_text = (
                    f"{full_name} - {user_login}"
                )

                self.ui.cmbChangeUser.addItem(
                    display_text,
                    userid
                )

        except Exception as e:

            QMessageBox.critical(
                self.window,
                "خطای دیتابیس",
                f"خطا در بارگذاری کاربران برای تغییر رمز:\n\n{e}"
            )

        finally:

            if conn is not None:

                try:
                    conn.close()
                except Exception:
                    pass

    # =====================================================
    # انتخاب کاربر از جدول مدیریت
    # =====================================================

    def select_user(self, row, column):

        # فقط SuperAdmin
        if not self.is_master:
            return

        table = self.ui.tblUsers

        # UserLogin در ستون صفر
        login_item = table.item(
            row,
            0
        )

        if login_item is None:
            return

        selected_login = (
            login_item.text().strip()
        )

        if not selected_login:
            return

        conn = None

        try:

            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    [userid],
                    [username],
                    [UserLogin],
                    [Samat],
                    [vahed],
                    [Userlevel]
                FROM [tbluser]
                WHERE [UserLogin] = ?
            """, (
                selected_login,
            ))

            user = cursor.fetchone()

            if user:

                self.selected_userid = user[0]

                self.ui.txtFullName.setText(
                    ""
                    if user[1] is None
                    else str(user[1])
                )

                self.ui.txtUserLogin.setText(
                    ""
                    if user[2] is None
                    else str(user[2])
                )

                self.ui.txtSamat.setText(
                    ""
                    if user[3] is None
                    else str(user[3])
                )

                self.set_combo_value(
                    self.ui.cmbUserVahed,
                    user[4]
                )

                self.set_combo_value(
                    self.ui.cmbUserLevel,
                    user[5]
                )

                # رمز هرگز نمایش داده نمی‌شود
                self.ui.txtPassword.clear()
                self.ui.txtPassword2.clear()

        except Exception as e:

            QMessageBox.critical(
                self.window,
                "خطا",
                f"خطا در خواندن اطلاعات کاربر:\n\n{e}"
            )

        finally:

            if conn is not None:

                try:
                    conn.close()
                except Exception:
                    pass

    # =====================================================
    # تنظیم ComboBox
    # =====================================================

    @staticmethod
    def set_combo_value(combo, value):

        if value is None:
            return

        index = combo.findText(
            str(value)
        )

        if index >= 0:
            combo.setCurrentIndex(index)

    # =====================================================
    # ثبت کاربر جدید
    # =====================================================

    def save_user(self):

        # فقط SuperAdmin
        if not self.is_master:

            QMessageBox.warning(
                self.window,
                "دسترسی",
                "شما اجازه تعریف کاربر جدید را ندارید."
            )

            return

        full_name = (
            self.ui.txtFullName.text().strip()
        )

        user_login = (
            self.ui.txtUserLogin.text().strip()
        )

        password = (
            self.ui.txtPassword.text()
        )

        password2 = (
            self.ui.txtPassword2.text()
        )

        samat = (
            self.ui.txtSamat.text().strip()
        )

        vahed = (
            self.ui.cmbUserVahed.currentText().strip()
        )

        user_level = (
            self.ui.cmbUserLevel.currentText().strip()
        )

        # -------------------------------------------------
        # اعتبارسنجی
        # -------------------------------------------------

        if not full_name:

            QMessageBox.warning(
                self.window,
                "ثبت کاربر",
                "نام و نام خانوادگی را وارد کنید."
            )

            self.ui.txtFullName.setFocus()
            return

        if not user_login:

            QMessageBox.warning(
                self.window,
                "ثبت کاربر",
                "نام کاربری را وارد کنید."
            )

            self.ui.txtUserLogin.setFocus()
            return

        if not password:

            QMessageBox.warning(
                self.window,
                "ثبت کاربر",
                "رمز عبور را وارد کنید."
            )

            self.ui.txtPassword.setFocus()
            return

        if password != password2:

            QMessageBox.warning(
                self.window,
                "ثبت کاربر",
                "رمز عبور و تکرار آن یکسان نیستند."
            )

            self.ui.txtPassword2.setFocus()
            return

        if not vahed:

            QMessageBox.warning(
                self.window,
                "ثبت کاربر",
                "واحد را انتخاب کنید."
            )

            return

        if not user_level:

            QMessageBox.warning(
                self.window,
                "ثبت کاربر",
                "سطح دسترسی را انتخاب کنید."
            )

            return

        conn = None

        try:

            conn = get_connection()
            cursor = conn.cursor()

            # بررسی نام کاربری تکراری
            cursor.execute("""
                SELECT COUNT(*)
                FROM [tbluser]
                WHERE [UserLogin] = ?
            """, (
                user_login,
            ))

            count = cursor.fetchone()[0]

            if count > 0:

                QMessageBox.warning(
                    self.window,
                    "ثبت کاربر",
                    "این نام کاربری قبلاً ثبت شده است."
                )

                self.ui.txtUserLogin.setFocus()
                return

            # ثبت
            cursor.execute("""
                INSERT INTO [tbluser]
                (
                    [username],
                    [UserLogin],
                    [password],
                    [Samat],
                    [vahed],
                    [Userlevel]
                )
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                full_name,
                user_login,
                password,
                samat,
                vahed,
                user_level
            ))

            conn.commit()

            QMessageBox.information(
                self.window,
                "ثبت کاربر",
                "کاربر با موفقیت ثبت شد."
            )

            self.load_combos()
            self.load_users()
            self.load_change_password_users()
            self.clear_form()

        except Exception as e:

            if conn is not None:

                try:
                    conn.rollback()
                except Exception:
                    pass

            QMessageBox.critical(
                self.window,
                "خطای ثبت",
                f"کاربر ثبت نشد:\n\n{e}"
            )

        finally:

            if conn is not None:

                try:
                    conn.close()
                except Exception:
                    pass

    # =====================================================
    # ویرایش کاربر
    # =====================================================

    def edit_user(self):

        # فقط SuperAdmin
        if not self.is_master:

            QMessageBox.warning(
                self.window,
                "دسترسی",
                "شما اجازه ویرایش کاربران را ندارید."
            )

            return

        if self.selected_userid is None:

            QMessageBox.warning(
                self.window,
                "ویرایش",
                "ابتدا یک کاربر را از جدول انتخاب کنید."
            )

            return

        full_name = (
            self.ui.txtFullName.text().strip()
        )

        user_login = (
            self.ui.txtUserLogin.text().strip()
        )

        samat = (
            self.ui.txtSamat.text().strip()
        )

        vahed = (
            self.ui.cmbUserVahed.currentText().strip()
        )

        user_level = (
            self.ui.cmbUserLevel.currentText().strip()
        )

        if not full_name:

            QMessageBox.warning(
                self.window,
                "ویرایش",
                "نام و نام خانوادگی را وارد کنید."
            )

            return

        if not user_login:

            QMessageBox.warning(
                self.window,
                "ویرایش",
                "نام کاربری را وارد کنید."
            )

            return

        conn = None

        try:

            conn = get_connection()
            cursor = conn.cursor()

            # بررسی تکراری نبودن نام کاربری
            cursor.execute("""
                SELECT COUNT(*)
                FROM [tbluser]
                WHERE [UserLogin] = ?
                  AND [userid] <> ?
            """, (
                user_login,
                self.selected_userid
            ))

            count = cursor.fetchone()[0]

            if count > 0:

                QMessageBox.warning(
                    self.window,
                    "ویرایش",
                    "این نام کاربری قبلاً برای کاربر دیگری ثبت شده است."
                )

                return

            cursor.execute("""
                UPDATE [tbluser]
                SET
                    [username] = ?,
                    [UserLogin] = ?,
                    [Samat] = ?,
                    [vahed] = ?,
                    [Userlevel] = ?
                WHERE [userid] = ?
            """, (
                full_name,
                user_login,
                samat,
                vahed,
                user_level,
                self.selected_userid
            ))

            conn.commit()

            QMessageBox.information(
                self.window,
                "ویرایش",
                "اطلاعات کاربر با موفقیت تغییر کرد."
            )

            self.load_combos()
            self.load_users()
            self.load_change_password_users()
            self.clear_form()

        except Exception as e:

            if conn is not None:

                try:
                    conn.rollback()
                except Exception:
                    pass

            QMessageBox.critical(
                self.window,
                "خطای ویرایش",
                f"اطلاعات کاربر تغییر نکرد:\n\n{e}"
            )

        finally:

            if conn is not None:

                try:
                    conn.close()
                except Exception:
                    pass

    # =====================================================
    # حذف کاربر
    # =====================================================

    def delete_user(self):

        # فقط SuperAdmin
        if not self.is_master:

            QMessageBox.warning(
                self.window,
                "دسترسی",
                "شما اجازه حذف کاربران را ندارید."
            )

            return

        if self.selected_userid is None:

            QMessageBox.warning(
                self.window,
                "حذف",
                "ابتدا یک کاربر را از جدول انتخاب کنید."
            )

            return

        conn = None

        try:

            conn = get_connection()
            cursor = conn.cursor()

            # -------------------------------------------------
            # بررسی کاربر
            # -------------------------------------------------

            cursor.execute("""
                SELECT
                    [username],
                    [usersecurity]
                FROM [tbluser]
                WHERE [userid] = ?
            """, (
                self.selected_userid,
            ))

            selected_user = cursor.fetchone()

            if selected_user is None:

                QMessageBox.warning(
                    self.window,
                    "حذف",
                    "کاربر موردنظر پیدا نشد."
                )

                return

            selected_security = str(
                selected_user[1] or ""
            ).strip()

            # -------------------------------------------------
            # جلوگیری از حذف SuperAdmin
            # -------------------------------------------------

            if selected_security.casefold() == "superadmin":

                QMessageBox.warning(
                    self.window,
                    "حذف کاربر",
                    "کاربر SuperAdmin قابل حذف نیست."
                )

                return

            # -------------------------------------------------
            # تأیید
            # -------------------------------------------------

            answer = QMessageBox.question(
                self.window,
                "حذف کاربر",
                f"آیا از حذف کاربر «{selected_user[0]}» مطمئن هستید؟",
                QMessageBox.Yes
                | QMessageBox.No,
                QMessageBox.No
            )

            if answer != QMessageBox.Yes:
                return

            cursor.execute("""
                DELETE FROM [tbluser]
                WHERE [userid] = ?
            """, (
                self.selected_userid,
            ))

            conn.commit()

            QMessageBox.information(
                self.window,
                "حذف کاربر",
                "کاربر با موفقیت حذف شد."
            )

            self.load_users()
            self.load_change_password_users()
            self.clear_form()

        except Exception as e:

            if conn is not None:

                try:
                    conn.rollback()
                except Exception:
                    pass

            QMessageBox.critical(
                self.window,
                "خطای حذف",
                f"کاربر حذف نشد:\n\n{e}"
            )

        finally:

            if conn is not None:

                try:
                    conn.close()
                except Exception:
                    pass

    # =====================================================
    # تغییر رمز عبور
    # =====================================================

    def change_password(self):

        index = (
            self.ui.cmbChangeUser.currentIndex()
        )

        if index < 0:

            QMessageBox.warning(
                self.window,
                "تغییر رمز",
                "کاربری برای تغییر رمز انتخاب نشده است."
            )

            return

        userid = (
            self.ui.cmbChangeUser.itemData(
                index
            )
        )

        # -------------------------------------------------
        # کاربر عادی فقط userid خودش
        # -------------------------------------------------

        if not self.is_master:

            current_userid = (
                self.current_user.get(
                    "userid"
                )
            )

            if userid != current_userid:

                QMessageBox.warning(
                    self.window,
                    "دسترسی",
                    "شما فقط اجازه تغییر رمز خودتان را دارید."
                )

                return

        # -------------------------------------------------
        # رمز جدید
        # -------------------------------------------------

        new_password = (
            self.ui.txtNewPassword.text()
        )

        new_password2 = (
            self.ui.txtNewPassword2.text()
        )

        if not new_password:

            QMessageBox.warning(
                self.window,
                "تغییر رمز",
                "رمز جدید را وارد کنید."
            )

            self.ui.txtNewPassword.setFocus()

            return

        if new_password != new_password2:

            QMessageBox.warning(
                self.window,
                "تغییر رمز",
                "رمز جدید و تکرار آن یکسان نیستند."
            )

            self.ui.txtNewPassword2.setFocus()

            return

        conn = None

        try:

            conn = get_connection()
            cursor = conn.cursor()

            # -------------------------------------------------
            # برای کاربر عادی، شرط userid خودش هم اعمال می‌شود
            # -------------------------------------------------

            if self.is_master:

                cursor.execute("""
                    UPDATE [tbluser]
                    SET [password] = ?
                    WHERE [userid] = ?
                """, (
                    new_password,
                    userid
                ))

            else:

                current_userid = (
                    self.current_user.get("userid")
                )

                cursor.execute("""
                    UPDATE [tbluser]
                    SET [password] = ?
                    WHERE [userid] = ?
                      AND [userid] = ?
                """, (
                    new_password,
                    userid,
                    current_userid
                ))

            # -------------------------------------------------
            # بررسی اینکه رکورد واقعاً تغییر کرده
            # -------------------------------------------------

            if cursor.rowcount == 0:

                conn.rollback()

                QMessageBox.warning(
                    self.window,
                    "تغییر رمز",
                    "تغییر رمز انجام نشد."
                )

                return

            conn.commit()

            QMessageBox.information(
                self.window,
                "تغییر رمز",
                "رمز عبور با موفقیت تغییر کرد."
            )

            self.clear_password_form()

        except Exception as e:

            if conn is not None:

                try:
                    conn.rollback()
                except Exception:
                    pass

            QMessageBox.critical(
                self.window,
                "خطای تغییر رمز",
                f"رمز عبور تغییر نکرد:\n\n{e}"
            )

        finally:

            if conn is not None:

                try:
                    conn.close()
                except Exception:
                    pass

    # =====================================================
    # پاک کردن فرم تعریف کاربر
    # =====================================================

    def clear_form(self):

        self.selected_userid = None

        self.ui.txtFullName.clear()
        self.ui.txtUserLogin.clear()
        self.ui.txtPassword.clear()
        self.ui.txtPassword2.clear()
        self.ui.txtSamat.clear()

        if self.ui.cmbUserVahed.count() > 0:

            self.ui.cmbUserVahed.setCurrentIndex(0)

        if self.ui.cmbUserLevel.count() > 0:

            self.ui.cmbUserLevel.setCurrentIndex(0)

        self.ui.tblUsers.clearSelection()

    # =====================================================
    # پاک کردن فرم تغییر رمز
    # =====================================================

    def clear_password_form(self):

        self.ui.txtNewPassword.clear()
        self.ui.txtNewPassword2.clear()


# =========================================================
# اجرای مستقیم برای تست
# =========================================================

if __name__ == "__main__":

    app = QApplication(sys.argv)

    QMessageBox.information(
        None,
        "مدیریت کاربران",
        "این فرم باید از داخل برنامه اصلی و پس از ورود کاربر اجرا شود."
    )

    sys.exit(0)
