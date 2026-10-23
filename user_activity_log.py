"""ثبت بی‌صدای رویدادهای کاربران در جدول LoginEvent دیتابیس Access."""
import os
from datetime import datetime

from db_config import get_connection


def log_user_event(
    username,
    action_type,
    module_name="",
    description="",
    record_id=None,
    result="Success",
    connection=None,
):
    """رویداد را بدون ایجاد مزاحمت برای عملیات اصلی ثبت می‌کند.

    اگر connection داده شود از اتصال موجود استفاده می‌شود؛ در غیر این صورت
    یک اتصال مستقل ایجاد و در پایان بسته خواهد شد. خطای لاگ‌گیری عمداً
    به رابط کاربری منتقل نمی‌شود تا ثبت فعالیت، ورود یا خروج برنامه را متوقف نکند.
    """
    own_connection = connection is None
    conn = connection
    cursor = None

    try:
        if conn is None:
            conn = get_connection()

        cursor = conn.cursor()
        normalized_record_id = None
        if record_id not in (None, ""):
            try:
                normalized_record_id = int(record_id)
            except (TypeError, ValueError, OverflowError):
                normalized_record_id = None

        computer_name = (os.environ.get("COMPUTERNAME") or os.environ.get("HOSTNAME") or "").strip()
        if len(computer_name) > 100:
            computer_name = computer_name[:100]

        cursor.execute(
            """
            INSERT INTO [LoginEvent]
                ([Username], [ActionType], [ModuleName], [Description],
                 [RecordID], [EventDateTime], [ComputerName], [Result])
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                str(username or "")[:100],
                str(action_type or "")[:50],
                str(module_name or "")[:50],
                str(description or ""),
                normalized_record_id,
                datetime.now(),
                computer_name,
                str(result or "Success")[:20],
            ),
        )
        if own_connection:
            conn.commit()
        return True
    except Exception:
        if own_connection and conn is not None:
            try:
                conn.rollback()
            except Exception:
                pass
        return False
    finally:
        if cursor is not None:
            try:
                cursor.close()
            except Exception:
                pass
        if own_connection and conn is not None:
            try:
                conn.close()
            except Exception:
                pass
