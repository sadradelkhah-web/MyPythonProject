"""پوسته اولیه پنجره اصلی نسخه Tkinter."""
from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from .rtl import rtl_text
from .theme import COLORS


UNIT_NAMES = {
    "tamerat": "تعمیرات عمومی",
    "kala": "عملیات کالا",
    "khadamat": "خدمات اداری و اجتماعی",
    "hse": "ایمنی",
    "harasat": "حراست",
}


class MainWindow:
    """پوسته اولیه؛ ماژول‌های عملیاتی در مراحل بعدی به آن متصل می‌شوند."""
    def __init__(self, root: tk.Tk, current_user: dict):
        self.root = root
        self.current_user = current_user
        self.root.title("سامانه مدیریت درخواست‌های تعمیرات")
        self.root.state("zoomed")
        self._build_shell()

    def _build_shell(self) -> None:
        self.root.configure(bg=COLORS["background"])
        header = ttk.Frame(self.root, padding=(22, 14), style="Surface.TFrame")
        header.pack(fill="x")
        name = self.current_user.get("username") or self.current_user.get("UserLogin") or "کاربر"
        unit_key = str(self.current_user.get("vahed") or "").strip().lower()
        unit = UNIT_NAMES.get(unit_key, unit_key or "نامشخص")
        ttk.Label(header, text=rtl_text("سامانه مدیریت درخواست‌های تعمیرات"), style="Title.TLabel", anchor="e").pack(side="right", fill="x", expand=True)
        ttk.Label(header, text=rtl_text(f"کاربر: {name}  |  واحد: {unit}"), anchor="e", justify="right").pack(side="left", padx=(12, 0))

        body = ttk.Frame(self.root, padding=22)
        body.pack(fill="both", expand=True)
        sidebar = ttk.Frame(body, style="Surface.TFrame", padding=14)
        sidebar.pack(side="right", fill="y", padx=(14, 0))
        content = ttk.Frame(body, style="Surface.TFrame", padding=24)
        content.pack(side="left", fill="both", expand=True)

        ttk.Label(sidebar, text=rtl_text("منوی سامانه"), font=("Tahoma", 12, "bold"), background=COLORS["surface"], anchor="e").pack(fill="x", pady=(4, 16))
        for label in ("صفحه اصلی", "ثبت درخواست تعمیرات", "گزارش‌ها", "اموال", "مهمانسرا", "لوازم‌التحریر", "مدیریت کاربران", "تنظیمات ظاهر"):
            ttk.Button(sidebar, text=rtl_text(label), command=lambda item=label: self.show_placeholder(item)).pack(fill="x", pady=4)
        ttk.Separator(sidebar).pack(fill="x", pady=12)
        ttk.Button(sidebar, text=rtl_text("خروج از برنامه"), command=self.root.destroy).pack(fill="x")

        self.page_title = ttk.Label(content, text=rtl_text("صفحه اصلی"), style="Title.TLabel", anchor="e")
        self.page_title.pack(fill="x", pady=(0, 14))
        self.page_message = ttk.Label(content, text=rtl_text("پوسته رابط کاربری آماده است. بخش‌های عملیاتی پس از انتقال و آزمایش به این قسمت متصل می‌شوند."), justify="right", anchor="ne", wraplength=900)
        self.page_message.pack(fill="both", expand=True, anchor="ne")

    def show_placeholder(self, title: str) -> None:
        self.page_title.configure(text=rtl_text(title))
        self.page_message.configure(text=rtl_text("این بخش هنوز از نسخه فعلی منتقل نشده است؛ در مراحل بعدی منطق و امکانات آن منتقل خواهد شد."))
