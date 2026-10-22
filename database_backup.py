"""پشتیبان‌گیری امن از فایل دیتابیس Access هنگام خروج SuperAdmin."""
from datetime import datetime
from pathlib import Path
import shutil

from db_config import DB_PATH


MAX_BACKUPS = 30


def create_database_backup(max_backups=MAX_BACKUPS):
    """یک نسخه زمان‌دار در پوشه Backups کنار دیتابیس می‌سازد.

    اگر دیتابیس موجود نباشد، فایل قفل Access نشان دهد که اتصال دیگری باز است،
    یا فایل هنگام کپی تغییر کند، از ثبت نسخه ناقص خودداری می‌شود.
    خروجی: (موفق بود؟، پیام، مسیر نسخه پشتیبان یا None)
    """
    temporary_path = None

    try:
        raw_path = str(DB_PATH or "").strip().strip('"').strip()
        if not raw_path:
            return False, "مسیر دیتابیس در تنظیمات خالی است.", None

        source = Path(raw_path).expanduser()
        # مسیر نسبی مانند اتصال pyodbc نسبت به پوشه کاری اجرای برنامه تفسیر می‌شود.
        if not source.is_absolute():
            source = Path.cwd() / source
        source = source.resolve()

        if source.suffix.casefold() not in (".mdb", ".accdb"):
            return False, "پسوند مسیر دیتابیس .mdb یا .accdb نیست.", None
        if not source.is_file():
            return False, f"فایل دیتابیس پیدا نشد:\n{source}", None

        # Access هنگام باز بودن دیتابیس معمولاً فایل قفل مجاور می‌سازد.
        # وجود آن می‌تواند به معنی اتصال فعال دیگری باشد؛ در این حالت کپی نمی‌کنیم.
        lock_paths = (
            source.with_suffix(".ldb"),
            source.with_suffix(".laccdb"),
        )
        active_locks = [str(path.name) for path in lock_paths if path.exists()]
        if active_locks:
            return (
                False,
                "فایل قفل Access وجود دارد (" + "، ".join(active_locks)
                + "). برای جلوگیری از نسخه ناسازگار، پشتیبان‌گیری انجام نشد. "
                  "مطمئن شوید دیتابیس در برنامه دیگری باز نیست و دوباره خارج شوید.",
                None,
            )

        backup_dir = source.parent / "Backups"
        backup_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        backup_path = backup_dir / f"{source.stem}_{timestamp}{source.suffix}"
        temporary_path = backup_dir / f".{backup_path.name}.tmp"

        before = source.stat()
        shutil.copy2(source, temporary_path)
        after = source.stat()

        # اگر حین کپی اندازه/زمان تغییر کرده یا قفل ظاهر شده، نسخه موقت را رد کن.
        changed_during_copy = (
            before.st_size != after.st_size
            or before.st_mtime_ns != after.st_mtime_ns
        )
        lock_appeared = any(path.exists() for path in lock_paths)
        if changed_during_copy or lock_appeared:
            temporary_path.unlink(missing_ok=True)
            reason = (
                "فایل دیتابیس حین کپی تغییر کرد."
                if changed_during_copy
                else "هنگام کپی اتصال دیگری به دیتابیس باز شد."
            )
            return False, reason + " نسخه پشتیبان ناقص نگه‌داری نشد.", None

        if temporary_path.stat().st_size != after.st_size:
            temporary_path.unlink(missing_ok=True)
            return False, "اندازه نسخه کپی‌شده با دیتابیس برابر نیست؛ نسخه رد شد.", None

        # فایل نهایی فقط پس از کامل‌شدن کپی قابل مشاهده می‌شود.
        temporary_path.replace(backup_path)
        temporary_path = None

        # نگه‌داری تعداد محدودی نسخه برای جلوگیری از پرشدن تدریجی درایو.
        pattern = f"{source.stem}_*{source.suffix}"
        backups = sorted(
            (
                item for item in backup_dir.glob(pattern)
                if item.is_file() and item != backup_path
            ),
            key=lambda item: item.stat().st_mtime_ns,
            reverse=True,
        )
        for old_backup in backups[max(0, int(max_backups) - 1):]:
            try:
                old_backup.unlink()
            except OSError:
                # خطای پاک‌کردن نسخه قدیمی نباید نسخه تازه را ناموفق اعلام کند.
                pass

        return True, f"نسخه پشتیبان با موفقیت ذخیره شد:\n{backup_path}", backup_path

    except Exception as exc:
        if temporary_path is not None:
            try:
                temporary_path.unlink(missing_ok=True)
            except OSError:
                pass
        return False, f"پشتیبان‌گیری با خطا مواجه شد:\n{exc}", None
