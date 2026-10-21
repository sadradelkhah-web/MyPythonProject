"""فرم تعیین سطح دسترسی کاربران؛ UI از user_permissions.ui بارگذاری می‌شود."""
from pathlib import Path
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMessageBox
from db_config import get_connection
from tab_permissions import PERMISSION_TABS, get_user_permissions, save_user_permissions

CHECKBOX_BY_TAB = {
    "tabHome": "chkTabHome",
    "tabKar": "chkTabKar",
    "tabReport": "chkTabReport",
    "tabChangePassword": "chkTabChangePassword",
    "tabAmval": "chkTabAmval",
    "tabHotel": "chkTabHotel",
    "tabAnbarTahrir": "chkTabAnbarTahrir",
    "tabMtoTahrir": "chkTabMtoTahrir",
    "tabUserManagement": "chkTabUserManagement",
    "tabMesc": "chkTabMesc",
}


def open_user_permissions_dialog(parent):
    ui_path = Path(__file__).with_name("user_permissions.ui")
    file = QFile(str(ui_path))
    if not file.open(QIODevice.OpenModeFlag.ReadOnly):
        QMessageBox.critical(parent, "خطای فرم", f"فایل فرم پیدا نشد:\n{ui_path}")
        return
    try:
        dialog = QUiLoader().load(file, parent)
    finally:
        file.close()
    if dialog is None:
        QMessageBox.critical(parent, "خطای فرم", "بارگذاری user_permissions.ui ناموفق بود.")
        return

    combo = dialog.findChild(__import__('PySide6.QtWidgets', fromlist=['QComboBox']).QComboBox, "cmbUsers")
    if combo is None:
        QMessageBox.critical(parent, "خطای فرم", "فیلد انتخاب کاربر (cmbUsers) در UI وجود ندارد.")
        dialog.deleteLater()
        return

    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT [userid], [username] FROM [tbluser] ORDER BY [username]")
        for row in cursor.fetchall():
            combo.addItem(str(row[1] or row[0]), int(row[0]))
    except Exception as exc:
        QMessageBox.critical(parent, "خطای دیتابیس", f"خواندن فهرست کاربران ناموفق بود.\n\n{exc}")
        dialog.deleteLater()
        return
    finally:
        if conn is not None:
            conn.close()

    if combo.count() == 0:
        QMessageBox.information(parent, "کاربران", "کاربری در جدول tbluser پیدا نشد.")
        dialog.deleteLater()
        return

    label = dialog.findChild(__import__('PySide6.QtWidgets', fromlist=['QLabel']).QLabel, "lblSelectedUser")
    checks = {name: dialog.findChild(__import__('PySide6.QtWidgets', fromlist=['QCheckBox']).QCheckBox, obj)
              for name, obj in CHECKBOX_BY_TAB.items()}
    # دسترسی مدیریت کاربران و MESC مختص سوپر ادمین است؛ از این فرم قابل اعطا نیست.
    for restricted in ("tabUserManagement", "tabMesc"):
        if checks.get(restricted):
            checks[restricted].setChecked(False)
            checks[restricted].setEnabled(False)

    def load_selected():
        userid = combo.currentData()
        if userid is None:
            return
        if label:
            label.setText(f"مجوزهای کاربر: {combo.currentText()}")
        try:
            perms = get_user_permissions(userid)
        except Exception as exc:
            QMessageBox.critical(dialog, "خطای مجوزها", f"خواندن مجوزها ناموفق بود.\n\n{exc}")
            perms = {name: False for name, _ in PERMISSION_TABS}
        for name, checkbox in checks.items():
            if checkbox is not None and name not in ("tabUserManagement", "tabMesc"):
                checkbox.setChecked(bool(perms.get(name, False)))

    def save():
        userid = combo.currentData()
        if userid is None:
            return
        perms = {name: bool(checks[name].isChecked()) for name, _ in PERMISSION_TABS if checks.get(name) is not None}
        # این تب‌ها همواره فقط برای سوپر ادمین محفوظ‌اند.
        perms["tabUserManagement"] = False
        perms["tabMesc"] = False
        try:
            save_user_permissions(userid, perms)
        except Exception as exc:
            QMessageBox.critical(dialog, "خطای ذخیره", f"ذخیره مجوزها ناموفق بود.\n\n{exc}")
            return
        QMessageBox.information(dialog, "ذخیره شد", "مجوزهای کاربر ذخیره شد. برای اعمال کامل، کاربر خارج شود و دوباره وارد شود.")
        dialog.accept()

    combo.currentIndexChanged.connect(load_selected)
    dialog.findChild(__import__('PySide6.QtWidgets', fromlist=['QPushButton']).QPushButton, "btnSavePermissions").clicked.connect(save)
    dialog.findChild(__import__('PySide6.QtWidgets', fromlist=['QPushButton']).QPushButton, "btnCancelPermissions").clicked.connect(dialog.reject)
    load_selected()
    dialog.exec()
