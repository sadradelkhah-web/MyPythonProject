"""پنجره اصلی نسخه Tkinter و ناوبری بین بخش‌های سامانه."""
from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from .rtl import rtl_text
from .theme import COLORS
from .request_page import RequestPage


UNIT_NAMES = {
    "tamerat": "تعمیرات عمومی",
    "kala": "عملیات کالا",
    "khadamat": "خدمات اداری و اجتماعی",
    "hse": "ایمنی",
    "harasat": "حراست",
}


class MainWindow:
    def __init__(self, root: tk.Tk, current_user: dict):
        self.root = root
        self.current_user = current_user or {}
        self.request_page = None
        self.root.title("سامانه مدیریت درخواست‌های تعمیرات")
        self.root.state("zoomed")
        self.root.minsize(1100, 700)
        self._build_shell()
        # اولین بخش عملیاتی منتقل‌شده پس از ورود باز می‌شود.
        self.show_requests()

    def _build_shell(self) -> None:
        self.root.configure(bg=COLORS["background"])
        header = ttk.Frame(self.root, padding=(22, 14), style="Surface.TFrame")
        header.pack(fill="x")
        name = self.current_user.get("username") or self.current_user.get("UserLogin") or "کاربر"
        unit_key = str(self.current_user.get("vahed") or "").strip().lower()
        unit = UNIT_NAMES.get(unit_key, str(self.current_user.get("vahed") or "نامشخص"))
        ttk.Label(
            header, text=rtl_text("سامانه مدیریت درخواست‌های تعمیرات"),
            style="Title.TLabel", anchor="e",
        ).pack(side="right", fill="x", expand=True)
        ttk.Label(
            header, text=rtl_text(f"کاربر: {name}  |  واحد: {unit}"),
            anchor="e", justify="right",
        ).pack(side="left", padx=(12, 0))

        body = ttk.Frame(self.root, padding=18)
        body.pack(fill="both", expand=True)
        sidebar = ttk.Frame(body, style="Surface.TFrame", padding=14)
        sidebar.pack(side="right", fill="y", padx=(14, 0))
        self.content = ttk.Frame(body, style="Surface.TFrame", padding=18)
        self.content.pack(side="left", fill="both", expand=True)

        ttk.Label(
            sidebar, text=rtl_text("منوی سامانه"),
            font=("Tahoma", 12, "bold"), background=COLORS["surface"], anchor="e",
        ).pack(fill="x", pady=(4, 16))

        ttk.Button(
            sidebar, text=rtl_text("ثبت و مشاهده درخواست‌ها"),
            style="Primary.TButton", command=self.show_requests,
        ).pack(fill="x", pady=4)

        for label in ("گزارش‌ها", "اموال", "مهمانسرا", "لوازم‌التحریر", "مدیریت کاربران", "تنظیمات ظاهر"):
            ttk.Button(
                sidebar, text=rtl_text(label),
                command=lambda item=label: self.show_placeholder(item),
            ).pack(fill="x", pady=4)

        ttk.Separator(sidebar).pack(fill="x", pady=12)
        ttk.Button(sidebar, text=rtl_text("خروج از برنامه"), command=self.root.destroy).pack(fill="x")

        self.page_title = ttk.Label(
            self.content, text=rtl_text("درخواست‌های تعمیرات"),
            style="Title.TLabel", anchor="e",
        )
        self.page_title.pack(fill="x", pady=(0, 12))
        self.page_body = ttk.Frame(self.content, style="Surface.TFrame")
        self.page_body.pack(fill="both", expand=True)

    def _clear_page(self) -> None:
        for child in self.page_body.winfo_children():
            child.destroy()
        self.request_page = None

    def show_requests(self) -> None:
        self._clear_page()
        self.page_title.configure(text=rtl_text("ثبت و مشاهده درخواست‌های تعمیرات"))
        self.request_page = RequestPage(self.page_body, self.current_user)
        self.request_page.pack(fill="both", expand=True)

    def show_placeholder(self, title: str) -> None:
        self._clear_page()
        self.page_title.configure(text=rtl_text(title))
        ttk.Label(
            self.page_body,
            text=rtl_text("این بخش هنوز از نسخه فعلی منتقل نشده است؛ پس از تکمیل بخش درخواست‌های تعمیرات به آن پرداخته می‌شود."),
            justify="right", anchor="ne", wraplength=900,
        ).pack(fill="both", expand=True, anchor="ne", padx=12, pady=12)
