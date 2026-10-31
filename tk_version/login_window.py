"""پنجره ورود نسخه Tkinter؛ احراز هویت با همان جدول tbluser نسخه فعلی."""
from __future__ import annotations

import hashlib
import hmac
import os
import tkinter as tk
from tkinter import messagebox, ttk

from db_config import get_connection
from user_activity_log import log_user_event
from .rtl import rtl_text
from .theme import COLORS


def _hash_password(plain: str) -> str:
    iterations = 260000
    salt = os.urandom(16)
    digest = hashlib.pbkdf2_hmac("sha256", plain.encode("utf-8"), salt, iterations)
    return f"pbkdf2:{iterations}:{salt.hex()}:{digest.hex()}"


def _verify_password(plain: str, stored: str) -> bool:
    stored = str(stored or "")
    if stored.startswith("pbkdf2:"):
        try:
            _, iterations_text, salt_hex, digest_hex = stored.split(":", 3)
            digest = hashlib.pbkdf2_hmac("sha256", plain.encode("utf-8"), bytes.fromhex(salt_hex), int(iterations_text))
            return hmac.compare_digest(digest, bytes.fromhex(digest_hex))
        except (ValueError, TypeError):
            return False
    return hmac.compare_digest(plain, stored)


class LoginWindow:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.current_user = None
        self.root.title("ورود به سامانه مدیریت درخواست‌های تعمیرات")
        self.root.geometry("480x570")
        self.root.minsize(420, 520)
        self.root.configure(bg=COLORS["background"])
        self.root.protocol("WM_DELETE_WINDOW", self.root.destroy)
        self._build()

    def _build(self) -> None:
        outer = ttk.Frame(self.root, padding=26)
        outer.pack(fill="both", expand=True)
        card = ttk.Frame(outer, style="Surface.TFrame", padding=(30, 32))
        card.pack(fill="both", expand=True)

        ttk.Label(card, text=rtl_text("سامانه مدیریت درخواست‌های تعمیرات"), style="Title.TLabel", anchor="e", justify="right").pack(fill="x", pady=(8, 8))
        ttk.Label(card, text=rtl_text("برای ورود، اطلاعات کاربری خود را وارد کنید"), style="Muted.TLabel", anchor="e", justify="right").pack(fill="x", pady=(0, 28))

        ttk.Label(card, text=rtl_text("نام کاربری"), anchor="e", justify="right").pack(fill="x", pady=(0, 7))
        self.username = ttk.Entry(card, justify="right")
        self.username.pack(fill="x", ipady=3, pady=(0, 18))

        ttk.Label(card, text=rtl_text("رمز عبور"), anchor="e", justify="right").pack(fill="x", pady=(0, 7))
        self.password = ttk.Entry(card, show="●", justify="right")
        self.password.pack(fill="x", ipady=3, pady=(0, 24))

        self.login_button = ttk.Button(card, text=rtl_text("ورود به سامانه"), style="Primary.TButton", command=self.login)
        self.login_button.pack(fill="x")
        ttk.Button(card, text=rtl_text("خروج"), command=self.root.destroy).pack(fill="x", pady=(10, 0))
        ttk.Label(card, text=rtl_text("نسخه آزمایشی رابط Tkinter"), style="Muted.TLabel", anchor="center").pack(fill="x", side="bottom", pady=(30, 0))

        self.username.focus_set()
        self.password.bind("<Return>", lambda _event: self.login())
        self.username.bind("<Return>", lambda _event: self.password.focus_set())

    def login(self) -> None:
        username = self.username.get().strip()
        password = self.password.get()
        if not username:
            messagebox.showwarning("ورود", "نام کاربری را وارد کنید.", parent=self.root)
            self.username.focus_set()
            return
        if not password:
            messagebox.showwarning("ورود", "رمز عبور را وارد کنید.", parent=self.root)
            self.password.focus_set()
            return

        connection = cursor = None
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("""SELECT [userid], [username], [UserLogin], [password], [usersecurity], [Samat], [vahed], [Userlevel]
                             FROM [tbluser] WHERE [UserLogin] = ?""", (username,))
            user = cursor.fetchone()
            if user is None or not _verify_password(password, str(user[3] or "")):
                log_user_event(username, "Login", "ورود", "تلاش ناموفق برای ورود؛ نام کاربری یا رمز عبور نامعتبر", result="Failed", connection=connection)
                try:
                    connection.commit()
                except Exception:
                    pass
                messagebox.showwarning("ورود ناموفق", "نام کاربری یا رمز عبور صحیح نیست.", parent=self.root)
                self.password.delete(0, "end")
                self.password.focus_set()
                return

            stored = str(user[3] or "")
            if not stored.startswith("pbkdf2:"):
                try:
                    cursor.execute("UPDATE [tbluser] SET [password] = ? WHERE [UserLogin] = ?", (_hash_password(password), username))
                    connection.commit()
                except Exception:
                    pass

            self.current_user = {
                "userid": user[0], "username": user[1], "UserLogin": user[2],
                "usersecurity": user[4], "Samat": user[5], "vahed": user[6], "Userlevel": user[7],
            }
            log_user_event(str(self.current_user.get("username") or username), "Login", "ورود", "ورود موفق به سامانه", result="Success", connection=connection)
            try:
                connection.commit()
            except Exception:
                pass
            self.root.destroy()
        except Exception as exc:
            messagebox.showerror("خطای اتصال", f"اتصال به پایگاه داده یا بررسی اطلاعات ورود با خطا مواجه شد:\n\n{exc}", parent=self.root)
        finally:
            if cursor is not None:
                try: cursor.close()
                except Exception: pass
            if connection is not None:
                try: connection.close()
                except Exception: pass
