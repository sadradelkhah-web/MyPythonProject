"""پشتیبان‌گیری بی‌صدای فایل دیتابیس Access هنگام خروج SuperAdmin."""
from pathlib import Path
import shutil

from db_config import DB_PATH


def create_database_backup():
    """یک نسخه ثابت را در پوشه Backups کنار دیتابیس ایجاد یا جایگزین می‌کند.

    اگر دیتابیس باز/قفل باشد یا حین کپی تغییر کند، از جایگزینی نسخه قبلی
    خودداری می‌شود. خروجی تابع (موفقیت، پیام، مسیر) است؛ رابط کاربری پیامی نشان نمی‌دهد.
    """
    temporary_path = None

    try:
        raw_path = str(DB_PATH or "").strip().strip('"').strip()
        if not raw_path:
            return False, "مسیر دیتابیس خالی است.", None

        source = Path(raw_path).expanduser()
        if not source.is_absolute():
            source = Path.cwd() / source
        source = source.resolve()

        if source.suffix.casefold() not in (".mdb", ".accdb") or not source.is_file():
            return False, "فایل دیتابیس معتبر پیدا نشد.", None

        lock_paths = (source.with_suffix(".ldb"), source.with_suffix(".laccdb"))
        if any(path.exists() for path in lock_paths):
            return False, "دیتابیس هنوز باز است؛ پشتیبان‌گیری رد شد.", None

        backup_dir = source.parent / "Backups"
        backup_dir.mkdir(parents=True, exist_ok=True)

        # فقط یک نسخه نهایی نگه‌داری می‌شود و در هر خروج با نسخه جدید جایگزین می‌شود.
        backup_path = backup_dir / f"{source.stem}_backup{source.suffix}"
        temporary_path = backup_dir / f".{backup_path.name}.tmp"

        before = source.stat()
        shutil.copy2(source, temporary_path)
        after = source.stat()

        if (
            before.st_size != after.st_size
            or before.st_mtime_ns != after.st_mtime_ns
            or any(path.exists() for path in lock_paths)
            or temporary_path.stat().st_size != after.st_size
        ):
            temporary_path.unlink(missing_ok=True)
            return False, "دیتابیس هنگام کپی تغییر کرده یا باز شده است.", None

        # جایگزینی اتمی: در صورت شکست کپی، نسخه قبلی دست‌نخورده می‌ماند.
        temporary_path.replace(backup_path)
        temporary_path = None
        return True, "پشتیبان‌گیری انجام شد.", backup_path

    except Exception as exc:
        return False, str(exc), None
    finally:
        if temporary_path is not None:
            try:
                temporary_path.unlink(missing_ok=True)
            except OSError:
                pass
