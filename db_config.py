import os
from pathlib import Path

import pyodbc
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / ".env"

load_dotenv(ENV_FILE)


DB_PATH = os.getenv("DB_PATH")
DB_PASSWORD = os.getenv("DB_PASSWORD")


if not DB_PATH:
    raise RuntimeError("DB_PATH در فایل .env تعریف نشده است.")

if not DB_PASSWORD:
    raise RuntimeError("DB_PASSWORD در فایل .env تعریف نشده است.")


def get_connection():

    connection_string = (
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
        rf"DBQ={DB_PATH};"
        rf"PWD={DB_PASSWORD};"
    )

    return pyodbc.connect(connection_string)