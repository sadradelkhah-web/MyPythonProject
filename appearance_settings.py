"""Global default and per-user visual preferences for the PySide6 application.

The application defaults are stored separately from overrides belonging to each
account, using tbluser.userid as the per-user key.
"""
from copy import deepcopy

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QMessageBox,
)

from db_config import get_connection


DEFAULT_APPEARANCE_SETTINGS = {
    "theme": "light",
    "font_family": "B Nazanin",
    "font_size": 11,
    "accent_color": "#1976D2",
    "table_row_height": 34,
    "alternating_rows": True,
}

ACCENT_OPTIONS = [
    ("آبی", "#1976D2"),
    ("سبز", "#2E7D32"),
    ("بنفش", "#6A1B9A"),
    ("فیروزه‌ای", "#00838F"),
    ("نارنجی", "#EF6C00"),
]


def installed_font_families():
    """Return the font families available to Qt on this computer."""
    try:
        families = QFontDatabase().families()
    except Exception:
        families = []

    # Keep the actual names returned by Windows/Qt, while removing duplicates.
    unique = {}
    for family in families:
        name = str(family).strip()
        if name:
            unique.setdefault(name.casefold(), name)

    result = sorted(unique.values(), key=str.casefold)
    if result:
        return result

    # Safe fallback for unusual environments where Qt cannot enumerate fonts.
    return ["Arial", "B Nazanin", "Calibri", "Segoe UI", "Tahoma"]


def _default_available_font(families=None):
    families = list(families or installed_font_families())
    by_casefold = {name.casefold(): name for name in families}
    for preferred in ("B Nazanin", "Tahoma", "Segoe UI", "Arial", "Calibri"):
        if preferred.casefold() in by_casefold:
            return by_casefold[preferred.casefold()]
    return families[0] if families else "Sans Serif"


def _clean_settings(values=None):
    settings = deepcopy(DEFAULT_APPEARANCE_SETTINGS)
    if isinstance(values, dict):
        settings.update(values)
    if settings.get("theme") not in ("light", "dark"):
        settings["theme"] = "light"
    available_fonts = installed_font_families()
    available_by_casefold = {name.casefold(): name for name in available_fonts}
    requested_font = str(settings.get("font_family") or "").strip()
    if requested_font.casefold() in available_by_casefold:
        # Use the canonical family spelling reported by this computer.
        settings["font_family"] = available_by_casefold[requested_font.casefold()]
    else:
        # A font chosen on another computer may not be installed here.
        settings["font_family"] = _default_available_font(available_fonts)
    try:
        settings["font_size"] = max(9, min(16, int(settings["font_size"])))
    except (TypeError, ValueError):
        settings["font_size"] = DEFAULT_APPEARANCE_SETTINGS["font_size"]
    valid_colors = {color for _, color in ACCENT_OPTIONS}
    if settings.get("accent_color") not in valid_colors:
        settings["accent_color"] = DEFAULT_APPEARANCE_SETTINGS["accent_color"]
    try:
        settings["table_row_height"] = int(settings["table_row_height"])
    except (TypeError, ValueError):
        settings["table_row_height"] = DEFAULT_APPEARANCE_SETTINGS["table_row_height"]
    if settings["table_row_height"] not in (28, 34, 42):
        settings["table_row_height"] = 34
    settings["alternating_rows"] = bool(settings.get("alternating_rows", True))
    return settings


def _ensure_settings_table(connection, cursor):
    """Create the preferences table when upgrading an existing Access database."""
    try:
        cursor.execute("SELECT TOP 1 [userid] FROM [tblUserAppearanceSettings]")
        return
    except Exception:
        pass

    try:
        cursor.execute("""
            CREATE TABLE [tblUserAppearanceSettings] (
                [userid] LONG NOT NULL,
                [theme] TEXT(12),
                [font_family] TEXT(64),
                [font_size] INTEGER,
                [accent_color] TEXT(16),
                [table_row_height] INTEGER,
                [alternating_rows] BIT,
                CONSTRAINT [PK_tblUserAppearanceSettings] PRIMARY KEY ([userid])
            )
        """)
        connection.commit()
    except Exception:
        # If another session created it at the same time, the verification query
        # succeeds. Otherwise the original database error is re-raised.
        cursor.execute("SELECT TOP 1 [userid] FROM [tblUserAppearanceSettings]")


def _ensure_defaults_table(connection, cursor):
    """Create the single-row application-defaults table when needed."""
    try:
        cursor.execute("SELECT TOP 1 [setting_id] FROM [tblAppAppearanceDefaults]")
        return
    except Exception:
        pass

    try:
        cursor.execute("""
            CREATE TABLE [tblAppAppearanceDefaults] (
                [setting_id] LONG NOT NULL,
                [theme] TEXT(12),
                [font_family] TEXT(64),
                [font_size] INTEGER,
                [accent_color] TEXT(16),
                [table_row_height] INTEGER,
                [alternating_rows] BIT,
                CONSTRAINT [PK_tblAppAppearanceDefaults] PRIMARY KEY ([setting_id])
            )
        """)
        connection.commit()
    except Exception:
        cursor.execute("SELECT TOP 1 [setting_id] FROM [tblAppAppearanceDefaults]")


def load_default_appearance_settings():
    """Load the administrator-defined defaults; use built-in values on first run."""
    settings = deepcopy(DEFAULT_APPEARANCE_SETTINGS)
    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        _ensure_defaults_table(connection, cursor)
        cursor.execute("""
            SELECT [theme], [font_family], [font_size], [accent_color],
                   [table_row_height], [alternating_rows]
            FROM [tblAppAppearanceDefaults]
            WHERE [setting_id] = 1
        """)
        row = cursor.fetchone()
        if row:
            settings.update({
                "theme": row[0] or settings["theme"],
                "font_family": row[1] or settings["font_family"],
                "font_size": row[2] if row[2] is not None else settings["font_size"],
                "accent_color": row[3] or settings["accent_color"],
                "table_row_height": row[4] if row[4] is not None else settings["table_row_height"],
                "alternating_rows": row[5] if row[5] is not None else settings["alternating_rows"],
            })
        else:
            cursor.execute("""
                INSERT INTO [tblAppAppearanceDefaults]
                ([setting_id], [theme], [font_family], [font_size], [accent_color],
                 [table_row_height], [alternating_rows])
                VALUES (1, ?, ?, ?, ?, ?, ?)
            """, (
                settings["theme"], settings["font_family"], settings["font_size"],
                settings["accent_color"], settings["table_row_height"],
                settings["alternating_rows"],
            ))
            connection.commit()
    except Exception:
        # The application must remain usable even if Access cannot store preferences.
        pass
    finally:
        if cursor is not None:
            try:
                cursor.close()
            except Exception:
                pass
        if connection is not None:
            try:
                connection.close()
            except Exception:
                pass
    return _clean_settings(settings)


def save_default_appearance_settings(values):
    """Save the defaults used by new/un-customized accounts."""
    settings = _clean_settings(values)
    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        _ensure_defaults_table(connection, cursor)
        cursor.execute(
            "SELECT [setting_id] FROM [tblAppAppearanceDefaults] WHERE [setting_id] = 1"
        )
        exists = cursor.fetchone() is not None
        if exists:
            cursor.execute("""
                UPDATE [tblAppAppearanceDefaults]
                SET [theme] = ?, [font_family] = ?, [font_size] = ?,
                    [accent_color] = ?, [table_row_height] = ?,
                    [alternating_rows] = ?
                WHERE [setting_id] = 1
            """, (
                settings["theme"], settings["font_family"], settings["font_size"],
                settings["accent_color"], settings["table_row_height"],
                settings["alternating_rows"],
            ))
        else:
            cursor.execute("""
                INSERT INTO [tblAppAppearanceDefaults]
                ([setting_id], [theme], [font_family], [font_size], [accent_color],
                 [table_row_height], [alternating_rows])
                VALUES (1, ?, ?, ?, ?, ?, ?)
            """, (
                settings["theme"], settings["font_family"], settings["font_size"],
                settings["accent_color"], settings["table_row_height"],
                settings["alternating_rows"],
            ))
        connection.commit()
    except Exception:
        if connection is not None:
            try:
                connection.rollback()
            except Exception:
                pass
        raise
    finally:
        if cursor is not None:
            try:
                cursor.close()
            except Exception:
                pass
        if connection is not None:
            try:
                connection.close()
            except Exception:
                pass
    return settings


def reset_user_appearance_settings(userid):
    """Remove a user's override so the account inherits current application defaults."""
    try:
        user_id = int(userid)
    except (TypeError, ValueError) as exc:
        raise ValueError("شناسه کاربر معتبر نیست؛ تنظیمات بازنشانی نشد.") from exc

    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        _ensure_settings_table(connection, cursor)
        cursor.execute(
            "DELETE FROM [tblUserAppearanceSettings] WHERE [userid] = ?",
            (user_id,),
        )
        connection.commit()
    except Exception:
        if connection is not None:
            try:
                connection.rollback()
            except Exception:
                pass
        raise
    finally:
        if cursor is not None:
            try:
                cursor.close()
            except Exception:
                pass
        if connection is not None:
            try:
                connection.close()
            except Exception:
                pass


def load_user_appearance_settings(userid):
    """Load personal overrides on top of the administrator-defined defaults."""
    settings = load_default_appearance_settings()
    try:
        user_id = int(userid)
    except (TypeError, ValueError):
        return settings

    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        _ensure_settings_table(connection, cursor)
        cursor.execute("""
            SELECT [theme], [font_family], [font_size], [accent_color],
                   [table_row_height], [alternating_rows]
            FROM [tblUserAppearanceSettings]
            WHERE [userid] = ?
        """, (user_id,))
        row = cursor.fetchone()
        if row:
            settings.update({
                "theme": row[0] or settings["theme"],
                "font_family": row[1] or settings["font_family"],
                "font_size": row[2] if row[2] is not None else settings["font_size"],
                "accent_color": row[3] or settings["accent_color"],
                "table_row_height": row[4] if row[4] is not None else settings["table_row_height"],
                "alternating_rows": row[5] if row[5] is not None else settings["alternating_rows"],
            })
    except Exception:
        # Keep the app usable with defaults if preferences are unavailable.
        pass
    finally:
        if cursor is not None:
            try:
                cursor.close()
            except Exception:
                pass
        if connection is not None:
            try:
                connection.close()
            except Exception:
                pass
    return _clean_settings(settings)


def save_user_appearance_settings(userid, values):
    """Insert or update preferences for one user account."""
    try:
        user_id = int(userid)
    except (TypeError, ValueError) as exc:
        raise ValueError("شناسه کاربر معتبر نیست؛ تنظیمات ذخیره نشد.") from exc

    settings = _clean_settings(values)
    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        _ensure_settings_table(connection, cursor)
        cursor.execute(
            "SELECT [userid] FROM [tblUserAppearanceSettings] WHERE [userid] = ?",
            (user_id,),
        )
        exists = cursor.fetchone() is not None
        if exists:
            cursor.execute("""
                UPDATE [tblUserAppearanceSettings]
                SET [theme] = ?, [font_family] = ?, [font_size] = ?,
                    [accent_color] = ?, [table_row_height] = ?,
                    [alternating_rows] = ?
                WHERE [userid] = ?
            """, (
                settings["theme"], settings["font_family"], settings["font_size"],
                settings["accent_color"], settings["table_row_height"],
                settings["alternating_rows"], user_id,
            ))
        else:
            cursor.execute("""
                INSERT INTO [tblUserAppearanceSettings]
                ([userid], [theme], [font_family], [font_size], [accent_color],
                 [table_row_height], [alternating_rows])
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                user_id, settings["theme"], settings["font_family"],
                settings["font_size"], settings["accent_color"],
                settings["table_row_height"], settings["alternating_rows"],
            ))
        connection.commit()
    except Exception:
        if connection is not None:
            try:
                connection.rollback()
            except Exception:
                pass
        raise
    finally:
        if cursor is not None:
            try:
                cursor.close()
            except Exception:
                pass
        if connection is not None:
            try:
                connection.close()
            except Exception:
                pass
    return settings


class UserAppearanceDialog(QDialog):
    """Appearance settings dialog with an explicit temporary-preview action."""

    previewRequested = Signal(dict)

    def __init__(
        self, parent=None, settings=None, *, title="تنظیمات ظاهری من",
        intro_text=None, reset_settings=None, reset_means_inherit=False,
        reset_button_text="بازگشت به پیش‌فرض",
    ):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.setMinimumWidth(430)
        self._settings = _clean_settings(settings)
        self._reset_settings = _clean_settings(
            reset_settings if reset_settings is not None else load_default_appearance_settings()
        )
        self._reset_means_inherit = bool(reset_means_inherit)
        self.reset_to_inherit = False

        root = QVBoxLayout(self)
        root.setContentsMargins(18, 18, 18, 18)
        root.setSpacing(12)

        intro = QLabel(
            intro_text or
            "این تنظیمات فقط برای حساب کاربری شما ذخیره می‌شود و روی ظاهر حساب‌های دیگر اثر ندارد."
        )
        intro.setWordWrap(True)
        root.addWidget(intro)

        form = QFormLayout()
        form.setSpacing(10)
        root.addLayout(form)

        self.cmbTheme = QComboBox(self)
        self.cmbTheme.addItem("روشن", "light")
        self.cmbTheme.addItem("تیره", "dark")
        form.addRow("پوسته برنامه:", self.cmbTheme)

        self.cmbFontFamily = QComboBox(self)
        # The list is generated on each computer from its locally installed fonts.
        self.cmbFontFamily.addItems(installed_font_families())
        form.addRow("نوع قلم (فونت‌های نصب‌شده):", self.cmbFontFamily)

        self.spinFontSize = QSpinBox(self)
        self.spinFontSize.setRange(9, 16)
        self.spinFontSize.setSuffix(" pt")
        form.addRow("اندازه قلم:", self.spinFontSize)

        self.cmbAccent = QComboBox(self)
        for label, color in ACCENT_OPTIONS:
            self.cmbAccent.addItem(label, color)
        form.addRow("رنگ تأکیدی:", self.cmbAccent)

        self.cmbRowHeight = QComboBox(self)
        self.cmbRowHeight.addItem("فشرده", 28)
        self.cmbRowHeight.addItem("استاندارد", 34)
        self.cmbRowHeight.addItem("درشت و خوانا", 42)
        form.addRow("ارتفاع ردیف‌های جدول:", self.cmbRowHeight)

        self.chkAlternatingRows = QCheckBox("رنگ متفاوت برای ردیف‌های یکی‌درمیان جدول‌ها", self)
        form.addRow("", self.chkAlternatingRows)

        actions = QHBoxLayout()
        self.btnDefaults = QPushButton(reset_button_text)
        self.btnDefaults.clicked.connect(self.reset_defaults)
        actions.addWidget(self.btnDefaults)
        actions.addStretch(1)
        root.addLayout(actions)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save | QDialogButtonBox.StandardButton.Cancel,
            parent=self,
        )
        buttons.button(QDialogButtonBox.StandardButton.Save).setText("ذخیره")
        buttons.button(QDialogButtonBox.StandardButton.Cancel).setText("انصراف")

        # پیش‌نمایش فقط ظاهر را موقتاً در پنجره اصلی تغییر می‌دهد؛ چیزی ذخیره نمی‌کند.
        self.btnPreview = QPushButton("اعمال آزمایشی", self)
        self.btnPreview.setToolTip(
            "ظاهر انتخاب‌شده را موقتاً روی برنامه اعمال می‌کند؛ برای ماندگاری روی «ذخیره» بزنید."
        )
        buttons.addButton(self.btnPreview, QDialogButtonBox.ButtonRole.ActionRole)
        self.btnPreview.clicked.connect(
            lambda checked=False: self.previewRequested.emit(self.selected_settings())
        )

        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        root.addWidget(buttons)

        if self._settings["theme"] == "dark":
            dialog_background = "#20252D"
            dialog_text = "#E7ECF2"
            control_background = "#252C35"
            dialog_border = "#4B5664"
        else:
            dialog_background = "#FFFFFF"
            dialog_text = "#263445"
            control_background = "#FFFFFF"
            dialog_border = "#C7D0DB"
        dialog_accent = self._settings["accent_color"]
        dialog_font_family = self._settings["font_family"].replace('"', "")
        dialog_font_size = self._settings["font_size"]
        self.setFont(QFont(dialog_font_family, dialog_font_size))
        self.setStyleSheet(f"""
            QDialog {{ background: {dialog_background}; color: {dialog_text}; font-family: "{dialog_font_family}"; font-size: {dialog_font_size}pt; }}
            QLabel {{ color: {dialog_text}; font-family: "{dialog_font_family}"; font-size: {dialog_font_size}pt; }}
            QComboBox, QSpinBox, QCheckBox, QPushButton, QDialogButtonBox {{
                font-family: "{dialog_font_family}"; font-size: {dialog_font_size}pt;
            }}
            QComboBox, QSpinBox {{
                min-height: 30px; padding: 3px 6px;
                background: {control_background}; color: {dialog_text};
                border: 1px solid {dialog_border}; border-radius: 4px;
            }}
            QComboBox:focus, QSpinBox:focus {{ border: 1px solid {dialog_accent}; }}
            QPushButton {{
                min-height: 32px; padding: 4px 10px;
                background: {control_background}; color: {dialog_text};
                border: 1px solid {dialog_border}; border-radius: 4px;
            }}
            QPushButton:hover {{ border-color: {dialog_accent}; }}
        """)
        self._populate(self._settings)
        self.cmbTheme.currentIndexChanged.connect(self._mark_custom_settings)
        self.cmbFontFamily.currentIndexChanged.connect(self._mark_custom_settings)
        self.spinFontSize.valueChanged.connect(self._mark_custom_settings)
        self.cmbAccent.currentIndexChanged.connect(self._mark_custom_settings)
        self.cmbRowHeight.currentIndexChanged.connect(self._mark_custom_settings)
        self.chkAlternatingRows.toggled.connect(self._mark_custom_settings)

    def _mark_custom_settings(self, *_):
        self.reset_to_inherit = False

    def _populate(self, settings):
        index = self.cmbTheme.findData(settings["theme"])
        self.cmbTheme.setCurrentIndex(max(0, index))
        index = self.cmbFontFamily.findText(settings["font_family"])
        self.cmbFontFamily.setCurrentIndex(max(0, index))
        self.spinFontSize.setValue(settings["font_size"])
        index = self.cmbAccent.findData(settings["accent_color"])
        self.cmbAccent.setCurrentIndex(max(0, index))
        index = self.cmbRowHeight.findData(settings["table_row_height"])
        self.cmbRowHeight.setCurrentIndex(max(0, index))
        self.chkAlternatingRows.setChecked(settings["alternating_rows"])

    def reset_defaults(self):
        self._populate(self._reset_settings)
        self.reset_to_inherit = self._reset_means_inherit

    def selected_settings(self):
        return _clean_settings({
            "theme": self.cmbTheme.currentData(),
            "font_family": self.cmbFontFamily.currentText(),
            "font_size": self.spinFontSize.value(),
            "accent_color": self.cmbAccent.currentData(),
            "table_row_height": self.cmbRowHeight.currentData(),
            "alternating_rows": self.chkAlternatingRows.isChecked(),
        })


def appearance_stylesheet(settings):
    """QSS override appended to the existing main.ui style without discarding it."""
    settings = _clean_settings(settings)
    accent = settings["accent_color"]
    font_family = settings["font_family"].replace('"', "")
    font_size = settings["font_size"]
    header_size = min(font_size + 1, 18)
    tab_size = min(font_size + 2, 20)

    if settings["theme"] == "dark":
        background = "#20252D"
        panel = "#272E37"
        input_background = "#252C35"
        text = "#E7ECF2"
        muted = "#B8C3D0"
        border = "#4B5664"
        alternate = "#2D3540"
        hover = "#364252"
        selected_text = "#FFFFFF"
        qss = f"""
            QWidget {{ background-color: {background}; color: {text}; }}
            QMainWindow, QDialog {{ background-color: {background}; color: {text}; }}
            QFrame#navigationPanel {{ background-color: {panel}; border: 1px solid {border}; border-radius: 8px; }}
            QFrame#navigationPanel QLabel {{ color: {text}; }}
            QPushButton {{ background-color: {panel}; color: {text}; border: 1px solid {border}; border-radius: 5px; }}
            QPushButton:hover {{ background-color: {hover}; border-color: {accent}; }}
            QPushButton:pressed {{ background-color: {accent}; color: {selected_text}; }}
            QLineEdit, QComboBox, QSpinBox, QDateEdit, QPlainTextEdit, QTextEdit, QTableWidget, QListWidget {{
                background-color: {input_background}; color: {text}; border: 1px solid {border}; selection-background-color: {accent}; selection-color: {selected_text};
            }}
            QHeaderView::section {{ background-color: {panel}; color: {text}; border: 1px solid {border}; }}
            QTableWidget {{ background-color: {input_background}; alternate-background-color: {alternate}; gridline-color: {border}; selection-background-color: {accent}; selection-color: {selected_text}; }}
            QTabBar::tab {{ background-color: {panel}; color: {text}; border: 1px solid {border}; }}
            QTabBar::tab:selected {{ background-color: {background}; color: {accent}; border-top: 3px solid {accent}; }}
            QTabWidget::pane {{ border: 1px solid {border}; background-color: {background}; }}
            QGroupBox {{ color: {text}; border: 1px solid {border}; }}
            QMenuBar, QMenu {{ background-color: {panel}; color: {text}; }}
            QMenu::item:selected {{ background-color: {accent}; color: {selected_text}; }}
            QStatusBar {{ background-color: {panel}; color: {text}; }}
            QToolTip {{ background-color: {panel}; color: {text}; border: 1px solid {border}; }}
        """
    else:
        background = "#FFFFFF"
        text = "#263445"
        border = "#C7D0DB"
        hover = "#DCEAF8"
        tint = {
            "#1976D2": "#D7E9FA",
            "#2E7D32": "#DDF1E0",
            "#6A1B9A": "#EBDDFA",
            "#00838F": "#D6F1F2",
            "#EF6C00": "#FCE8D8",
        }.get(accent, "#D7E9FA")
        qss = f"""
            QPushButton:hover {{ border-color: {accent}; background-color: {hover}; }}
            QPushButton:focus {{ border-color: {accent}; }}
            QLineEdit:focus, QComboBox:focus, QSpinBox:focus, QDateEdit:focus, QPlainTextEdit:focus, QTextEdit:focus {{
                border: 1px solid {accent};
            }}
            QTabBar::tab:selected {{ color: {accent}; border-top: 3px solid {accent}; }}
            QTableWidget::item:selected {{ background-color: {tint}; color: {text}; }}
            QHeaderView::section {{ border-color: {border}; }}
        """

    font_qss = f"""
        QWidget, QMenu, QMenuBar, QStatusBar {{
            font-family: "{font_family}";
        }}
        QLabel, QLineEdit, QComboBox, QSpinBox, QDateEdit, QDateTimeEdit,
        QPlainTextEdit, QTextEdit, QPushButton, QToolButton, QCheckBox,
        QRadioButton, QTableWidget, QTableView, QTreeWidget, QTreeView,
        QListWidget, QHeaderView::section, QMenuBar, QMenu, QStatusBar,
        QComboBox QAbstractItemView {{
            font-family: "{font_family}"; font-size: {font_size}pt;
        }}
        QGroupBox {{ font-family: "{font_family}"; font-size: {header_size}pt; }}
        QTabBar::tab {{ font-family: "{font_family}"; font-size: {tab_size}pt; }}
        QMenu::item {{ font-family: "{font_family}"; font-size: {font_size}pt; }}
    """
    return qss + font_qss
