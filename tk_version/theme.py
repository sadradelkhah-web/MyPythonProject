"""قالب مدرن و فارسی برنامه Tkinter."""
from __future__ import annotations

import tkinter as tk
from tkinter import ttk


COLORS = {
    "background": "#F3F6FB",
    "surface": "#FFFFFF",
    "primary": "#2457C5",
    "primary_hover": "#1947A8",
    "text": "#17243A",
    "muted": "#68778D",
    "border": "#DCE4F0",
    "danger": "#C0392B",
}


def apply_theme(root: tk.Tk) -> None:
    root.configure(bg=COLORS["background"])
    style = ttk.Style(root)
    try:
        style.theme_use("clam")
    except tk.TclError:
        pass
    style.configure("TFrame", background=COLORS["background"])
    style.configure("Surface.TFrame", background=COLORS["surface"])
    style.configure("TLabel", background=COLORS["background"], foreground=COLORS["text"], font=("Tahoma", 10))
    style.configure("Title.TLabel", font=("Tahoma", 19, "bold"), foreground=COLORS["text"])
    style.configure("Muted.TLabel", foreground=COLORS["muted"], font=("Tahoma", 9))
    style.configure("TEntry", padding=(10, 9), font=("Tahoma", 11), fieldbackground=COLORS["surface"])
    style.configure("Primary.TButton", font=("Tahoma", 10, "bold"), padding=(16, 10), background=COLORS["primary"], foreground="#FFFFFF")
    style.map("Primary.TButton", background=[("active", COLORS["primary_hover"]), ("pressed", COLORS["primary_hover"])])
    style.configure("TButton", font=("Tahoma", 10), padding=(12, 8))
    style.configure("TSeparator", background=COLORS["border"])
