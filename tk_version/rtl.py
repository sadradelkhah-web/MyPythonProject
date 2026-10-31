"""ابزارهای نمایش راست‌به‌چپ برای رابط فارسی Tkinter.

رشته اصلی داده‌ها هرگز در این ماژول تغییر نمی‌کند؛ فقط متن نمایشی شکل‌دهی می‌شود.
برای پشتیبانی بهتر از حروف فارسی، arabic-reshaper و python-bidi پیشنهاد می‌شوند.
"""
from __future__ import annotations

try:
    import arabic_reshaper
    from bidi.algorithm import get_display
except ImportError:  # امکان اجرای پایه بدون وابستگی اختیاری
    arabic_reshaper = None
    get_display = None


def rtl_text(value: object) -> str:
    """متن را فقط برای نمایش در ویجت‌های غیرقابل‌ویرایش آماده می‌کند."""
    text = "" if value is None else str(value)
    if arabic_reshaper is None or get_display is None:
        return text
    try:
        return get_display(arabic_reshaper.reshape(text))
    except Exception:
        return text


def configure_rtl_widget(widget, *, justify: str = "right") -> None:
    """تنظیمات عمومی راست‌چین؛ از تغییر مقدار ذخیره‌شده خودداری می‌شود."""
    try:
        widget.configure(justify=justify)
    except Exception:
        pass
    try:
        widget.configure(anchor="e")
    except Exception:
        pass
