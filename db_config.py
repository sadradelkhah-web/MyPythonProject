import os
from pathlib import Path

import pyodbc
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / ".env"

# مقادیر فایل .env باید بر متغیرهای محیطی قدیمی اولویت داشته باشند.
load_dotenv(ENV_FILE, override=True)

DB_PATH = os.getenv("DB_PATH")
DB_PASSWORD = os.getenv("DB_PASSWORD")


if not DB_PATH:
    raise RuntimeError("DB_PATH در فایل .env تعریف نشده است.")

if not DB_PASSWORD:
    raise RuntimeError("DB_PASSWORD در فایل .env تعریف نشده است.")


def get_connection():
    db_file = Path(DB_PATH)

    if not db_file.is_file():
        raise FileNotFoundError(
            f"فایل پایگاه داده پیدا نشد: {DB_PATH}"
        )

    # قالب‌بندی مقدار PWD برای جلوگیری از تفسیر اشتباه کاراکترهای خاص ODBC
    safe_password = "{" + DB_PASSWORD.replace("}", "}}") + "}"

    connection_string = (
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
        f"DBQ={db_file};"
        f"PWD={safe_password};"
    )

    return pyodbc.connect(connection_string, timeout=15)
