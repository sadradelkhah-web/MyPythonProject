# tab_permissions.py
# مدیریت مجوز مشاهده تب‌ها در برنامه تعمیرات
#
# جدول Access مورد انتظار:
# tblUserTabPermissions(id AutoNumber, userid Long Integer,
#                   tabname Short Text, canview Yes/No)

from PySide6.QtWidgets import QMessageBox
from db_config import get_connection


# نام‌های فنی باید دقیقاً با objectName تب‌ها در Qt Designer یکی باشند.
# اگر در برنامه نام فنی تب دیگری دارید، آن را به این فهرست اضافه کنید.
PERMISSION_TABS = [
    ("tabHome", "صفحه اصلی"),
    ("tabKar", "ثبت درخواست‌ها"),
    ("tabReport", "گزارش‌ها"),
    ("tabChangePassword", "تغییر رمز عبور"),
    ("tabAmval", "اموال"),
    ("tabHotel", "اتاق‌داری مهمانسرا"),
    ("tabAnbarTahrir", "انبار لوازم‌التحریر"),
    ("tabMtoTahrir", "تقاضای لوازم‌التحریر"),
    ("tabMesc", "مشخصات کالا (فقط SuperAdmin)"),
    ("tabUserManagement", "مدیریت کاربران (فقط SuperAdmin)"),
]


def is_superadmin(current_user):
    """تشخیص SuperAdmin بر اساس فیلد usersecurity."""
    security = str((current_user or {}).get("usersecurity") or "").strip()
    return security.casefold() == "superadmin"


def get_user_permissions(userid):
    """
    خروجی: dict مانند {"tabHome": True, "tabReport": False}
    اگر برای تب رکوردی وجود نداشته باشد، مقدار پیش‌فرض False است.
    """
    permissions = {tabname: False for tabname, _ in PERMISSION_TABS}
    if userid is None:
        return permissions

    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT [tabname], [canview]
            FROM [tblUserTabPermissions]
            WHERE [userid] = ?
        """, (int(userid),))

        for row in cursor.fetchall():
            tabname = str(row[0] or "").strip()
            if tabname in permissions:
                permissions[tabname] = bool(row[1])
        return permissions
    finally:
        if conn is not None:
            conn.close()


def save_user_permissions(userid, permissions):
    """
    ثبت مجوزها با به‌روزرسانی رکوردهای قبلی.
    برای جلوگیری از وابستگی به قابلیت‌های خاص SQL Access، عملیات ساده و
    سازگار با pyodbc استفاده شده است.
    """
    if userid is None:
        raise ValueError("شناسه کاربر مشخص نیست.")

    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        for tabname, _label in PERMISSION_TABS:
            canview = bool(permissions.get(tabname, False))
            cursor.execute("""
                SELECT [id]
                FROM [tblUserTabPermissions]
                WHERE [userid] = ? AND [tabname] = ?
            """, (int(userid), tabname))
            rows = cursor.fetchall()

            if rows:
                # رکورد اول به‌روزرسانی و رکوردهای تکراری احتمالی حذف می‌شوند.
                first_id = rows[0][0]
                cursor.execute("""
                    UPDATE [tblUserTabPermissions]
                    SET [canview] = ?
                    WHERE [id] = ?
                """, (canview, first_id))

                for duplicate in rows[1:]:
                    cursor.execute("""
                        DELETE FROM [tblUserTabPermissions]
                        WHERE [id] = ?
                    """, (duplicate[0],))
            else:
                cursor.execute("""
                    INSERT INTO [tblUserTabPermissions]
                        ([userid], [tabname], [canview])
                    VALUES (?, ?, ?)
                """, (int(userid), tabname, canview))

        conn.commit()
    except Exception:
        if conn is not None:
            try:
                conn.rollback()
            except Exception:
                pass
        raise
    finally:
        if conn is not None:
            conn.close()


def apply_tab_permissions(ui, current_user, parent=None):
    """
    مجوزها را روی QTabWidget با نام tabMain اعمال می‌کند.
    برای SuperAdmin همه تب‌ها قابل مشاهده‌اند.
    مدیریت کاربران فقط برای SuperAdmin نمایش داده می‌شود.
    """
    tab_widget = getattr(ui, "tabMain", None)
    if tab_widget is None:
        # اگر نام QTabWidget در فرم متفاوت است، این تابع باید با نام درست فراخوانی شود.
        return

    if is_superadmin(current_user):
        for index in range(tab_widget.count()):
            tab_widget.setTabVisible(index, True)
        return

    userid = (current_user or {}).get("userid")
    try:
        permissions = get_user_permissions(userid)
    except Exception as exc:
        # در صورت خطای دیتابیس، دسترسی‌ها به‌صورت باز (allow-all) اعمال نمی‌شوند.
        if parent is not None:
            QMessageBox.critical(
                parent,
                "خطای مجوزها",
                "خواندن مجوزهای کاربر از جدول tblUserTabPermissions ناموفق بود.\n\n"
                f"{exc}\n\nتب‌های دارای مجوز به‌صورت امن محدود می‌شوند."
            )
        permissions = {tabname: False for tabname, _ in PERMISSION_TABS}

    for index in range(tab_widget.count()):
        page = tab_widget.widget(index)
        tabname = page.objectName()

        # مدیریت کاربران صرفاً برای SuperAdmin است، حتی اگر در جدول مجاز شده باشد.
        if tabname == "tabUserManagement":
            allowed = False
        elif tabname in permissions:
            allowed = permissions[tabname]
        else:
            # تب ناشناخته را به‌طور پیش‌فرض مخفی می‌کنیم تا مجوز صریح تعیین شود.
            allowed = False

        tab_widget.setTabVisible(index, allowed)

    # اگر تب فعلی مخفی شد، به اولین تب قابل مشاهده برو.
    current_index = tab_widget.currentIndex()
    if current_index >= 0 and not tab_widget.isTabVisible(current_index):
        for index in range(tab_widget.count()):
            if tab_widget.isTabVisible(index):
                tab_widget.setCurrentIndex(index)
                break
