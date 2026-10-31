"""نقطه شروع نسخه آزمایشی Tkinter.
اجرا از ریشه پروژه: python -m tk_version.app
"""
from __future__ import annotations

import tkinter as tk

from .login_window import LoginWindow
from .main_window import MainWindow
from .theme import apply_theme


def main() -> int:
    root = tk.Tk()
    apply_theme(root)
    login = LoginWindow(root)
    root.mainloop()
    if login.current_user is None:
        return 0

    main_root = tk.Tk()
    apply_theme(main_root)
    MainWindow(main_root, login.current_user)
    main_root.mainloop()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
