import re
import jdatetime
from datetime import datetime, date as py_date

from PySide6.QtCore import QDate, QDateTime, QTimer, Qt, QStringListModel
from PySide6.QtGui import QAction, QFont, QIcon, QPainter, QPen, QPixmap, QColor, QTextDocument
from PySide6.QtPrintSupport import QPrinter, QPrintDialog
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTabBar,
    QTabWidget,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QComboBox,
    QCompleter,
    QCheckBox,
    QLayout,
    QTableWidget,
    QTableWidgetItem,
    QAbstractItemView,
    QHeaderView,
    QFileDialog,
    QScrollArea,
    QFrame,
)

from ui_main import Ui_MainWindow
from db_config import get_connection
from user_management import UserManagement
from tab_permissions import get_user_permissions, apply_tab_permissions
from user_permissions import open_user_permissions_dialog



PERSIAN_MONTHS = [
    "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور",
    "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"
]
PERSIAN_WEEKDAYS = ["ش", "ی", "د", "س", "چ", "پ", "ج"]


class JalaliCalendarDialog(QDialog):
    """تقویم شمسی سبک و داخلی؛ بدون نیاز به افزونه جداگانه."""
    def __init__(self, parent=None, initial_date=None, on_selected=None):
        super().__init__(parent, Qt.WindowType.Dialog)
        self.setWindowTitle("انتخاب تاریخ شمسی")
        # از Popup استفاده نمی‌کنیم؛ در ویندوز ممکن است هنگام exec فوراً بسته شود.
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setMinimumWidth(330)
        self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.on_selected = on_selected
        try:
            self.current = jdatetime.date(
                int(initial_date[:4]), int(initial_date[4:6]), int(initial_date[6:8])
            ) if initial_date and len(initial_date) == 8 else jdatetime.date.today()
        except Exception:
            self.current = jdatetime.date.today()
        self.year = self.current.year
        self.month = self.current.month
        self._build_ui()
        self._render_days()

    def _build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(10, 10, 10, 10)
        root.setSpacing(8)
        nav = QHBoxLayout()
        self.prev_button = QPushButton("ماه قبل ◀")
        self.next_button = QPushButton("▶ ماه بعد")
        self.month_label = QLabel()
        self.month_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.month_label.setStyleSheet("font-weight: bold; font-size: 14pt;")
        nav.addWidget(self.prev_button)
        nav.addWidget(self.month_label, 1)
        nav.addWidget(self.next_button)
        root.addLayout(nav)
        self.days_grid = QGridLayout()
        self.days_grid.setSpacing(4)
        root.addLayout(self.days_grid)
        bottom = QHBoxLayout()
        today_button = QPushButton("امروز")
        clear_button = QPushButton("پاک کردن")
        bottom.addWidget(today_button)
        bottom.addWidget(clear_button)
        root.addLayout(bottom)
        self.prev_button.clicked.connect(lambda: self._change_month(-1))
        self.next_button.clicked.connect(lambda: self._change_month(1))
        today_button.clicked.connect(self._choose_today)
        clear_button.clicked.connect(self._clear_date)
        self.setStyleSheet("""
            QDialog { background: white; border: 1px solid #9AA8B7; }
            QPushButton { min-width: 32px; min-height: 30px; padding: 3px; }
            QPushButton:hover { background: #DCEBFA; }
        """)

    def _clear_grid(self):
        while self.days_grid.count():
            item = self.days_grid.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    def _render_days(self):
        self._clear_grid()
        self.month_label.setText(f"{PERSIAN_MONTHS[self.month - 1]} {self.year}")
        for col, name in enumerate(PERSIAN_WEEKDAY_HEADERS):
            label = QLabel(str(name))
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label.setStyleSheet("font-weight: bold; color: #245B87;")
            self.days_grid.addWidget(label, 0, col)
        first = jdatetime.date(self.year, self.month, 1)
        if self.month == 12:
            next_month = jdatetime.date(self.year + 1, 1, 1)
        else:
            next_month = jdatetime.date(self.year, self.month + 1, 1)
        day_count = (next_month - first).days
        # jdatetime.weekday: Monday=0; ستون اول تقویم شنبه است.
        start_col = (first.weekday() + 2) % 7
        for day in range(1, day_count + 1):
            button = QPushButton(str(day))
            button.setFixedSize(38, 32)
            if (self.year, self.month, day) == (self.current.year, self.current.month, self.current.day):
                button.setStyleSheet("background: #1976D2; color: white; font-weight: bold;")
            button.clicked.connect(lambda checked=False, d=day: self._choose_day(d))
            index = start_col + day - 1
            self.days_grid.addWidget(button, 1 + index // 7, index % 7)

    def _change_month(self, delta):
        month_index = self.year * 12 + (self.month - 1) + delta
        self.year, month0 = divmod(month_index, 12)
        self.month = month0 + 1
        self._render_days()

    def _choose_day(self, day):
        value = jdatetime.date(self.year, self.month, day).strftime("%Y%m%d")
        if self.on_selected:
            self.on_selected(value)
        self.accept()

    def _choose_today(self):
        self.current = jdatetime.date.today()
        self.year, self.month = self.current.year, self.current.month
        self._choose_day(self.current.day)

    def _clear_date(self):
        if self.on_selected:
            self.on_selected("")
        self.accept()


def replace_widget_in_layout(layout, old_widget, new_widget):
    """جایگزینی مطمئن ویجت حتی وقتی داخل layoutهای تو در تو باشد."""
    if layout is None:
        return False
    for index in range(layout.count()):
        item = layout.itemAt(index)
        if item is None:
            continue
        if item.widget() is old_widget:
            layout.replaceWidget(old_widget, new_widget)
            return True
        child_layout = item.layout()
        if child_layout is not None and replace_widget_in_layout(
            child_layout, old_widget, new_widget
        ):
            return True
    return False


def install_calendar_action(line_edit):
    """اگر جایگزینی ویجت ممکن نبود، تقویم را مستقیماً به همان QLineEdit وصل کن."""
    if line_edit.property("jalaliCalendarActionInstalled"):
        return
    pixmap = QPixmap(18, 18)
    pixmap.fill(Qt.GlobalColor.transparent)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    painter.setPen(QPen(QColor("#245B87"), 1.4))
    painter.setBrush(QColor("#FFFFFF"))
    painter.drawRoundedRect(2, 3, 14, 13, 2, 2)
    painter.drawLine(2, 7, 16, 7)
    painter.drawLine(6, 1, 6, 5)
    painter.drawLine(12, 1, 12, 5)
    painter.setBrush(QColor("#245B87"))
    painter.setPen(Qt.PenStyle.NoPen)
    for x, y in ((5, 9), (9, 9), (5, 12), (9, 12)):
        painter.drawRect(x, y, 2, 2)
    painter.end()
    action = QAction(QIcon(pixmap), "انتخاب تاریخ شمسی", line_edit)
    action.setToolTip("انتخاب تاریخ شمسی")
    line_edit.addAction(action, QLineEdit.ActionPosition.TrailingPosition)

    def open_calendar():
        raw = normalize_digits(line_edit.text()).strip()
        digits = "".join(ch for ch in raw if ch.isdigit())
        if len(digits) != 8:
            digits = ""

        def set_date(value):
            line_edit.setText(
                f"{value[:4]}/{value[4:6]}/{value[6:8]}" if value else ""
            )

        try:
            dialog = JalaliCalendarDialog(line_edit, digits, set_date)
            dialog.exec()
        except Exception as exc:
            QMessageBox.critical(
                line_edit.window(), "خطای تقویم شمسی",
                f"پنجره تقویم باز نشد:\n{exc}"
            )

    # صریحاً آرگومان checked سیگنال QAction را نادیده بگیر.
    action.triggered.connect(lambda checked=False: open_calendar())
    line_edit.setProperty("jalaliCalendarActionInstalled", True)


class JalaliDateLineEdit(QLineEdit):
    """فیلد تاریخ شمسی با یک آیکون تقویم داخل خود فیلد."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.setPlaceholderText("شمسی: 1405/07/18")
        # آیکون تقویم به‌صورت واقعی رسم می‌شود تا در ویندوز وابسته به فونت Emoji نباشد.
        pixmap = QPixmap(18, 18)
        pixmap.fill(Qt.GlobalColor.transparent)
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(QPen(QColor("#245B87"), 1.4))
        painter.setBrush(QColor("#FFFFFF"))
        painter.drawRoundedRect(2, 3, 14, 13, 2, 2)
        painter.drawLine(2, 7, 16, 7)
        painter.drawLine(6, 1, 6, 5)
        painter.drawLine(12, 1, 12, 5)
        painter.setBrush(QColor("#245B87"))
        painter.setPen(Qt.PenStyle.NoPen)
        for x, y in ((5, 9), (9, 9), (5, 12), (9, 12)):
            painter.drawRect(x, y, 2, 2)
        painter.end()
        self.calendar_action = QAction(QIcon(pixmap), "انتخاب تاریخ شمسی", self)
        self.calendar_action.setToolTip("انتخاب تاریخ شمسی")
        self.addAction(self.calendar_action, QLineEdit.ActionPosition.TrailingPosition)
        # QAction.triggered یک مقدار bool هم می‌فرستد؛ اتصال بدون ابهام انجام شود.
        self.calendar_action.triggered.connect(
            lambda checked=False: self.open_calendar()
        )

    def open_calendar(self):
        raw = normalize_digits(self.text()).strip()
        digits = "".join(ch for ch in raw if ch.isdigit())
        if len(digits) != 8:
            digits = ""
        try:
            dialog = JalaliCalendarDialog(self, digits, self._set_selected_date)
            dialog.exec()
        except Exception as exc:
            QMessageBox.critical(
                self.window(), "خطای تقویم شمسی",
                f"پنجره تقویم باز نشد:\n{exc}"
            )

    def _set_selected_date(self, value):
        if value:
            self.setText(f"{value[:4]}/{value[4:6]}/{value[6:8]}")
        else:
            self.clear()


# ==================================================
# تبدیل ارقام فارسی و عربی به انگلیسی
# ==================================================

def normalize_digits(value):
    if value is None:
        return ""

    value = str(value)

    translation_table = str.maketrans(
        "۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩",
        "01234567890123456789"
    )

    return value.translate(translation_table)


def normalize_status(value):
    """یکسان‌سازی متن وضعیت برای جلوگیری از خطاهای فاصله و حروف فارسی/عربی."""
    value = str(value or "").strip()
    value = value.replace("ي", "ی").replace("ك", "ک")
    value = value.replace("‌", "").replace("‏", "").replace("‎", "")
    value = "".join(value.split())
    key = value.casefold()
    aliases = {
        "ثبتنشده": "ثبت نشده",
        "درانتظاربررسی": "در انتظار بررسی",
        "درحالح انجام": "در حال انجام",
        "درحالح انجام": "در حال انجام",
        "درحالت انجام": "در حال انجام",
        "درحالانجام": "در حال انجام",
        "متوقفشده": "متوقف شده",
        "پایان": "پایان",
        "تکمیلشده": "پایان",
    }
    return aliases.get(key, value)


# ==================================================
# واحدها
# ==================================================

UNIT_MAPPING = {
    "tamerat": "تعمیرات عمومی",
    "kala": "تدارکات کالا",
    "khadamat": "خدمات اداری و اجتماعی",
    "hse": "ایمنی",
    "harasat": "حراست",
}

PERSIAN_UNITS = set(UNIT_MAPPING.values())


def map_unit_name(value):
    value = str(value or "").strip()
    if not value:
        return ""
    mapped = UNIT_MAPPING.get(value.casefold())
    if mapped:
        return mapped
    if value in PERSIAN_UNITS:
        return value
    return value


# ==================================================
# کلاس اصلی فرم
# ==================================================


# -----------------------------
# تبدیل تاریخ میلادی به شمسی
# -----------------------------
def gregorian_to_jalali(gy, gm, gd):
    g_d_m = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

    gy2 = gy + 1 if gm > 2 else gy
    days = (
        355666
        + 365 * gy
        + (gy2 + 3) // 4
        - (gy2 + 99) // 100
        + (gy2 + 399) // 400
        + gd
        + g_d_m[gm - 1]
    )

    jy = -1595 + 33 * (days // 12053)
    days %= 12053
    jy += 4 * (days // 1461)
    days %= 1461

    if days > 365:
        jy += (days - 1) // 365
        days = (days - 1) % 365

    if days < 186:
        jm = 1 + days // 31
        jd = 1 + days % 31
    else:
        jm = 7 + (days - 186) // 30
        jd = 1 + (days - 186) % 30

    return jy, jm, jd


PERSIAN_WEEKDAY_HEADERS = ["ش", "ی", "د", "س", "چ", "پ", "ج"]


PERSIAN_WEEKDAYS = {
    1: "دوشنبه",
    2: "سه‌شنبه",
    3: "چهارشنبه",
    4: "پنجشنبه",
    5: "جمعه",
    6: "شنبه",
    7: "یکشنبه",
}


class MainWindow(QMainWindow):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._configure_responsive_window()
        self.open_forms = {}
        self.is_master = str(self.user.get("usersecurity") or "").strip().casefold() == "superadmin"
        self.username = str(self.user.get("username") or "").strip()
        self.usersecurity = str(self.user.get("usersecurity") or "").strip()
        self.userlevel = str(self.user.get("Userlevel") or "").strip()
        self.user_vahed = map_unit_name(self.user.get("vahed", ""))
        self.user_samat = str(self.user.get("Samat") or "").strip()
        self.tab_permissions = {}
        if not self.is_master:
            try:
                self.tab_permissions = get_user_permissions(self.user.get("userid"))
            except Exception as exc:
                QMessageBox.critical(self, "خطای مجوزها", f"خواندن مجوزهای دسترسی ناموفق بود؛ دسترسی‌ها محدود می‌شوند.\n\n{exc}")
                self.tab_permissions = {}
        self.setWindowTitle("سامانه مدیریت درخواست‌های تعمیرات")
        self.setLayoutDirection(Qt.RightToLeft)
        self.setup_status_bar()
        self.build_application_shell()
        self.build_menus()
        self.setup_kar_tab()
        self.setup_report_tab()
        self.setup_mesc_tab()
        self.setup_amval_tab()
        self.setup_tahrir_tabs()
        self.setup_hotel_tab()
        self.load_kar_list()
        self.load_report_data()
        self.update_clock()
        self.clock_timer = QTimer(self)
        self.clock_timer.timeout.connect(self.update_clock)
        self.clock_timer.start(1000)
        # اجرای مجدد پس از ساخته‌شدن همه تب‌ها؛ تب‌ها در زمان اجرای setup ساخته می‌شوند.
        self._configure_responsive_window()
        self.showMaximized()

    def _configure_responsive_window(self):
        """Adapt the main window to the current screen and Windows display scaling."""
        try:
            # Qt 6 uses logical pixels for widget geometry, so availableGeometry()
            # respects Windows display scaling (DPI) on supported configurations.
            screen = self.screen()
            if screen is None:
                screen = QApplication.primaryScreen()
            available = screen.availableGeometry() if screen is not None else None

            central = self.centralWidget()
            if central is not None:
                central.setMinimumSize(0, 0)
                central.setSizePolicy(QSizePolicy.Policy.Ignored,
                                      QSizePolicy.Policy.Ignored)

            # Designer layouts must be allowed to shrink below their aggregate
            # sizeHint. This prevents a long form from forcing a 1083px window
            # minimum on a laptop with a shorter work area.
            for layout in self.findChildren(QLayout):
                try:
                    layout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
                except (AttributeError, RuntimeError):
                    pass

            # Relax only oversized composite minimums. Keep intentionally fixed
            # navigation width and room-card sizes, while letting tabs, group
            # boxes, tables and scroll areas contract to the available viewport.
            for widget in self.findChildren(QWidget):
                name = widget.objectName()
                cls = widget.metaObject().className()
                if name == "navigationPanel" or name == "hotelRoomCardButton":
                    continue

                if isinstance(widget, (QTabWidget, QGroupBox, QTableWidget, QScrollArea)) or cls in (
                    "QPlainTextEdit", "QTextEdit", "QFrame", "QWidget"
                ):
                    minimum = widget.minimumSize()
                    if minimum.width() > 400:
                        widget.setMinimumWidth(0)
                    if minimum.height() > 180:
                        widget.setMinimumHeight(0)

                if isinstance(widget, QTableWidget):
                    widget.setSizePolicy(QSizePolicy.Policy.Expanding,
                                         QSizePolicy.Policy.Expanding)
                elif isinstance(widget, QScrollArea):
                    widget.setMinimumHeight(min(widget.minimumHeight(), 100))
                    widget.setSizePolicy(QSizePolicy.Policy.Expanding,
                                         QSizePolicy.Policy.Expanding)
                elif isinstance(widget, QTabWidget):
                    widget.setMinimumSize(0, 0)
                    widget.setSizePolicy(QSizePolicy.Policy.Expanding,
                                         QSizePolicy.Policy.Expanding)
                elif cls in ("QPlainTextEdit", "QTextEdit") and widget.minimumHeight() > 80:
                    widget.setMinimumHeight(60)

            if available is not None and available.width() > 0 and available.height() > 0:
                # Keep a small sensible minimum, but never exceed this screen's
                # available work area. Maximization later uses the same screen.
                min_w = min(900, max(480, available.width() - 32))
                min_h = min(560, max(360, available.height() - 32))
                self.setMinimumSize(min_w, min_h)
                self.resize(min(available.width(), 1500),
                            min(available.height(), 900))
            else:
                self.setMinimumSize(760, 480)
        except Exception:
            # A sizing adjustment must never prevent login/application startup.
            try:
                self.setMinimumSize(480, 360)
            except Exception:
                pass

    # -----------------------------
    # نوار وضعیت
    # -----------------------------
    def setup_status_bar(self):
        status_bar = self.statusBar()
        status_bar.setMinimumHeight(36)
        status_bar.setMaximumHeight(36)
        status_bar.setSizeGripEnabled(False)
        status_bar.setLayoutDirection(Qt.RightToLeft)
        status_bar.setStyleSheet("""
            QStatusBar {
                background-color: #f3f6fa;
                border-top: 1px solid #d8e0ea;
                color: #263548;
                font-family: 'B Nazanin';
                font-size: 10pt;
            }
            QStatusBar::item { border: none; }
        """)

        # این برچسب‌ها در main.ui تعریف شده‌اند و از Qt Designer قابل ویرایش‌اند.
        status_labels = (
            (self.ui.lblStatusUser, 145),
            (self.ui.lblStatusUnit, 165),
            (self.ui.lblStatusSecurity, 135),
            (self.ui.lblStatusLevel, 125),
            (self.ui.lblStatusWeekday, 85),
            (self.ui.lblStatusDate, 105),
            (self.ui.lblStatusTime, 100),
        )
        for label, min_width in status_labels:
            # نوار وضعیت باید همیشه در پایین پنجره و با همه اطلاعات قابل مشاهده باشد.
            label.setMinimumWidth(min_width)
            label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
            label.setMinimumHeight(27)
            label.setVisible(True)
            label.setAlignment(Qt.AlignCenter)
            label.setLayoutDirection(Qt.RightToLeft)
            label.setTextInteractionFlags(Qt.NoTextInteraction)
            label.setStyleSheet("""
                QLabel {
                    color: #263548;
                    background-color: #ffffff;
                    border: 1px solid #dce4ee;
                    border-radius: 5px;
                    padding: 2px 7px;
                    margin: 3px 3px;
                    font-family: 'B Nazanin';
                    font-size: 10pt;
                }
            """)
            status_bar.addWidget(label)

        username = str(self.user.get("username") or "—").strip()
        vahed = str(self.user.get("vahed") or "—").strip()
        user_security = str(self.user.get("usersecurity") or "—").strip()
        user_level = str(self.user.get("Userlevel") or "—").strip()

        self.ui.lblStatusUser.setText(f"کاربر: {username}")
        self.ui.lblStatusUnit.setText(f"واحد: {vahed}")
        self.ui.lblStatusSecurity.setText(f"نوع کاربر: {user_security}")
        self.ui.lblStatusLevel.setText(f"سطح دسترسی: {user_level}")

    def update_clock(self):
        now = QDateTime.currentDateTime()
        d = now.date()

        jy, jm, jd = gregorian_to_jalali(d.year(), d.month(), d.day())
        weekday = PERSIAN_WEEKDAYS.get(d.dayOfWeek(), "")

        self.ui.lblStatusWeekday.setText(weekday)
        self.ui.lblStatusDate.setText(f"{jy:04d}/{jm:02d}/{jd:02d}")
        self.ui.lblStatusTime.setText(now.toString("HH:mm:ss"))

    # -----------------------------
    # پوسته اصلی برنامه
    # -----------------------------
    def build_application_shell(self):
        """ناوبری برنامه: در شروع فقط صفحه اصلی نمایش داده می‌شود."""
        self.tabMain = self.ui.tabMain
        self.home_widget = self.ui.tabHome
        self.open_forms = getattr(self, "open_forms", {})
        self.tabMain.setTabsClosable(False)
        self.tabMain.setMovable(False)
        self.tabMain.setDocumentMode(False)
        self.tabMain.setLayoutDirection(Qt.RightToLeft)
        self.tabMain.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.tabMain.tabBar().setExpanding(True)
        self.tabMain.tabBar().setUsesScrollButtons(False)

        # در شروع فقط صفحه اصلی باز است؛ سایر تب‌ها از QTabWidget خارج می‌شوند
        # ولی خود ویجت‌ها باقی می‌مانند تا هنگام ورود دوباره اضافه شوند.
        self._main_tab_titles = {}
        for i in range(self.tabMain.count()):
            widget = self.tabMain.widget(i)
            if widget is not None:
                self._main_tab_titles[widget] = self.tabMain.tabText(i)
        for i in range(self.tabMain.count() - 1, -1, -1):
            if self.tabMain.widget(i) is not self.home_widget:
                self.tabMain.removeTab(i)

        self.tabMain.currentChanged.connect(self._on_main_tab_changed)

        self.ui.lblNavigationUser.setText(f"خوش آمدید\n{self.username}")

        # اتصال دکمه‌های منوی کناری
        self.ui.btnHome.clicked.connect(self.show_home)
        self.ui.btnPassword.clicked.connect(self.open_password_form)
        self.ui.btnUsers.clicked.connect(self.open_user_management)

        # دکمه تعیین مجوزها در خود main.ui تعریف شده تا در Qt Designer قابل ویرایش باشد.
        self.ui.btnTabPermissions.setVisible(self.is_master)
        self.ui.btnTabPermissions.clicked.connect(self.manage_user_permissions)

        self.ui.btnRepairs.clicked.connect(lambda: self.open_page(self.ui.tabKar))
        self.ui.btnAssets.clicked.connect(lambda: self.open_page(self.ui.tabAmval))
        self.ui.btnHotel.clicked.connect(lambda: self.open_page(self.ui.tabHotel))
        self.ui.btnAnbarTahrir.clicked.connect(lambda: self.open_page(self.ui.tabAnbarTahrir))
        self.ui.btnMtoTahrir.clicked.connect(lambda: self.open_page(self.ui.tabMtoTahrir))
        self.ui.btnEquipment.clicked.connect(lambda: self.open_placeholder("تجهیزات"))
        self.ui.btnReports.clicked.connect(lambda: self.open_page(self.ui.tabReport))
        self.ui.btnExit.clicked.connect(self.close)

        # دکمه‌های داخل صفحه اصلی
        self.ui.btnOpenKar.clicked.connect(lambda: self.open_page(self.ui.tabKar))
        self.ui.btnOpenUsers.clicked.connect(self.open_user_management)
        self.ui.btnOpenPassword.clicked.connect(self.open_password_form)
        self.ui.btnOpenReports.clicked.connect(lambda: self.open_page(self.ui.tabReport))
        self.ui.btnOpenEquipment.clicked.connect(lambda: self.open_placeholder("تجهیزات"))
        self.ui.btnOpenAssets.clicked.connect(lambda: self.open_page(self.ui.tabAmval))
        self.ui.btnOpenHotel.clicked.connect(lambda: self.open_page(self.ui.tabHotel))
        self.ui.btnOpenAnbarTahrir.clicked.connect(lambda: self.open_page(self.ui.tabAnbarTahrir))
        self.ui.btnOpenMtoTahrir.clicked.connect(lambda: self.open_page(self.ui.tabMtoTahrir))
        self.ui.btnOpenMesc.clicked.connect(self.open_mesc_tab)

        # دکمه خروج از هر تب به صفحه اصلی
        self.exit_tab_buttons = (
            self.ui.btnBackHomeKar,
            self.ui.btnBackHomeUsers,
            self.ui.btnBackHomePassword,
            self.ui.btnBackHomeReport,
            self.ui.btnBackHomeAmval,
            self.ui.btnBackHomeMesc,
            self.ui.btnBackHomeHotel,
            self.ui.btnBackHomeAnbarTahrir,
            self.ui.btnBackHomeMtoTahrir,
        )
        exit_pages = (
            self.ui.tabKar,
            self.ui.tabUserManagement,
            self.ui.tabChangePassword,
            self.ui.tabReport,
            self.ui.tabAmval,
            self.ui.tabMesc,
            self.ui.tabHotel,
            self.ui.tabAnbarTahrir,
            self.ui.tabMtoTahrir,
        )
        for button, page in zip(self.exit_tab_buttons, exit_pages):
            button.setText("خروج از این تب")
            button.setToolTip("بستن این بخش و بازگشت به صفحه اصلی")
            button.clicked.connect(lambda checked=False, p=page: self.close_main_tab(p))

        # مدیریت کاربران فقط برای SuperAdmin نمایش داده می‌شود.
        self.ui.btnUsers.setVisible(self.is_master)
        self.ui.btnOpenUsers.setVisible(self.is_master)
        # دکمه MESC برای همه کاربران قابل مشاهده است؛ دسترسی با مجوز تب کنترل می‌شود.
        self.ui.btnOpenMesc.setVisible(True)

        # دکمه‌های بخش‌هایی که کاربر مجوز ندارند غیرفعال می‌شوند؛
        # Qt آن‌ها را به‌صورت کم‌رنگ نمایش می‌دهد و کلیک هم نمی‌پذیرند.
        self.apply_navigation_permissions()

        # در شروع فقط صفحه اصلی قابل مشاهده باشد؛ بقیه تب‌ها هنگام درخواست باز می‌شوند.
        self.show_home()

    def apply_navigation_permissions(self):
        """دکمه‌ها و فرمان‌های منو را با مجوز تب‌ها هماهنگ می‌کند.

        برای کاربر فاقد مجوز، دکمه غیرفعال می‌شود تا در رابط کاربری
        کم‌رنگ دیده شود و نتواند با کلیک آن بخش را باز کند.
        """
        # دکمه‌های نوار کناری
        nav_map = {
            "tabHome": (self.ui.btnHome,),
            "tabKar": (self.ui.btnRepairs, self.ui.btnOpenKar),
            "tabReport": (self.ui.btnReports, self.ui.btnOpenReports),
            "tabAmval": (self.ui.btnAssets, self.ui.btnOpenAssets),
            "tabHotel": (self.ui.btnHotel, self.ui.btnOpenHotel),
            "tabAnbarTahrir": (self.ui.btnAnbarTahrir, self.ui.btnOpenAnbarTahrir),
            "tabMtoTahrir": (self.ui.btnMtoTahrir, self.ui.btnOpenMtoTahrir),
            "tabChangePassword": (self.ui.btnPassword, self.ui.btnOpenPassword),
            "tabMesc": (self.ui.btnOpenMesc,),
        }
        for tab_name, buttons in nav_map.items():
            allowed = self.is_master or bool(self.tab_permissions.get(tab_name, False))
            for button in buttons:
                button.setEnabled(allowed)
                if not allowed:
                    button.setToolTip("برای استفاده از این بخش، سوپر ادمین باید دسترسی آن را فعال کند.")

        # فرمان‌های منو نیز همان محدودیت را رعایت می‌کنند.
        menu_actions = {
            "tabHome": ("actionHome",),
            "tabChangePassword": ("actionPassword",),
            "tabKar": ("actionRepairsRequest", "actionRepairsHistory"),
            "tabReport": ("actionReportRepairs", "actionReportEquipment"),
            "tabAmval": ("actionAssets",),
            "tabAnbarTahrir": ("actionAnbarTahrir",),
            "tabMtoTahrir": ("actionMtoTahrir",),
        }
        for tab_name, action_names in menu_actions.items():
            allowed = self.is_master or bool(self.tab_permissions.get(tab_name, False))
            for action_name in action_names:
                action = getattr(self.ui, action_name, None)
                if action is not None:
                    action.setEnabled(allowed)

    # -----------------------------
    # منوها
    # -----------------------------
    def build_menus(self):
        """اتصال منوهای برنامه به همان توابع ناوبری دکمه‌ها."""
        ui = self.ui
        ui.actionHome.triggered.connect(self.show_home)
        if self.is_master:
            self.actionUserPermissions = QAction("تعیین دسترسی به تب‌های کاربران", self)
            self.actionUserPermissions.triggered.connect(self.manage_user_permissions)
            ui.menuUsers.addAction(self.actionUserPermissions)
        ui.actionPassword.triggered.connect(self.open_password_form)
        ui.actionExit.triggered.connect(self.close)
        ui.actionUserManagement.triggered.connect(self.open_user_management)
        ui.actionRepairsRequest.triggered.connect(
            lambda checked=False: self.open_page(self.ui.tabKar)
        )
        ui.actionRepairsHistory.triggered.connect(
            lambda checked=False: self.open_page(self.ui.tabKar)
        )
        ui.actionEquipmentList.triggered.connect(
            lambda checked=False: self.open_placeholder("تجهیزات")
        )
        ui.actionReportRepairs.triggered.connect(
            lambda checked=False: self.open_page(self.ui.tabReport)
        )
        ui.actionReportEquipment.triggered.connect(
            lambda checked=False: self.open_page(self.ui.tabReport)
        )
        ui.actionAbout.triggered.connect(self.show_about)
        ui.actionAssets.triggered.connect(lambda checked=False: self.open_page(self.ui.tabAmval))
        ui.actionAnbarTahrir.triggered.connect(lambda checked=False: self.open_page(self.ui.tabAnbarTahrir))
        ui.actionMtoTahrir.triggered.connect(lambda checked=False: self.open_page(self.ui.tabMtoTahrir))
        ui.menuUsers.menuAction().setVisible(self.is_master)
        ui.actionUserManagement.setVisible(self.is_master)

    # -----------------------------
    # مدیریت نمایش صفحه‌ها
    # -----------------------------
    def _page_allowed(self, page):
        """بررسی مجوز تب؛ سوپر ادمین دسترسی کامل دارد."""
        if self.is_master:
            return True
        name = page.objectName() if page is not None else ""
        if name == "tabUserManagement":
            return False
        return bool(self.tab_permissions.get(name, False))

    def manage_user_permissions(self):
        if not self.is_master:
            QMessageBox.warning(self, "عدم دسترسی", "فقط SuperAdmin می‌تواند سطح دسترسی کاربران را تعیین کند.")
            return
        open_user_permissions_dialog(self)

    def show_page(self, page):
        """تب را در صورت نیاز باز می‌کند و فعال می‌سازد."""
        if not self._page_allowed(page):
            QMessageBox.warning(self, "عدم دسترسی", "برای ورود به این بخش مجوز ندارید. با سوپر ادمین تماس بگیرید.")
            return

        index = self.tabMain.indexOf(page)
        if index < 0:
            title = self._main_tab_titles.get(page, page.objectName())
            index = self.tabMain.addTab(page, title)
        self.tabMain.setCurrentIndex(index)

    def open_page(self, page):
        """باز کردن تب موردنظر؛ تب‌های باز دیگر بسته نمی‌شوند."""
        self.show_page(page)

    def show_home(self):
        """بازگشت به صفحه اصلی؛ تب صفحه اصلی همیشه باز می‌ماند."""
        target = self.home_widget if self._page_allowed(self.home_widget) else None
        if target is None:
            for i in range(self.tabMain.count()):
                candidate = self.tabMain.widget(i)
                if self._page_allowed(candidate):
                    target = candidate
                    break
        if target is None:
            QMessageBox.critical(self, "بدون دسترسی", "هیچ بخشی برای این کاربر مجاز نشده است. با سوپر ادمین تماس بگیرید.")
            return

        index = self.tabMain.indexOf(target)
        if index < 0:
            index = self.tabMain.addTab(target, self._main_tab_titles.get(target, "صفحه اصلی"))
        self.tabMain.setCurrentIndex(index)

    def _on_main_tab_changed(self, index):
        """فقط مجوز تب انتخاب‌شده را بررسی می‌کند؛ تب قبلی بسته نمی‌شود."""
        if index < 0:
            return
        page = self.tabMain.widget(index)
        if page is None:
            return
        if not self._page_allowed(page):
            self.show_home()

    def open_user_management(self):
        # تب «مدیریت کاربران» فقط برای SuperAdmin مجاز است.
        if not self.is_master:
            QMessageBox.warning(
                self,
                "عدم دسترسی",
                "فقط SuperAdmin مجاز به دسترسی به مدیریت کاربران است."
            )
            return
        self.open_management_form(password_only=False)

    def open_password_form(self):
        self.open_management_form(password_only=True)

    def open_management_form(self, password_only=False):
        """باز کردن تب‌های طراحی‌شده در main.ui؛ UserManagement کنترلر است، نه ویجت."""
        if not password_only and not self.is_master:
            QMessageBox.warning(
                self,
                "عدم دسترسی",
                "فقط SuperAdmin مجاز به دسترسی به تب کاربران است."
            )
            return

        # کنترلر فقط یک بار ساخته شود؛ خودش سیگنال دکمه‌های فرم را متصل می‌کند.
        if not hasattr(self, "user_management_controller"):
            self.user_management_controller = UserManagement(
                parent_window=self,
                ui=self.ui,
                current_user=self.user,
            )

        if password_only:
            target = self.ui.tabChangePassword
            title = "تغییر رمز عبور"
        else:
            target = self.ui.tabUserManagement
            title = "مدیریت کاربران"

        self.show_page(target)

    def close_main_tab(self, page):
        """بستن یکی از تب‌های اصلی و بازگشت به صفحه اصلی.

        صفحه اصلی هرگز بسته نمی‌شود. سایر تب‌ها فقط با همین فرمان خروج
        از QTabWidget حذف می‌شوند و خود ویجت برای استفاده مجدد باقی می‌ماند.
        """
        if page is self.home_widget:
            self.show_home()
            return
        index = self.tabMain.indexOf(page)
        if index >= 0:
            self.tabMain.removeTab(index)
        self.show_home()

    def remove_form_tab(self, widget):
        """سازگاری با کنترلرهای قدیمی برای بستن تب‌های اصلی."""
        self.close_main_tab(widget)

    def open_placeholder(self, title):
        if title in ("درخواست کار", "تعمیرات", "سوابق تعمیرات"):
            self.show_page(self.ui.tabKar)
            return
        if title in ("گزارش و پیگیری", "گزارش‌ها", "گزارش تعمیرات", "گزارش تجهیزات"):
            self.show_page(self.ui.tabReport)
            return

        key = f"placeholder:{title}"
        existing = self.open_forms.get(key)
        if existing is not None:
            index = self.tabMain.indexOf(existing)
            if index >= 0:
                self.show_page(existing)
                return
            self.open_forms.pop(key, None)

        page = QWidget()
        page.setObjectName(f"page_{title}")
        page.setLayoutDirection(Qt.RightToLeft)
        layout = QVBoxLayout(page)
        layout.setContentsMargins(30, 20, 30, 30)

        back_button = QPushButton("بازگشت به صفحه اصلی")
        back_button.setMinimumHeight(36)
        back_button.setMaximumWidth(190)
        back_button.clicked.connect(lambda checked=False, p=page: self.close_dynamic_page(p))
        layout.addWidget(back_button, 0, Qt.AlignRight)

        lbl_title = QLabel(title)
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        lbl_title.setFont(font)
        lbl_title.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl_title)

        lbl_text = QLabel("این بخش هنوز فرم اختصاصی ندارد و برای توسعه بعدی آماده است.")
        lbl_text.setAlignment(Qt.AlignCenter)
        lbl_text.setWordWrap(True)
        layout.addWidget(lbl_text)
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.tabMain.addTab(page, title)
        self.open_forms[key] = page
        self.show_page(page)

    def close_dynamic_page(self, page):
        index = self.tabMain.indexOf(page)
        if index >= 0:
            self.tabMain.removeTab(index)
        for key, value in list(self.open_forms.items()):
            if value is page:
                self.open_forms.pop(key, None)
        page.deleteLater()
        self.show_home()

    def show_about(self):
        QMessageBox.information(
            self,
            "درباره برنامه",
            "سامانه مدیریت\n\nنسخه اولیه مدیریت کاربران و ماژول‌های برنامه",
        )


    @staticmethod
    def format_jalali_input_date(value):
        digits = normalize_digits(value)
        digits = "".join(ch for ch in digits if ch.isdigit())
        if len(digits) == 8:
            return f"{digits[:4]}/{digits[4:6]}/{digits[6:8]}"
        return str(value or "")

    @staticmethod
    def jalali_storage_date(value):
        digits = normalize_digits(value)
        return "".join(ch for ch in digits if ch.isdigit())

    def setup_kar_tab(self):
        # فیلد تاریخ درخواست را به فیلد دارای تقویم شمسی تبدیل کن.
        self.setup_request_date_calendar()

        # بارگذاری گزینه‌های واحد و موضوع؛ در UI فقط خود کمبوباکس‌ها طراحی شده‌اند.
        self.load_request_comboboxes()

        self.ui.dateTarikhdarkhast.setText(
            jdatetime.date.today().strftime("%Y/%m/%d")
        )

        table = self.ui.tblKarList

        table.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )

        table.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )

        table.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )

        # مخفی کردن شماره‌گذاری خودکار سمت چپ
        table.verticalHeader().setVisible(False)

        # فونت عنوان ستون‌ها
        header = table.horizontalHeader()

        header_font = QFont("B Nazanin", 14)
        header_font.setBold(True)

        header.setFont(header_font)
        header.setMinimumHeight(42)

        header.setSectionResizeMode(
            QHeaderView.ResizeMode.Interactive
        )

        header.setStyleSheet("""
            QHeaderView::section {
                background-color: #E8EEF5;
                color: #1F2937;
                font-family: "B Nazanin";
                font-size: 14pt;
                font-weight: bold;
                padding: 7px;
                border: 1px solid #C7D0DB;
            }

            QHeaderView::section:hover {
                background-color: #DCE6F1;
            }
        """)

        # ظاهر جدول
        table.setAlternatingRowColors(True)

        table.setStyleSheet("""
            QTableWidget {
                background-color: white;
                alternate-background-color: #F7F9FC;
                gridline-color: #D6DCE3;
                border: 1px solid #C7D0DB;
                border-radius: 6px;
                font-family: "B Nazanin";
                font-size: 12pt;
                selection-background-color: #B8D7F0;
                selection-color: #000000;
            }

            QTableWidget::item {
                padding: 5px;
                border: none;
            }

            QTableWidget::item:selected {
                background-color: #B8D7F0;
                color: #000000;
            }
        """)

        table.verticalHeader().setDefaultSectionSize(34)

        # اتصال دکمه‌ها
        self.ui.btnSaveKar.clicked.connect(self.save_kar)
        self.ui.btnNewKar.clicked.connect(self.new_kar)
        self.ui.btnClearKar.clicked.connect(self.clear_kar)

        self.ui.txtSearchKar.textChanged.connect(
            self.search_kar
        )

    def setup_request_date_calendar(self):
        """فیلد طراحی‌شده در main.ui را با فیلد دارای تقویم شمسی جایگزین می‌کند."""
        old_widget = getattr(self.ui, "dateTarikhdarkhast", None)
        if old_widget is None or isinstance(old_widget, JalaliDateLineEdit):
            return

        parent = old_widget.parentWidget()
        layout = parent.layout() if parent is not None else None
        new_widget = JalaliDateLineEdit(parent)
        new_widget.setObjectName("dateTarikhdarkhast")
        new_widget.setText(old_widget.text())
        new_widget.setMinimumWidth(max(140, old_widget.minimumWidth()))
        new_widget.setSizePolicy(old_widget.sizePolicy())

        if not replace_widget_in_layout(layout, old_widget, new_widget):
            new_widget.deleteLater()
            old_widget.setPlaceholderText("برای انتخاب تاریخ روی فیلد تاریخ دوبار کلیک کنید")
            old_widget.setProperty("jalaliCalendarUnavailable", True)
            # جایگزین مطمئن: با دوبار کلیک روی خود فیلد، تقویم باز شود.
            install_calendar_action(old_widget)
            return

        old_widget.hide()
        old_widget.setParent(None)
        old_widget.deleteLater()
        self.ui.dateTarikhdarkhast = new_widget

    def load_request_comboboxes(self):
        """پر کردن کمبوباکس‌های درخواست کار با واحدها و موضوعات موجود."""
        unit_combo = self.ui.cmbVahed
        previous_unit = map_unit_name(unit_combo.currentText())
        unit_combo.setEnabled(True)
        unit_combo.clear()
        unit_combo.addItem("", "")
        for unit in sorted(PERSIAN_UNITS):
            unit_combo.addItem(unit, unit)

        topic_combo = self.ui.cmbMozooe
        previous_topic = topic_combo.currentText().strip()
        topics = []
        conn = None
        cursor = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT DISTINCT mozooe FROM tblkar "
                "WHERE mozooe IS NOT NULL AND Trim(mozooe) <> '' "
                "ORDER BY mozooe"
            )
            topics = [str(row[0]).strip() for row in cursor.fetchall() if row[0] and str(row[0]).strip()]
        except Exception:
            # اگر جدول هنوز موضوعی نداشته باشد یا دیتابیس موقتاً در دسترس نباشد،
            # فهرست اولیه نمایش داده می‌شود.
            topics = []
        finally:
            try:
                if cursor:
                    cursor.close()
            except Exception:
                pass
            try:
                if conn:
                    conn.close()
            except Exception:
                pass

        if not topics:
            topics = ["برق", "مکانیک", "تأسیسات", "ساختمانی", "ابزار دقیق", "سایر"]
        topics = list(dict.fromkeys(topics))
        topic_combo.clear()
        topic_combo.addItem("", "")
        for topic in topics:
            topic_combo.addItem(topic, topic)

        # برای کاربران عادی، واحد خودشان انتخاب شود و امکان تغییر واحد نداشته باشند.
        if self.usersecurity.casefold() != "superadmin" and self.user_vahed:
            index = unit_combo.findData(self.user_vahed)
            if index < 0:
                index = unit_combo.findText(self.user_vahed)
            if index >= 0:
                unit_combo.setCurrentIndex(index)
                unit_combo.setEnabled(False)
            else:
                unit_combo.setCurrentIndex(0)
                unit_combo.setEnabled(True)
        elif previous_unit:
            index = unit_combo.findText(previous_unit)
            if index >= 0:
                unit_combo.setCurrentIndex(index)

        if previous_topic:
            index = topic_combo.findText(previous_topic)
            if index >= 0:
                topic_combo.setCurrentIndex(index)
        else:
            topic_combo.setCurrentIndex(0)

    def get_next_wonumber(self):

        conn = None
        cursor = None

        try:

            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT MAX(VAL(wonumber))
                FROM tblkar
            """)

            result = cursor.fetchone()

            if result is None or result[0] is None:
                return 1

            return int(result[0]) + 1

        except Exception as e:

            QMessageBox.critical(
                self,
                "خطا",
                f"خطا در دریافت شماره درخواست:\n{e}"
            )

            return 1

        finally:

            try:
                if cursor:
                    cursor.close()
            except Exception:
                pass

            try:
                if conn:
                    conn.close()
            except Exception:
                pass

    def new_kar(self):

        self.clear_kar()

        wonumber = self.get_next_wonumber()

        self.ui.lblWonumber.setText(str(wonumber))

        self.ui.dateTarikhdarkhast.setText(
            jdatetime.date.today().strftime("%Y/%m/%d")
        )

        if self.usersecurity.lower() != "superadmin":

            if self.user_vahed:

                index = self.ui.cmbVahed.findText(
                    self.user_vahed
                )

                if index >= 0:
                    self.ui.cmbVahed.setCurrentIndex(index)

                self.ui.cmbVahed.setEnabled(False)

        else:

            self.ui.cmbVahed.setEnabled(True)

    def clear_kar(self):

        self.ui.cmbMozooe.setCurrentIndex(0)
        self.ui.txtMahalkarf.clear()
        self.ui.txtMahalkara.clear()
        self.ui.txtSharh.clear()

        self.ui.dateTarikhdarkhast.setText(
            jdatetime.date.today().strftime("%Y/%m/%d")
        )

        if self.usersecurity.lower() != "superadmin":

            if self.user_vahed:

                index = self.ui.cmbVahed.findText(
                    self.user_vahed
                )

                if index >= 0:
                    self.ui.cmbVahed.setCurrentIndex(index)

                self.ui.cmbVahed.setEnabled(False)

        else:

            self.ui.cmbVahed.setEnabled(True)

    def save_kar(self):

        wonumber = self.ui.lblWonumber.text().strip()
        vahed = str(self.ui.cmbVahed.currentData() or self.ui.cmbVahed.currentText()).strip()

        tarikhdarkhast_display = self.ui.dateTarikhdarkhast.text().strip()
        tarikhdarkhast = self.jalali_storage_date(tarikhdarkhast_display)

        # تاریخ برای ذخیره باید دقیقاً YYYYMMDD باشد؛
        # اما در فرم کاربر آن را به صورت YYYY/MM/DD می‌بیند.
        if len(tarikhdarkhast) != 8 or not tarikhdarkhast.isdigit():
            QMessageBox.warning(
                self,
                "تاریخ نامعتبر",
                "تاریخ درخواست را به صورت 1405/07/18 وارد کنید."
            )
            return

        mozooe = str(self.ui.cmbMozooe.currentData() or self.ui.cmbMozooe.currentText()).strip()
        mahalkarf = self.ui.txtMahalkarf.text().strip()
        mahalkara = self.ui.txtMahalkara.text().strip()
        sharh = self.ui.txtSharh.toPlainText().strip()
        darkhastkonande = self.username

        if not wonumber:
            QMessageBox.warning(
                self,
                "هشدار",
                "شماره درخواست مشخص نیست."
            )
            return

        if not vahed:
            QMessageBox.warning(
                self,
                "هشدار",
                "لطفاً واحد را انتخاب کنید."
            )
            return

        if not tarikhdarkhast:
            QMessageBox.warning(
                self,
                "هشدار",
                "تاریخ درخواست مشخص نیست."
            )
            return

        if not mozooe:
            QMessageBox.warning(
                self,
                "هشدار",
                "لطفاً موضوع درخواست را انتخاب کنید."
            )
            return

        if not mahalkarf:
            QMessageBox.warning(
                self,
                "هشدار",
                "لطفاً محل کار را وارد کنید."
            )
            return

        if not sharh:
            QMessageBox.warning(
                self,
                "هشدار",
                "لطفاً شرح درخواست را وارد کنید."
            )
            return

        if self.usersecurity.lower() != "superadmin":

            if vahed != self.user_vahed:
                QMessageBox.warning(
                    self,
                    "عدم دسترسی",
                    "شما فقط مجاز به ثبت درخواست برای واحد خود هستید."
                )
                return

        conn = None
        cursor = None

        try:

            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO tblkar
                (
                    wonumber,
                    vahed,
                    tarikhdarkhast,
                    mozooe,
                    mahalkarf,
                    mahalkara,
                    sharh,
                    darkhastkonande,
                    vaziyat,
                    payan,
                    tarikh,
                    editor,
                    sharhepey
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                wonumber,
                vahed,
                int(tarikhdarkhast),
                mozooe,
                mahalkarf,
                mahalkara,
                sharh,
                darkhastkonande,
                "ثبت نشده",
                False,
                None,
                self.username,
                ""
            ))

            conn.commit()

            QMessageBox.information(
                self,
                "ثبت درخواست",
                "درخواست با موفقیت ثبت شد."
            )

            self.load_kar_list()
            self.new_kar()

        except Exception as e:

            if conn:
                try:
                    conn.rollback()
                except Exception:
                    pass

            QMessageBox.critical(
                self,
                "خطا",
                f"خطا در ثبت درخواست:\n{e}"
            )

        finally:

            try:
                if cursor:
                    cursor.close()
            except Exception:
                pass

            try:
                if conn:
                    conn.close()
            except Exception:
                pass

    def load_kar_list(self):

        try:
            search_text = self.ui.txtSearchKar.text().strip()
        except Exception:
            search_text = ""

        self.load_kar_data(search_text)

    def search_kar(self):

        search_text = self.ui.txtSearchKar.text().strip()

        self.load_kar_data(search_text)

    def load_kar_data(self, search_text=""):

        table = self.ui.tblKarList

        conn = None
        cursor = None

        try:

            conn = get_connection()
            cursor = conn.cursor()

            is_superadmin = (
                self.usersecurity.lower() == "superadmin"
            )

            is_admin = (
                self.usersecurity.lower() == "admin"
            )

            query = """
                SELECT
                    [wonumber],
                    [vahed],
                    [tarikhdarkhast],
                    [mozooe],
                    [mahalkara],
                    [mahalkarf],
                    [darkhastkonande],
                    [sharh],
                    [vaziyat],
                    [tarikh],
                    [sharhepey]
                FROM [tblkar]
            """

            conditions = []
            params = []

            # محدودیت دسترسی
            if is_superadmin:
                pass

            elif is_admin:

                if self.user_vahed:
                    conditions.append("[vahed] = ?")
                    params.append(self.user_vahed)

            else:

                conditions.append("[darkhastkonande] = ?")
                params.append(self.username)

            # جستجو در ستون‌ها
            if search_text:

                normalized_search = normalize_digits(search_text)

                search_conditions = [
                    "[vahed] LIKE ?",
                    "[mozooe] LIKE ?",
                    "[mahalkarf] LIKE ?",
                    "[mahalkara] LIKE ?",
                    "[sharh] LIKE ?",
                    "[darkhastkonande] LIKE ?",
                ]

                for _ in search_conditions:
                    params.append(f"%{search_text}%")

                if normalized_search.isdigit():

                    search_conditions.append(
                        "VAL(wonumber) = ?"
                    )

                    params.append(int(normalized_search))

                conditions.append(
                    "(" + " OR ".join(search_conditions) + ")"
                )

            if conditions:
                query += " WHERE " + " AND ".join(conditions)

            query += " ORDER BY [id] DESC"

            cursor.execute(query, params)

            rows = cursor.fetchall()

            headers = [
                "شماره ردیف",
                "شماره درخواست",
                "واحد",
                "تاریخ درخواست",
                "موضوع",
                "محل کار",
                "محل کار فرعی",
                "درخواست‌کننده",
                "شرح",
                "وضعیت",
                "تاریخ پیگیری",
                "شرح پیگیری",
            ]

            table.clear()
            table.setColumnCount(len(headers))
            table.setHorizontalHeaderLabels(headers)
            table.setRowCount(len(rows))

            for row_index, row in enumerate(rows):

                # شماره ردیف نمایشی
                table.setItem(
                    row_index,
                    0,
                    QTableWidgetItem(str(row_index + 1))
                )

                # اطلاعات دیتابیس
                for col_index, value in enumerate(row):

                    if value is None:
                        value = ""

                    # تبدیل تاریخ به نمایش YYYY/MM/DD
                    if col_index == 2 and value != "":

                        value = normalize_digits(value)
                        value = str(value)

                        if len(value) == 8 and value.isdigit():

                            value = (
                                value[:4]
                                + "/"
                                + value[4:6]
                                + "/"
                                + value[6:]
                            )

                    item = QTableWidgetItem(str(value))

                    item.setTextAlignment(
                        Qt.AlignmentFlag.AlignCenter
                    )

                    table.setItem(
                        row_index,
                        col_index + 1,
                        item
                    )

                # راست‌چین کردن شماره ردیف
                first_item = table.item(row_index, 0)

                if first_item:
                    first_item.setTextAlignment(
                        Qt.AlignmentFlag.AlignCenter
                    )

            # عرض اولیه ستون‌ها؛ کاربر می‌تواند بعداً تغییر دهد
            column_widths = [
                80,
                110,
                180,
                120,
                180,
                160,
                160,
                140,
                350,
                120,
                120,
                300,
            ]

            for index, width in enumerate(column_widths):
                table.setColumnWidth(index, width)

        except Exception as e:

            QMessageBox.critical(
                self,
                "خطا",
                f"خطا در دریافت لیست درخواست‌ها:\n{e}"
            )

        finally:

            try:
                if cursor:
                    cursor.close()
            except Exception:
                pass

            try:
                if conn:
                    conn.close()
            except Exception:
                pass

    def is_maintenance_unit(self):
        return self.user_vahed == "تعمیرات عمومی"

    def can_manage_tracking(self):
        return (
            self.usersecurity.casefold() == "superadmin"
            or self.is_maintenance_unit()
        )

    def ensure_tracking_table(self):
        """سازگاری با نسخه‌های قبلی؛ پیگیری‌ها اکنون مستقیماً در tblkar ذخیره می‌شوند."""
        return


    # ---------------------------------------------------------
    # -----------------------------
    # مدیریت اتاق‌داری مهمانسرا: tblMehmansera (اتاق‌ها) و tblHotel (سوابق اقامت)
    # -----------------------------
    def setup_hotel_tab(self):
        """رابط اتاق‌داری با چیدمان حرفه‌ای پذیرش هتل."""
        self._hotel_room_schema = None
        self._hotel_guest_schema = None
        self._hotel_rooms = []
        self._hotel_guests = []
        self._hotel_building_filter = ""
        self.ui.cmbHotelBuilding.clear()
        self.ui.cmbHotelBuilding.addItems(["لاله", "لیان"])
        self.ui.cmbHotelNational.setEditable(True)
        self.ui.cmbHotelNational.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
        self.ui.cmbHotelOrg.setEditable(True)
        self.ui.cmbHotelOrg.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)

        root = self.ui.verticalLayoutHotel
        back_button = self.ui.btnBackHomeHotel
        while root.count():
            item = root.takeAt(0)
            widget = item.widget()
            if widget and widget is not back_button:
                widget.setParent(None)
            elif item.layout():
                item.layout().setParent(None)

        self.hotelSections = QTabWidget(self.ui.tabHotel)
        self.hotelSections.setObjectName("hotelSectionsRuntime")
        self.hotelSections.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.hotelSections.setDocumentMode(True)
        root.addWidget(back_button)
        root.addWidget(self.hotelSections, 1)
        self.hotelRoomsPage, self.hotelReceptionPage, self.hotelMovementsPage, self.hotelHistoryPage = [QWidget() for _ in range(4)]

        layout = QVBoxLayout(self.hotelRoomsPage)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(10)
        layout.addWidget(self.ui.groupHotelSummary)
        layout.addWidget(self.ui.groupHotelRooms, 1)

        layout = QVBoxLayout(self.hotelReceptionPage)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(12)
        layout.addWidget(self.ui.groupHotelGuestForm)

        # فقط آیتم‌های داخل Layout را به صفحه پذیرش منتقل می‌کنیم.
        # خود Layout قبلی در tabHotel باقی نمی‌ماند؛ در غیر این صورت
        # ویجت‌های دکمه‌ها ممکن است در گوشه بالا-چپ همه تب‌ها دیده شوند.
        def move_layout_widgets(source_layout, target_layout, target_widget):
            if source_layout is None:
                return
            while source_layout.count():
                item = source_layout.takeAt(0)
                widget = item.widget()
                child_layout = item.layout()
                if widget is not None:
                    widget.setParent(target_widget)
                    target_layout.addWidget(widget)
                elif child_layout is not None:
                    move_layout_widgets(child_layout, target_layout, target_widget)

        actions = self.findChild(QHBoxLayout, "horizontalLayoutHotelActions")
        if actions:
            move_layout_widgets(actions, layout, self.hotelReceptionPage)
        reception_status_actions = QHBoxLayout()
        self.btnHotelReceptionCheckIn = QPushButton("ثبت ورود مهمان انتخاب‌شده")
        self.btnHotelReceptionCheckOut = QPushButton("ثبت خروج مهمان انتخاب‌شده")
        self.btnHotelReceptionCheckIn.setMinimumHeight(42)
        self.btnHotelReceptionCheckOut.setMinimumHeight(42)
        self.btnHotelReceptionCheckIn.setStyleSheet("background:#E6F4EA; border:1px solid #9CCBA8; font-weight:bold;")
        self.btnHotelReceptionCheckOut.setStyleSheet("background:#FFF0E8; border:1px solid #E8B49A; font-weight:bold;")
        self.btnHotelReceptionCheckIn.clicked.connect(lambda: self._hotel_set_actual_date("checkin"))
        self.btnHotelReceptionCheckOut.clicked.connect(lambda: self._hotel_set_actual_date("checkout"))
        reception_status_actions.addWidget(self.btnHotelReceptionCheckIn)
        reception_status_actions.addWidget(self.btnHotelReceptionCheckOut)
        layout.addLayout(reception_status_actions)
        layout.addStretch(1)

        layout = QVBoxLayout(self.hotelMovementsPage)
        layout.setContentsMargins(10, 10, 10, 10)
        intro = QLabel("ورودهای برنامه‌ریزی‌شده و خروج‌های امروز؛ ردیف مهمان را انتخاب کنید و ورود یا خروج را ثبت کنید.")
        layout.addWidget(intro)
        self.tblHotelToday = QTableWidget(self.hotelMovementsPage)
        self.tblHotelToday.setObjectName("tblHotelToday")
        self.tblHotelToday.setColumnCount(7)
        self.tblHotelToday.setHorizontalHeaderLabels(["شناسه", "عملیات", "ساختمان", "اتاق", "نام مهمان", "نفرات", "تاریخ برنامه‌ریزی‌شده"])
        self.tblHotelToday.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblHotelToday.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tblHotelToday.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblHotelToday.setAlternatingRowColors(True)
        self.tblHotelToday.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.tblHotelToday.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.tblHotelToday, 1)
        movement_actions = QHBoxLayout()
        movement_actions.addWidget(self.ui.btnHotelCheckIn)
        movement_actions.addWidget(self.ui.btnHotelCheckOut)
        movement_actions.addWidget(self.ui.btnHotelRefresh)
        layout.addLayout(movement_actions)

        layout = QVBoxLayout(self.hotelHistoryPage)
        layout.setContentsMargins(10, 10, 10, 10)
        search_layout = self.findChild(QHBoxLayout, "horizontalLayoutHotelSearch")
        if search_layout:
            move_layout_widgets(search_layout, layout, self.hotelHistoryPage)
        layout.addWidget(self.ui.groupHotelHistory, 1)

        self.hotelSections.addTab(self.hotelRoomsPage, "وضعیت اتاق‌ها")
        self.hotelSections.addTab(self.hotelReceptionPage, "پذیرش و رزرو")
        self.hotelSections.addTab(self.hotelMovementsPage, "ورود و خروج امروز")
        self.hotelSections.addTab(self.hotelHistoryPage, "سوابق اقامت")

        self.ui.tblHotelRooms.hide()
        # از اسکرول‌اریا و گرید موجود در main.ui استفاده می‌کنیم.
        # ساختن اسکرول‌اریا و درج دوباره آن در همین layout باعث ایجاد کادر/لایهٔ اضافی
        # روی کارت‌های اتاق و مزاحمت برای شماره اتاق‌ها می‌شد.
        self.hotelRoomScroll = self.ui.hotelRoomScroll
        self.hotelRoomCardsHost = self.ui.hotelRoomCardsHost
        self.hotelRoomCardsLayout = self.ui.hotelRoomCardsLayout
        self.hotelRoomScroll.setWidgetResizable(True)
        self.hotelRoomCardsLayout.setContentsMargins(6, 6, 6, 6)
        self.hotelRoomCardsLayout.setSpacing(10)

        self.ui.cmbHotelBuilding.currentTextChanged.connect(self._hotel_refresh_room_combo)
        # کد ملی هم از فهرست قابل انتخاب است و هم قابل تایپ؛ با تطبیق دقیق، مشخصات قبلی پر می‌شود.
        self.ui.cmbHotelNational.setEditable(True)
        self.ui.cmbHotelNational.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
        self.ui.cmbHotelNational.currentTextChanged.connect(self._hotel_national_changed)
        self.ui.btnHotelLaleh.clicked.connect(lambda: self._hotel_set_building_filter("لاله"))
        self.ui.btnHotelLian.clicked.connect(lambda: self._hotel_set_building_filter("لیان"))
        self.ui.btnHotelAll.clicked.connect(lambda: self._hotel_set_building_filter(""))
        self.ui.btnHotelNew.clicked.connect(self._hotel_clear_form)
        self.ui.btnHotelSave.clicked.connect(self._hotel_save_guest)
        self.ui.btnHotelEdit.clicked.connect(self._hotel_edit_guest)
        if hasattr(self.ui, "btnHotelExtendStay"):
            self.ui.btnHotelExtendStay.clicked.connect(self._hotel_extend_stay)
        self.ui.btnHotelCheckIn.clicked.connect(lambda: self._hotel_set_actual_date("checkin"))
        self.ui.btnHotelCheckOut.clicked.connect(lambda: self._hotel_set_actual_date("checkout"))
        self.ui.btnHotelRefresh.clicked.connect(self._hotel_load_all)
        self.ui.txtHotelSearch.textChanged.connect(self._hotel_load_history)
        self.ui.tblHotelRooms.itemSelectionChanged.connect(self._hotel_room_selected)
        self.ui.tblHotelHistory.itemSelectionChanged.connect(self._hotel_history_selected)
        self.tblHotelToday.itemSelectionChanged.connect(self._hotel_today_selected)
        for table in (self.ui.tblHotelRooms, self.ui.tblHotelHistory, self.tblHotelToday):
            table.setAlternatingRowColors(True)
            table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
            table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
            table.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        for table in (self.ui.tblHotelRooms, self.ui.tblHotelHistory):
            table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.hotelSections.setStyleSheet('QTabBar::tab { min-height: 42px; padding: 7px 18px; font-family: "B Nazanin"; font-size: 13pt; font-weight: bold; } QGroupBox { font-size: 12pt; font-weight: bold; border: 1px solid #D6DEE8; border-radius: 8px; margin-top: 12px; padding-top: 10px; } QGroupBox::title { subcontrol-origin: margin; right: 12px; padding: 0 6px; } QLineEdit, QComboBox { min-height: 32px; padding: 3px 7px; border: 1px solid #C7D2DF; border-radius: 5px; } QTableWidget { gridline-color: #E3E8EF; alternate-background-color: #F5F8FC; selection-background-color: #D7E9FA; selection-color: #17324D; }')
        self.ui.txtHotelArrival.setText(self._hotel_today_jalali())
        self.ui.txtHotelDeparture.setText(self._hotel_today_jalali())
        self.ui.txtHotelActualArrival.clear()
        self.ui.txtHotelActualDeparture.clear()
        install_calendar_action(self.ui.txtHotelArrival)
        install_calendar_action(self.ui.txtHotelDeparture)
        install_calendar_action(self.ui.txtHotelActualArrival)
        install_calendar_action(self.ui.txtHotelActualDeparture)
        self._hotel_load_all()

    def _hotel_today_selected(self):
        row = self.tblHotelToday.currentRow()
        if row < 0:
            return
        item = self.tblHotelToday.item(row, 0)
        rid = item.data(Qt.ItemDataRole.UserRole) if item else None
        guest = next((r for r in self._hotel_guests if str(r.get(self._hotel_pick(r, "ID", "id"))) == str(rid)), None)
        if guest:
            self._hotel_fill_form_from_guest(guest)

    def _hotel_fill_form_from_guest(self, row):
        self._hotel_loading_guest_form = True
        id_col = self._hotel_pick(row, "ID", "id")
        self._hotel_active_guest_id = row.get(id_col) if id_col else None
        mapping = {"txtHotelFirstName": ("Nam", "name"), "txtHotelLastName": ("Family", "family"), "txtHotelPeople": ("TedadAfrad", "people"), "txtHotelEmployee": ("Codepersoneli", "personnelcode")}
        national_col = self._hotel_pick(row, "CodeMeli", "nationalcode")
        self.ui.cmbHotelNational.setCurrentText(self._hotel_text(row.get(national_col)) if national_col else "")
        for widget_name, aliases in mapping.items():
            col = self._hotel_pick(row, *aliases)
            getattr(self.ui, widget_name).setText(self._hotel_text(row.get(col)) if col else "")
        org_col = self._hotel_pick(row, "Sazman", "organization")
        self.ui.cmbHotelOrg.setCurrentText(self._hotel_text(row.get(org_col)) if org_col else "")
        self.ui.btnHotelEdit.setEnabled(self._hotel_active_guest_id is not None)
        actual_in_col = self._hotel_pick(row, "TarikhIn", "actualcheckin")
        actual_out_col = self._hotel_pick(row, "tarikhOut", "actualcheckout")
        self.ui.txtHotelActualArrival.setText(self._hotel_text(row.get(actual_in_col)) if actual_in_col and row.get(actual_in_col) else "")
        self.ui.txtHotelActualDeparture.setText(self._hotel_text(row.get(actual_out_col)) if actual_out_col and row.get(actual_out_col) else "")
        building = self._hotel_building_name(row)
        idx = self.ui.cmbHotelBuilding.findText(building)
        if idx >= 0:
            self.ui.cmbHotelBuilding.setCurrentIndex(idx)
        room = self._hotel_guest_room(row)
        idx = self.ui.cmbHotelRoom.findText(room)
        if idx < 0 and room:
            self.ui.cmbHotelRoom.addItem(room, room)
            idx = self.ui.cmbHotelRoom.findText(room)
        if idx >= 0:
            self.ui.cmbHotelRoom.setCurrentIndex(idx)
        for widget_name, aliases in (("txtHotelArrival", ("TarikhVorod", "arrival")), ("txtHotelDeparture", ("TarikhKhoroj", "departure"))):
            col = self._hotel_pick(row, *aliases)
            if col:
                getattr(self.ui, widget_name).setText(self._hotel_text(row.get(col)))
        for widget_name, aliases in (("chkHotelBreakfast", ("sobhmanne", "breakfast")), ("chkHotelLunch", ("nahar", "lunch")), ("chkHotelDinner", ("sham", "dinner"))):
            col = self._hotel_pick(row, *aliases)
            if col:
                getattr(self.ui, widget_name).setChecked(self._hotel_bool(row.get(col), False))
        self._hotel_loading_guest_form = False

    def _hotel_load_today_movements(self):
        table = getattr(self, "tblHotelToday", None)
        if table is None:
            return
        today = self._hotel_today_jalali().replace("/", "")
        table.setRowCount(0)
        for row in reversed(self._hotel_guests):
            id_col = self._hotel_pick(row, "ID", "id")
            arr_col = self._hotel_pick(row, "TarikhVorod", "arrival")
            dep_col = self._hotel_pick(row, "TarikhKhoroj", "departure")
            actual_in = self._hotel_pick(row, "TarikhIn", "actualcheckin")
            actual_out = self._hotel_pick(row, "tarikhOut", "actualcheckout")
            first_col = self._hotel_pick(row, "Nam", "name")
            family_col = self._hotel_pick(row, "Family", "family")
            full_name = " ".join(x for x in (self._hotel_text(row.get(first_col)) if first_col else "", self._hotel_text(row.get(family_col)) if family_col else "") if x)
            people_col = self._hotel_pick(row, "TedadAfrad", "people")
            for action, date_col in (("ورود امروز", arr_col), ("خروج امروز", dep_col)):
                date_text = self._hotel_text(row.get(date_col)) if date_col else ""
                normalized_date = self._hotel_date_db(row.get(date_col)) if date_col else None
                if normalized_date != today:
                    continue
                if action == "ورود امروز" and actual_in and row.get(actual_in):
                    continue
                if action == "خروج امروز" and actual_out and row.get(actual_out):
                    continue
                values = [self._hotel_text(row.get(id_col)) if id_col else "", action, self._hotel_building_name(row), self._hotel_guest_room(row), full_name, self._hotel_text(row.get(people_col)) if people_col else "", date_text]
                idx = table.rowCount()
                table.insertRow(idx)
                for col, value in enumerate(values):
                    table.setItem(idx, col, QTableWidgetItem(str(value)))
                table.item(idx, 0).setData(Qt.ItemDataRole.UserRole, row.get(id_col) if id_col else None)

    @staticmethod
    def _hotel_today_jalali():
        d = jdatetime.date.today()
        return f"{d.year:04d}/{d.month:02d}/{d.day:02d}"

    @staticmethod
    def _hotel_norm(value):
        return "".join(ch.casefold() for ch in str(value or "").strip() if ch not in " _-./\\")

    @staticmethod
    def _hotel_text(value):
        if value is None:
            return ""
        if isinstance(value, bool):
            return "بله" if value else "خیر"
        if hasattr(value, "strftime"):
            try:
                jd = jdatetime.date.fromgregorian(date=value.date() if isinstance(value, datetime) else value)
                return f"{jd.year:04d}/{jd.month:02d}/{jd.day:02d}"
            except Exception:
                return value.strftime("%Y-%m-%d")
        text = str(value).strip()
        # فیلدهای Number در Access ممکن است به صورت 14050722.0 برگردند.
        numeric_date = re.fullmatch(r"(\d{7,8})(?:\.0+)?", text)
        if numeric_date:
            digits = numeric_date.group(1)
            if len(digits) == 8:
                return f"{digits[:4]}/{digits[4:6]}/{digits[6:8]}"
            # نمونه عدد شمسی با حذف صفر ابتدای ماه: 1405718
            year, rest = digits[:4], digits[4:]
            month, day = int(rest[0]), int(rest[1:])
            if 1 <= month <= 12 and 1 <= day <= 31:
                return f"{int(year):04d}/{month:02d}/{day:02d}"
        digits = "".join(c for c in text if c.isdigit())
        if len(digits) == 8 and digits.isdigit():
            return f"{digits[:4]}/{digits[4:6]}/{digits[6:8]}"
        return text

    @staticmethod
    def _hotel_date_db(value):
        """نرمال‌سازی تاریخ برای مقایسه؛ پشتیبانی از تاریخ شمسی و Date/Time اکسس."""
        if value is None or value == "":
            return None

        # فیلدهای Date/Time اکسس معمولاً به شکل datetime/date از pyodbc برمی‌گردند.
        if isinstance(value, datetime):
            gregorian = value.date()
            jalali = jdatetime.date.fromgregorian(date=gregorian)
            return f"{jalali.year:04d}{jalali.month:02d}{jalali.day:02d}"
        if isinstance(value, py_date):
            jalali = jdatetime.date.fromgregorian(date=value)
            return f"{jalali.year:04d}{jalali.month:02d}{jalali.day:02d}"

        raw = str(value).strip()
        if not raw:
            return None
        # تبدیل ارقام فارسی و عربی به ارقام لاتین قبل از مقایسه.
        digit_map = str.maketrans("۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩", "01234567890123456789")
        raw = raw.translate(digit_map)

        import re
        # Access Number ممکن است مقدار شمسی را به شکل 14050722.0 برگرداند.
        # اعشار صفر را حذف می‌کنیم تا تاریخ ۸ رقمی به اشتباه ۹ رقمی نشود.
        numeric_date = re.fullmatch(r"(\d{7,8})(?:\.0+)?", raw)
        if numeric_date:
            raw = numeric_date.group(1)

        # تاریخ میلادی متنی (مانند 2026-10-17 یا 2026-10-17 00:00:00).
        match = re.match(r"^(\d{4})[-/.](\d{1,2})[-/.](\d{1,2})", raw)
        if match and int(match.group(1)) >= 1900:
            try:
                gregorian = py_date(int(match.group(1)), int(match.group(2)), int(match.group(3)))
                jalali = jdatetime.date.fromgregorian(date=gregorian)
                return f"{jalali.year:04d}{jalali.month:02d}{jalali.day:02d}"
            except ValueError:
                return None

        digits = "".join(c for c in raw if c.isdigit())
        if len(digits) == 8:
            # اگر مقدار عددی/متنی میلادی باشد، آن را به شمسی تبدیل کن.
            if digits.startswith(("19", "20")):
                try:
                    gregorian = py_date(int(digits[:4]), int(digits[4:6]), int(digits[6:8]))
                    jalali = jdatetime.date.fromgregorian(date=gregorian)
                    return f"{jalali.year:04d}{jalali.month:02d}{jalali.day:02d}"
                except ValueError:
                    return None
            return digits
        if len(digits) == 7:
            # عددهای شمسی Access که صفر ابتدای ماه را حذف کرده‌اند، مثل 1405718.
            year, rest = digits[:4], digits[4:]
            if len(rest) == 3:
                month, day = int(rest[0]), int(rest[1:])
            else:
                month, day = int(rest[:2]), int(rest[2:])
            if 1 <= month <= 12 and 1 <= day <= 31:
                return f"{int(year):04d}{month:02d}{day:02d}"
        return None

    def _hotel_get_schema(self, cursor, table_name, cache_attr):
        cached = getattr(self, cache_attr, None)
        if cached is not None:
            return cached
        cursor.execute(f"SELECT TOP 1 * FROM [{table_name}]")
        schema = [d[0] for d in cursor.description]
        setattr(self, cache_attr, schema)
        return schema

    def _hotel_db_date_value(self, cursor, table_name, column_name, jalali_value):
        """تبدیل تاریخ شمسی به نوع واقعی ستون Access (Date/Time، عدد یا متن)."""
        if jalali_value in (None, ""):
            return None
        digits = re.sub(r"\D", "", normalize_digits(jalali_value))
        if len(digits) != 8:
            raise ValueError(f"تاریخ {jalali_value!r} معتبر نیست؛ نمونه: 1405/07/18")
        try:
            jd = jdatetime.date(int(digits[:4]), int(digits[4:6]), int(digits[6:8]))
        except Exception as exc:
            raise ValueError(f"تاریخ شمسی {jalali_value!r} معتبر نیست.") from exc

        # اطلاعات نوع ستون را از metadata خود درایور Access می‌خوانیم.
        cache = getattr(self, "_hotel_column_types", None)
        if cache is None:
            cache = {}
            self._hotel_column_types = cache
        key = (table_name.casefold(), column_name.casefold())
        type_name = cache.get(key)
        if type_name is None:
            try:
                for meta in cursor.columns(table=table_name):
                    col = getattr(meta, "column_name", None)
                    if col and str(col).casefold() == column_name.casefold():
                        type_name = str(getattr(meta, "type_name", "") or "").casefold()
                        break
            except Exception:
                type_name = ""
            cache[key] = type_name or ""

        if any(token in type_name for token in ("date", "time")):
            return jd.togregorian()
        if any(token in type_name for token in ("char", "text", "memo", "string")):
            return digits
        # ستون‌های Number/Integer/Decimal؛ رفتار پیش‌فرض برای دیتابیس فعلی.
        return int(digits)

    def _hotel_pick(self, row, *aliases):
        lookup = {self._hotel_norm(k): k for k in row.keys()}
        for alias in aliases:
            key = lookup.get(self._hotel_norm(alias))
            if key is not None:
                return key
        return None

    def _hotel_read_rows(self, cursor, table_name, cache_attr):
        cursor.execute(f"SELECT * FROM [{table_name}]")
        schema = [d[0] for d in cursor.description]
        setattr(self, cache_attr, schema)
        return [dict(zip(schema, tuple(record))) for record in cursor.fetchall()]

    def _hotel_room_defaults(self):
        rooms = []
        for section in "ABCDEF":
            for n in range(1, 5):
                rooms.append(("لاله", f"{section}{n}", 3))
        for suite in "ABCDEF":
            rooms.append(("لیان", suite, 2))
        return rooms

    def _hotel_refresh_org_combo(self):
        """سازمان‌های قبلاً ثبت‌شده را پیشنهاد می‌دهد و ورود دستی را هم مجاز می‌گذارد."""
        combo = getattr(self.ui, "cmbHotelOrg", None)
        if combo is None:
            return
        current = combo.currentText().strip()
        org_col_aliases = ("Sazman", "organization")
        orgs = set()
        for row in getattr(self, "_hotel_guests", []):
            col = self._hotel_pick(row, *org_col_aliases)
            value = self._hotel_text(row.get(col)).strip() if col else ""
            if value:
                orgs.add(value)
        ordered = sorted(orgs, key=lambda value: value.casefold())
        combo.blockSignals(True)
        combo.clear()
        combo.addItems(ordered)
        combo.setCurrentIndex(-1)
        combo.setEditText(current)
        combo.blockSignals(False)

    def _hotel_refresh_national_combo(self):
        combo = getattr(self.ui, "cmbHotelNational", None)
        if combo is None:
            return
        current = combo.currentText().strip()
        values = set()
        for row in getattr(self, "_hotel_guests", []):
            col = self._hotel_pick(row, "CodeMeli", "nationalcode")
            value = self._hotel_text(row.get(col)).strip() if col else ""
            if value:
                values.add(value)
        ordered = sorted(values, key=lambda value: value.casefold())
        combo.blockSignals(True)
        combo.clear()
        combo.addItems(ordered)
        combo.setCurrentIndex(-1)
        combo.setEditText(current)
        combo.blockSignals(False)

    def _hotel_national_changed(self, value):
        """با وارد کردن کد ملی ذخیره‌شده، مشخصات فردی آخرین سابقه را خودکار پر می‌کند.

        این کار یک اقامت جدید را آماده می‌کند؛ شناسه رکورد قبلی به‌عنوان رکورد ویرایشی
        انتخاب نمی‌شود تا ثبت مهمان جدید با همان کد ملی سابقه قبلی را بازنویسی نکند.
        """
        if getattr(self, "_hotel_loading_guest_form", False):
            return
        national = normalize_digits(value).strip()
        if not national:
            return
        matches = []
        for row in getattr(self, "_hotel_guests", []):
            col = self._hotel_pick(row, "CodeMeli", "nationalcode")
            saved = normalize_digits(self._hotel_text(row.get(col))).strip() if col else ""
            if saved and saved == national:
                matches.append(row)
        if not matches:
            return
        # آخرین رکورد (با ID بزرگ‌تر در صورت عددی بودن) اولویت دارد.
        def sort_key(row):
            col = self._hotel_pick(row, "ID", "id")
            try:
                return int(row.get(col) or 0)
            except (TypeError, ValueError):
                return 0
        guest = max(matches, key=sort_key)
        for widget_name, aliases in (
            ("txtHotelFirstName", ("Nam", "name")),
            ("txtHotelLastName", ("Family", "family")),
            ("txtHotelPeople", ("TedadAfrad", "people")),
            ("txtHotelEmployee", ("Codepersoneli", "personnelcode")),
        ):
            col = self._hotel_pick(guest, *aliases)
            widget = getattr(self.ui, widget_name)
            if col and (not widget.text().strip() or widget_name in ("txtHotelFirstName", "txtHotelLastName")):
                widget.setText(self._hotel_text(guest.get(col)))
        org_col = self._hotel_pick(guest, "Sazman", "organization")
        if org_col and not self.ui.cmbHotelOrg.currentText().strip():
            self.ui.cmbHotelOrg.setEditText(self._hotel_text(guest.get(org_col)))

    def _hotel_load_all(self, *_args):
        try:
            conn = get_connection()
            try:
                cur = conn.cursor()
                room_rows = self._hotel_read_rows(cur, "tblMehmansera", "_hotel_room_schema")
                guest_rows = self._hotel_read_rows(cur, "tblHotel", "_hotel_guest_schema")
            finally:
                conn.close()
            # همیشه موجودی کامل شناخته‌شده نمایش داده شود؛ حتی اگر برای بعضی اتاق‌ها
            # در tblMehmansera رکوردی وجود نداشته باشد. این ردیف‌های موقت فقط برای نمایش‌اند
            # و هیچ رکوردی در دیتابیس درج یا تغییر داده نمی‌شود.
            # کلید یکتا برای هر اتاق؛ فاصله، خط تیره و تفاوت حروف نباید کارت تکراری بسازند.
            # فقط فهرست استاندارد ۳۰ اتاق/سوئیت نمایش داده می‌شود؛ رکوردهای تکراری یا نام‌های
            # قدیمی/ناهمسان دیتابیس به‌عنوان کارت اضافه وارد صفحه نمی‌شوند.
            room_by_key = {}
            for saved_room in room_rows:
                b = self._hotel_building_name(saved_room)
                r = self._hotel_room_name(saved_room)
                if not b or not r:
                    continue
                key = (self._hotel_norm(b), self._hotel_room_key(r))
                previous = room_by_key.get(key)
                if previous is None:
                    room_by_key[key] = saved_room
                else:
                    # اگر رکوردهای تکراری برای یک اتاق وجود دارند، رکوردی که empty=False
                    # دارد ترجیح داده می‌شود تا وضعیت اشغال ناخواسته به خالی تبدیل نشود.
                    empty_col = self._hotel_pick(saved_room, "empty")
                    prev_empty_col = self._hotel_pick(previous, "empty")
                    if empty_col and prev_empty_col and previous.get(prev_empty_col) is True and saved_room.get(empty_col) is False:
                        room_by_key[key] = saved_room
            complete_rooms = []
            for b, r, capacity in self._hotel_room_defaults():
                saved_room = room_by_key.get((self._hotel_norm(b), self._hotel_room_key(r)))
                if saved_room is not None:
                    complete_rooms.append(saved_room)
                else:
                    complete_rooms.append({
                        "ID": None, "build": b, "namOtagh": r,
                        "Status": "فعال", "empty": True, "_display_only": True,
                    })
            self._hotel_rooms = complete_rooms
            self._hotel_guests = guest_rows
            self._hotel_refresh_org_combo()
            self._hotel_refresh_national_combo()
            self._hotel_render_rooms()
            self._hotel_load_history()
            self._hotel_refresh_room_combo()
            self._hotel_update_summary()
            self._hotel_load_today_movements()
        except Exception as exc:
            QMessageBox.warning(self, "اتاق‌داری", f"خواندن جدول‌های tblMehmansera و tblHotel ناموفق بود:\n{exc}\n\nنام فیلدها و نوع داده‌ها را بررسی کنید.")
            self.ui.tblHotelRooms.setRowCount(0)
            self.ui.tblHotelHistory.setRowCount(0)

    def _hotel_set_building_filter(self, building):
        self._hotel_building_filter = building
        self._hotel_render_rooms()

    def _hotel_room_name(self, row):
        col = self._hotel_pick(row, "namOtagh", "namOt agh", "namOtakh", "room", "roomname", "نام اتاق")
        return self._hotel_text(row.get(col)) if col else ""

    def _hotel_building_name(self, row):
        col = self._hotel_pick(row, "build", "building", "sazman", "ساختمان")
        value = self._hotel_text(row.get(col)) if col else ""
        low = value.casefold().replace("ي", "ی").replace("ك", "ک")
        if "لاله" in low or "laleh" in low:
            return "لاله"
        if "لیان" in low or "lian" in low:
            return "لیان"
        return value.strip()

    def _hotel_guest_room(self, row):
        col = self._hotel_pick(row, "namOtahg", "namOtagh", "namOt agh", "room", "roomname", "اتاق")
        return self._hotel_text(row.get(col)) if col else ""

    def _hotel_room_key(self, value):
        """کلید یکسان برای نام‌های معادل اتاق/سوئیت در دو جدول."""
        text = str(value or "").strip().casefold().replace("ي", "ی").replace("ك", "ک")
        text = re.sub(r"(?:سوئیت|سویت|سوئيت|suite|room|اتاق)", "", text, flags=re.IGNORECASE)
        return re.sub(r"[^a-z0-9آ-ی]", "", text)

    def _hotel_same_room(self, first, second):
        a = self._hotel_room_key(first)
        b = self._hotel_room_key(second)
        return bool(a and b and a == b)

    def _hotel_same_building(self, first, second):
        return self._hotel_norm(self._hotel_building_name({"build": first})) == self._hotel_norm(self._hotel_building_name({"build": second}))

    @staticmethod
    def _hotel_bool(value, default=False):
        """تبدیل مطمئن مقدار Yes/No اکسس به bool؛ رشته False نباید True شود."""
        if value is None:
            return default
        if isinstance(value, bool):
            return value
        if isinstance(value, (int, float)):
            return value != 0
        text = str(value).strip().casefold()
        if text in ("false", "no", "نخیر", "خیر", "0", "0.0", "off", "غیرفعال"):
            return False
        if text in ("true", "yes", "بله", "1", "1.0", "on", "فعال"):
            return True
        return default

    def _hotel_current_guest(self, building, room):
        """مهمان جاری اتاق را بدون اتکا به فیلد empty تشخیص می‌دهد.

        معیارهای اشغال:
        1) ورود واقعی ثبت شده و خروج واقعی ثبت نشده؛ یا
        2) امروز داخل بازه ورود/خروج برنامه‌ریزی‌شده است و خروج واقعی ثبت نشده.
        تاریخ‌های Number اکسس مثل 14050722 و 14050722.0 به یک قالب تبدیل می‌شوند.
        """
        today = self._hotel_date_db(self._hotel_today_jalali())
        actual_candidates = []
        date_candidates = []
        for row in self._hotel_guests:
            if not self._hotel_same_building(self._hotel_building_name(row), building):
                continue
            if not self._hotel_same_room(self._hotel_guest_room(row), room):
                continue

            out_col = self._hotel_pick(row, "tarikhOut", "actualcheckout", "تاریخ خروج واقعی")
            in_col = self._hotel_pick(row, "TarikhIn", "actualcheckin", "تاریخ ورود واقعی")
            arr_col = self._hotel_pick(row, "TarikhVorod", "arrival", "تاریخ ورود")
            dep_col = self._hotel_pick(row, "TarikhKhoroj", "departure", "تاریخ خروج")

            actual_out = self._hotel_date_db(row.get(out_col)) if out_col else None
            actual_in = self._hotel_date_db(row.get(in_col)) if in_col else None
            # خروج واقعی ثبت شده یعنی این اقامت خاتمه یافته و نباید اتاق را اشغال کند.
            if actual_out:
                continue

            if actual_in:
                actual_candidates.append((actual_in, row))
                continue

            planned_in = self._hotel_date_db(row.get(arr_col)) if arr_col else None
            planned_out = self._hotel_date_db(row.get(dep_col)) if dep_col else None
            if today and planned_in and planned_out and planned_in <= today <= planned_out:
                date_candidates.append((planned_in, planned_out, row))

        # ورود واقعی بر رکورد صرفاً برنامه‌ریزی‌شده اولویت دارد.
        if actual_candidates:
            return sorted(actual_candidates, key=lambda item: item[0], reverse=True)[0][1]
        if date_candidates:
            return sorted(date_candidates, key=lambda item: (item[0], item[1]), reverse=True)[0][2]
        return None

    def _hotel_has_date_overlap(self, building, room, arrival, departure):
        new_arrival = self._hotel_date_db(arrival)
        new_departure = self._hotel_date_db(departure)
        if not new_arrival or not new_departure:
            return False
        editing_id = getattr(self, "_hotel_active_guest_id", None)
        for row in self._hotel_guests:
            if not self._hotel_same_building(self._hotel_building_name(row), building):
                continue
            if not self._hotel_same_room(self._hotel_guest_room(row), room):
                continue
            id_col = self._hotel_pick(row, "ID", "id")
            if editing_id is not None and id_col and str(row.get(id_col)) == str(editing_id):
                continue
            arr_col = self._hotel_pick(row, "TarikhVorod", "arrival")
            dep_col = self._hotel_pick(row, "TarikhKhoroj", "departure")
            out_col = self._hotel_pick(row, "tarikhOut", "actualcheckout")
            old_arr = self._hotel_date_db(row.get(arr_col)) if arr_col else None
            old_dep = self._hotel_date_db(row.get(dep_col)) if dep_col else None
            actual_out = self._hotel_date_db(row.get(out_col)) if out_col else None
            if actual_out or not old_arr or not old_dep:
                continue
            if old_arr <= new_departure and new_arrival <= old_dep:
                return True
        return False

    def _hotel_render_rooms(self):
        table = self.ui.tblHotelRooms
        table.setRowCount(0)
        grid = getattr(self, "hotelRoomCardsLayout", None)
        if grid:
            while grid.count():
                item = grid.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
        card_index = 0
        for room_row in self._hotel_rooms:
            building = self._hotel_building_name(room_row)
            room = self._hotel_room_name(room_row)
            if not building or not room or (self._hotel_building_filter and building != self._hotel_building_filter):
                continue
            status_col = self._hotel_pick(room_row, "Status", "status", "vaziyat", "فعال")
            active = self._hotel_text(room_row.get(status_col)) if status_col else "فعال"
            empty_col = self._hotel_pick(room_row, "empty")
            empty_value = self._hotel_bool(room_row.get(empty_col), default=True) if empty_col else True
            guest = self._hotel_current_guest(building, room)
            reservation = None
            today_digits = self._hotel_date_db(self._hotel_today_jalali()) or ""

            # وضعیت اتاق فقط از فیلد empty تعیین نمی‌شود.
            # اگر تاریخ امروز داخل بازه ورود/خروج یک مهمان باشد، اتاق باید «پر» باشد،
            # حتی اگر TarikhIn هنوز ثبت نشده یا empty در tblMehmansera اشتباهاً True باشد.
            active_date_guest = None
            if today_digits:
                dated_candidates = []
                for candidate in self._hotel_guests:
                    if not self._hotel_same_building(self._hotel_building_name(candidate), building) or not self._hotel_same_room(self._hotel_guest_room(candidate), room):
                        continue
                    arr_col_candidate = self._hotel_pick(candidate, "TarikhVorod", "arrival")
                    dep_col_candidate = self._hotel_pick(candidate, "TarikhKhoroj", "departure")
                    out_col = self._hotel_pick(candidate, "tarikhOut", "actualcheckout")
                    start_digits = self._hotel_date_db(candidate.get(arr_col_candidate)) if arr_col_candidate else None
                    end_digits = self._hotel_date_db(candidate.get(dep_col_candidate)) if dep_col_candidate else None
                    actual_out = self._hotel_date_db(candidate.get(out_col)) if out_col else None
                    if actual_out or not start_digits or not end_digits:
                        continue
                    if start_digits <= today_digits <= end_digits:
                        dated_candidates.append((start_digits, end_digits, candidate))
                if dated_candidates:
                    # در صورت وجود چند رکورد، رکوردی که نزدیک‌ترین تاریخ ورود را دارد انتخاب شود.
                    active_date_guest = sorted(dated_candidates, key=lambda item: (item[0], item[1]), reverse=True)[0][2]

            if guest is None and active_date_guest is not None:
                guest = active_date_guest

            # رزرو آینده فقط «رزرو» است و هنوز اتاق را پر نشان نمی‌دهد.
            if guest is None:
                candidates = []
                for candidate in self._hotel_guests:
                    if not self._hotel_same_building(self._hotel_building_name(candidate), building) or not self._hotel_same_room(self._hotel_guest_room(candidate), room):
                        continue
                    in_col = self._hotel_pick(candidate, "TarikhIn", "actualcheckin")
                    out_col = self._hotel_pick(candidate, "tarikhOut", "actualcheckout")
                    arr_col_candidate = self._hotel_pick(candidate, "TarikhVorod", "arrival")
                    dep_col_candidate = self._hotel_pick(candidate, "TarikhKhoroj", "departure")
                    if (in_col and candidate.get(in_col)) or (out_col and candidate.get(out_col)) or not arr_col_candidate or not dep_col_candidate:
                        continue
                    start_digits = self._hotel_date_db(candidate.get(arr_col_candidate))
                    end_digits = self._hotel_date_db(candidate.get(dep_col_candidate))
                    if start_digits and end_digits and today_digits and start_digits > today_digits:
                        candidates.append((start_digits, candidate))
                if candidates:
                    reservation = sorted(candidates, key=lambda item: item[0])[0][1]

            display_guest = guest or reservation
            # اگر امروز بین تاریخ ورود و خروج است، اتاق قطعاً پر است؛
            # این شرط عمداً بر empty=True غلبه می‌کند.
            # منبع معتبر وضعیت اتاق، بازه اقامت و تاریخ‌های واقعی در tblHotel است؛ فیلد empty نادیده گرفته می‌شود.
            occupied = guest is not None
            if occupied:
                status = "اشغال"
            elif reservation:
                status = "رزرو"
            else:
                status = "خالی" if active.casefold() not in ("غیرفعال", "inactive", "0") else "غیرفعال"
            name_col = self._hotel_pick(display_guest or {}, "Nam", "name") if display_guest else None
            family_col = self._hotel_pick(display_guest or {}, "Family", "family") if display_guest else None
            people_col = self._hotel_pick(display_guest or {}, "TedadAfrad", "people") if display_guest else None
            arr_col = self._hotel_pick(display_guest or {}, "TarikhVorod", "arrival") if display_guest else None
            dep_col = self._hotel_pick(display_guest or {}, "TarikhKhoroj", "departure") if display_guest else None
            actual_in_col = self._hotel_pick(display_guest or {}, "TarikhIn", "actualcheckin") if display_guest else None
            actual_out_col = self._hotel_pick(display_guest or {}, "tarikhOut", "actualcheckout") if display_guest else None
            planned_in = self._hotel_text(display_guest.get(arr_col)) if display_guest and arr_col else ""
            planned_out = self._hotel_text(display_guest.get(dep_col)) if display_guest and dep_col else ""
            actual_in = self._hotel_text(display_guest.get(actual_in_col)) if display_guest and actual_in_col else ""
            actual_out = self._hotel_text(display_guest.get(actual_out_col)) if display_guest and actual_out_col else ""
            guest_name = " ".join(x for x in (self._hotel_text(display_guest.get(name_col)) if display_guest and name_col else "", self._hotel_text(display_guest.get(family_col)) if display_guest and family_col else "") if x)
            values = [building, room, status, guest_name, self._hotel_text(display_guest.get(people_col)) if display_guest and people_col else "", actual_in or planned_in, planned_out, ""]
            row_idx = table.rowCount()
            table.insertRow(row_idx)
            for col_idx, value in enumerate(values):
                table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
            table.item(row_idx, 0).setData(Qt.ItemDataRole.UserRole, room_row.get(self._hotel_pick(room_row, "ID", "id")))
            if grid:
                if status == "خالی":
                    bg, border, accent = "#F0F9F3", "#8CC9A0", "#21864B"
                elif status == "اشغال":
                    bg, border, accent = "#FFF3F1", "#E6A39B", "#B9382B"
                elif status == "رزرو":
                    bg, border, accent = "#FFF7E8", "#E7C078", "#996515"
                else:
                    bg, border, accent = "#F1F3F5", "#C9CED4", "#667085"
                capacity = "۳ نفر ظرفیت" if building == "لاله" else "۲ نفر ظرفیت"
                guest_line = guest_name or ("آماده پذیرش" if status == "خالی" else "اطلاعات مهمان ثبت نشده")
                people_line = f"{self._hotel_text(display_guest.get(people_col))} نفر" if display_guest and people_col else capacity
                shown_in = actual_in or planned_in
                shown_out = actual_out or planned_out
                date_line = f"\nورود {shown_in}   |   خروج {shown_out}" if shown_in or shown_out else ""
                card_text = f"{room}  ·  {building}\n●  {status}\n{guest_line}\n{people_line}{date_line}"
                card = QPushButton(card_text, self.hotelRoomCardsHost)
                card.setObjectName("hotelRoomCardButton")
                card.setMinimumSize(155, 128)
                card.setMaximumWidth(280)
                card.setCursor(Qt.CursorShape.PointingHandCursor)
                card.setStyleSheet(f"QPushButton#hotelRoomCardButton {{ text-align:center; white-space:pre-wrap; background:{bg}; border:1px solid {border}; border-radius:10px; padding:9px; color:{accent}; font-size:11pt; font-weight:bold; }} QPushButton#hotelRoomCardButton:hover {{ border:2px solid {accent}; }}")
                card.clicked.connect(lambda checked=False, b=building, r=room: self._hotel_open_room_for_reception(b, r))
                cols = 5 if self.ui.tabHotel.width() > 1100 else 4
                grid.addWidget(card, card_index // cols, card_index % cols)
            card_index += 1
        if grid:
            grid.setRowStretch(card_index // 5 + 1, 1)

    def _hotel_open_room_for_reception(self, building, room):
        idx = self.ui.cmbHotelBuilding.findText(building)
        if idx >= 0:
            self.ui.cmbHotelBuilding.setCurrentIndex(idx)
        idx = self.ui.cmbHotelRoom.findText(room)
        if idx < 0:
            self.ui.cmbHotelRoom.addItem(room, room)
            idx = self.ui.cmbHotelRoom.findText(room)
        if idx >= 0:
            self.ui.cmbHotelRoom.setCurrentIndex(idx)
        guest = self._hotel_current_guest(building, room)
        if guest:
            self._hotel_fill_form_from_guest(guest)
        else:
            self._hotel_clear_form(keep_room=True)
            idx = self.ui.cmbHotelBuilding.findText(building)
            if idx >= 0:
                self.ui.cmbHotelBuilding.setCurrentIndex(idx)
            idx = self.ui.cmbHotelRoom.findText(room)
            if idx >= 0:
                self.ui.cmbHotelRoom.setCurrentIndex(idx)
            self.ui.txtHotelFirstName.setFocus()
        self.hotelSections.setCurrentWidget(self.hotelReceptionPage)

    def _hotel_refresh_room_combo(self, *_args):
        building = self.ui.cmbHotelBuilding.currentText().strip()
        combo = self.ui.cmbHotelRoom
        previous = combo.currentText()
        combo.blockSignals(True); combo.clear()
        for row in self._hotel_rooms:
            if self._hotel_building_name(row) != building:
                continue
            room = self._hotel_room_name(row)
            if room:
                current = self._hotel_current_guest(building, room)
                if current is None:
                    combo.addItem(room, room)
        if previous:
            idx = combo.findText(previous)
            if idx >= 0: combo.setCurrentIndex(idx)
        combo.blockSignals(False)

    def _hotel_update_summary(self):
        total = len([r for r in self._hotel_rooms if self._hotel_building_name(r) and self._hotel_room_name(r)])
        occupied = 0
        for r in self._hotel_rooms:
            b, room = self._hotel_building_name(r), self._hotel_room_name(r)
            if b and room and self._hotel_current_guest(b, room) is not None: occupied += 1
        vacant = max(0, total-occupied)
        self.ui.lblHotelLaleh.setText(f"ساختمان لاله: {sum(1 for r in self._hotel_rooms if self._hotel_building_name(r)=='لاله')} اتاق")
        self.ui.lblHotelLian.setText(f"ساختمان لیان: {sum(1 for r in self._hotel_rooms if self._hotel_building_name(r)=='لیان')} سوئیت")
        self.ui.lblHotelVacant.setText(f"خالی: {vacant}")
        self.ui.lblHotelOccupied.setText(f"اشغال: {occupied}")
        today = self._hotel_today_jalali().replace('/', '')
        arrivals = departures = 0
        for r in self._hotel_guests:
            ac = self._hotel_pick(r, "TarikhVorod", "arrival")
            dc = self._hotel_pick(r, "TarikhKhoroj", "departure")
            if ac and ''.join(c for c in self._hotel_text(r.get(ac)) if c.isdigit()) == today: arrivals += 1
            if dc and ''.join(c for c in self._hotel_text(r.get(dc)) if c.isdigit()) == today: departures += 1
        self.ui.lblHotelArrivals.setText(f"ورود امروز: {arrivals}")
        self.ui.lblHotelDepartures.setText(f"خروج امروز: {departures}")

    def _hotel_load_history(self, *_args):
        table = self.ui.tblHotelHistory
        search = self.ui.txtHotelSearch.text().strip().casefold()
        rows = self._hotel_guests
        if search:
            rows = [r for r in rows if search in " ".join(self._hotel_text(v) for v in r.values()).casefold()]
        table.setRowCount(0)
        for row in reversed(rows):
            id_col = self._hotel_pick(row, "ID", "id")
            name_col = self._hotel_pick(row, "Nam", "name")
            family_col = self._hotel_pick(row, "Family", "family")
            national_col = self._hotel_pick(row, "CodeMeli", "nationalcode")
            people_col = self._hotel_pick(row, "TedadAfrad", "people")
            arr_col = self._hotel_pick(row, "TarikhVorod", "arrival")
            dep_col = self._hotel_pick(row, "TarikhKhoroj", "departure")
            in_col = self._hotel_pick(row, "TarikhIn", "actualcheckin")
            out_col = self._hotel_pick(row, "tarikhOut", "actualcheckout")
            stay_col = self._hotel_pick(row, "modat eqhamat", "modateghamat", "stayduration")
            vals=[self._hotel_text(row.get(id_col)) if id_col else "", " ".join(x for x in [self._hotel_text(row.get(name_col)) if name_col else "",self._hotel_text(row.get(family_col)) if family_col else ""] if x),self._hotel_text(row.get(national_col)) if national_col else "",self._hotel_building_name(row),self._hotel_guest_room(row),self._hotel_text(row.get(people_col)) if people_col else "",self._hotel_text(row.get(arr_col)) if arr_col else "",self._hotel_text(row.get(dep_col)) if dep_col else "",self._hotel_text(row.get(in_col)) if in_col else "",self._hotel_text(row.get(out_col)) if out_col else "",self._hotel_text(row.get(stay_col)) if stay_col else ""]
            idx=table.rowCount(); table.insertRow(idx)
            for c,v in enumerate(vals): table.setItem(idx,c,QTableWidgetItem(str(v)))
            table.item(idx,0).setData(Qt.ItemDataRole.UserRole,row.get(id_col) if id_col else None)

    def _hotel_clear_form(self, *_args, keep_room=False):
        self._hotel_loading_guest_form = True
        self._hotel_active_guest_id = None
        self.ui.btnHotelEdit.setEnabled(False)
        self.ui.cmbHotelNational.setCurrentIndex(-1)
        self.ui.cmbHotelNational.setEditText("")
        for name in ("txtHotelFirstName","txtHotelLastName","txtHotelPeople","txtHotelEmployee"):
            getattr(self.ui,name).clear()
        self.ui.cmbHotelOrg.setCurrentIndex(-1)
        self.ui.cmbHotelOrg.setEditText("")
        self.ui.txtHotelArrival.setText(self._hotel_today_jalali())
        self.ui.txtHotelDeparture.setText(self._hotel_today_jalali())
        self.ui.txtHotelActualArrival.clear()
        self.ui.txtHotelActualDeparture.clear()
        self.ui.chkHotelBreakfast.setChecked(False); self.ui.chkHotelLunch.setChecked(False); self.ui.chkHotelDinner.setChecked(False)
        if not keep_room:
            self.ui.cmbHotelBuilding.setCurrentIndex(0); self._hotel_refresh_room_combo()
        self._hotel_loading_guest_form = False

    def _hotel_save_guest(self, *_args, checkin_now=False):
        # اگر رکوردی از کارت اتاق/جدول انتخاب شده باشد، «ثبت اقامت» همان ویرایش آن رکورد است.
        if not checkin_now and getattr(self, "_hotel_active_guest_id", None) not in (None, ""):
            self._hotel_edit_guest()
            return
        national = self.ui.cmbHotelNational.currentText().strip()
        first = self.ui.txtHotelFirstName.text().strip()
        family = self.ui.txtHotelLastName.text().strip()
        building = self.ui.cmbHotelBuilding.currentText().strip()
        room = self.ui.cmbHotelRoom.currentText().strip()
        # نام ساختمان و اتاق دقیقاً از کنترل‌های انتخاب‌شده خوانده می‌شوند؛
        # جلوی ثبت اقامت بدون نام اتاق گرفته شود.
        if not first or not family or not room:
            QMessageBox.warning(self,"ثبت اقامت","نام، نام خانوادگی و اتاق را مشخص کنید."); return
        if self._hotel_current_guest(building,room):
            QMessageBox.warning(self,"اتاق اشغال است","برای این اتاق اقامت فعال ثبت شده است."); return
        arrival=self._hotel_date_db(self.ui.txtHotelArrival.text())
        departure=self._hotel_date_db(self.ui.txtHotelDeparture.text())
        if not arrival or not departure:
            QMessageBox.warning(self,"تاریخ نامعتبر","تاریخ ورود و خروج را به‌صورت شمسی ۸ رقمی وارد کنید؛ مثال 1405/07/18."); return
        if departure < arrival:
            QMessageBox.warning(self,"تاریخ نامعتبر","تاریخ خروج نمی‌تواند قبل از تاریخ ورود باشد."); return
        actual_arrival = self._hotel_date_db(self.ui.txtHotelActualArrival.text())
        actual_departure = self._hotel_date_db(self.ui.txtHotelActualDeparture.text())
        if self.ui.txtHotelActualArrival.text().strip() and not actual_arrival:
            QMessageBox.warning(self,"تاریخ نامعتبر","تاریخ ورود واقعی را به شکل شمسی ۸ رقمی وارد کنید."); return
        if self.ui.txtHotelActualDeparture.text().strip() and not actual_departure:
            QMessageBox.warning(self,"تاریخ نامعتبر","تاریخ خروج واقعی را به شکل شمسی ۸ رقمی وارد کنید."); return
        if actual_arrival and actual_departure and actual_departure < actual_arrival:
            QMessageBox.warning(self,"تاریخ نامعتبر","تاریخ خروج واقعی نمی‌تواند قبل از ورود واقعی باشد."); return
        if self._hotel_has_date_overlap(building, room, arrival, departure):
            QMessageBox.warning(self,"تداخل اقامت","برای این اتاق در بازه انتخاب‌شده اقامت دیگری ثبت شده است."); return
        try:
            conn=get_connection()
            try:
                cur=conn.cursor()
                schema=self._hotel_get_schema(cur,"tblHotel","_hotel_guest_schema")
                norm={self._hotel_norm(x):x for x in schema}
                values={
                    "codemeli": national or None,
                    "nam": first,
                    "family": family,
                    "tedadafrad": int(self.ui.txtHotelPeople.text().strip() or "1"),
                    "sazman": self.ui.cmbHotelOrg.currentText().strip() or None,
                    "build": building,
                    "namotahg": room,
                    # فیلدهای تاریخ در Access از نوع Number هستند؛ مقدار باید عدد باشد نه رشته.
                    "tarikhvorod": int(arrival),
                    "tarikhkhoroj": int(departure),
                    "tarikhin": int(actual_arrival or self._hotel_date_db(self._hotel_today_jalali())) if (actual_arrival or checkin_now) else None,
                    "tarikhout": int(actual_departure) if actual_departure else None,
                    "modateghamat": max(0, int(departure)-int(arrival)),
                    "empty": not (checkin_now or (arrival <= (self._hotel_date_db(self._hotel_today_jalali()) or "") <= departure and not actual_departure)),
                    "sobhmanne": self.ui.chkHotelBreakfast.isChecked(),
                    "nahar": self.ui.chkHotelLunch.isChecked(),
                    "sham": self.ui.chkHotelDinner.isChecked(),
                    "darkhastkonande": self.username,
                    "editor": self.username,
                    # کد پرسنلی اختیاری است؛ رشته خالی به فیلد عددی Access ارسال نشود.
                    "codepersoneli": self.ui.txtHotelEmployee.text().strip() or None,
                }
                insert_cols=[]; params=[]
                # نام فیلد اتاق در نسخه‌های مختلف دیتابیس با دو املای رایج دیده شده:
                # namOtahg (املای قدیمی) و namOtagh. هر دو باید پشتیبانی شوند.
                field_aliases = {
                    "namotahg": ("namotahg", "namotagh", "room", "roomname"),
                    "build": ("build", "building"),
                }
                for alias,val in values.items():
                    if alias == "codepersoneli" and isinstance(val, str) and val.isdigit():
                        val = int(val)
                    candidates = field_aliases.get(alias, (alias,))
                    col = next((norm.get(self._hotel_norm(candidate)) for candidate in candidates
                                if norm.get(self._hotel_norm(candidate))), None)
                    if alias == "namotahg" and not col:
                        raise RuntimeError(
                            "فیلد نام اتاق در tblHotel پیدا نشد. نام فیلد باید namOtahg یا namOtagh باشد."
                        )
                    if col and self._hotel_norm(col) != "id":
                        if alias in ("tarikhvorod", "tarikhkhoroj", "tarikhin", "tarikhout"):
                            val = self._hotel_db_date_value(cur, "tblHotel", col, val)
                        insert_cols.append(f"[{col}]"); params.append(val)
                if not insert_cols:
                    raise RuntimeError("ساختار فیلدهای tblHotel با فیلدهای مورد انتظار تطبیق ندارد.")
                sql=f"INSERT INTO [tblHotel] ({', '.join(insert_cols)}) VALUES ({', '.join('?' for _ in params)})"
                cur.execute(sql,params)
                today_digits = self._hotel_date_db(self._hotel_today_jalali()) or ""
                occupies_room = bool(checkin_now or (today_digits and arrival <= today_digits <= departure and not actual_departure))
                if occupies_room:
                    # اقامت جاری یا رزروِ امروز باید اتاق را اشغال نشان دهد.
                    room_schema = self._hotel_get_schema(cur, "tblMehmansera", "_hotel_room_schema")
                    room_build_col = next((c for c in room_schema if self._hotel_norm(c) in ("build", "building")), None)
                    room_name_col = next((c for c in room_schema if self._hotel_norm(c) in ("namotagh", "room", "roomname")), None)
                    room_empty_col = next((c for c in room_schema if self._hotel_norm(c) == "empty"), None)
                    if room_build_col and room_name_col and room_empty_col:
                        cur.execute(f"UPDATE [tblMehmansera] SET [{room_empty_col}]=? WHERE [{room_build_col}]=? AND [{room_name_col}]=?", False, building, room)
                conn.commit()
            finally: conn.close()
            self._hotel_load_all(); self._hotel_clear_form()
            QMessageBox.information(self,"ثبت اقامت", "مهمان ثبت شد و ورود واقعی او نیز ثبت گردید؛ اتاق اشغال شد." if checkin_now else "اطلاعات اقامت ثبت شد و در سوابق باقی می‌ماند.")
        except Exception as exc:
            QMessageBox.critical(self,"خطای ثبت اقامت",f"ثبت در tblHotel انجام نشد:\n{exc}\n\nممکن است فیلد اجباری دیگری در دیتابیس وجود داشته باشد.")

    def _hotel_edit_guest(self, *_args):
        guest_id = getattr(self, "_hotel_active_guest_id", None)
        if guest_id in (None, ""):
            QMessageBox.information(self, "ویرایش اقامت", "ابتدا مهمان را از کارت اتاق یا جدول سوابق انتخاب کنید.")
            return

        national = self.ui.cmbHotelNational.currentText().strip()
        first = self.ui.txtHotelFirstName.text().strip()
        family = self.ui.txtHotelLastName.text().strip()
        building = self.ui.cmbHotelBuilding.currentText().strip()
        room = self.ui.cmbHotelRoom.currentText().strip()
        if not first or not family or not room:
            QMessageBox.warning(self, "ویرایش اقامت", "نام، نام خانوادگی و اتاق را مشخص کنید.")
            return

        arrival = self._hotel_date_db(self.ui.txtHotelArrival.text())
        departure = self._hotel_date_db(self.ui.txtHotelDeparture.text())
        actual_arrival = self._hotel_date_db(self.ui.txtHotelActualArrival.text())
        actual_departure = self._hotel_date_db(self.ui.txtHotelActualDeparture.text())
        if not arrival or not departure:
            QMessageBox.warning(self, "تاریخ نامعتبر", "تاریخ ورود و خروج را به‌صورت شمسی ۸ رقمی وارد کنید؛ مثال 1405/07/18.")
            return
        if departure < arrival:
            QMessageBox.warning(self, "تاریخ نامعتبر", "تاریخ خروج نمی‌تواند قبل از تاریخ ورود باشد.")
            return
        if self.ui.txtHotelActualArrival.text().strip() and not actual_arrival:
            QMessageBox.warning(self, "تاریخ نامعتبر", "تاریخ ورود واقعی را به شکل شمسی ۸ رقمی وارد کنید.")
            return
        if self.ui.txtHotelActualDeparture.text().strip() and not actual_departure:
            QMessageBox.warning(self, "تاریخ نامعتبر", "تاریخ خروج واقعی را به شکل شمسی ۸ رقمی وارد کنید.")
            return
        if actual_arrival and actual_departure and actual_departure < actual_arrival:
            QMessageBox.warning(self, "تاریخ نامعتبر", "تاریخ خروج واقعی نمی‌تواند قبل از ورود واقعی باشد.")
            return
        if self._hotel_has_date_overlap(building, room, arrival, departure):
            QMessageBox.warning(self, "تداخل اقامت", "برای این اتاق در بازه انتخاب‌شده اقامت دیگری ثبت شده است.")
            return

        conn = cursor = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            schema = self._hotel_get_schema(cursor, "tblHotel", "_hotel_guest_schema")
            id_col = next((c for c in schema if self._hotel_norm(c) == "id"), None)
            if not id_col:
                raise RuntimeError("فیلد ID در tblHotel پیدا نشد.")

            norm = {self._hotel_norm(x): x for x in schema}
            values = {
                "codemeli": national or None,
                "nam": first,
                "family": family,
                "tedadafrad": int(self.ui.txtHotelPeople.text().strip() or "1"),
                "sazman": self.ui.cmbHotelOrg.currentText().strip() or None,
                "build": building,
                "namotahg": room,
                "tarikhvorod": int(arrival),
                "tarikhkhoroj": int(departure),
                "tarikhin": int(actual_arrival) if actual_arrival else None,
                "tarikhout": int(actual_departure) if actual_departure else None,
                "modateghamat": max(0, int(departure) - int(arrival)),
                "sobhmanne": self.ui.chkHotelBreakfast.isChecked(),
                "nahar": self.ui.chkHotelLunch.isChecked(),
                "sham": self.ui.chkHotelDinner.isChecked(),
                "editor": self.username,
                "codepersoneli": self.ui.txtHotelEmployee.text().strip() or None,
            }
            field_aliases = {
                "namotahg": ("namotahg", "namotagh", "room", "roomname"),
                "build": ("build", "building"),
            }
            assignments = []
            params = []
            for alias, value in values.items():
                candidates = field_aliases.get(alias, (alias,))
                col = next((norm.get(self._hotel_norm(candidate)) for candidate in candidates if norm.get(self._hotel_norm(candidate))), None)
                if alias == "namotahg" and not col:
                    raise RuntimeError("فیلد نام اتاق در tblHotel پیدا نشد.")
                if col and self._hotel_norm(col) != "id":
                    if alias in ("tarikhvorod", "tarikhkhoroj", "tarikhin", "tarikhout"):
                        value = self._hotel_db_date_value(cursor, "tblHotel", col, value)
                    if alias == "codepersoneli" and isinstance(value, str) and value.isdigit():
                        value = int(value)
                    assignments.append(f"[{col}] = ?")
                    params.append(value)
            if not assignments:
                raise RuntimeError("هیچ فیلد قابل ویرایشی در tblHotel پیدا نشد.")
            params.append(guest_id)
            cursor.execute(f"UPDATE [tblHotel] SET {', '.join(assignments)} WHERE [{id_col}] = ?", params)

            # همگام‌سازی وضعیت اتاق در tblMehmansera با اطلاعات ویرایش‌شده.
            room_schema = self._hotel_get_schema(cursor, "tblMehmansera", "_hotel_room_schema")
            room_build_col = next((c for c in room_schema if self._hotel_norm(c) in ("build", "building")), None)
            room_name_col = next((c for c in room_schema if self._hotel_norm(c) in ("namotagh", "room", "roomname")), None)
            room_empty_col = next((c for c in room_schema if self._hotel_norm(c) == "empty"), None)
            if room_build_col and room_name_col and room_empty_col:
                # همه رکوردهای اتاق‌های مربوط به این مهمان ابتدا آزاد می‌شوند؛
                # سپس اتاق مقصد در صورت ورود واقعی دوباره اشغال می‌شود.
                old_row = next((r for r in self._hotel_guests if str(r.get(self._hotel_pick(r, "ID", "id"))) == str(guest_id)), None)
                old_building = self._hotel_building_name(old_row) if old_row else building
                old_room = self._hotel_guest_room(old_row) if old_row else room
                if old_building and old_room:
                    cursor.execute(
                        f"UPDATE [tblMehmansera] SET [{room_empty_col}]=? WHERE [{room_build_col}]=? AND [{room_name_col}]=?",
                        True, old_building, old_room
                    )
                today_digits = self._hotel_date_db(self._hotel_today_jalali()) or ""
                occupies_destination = bool(
                    not actual_departure and (
                        actual_arrival or (today_digits and arrival <= today_digits <= departure)
                    )
                )
                cursor.execute(
                    f"UPDATE [tblMehmansera] SET [{room_empty_col}]=? WHERE [{room_build_col}]=? AND [{room_name_col}]=?",
                    not occupies_destination, building, room
                )
            conn.commit()
            self._hotel_load_all()
            # رکورد ویرایش‌شده را دوباره انتخاب کن تا کاربر بلافاصله نتیجه را ببیند.
            updated = next((r for r in self._hotel_guests if str(r.get(self._hotel_pick(r, 'ID', 'id'))) == str(guest_id)), None)
            if updated:
                self._hotel_fill_form_from_guest(updated)
            QMessageBox.information(self, "ویرایش اقامت", "اطلاعات مهمان با موفقیت ویرایش و ذخیره شد.")
        except Exception as exc:
            if conn is not None:
                try:
                    conn.rollback()
                except Exception:
                    pass
            QMessageBox.critical(self, "خطای ویرایش اقامت", f"تغییرات ذخیره نشد:\n{exc}")
        finally:
            if cursor is not None:
                try:
                    cursor.close()
                except Exception:
                    pass
            if conn is not None:
                try:
                    conn.close()
                except Exception:
                    pass

    def _hotel_extend_stay(self, *_args):
        """تمدید اقامت مهمان جاری بدون دست‌کاری تاریخ‌های واقعی ورود/خروج."""
        guest_id = getattr(self, "_hotel_active_guest_id", None)
        if guest_id in (None, ""):
            QMessageBox.information(self, "تمدید اقامت", "ابتدا مهمان ساکن را از کارت اتاق یا جدول سوابق انتخاب کنید.")
            return

        guest = next((r for r in self._hotel_guests
                      if str(r.get(self._hotel_pick(r, "ID", "id"))) == str(guest_id)), None)
        if not guest:
            QMessageBox.warning(self, "تمدید اقامت", "رکورد مهمان پیدا نشد؛ ابتدا فهرست را تازه‌سازی کنید.")
            return
        actual_in_col = self._hotel_pick(guest, "TarikhIn", "actualcheckin")
        actual_out_col = self._hotel_pick(guest, "tarikhOut", "actualcheckout")
        if not actual_in_col or not guest.get(actual_in_col):
            QMessageBox.warning(self, "تمدید اقامت", "این مهمان هنوز ورود واقعی ندارد؛ تمدید فقط برای مهمان پذیرش‌شده امکان‌پذیر است.")
            return
        if actual_out_col and guest.get(actual_out_col):
            QMessageBox.warning(self, "تمدید اقامت", "برای این مهمان خروج واقعی ثبت شده است. برای اقامت جدید، رکورد جدید بسازید.")
            return

        arrival = self._hotel_date_db(self.ui.txtHotelArrival.text())
        new_departure = self._hotel_date_db(self.ui.txtHotelDeparture.text())
        dep_col_guest = self._hotel_pick(guest, "TarikhKhoroj", "departure")
        old_departure = self._hotel_date_db(guest.get(dep_col_guest)) if dep_col_guest else None
        if not arrival or not new_departure:
            QMessageBox.warning(self, "تاریخ نامعتبر", "تاریخ ورود و خروج مورد انتظار را به شکل شمسی وارد کنید؛ مثال 1405/07/18.")
            return
        if old_departure and new_departure <= old_departure:
            QMessageBox.information(self, "تمدید اقامت", "برای تمدید، تاریخ خروج مورد انتظار باید بعد از تاریخ فعلی باشد.")
            return
        building = self._hotel_building_name(guest)
        room = self._hotel_guest_room(guest)
        if self._hotel_has_date_overlap(building, room, arrival, new_departure):
            QMessageBox.warning(self, "تداخل اقامت", "این اتاق در تاریخ جدید با اقامت دیگری تداخل دارد.")
            return

        conn = cursor = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            schema = self._hotel_get_schema(cursor, "tblHotel", "_hotel_guest_schema")
            id_col = next((c for c in schema if self._hotel_norm(c) == "id"), None)
            dep_col = next((c for c in schema if self._hotel_norm(c) == "tarikhkhoroj"), None)
            stay_col = next((c for c in schema if self._hotel_norm(c) in ("modateghamat", "modateghamat", "stayduration")), None)
            if not id_col or not dep_col:
                raise RuntimeError("فیلد ID یا TarikhKhoroj در tblHotel پیدا نشد.")
            db_departure = self._hotel_db_date_value(cursor, "tblHotel", dep_col, new_departure)
            if stay_col:
                try:
                    arrival_date = jdatetime.date(int(arrival[:4]), int(arrival[4:6]), int(arrival[6:8]))
                    departure_date = jdatetime.date(int(new_departure[:4]), int(new_departure[4:6]), int(new_departure[6:8]))
                    stay_days = max(0, (departure_date - arrival_date).days)
                except Exception:
                    stay_days = 0
                cursor.execute(
                    f"UPDATE [tblHotel] SET [{dep_col}]=?, [{stay_col}]=? WHERE [{id_col}]=?",
                    db_departure, stay_days, guest_id
                )
            else:
                cursor.execute(f"UPDATE [tblHotel] SET [{dep_col}]=? WHERE [{id_col}]=?", db_departure, guest_id)
            conn.commit()
            self._hotel_load_all()
            updated = next((r for r in self._hotel_guests
                            if str(r.get(self._hotel_pick(r, "ID", "id"))) == str(guest_id)), None)
            if updated:
                self._hotel_fill_form_from_guest(updated)
            QMessageBox.information(self, "تمدید اقامت", f"اقامت اتاق {room} تا تاریخ {self.ui.txtHotelDeparture.text()} تمدید شد. تاریخ خروج واقعی تغییری نکرده است.")
        except Exception as exc:
            if conn is not None:
                try: conn.rollback()
                except Exception: pass
            QMessageBox.critical(self, "خطای تمدید اقامت", f"تمدید ذخیره نشد:\n{exc}")
        finally:
            if cursor is not None:
                try: cursor.close()
                except Exception: pass
            if conn is not None:
                try: conn.close()
                except Exception: pass

    def _hotel_selected_guest_id(self):
        # اگر مهمان قبلی از سوابق باز شده باشد، شناسه همان رکورد معتبر است.
        active_id = getattr(self, "_hotel_active_guest_id", None)
        if active_id is not None:
            return active_id

        # فرم با نام و نام خانوادگی پر شده ولی رکوردی از سوابق بارگذاری نشده است؛
        # این یک مهمان جدید است. ردیف باقی‌مانده/انتخاب‌شده در جدول سوابق نباید
        # باعث شود ورود به اشتباه روی مهمان قبلی ثبت شود و نام اتاق جدید ذخیره نشود.
        first_name = self.ui.txtHotelFirstName.text().strip()
        last_name = self.ui.txtHotelLastName.text().strip()
        if first_name or last_name:
            return None

        if getattr(self, "hotelSections", None) and self.hotelSections.currentWidget() is getattr(self, "hotelMovementsPage", None):
            row = self.tblHotelToday.currentRow()
            if row >= 0:
                item = self.tblHotelToday.item(row, 0)
                return item.data(Qt.ItemDataRole.UserRole) if item else None
        row = self.ui.tblHotelHistory.currentRow()
        if row < 0:
            return None
        item = self.ui.tblHotelHistory.item(row, 0)
        return item.data(Qt.ItemDataRole.UserRole) if item else None

    def _hotel_history_selected(self):
        rid = self._hotel_selected_guest_id()
        if rid is None:
            return
        row = next((r for r in self._hotel_guests if str(r.get(self._hotel_pick(r, "ID", "id"))) == str(rid)), None)
        if row:
            self._hotel_fill_form_from_guest(row)

    def _hotel_room_selected(self):
        row = self.ui.tblHotelRooms.currentRow()
        if row < 0:
            return
        building_item = self.ui.tblHotelRooms.item(row, 0)
        room_item = self.ui.tblHotelRooms.item(row, 1)
        if not building_item or not room_item:
            return
        building = building_item.text().strip()
        room = room_item.text().strip()
        i = self.ui.cmbHotelBuilding.findText(building)
        if i >= 0:
            self.ui.cmbHotelBuilding.setCurrentIndex(i)
        i = self.ui.cmbHotelRoom.findText(room)
        if i < 0:
            self.ui.cmbHotelRoom.addItem(room, room)
            i = self.ui.cmbHotelRoom.findText(room)
        if i >= 0:
            self.ui.cmbHotelRoom.setCurrentIndex(i)
        guest = self._hotel_current_guest(building, room)
        if guest:
            self._hotel_fill_form_from_guest(guest)
            if getattr(self, "hotelSections", None):
                self.hotelSections.setCurrentWidget(self.hotelReceptionPage)
        else:
            self._hotel_clear_form(keep_room=True)

    def _hotel_set_actual_date(self, action):
        rid=self._hotel_selected_guest_id()
        if rid is None:
            # برای مهمان جدید، ثبت ورود واقعی باید بتواند همان‌جا رکورد تازه بسازد؛
            # انتخاب ردیف از سوابق فقط برای مهمان از قبل ثبت‌شده لازم است.
            if action == "checkin" and self.ui.txtHotelFirstName.text().strip() and self.ui.txtHotelLastName.text().strip():
                if not self.ui.txtHotelActualArrival.text().strip():
                    self.ui.txtHotelActualArrival.setText(self._hotel_today_jalali())
                self._hotel_save_guest(checkin_now=True)
                return
            QMessageBox.information(self,"انتخاب اقامت","برای ورود مهمان جدید، نام و نام خانوادگی را وارد کنید؛ برای مهمان قبلی، ردیف او را از سوابق انتخاب کنید."); return
        actual_col="TarikhIn" if action=="checkin" else "tarikhOut"
        try:
            conn=get_connection()
            try:
                cur=conn.cursor()
                schema=self._hotel_get_schema(cur,"tblHotel","_hotel_guest_schema")
                id_col=next((c for c in schema if self._hotel_norm(c)=="id"),None)
                date_col=next((c for c in schema if self._hotel_norm(c)==self._hotel_norm(actual_col)),None)
                if not id_col or not date_col: raise RuntimeError(f"فیلد ID یا {actual_col} در tblHotel پیدا نشد.")
                selected = next((r for r in self._hotel_guests if str(r.get(self._hotel_pick(r,"ID","id"))) == str(rid)), None)
                if selected is None:
                    raise RuntimeError("رکورد مهمان در سوابق پیدا نشد؛ فهرست را تازه‌سازی کنید.")
                in_col = self._hotel_pick(selected, "TarikhIn", "actualcheckin")
                out_col = self._hotel_pick(selected, "tarikhOut", "actualcheckout")
                already_in = bool(in_col and selected.get(in_col))
                already_out = bool(out_col and selected.get(out_col))
                if action == "checkin" and already_in:
                    raise RuntimeError("ورود واقعی این مهمان قبلاً ثبت شده است.")
                if action == "checkin" and already_out:
                    raise RuntimeError("برای اقامتی که خروج واقعی دارد، ورود مجدد ثبت نمی‌شود؛ اقامت جدید بسازید.")
                if action == "checkout" and not already_in:
                    raise RuntimeError("ابتدا باید ورود واقعی مهمان ثبت شود.")
                if action == "checkout" and already_out:
                    raise RuntimeError("خروج واقعی این مهمان قبلاً ثبت شده است.")
                date_widget = self.ui.txtHotelActualArrival if action == "checkin" else self.ui.txtHotelActualDeparture
                selected_date = self._hotel_date_db(date_widget.text())
                if date_widget.text().strip() and not selected_date:
                    raise RuntimeError("تاریخ واقعی را به شکل شمسی ۸ رقمی وارد کنید؛ مثال 1405/07/18.")
                if not selected_date:
                    selected_date = self._hotel_date_db(self._hotel_today_jalali())
                    date_widget.setText(self._hotel_text(int(selected_date)))
                if action == "checkout" and in_col and selected.get(in_col):
                    in_date = self._hotel_date_db(selected.get(in_col))
                    if in_date and selected_date < in_date:
                        raise RuntimeError("تاریخ خروج واقعی نمی‌تواند قبل از ورود واقعی باشد.")
                # نوع ستون را از Access می‌گیریم؛ بعضی نسخه‌ها Number و بعضی Date/Time هستند.
                db_date_value = self._hotel_db_date_value(cur, "tblHotel", date_col, selected_date)
                cur.execute(f"UPDATE [tblHotel] SET [{date_col}]=? WHERE [{id_col}]=?", db_date_value, rid)
                if selected:
                    building = self._hotel_building_name(selected)
                    room = self._hotel_guest_room(selected)
                    room_schema = self._hotel_get_schema(cur, "tblMehmansera", "_hotel_room_schema")
                    room_id_col = next((c for c in room_schema if self._hotel_norm(c) == "id"), None)
                    room_build_col = next((c for c in room_schema if self._hotel_norm(c) in ("build", "building")), None)
                    room_name_col = next((c for c in room_schema if self._hotel_norm(c) in ("namotagh", "room", "roomname")), None)
                    empty_col = next((c for c in room_schema if self._hotel_norm(c) == "empty"), None)
                    if room_build_col and room_name_col and empty_col:
                        # در زمان ورود اتاق اشغال (False) و در زمان خروج خالی (True) می‌شود.
                        empty_value = action == "checkout"
                        cur.execute(f"UPDATE [tblMehmansera] SET [{empty_col}]=? WHERE [{room_build_col}]=? AND [{room_name_col}]=?", empty_value, building, room)
                # ثبت وضعیت خالی/اشغال در رکورد اقامت نیز، بدون حذف سابقه
                guest_empty_col = next((c for c in schema if self._hotel_norm(c) == "empty"), None)
                if guest_empty_col:
                    cur.execute(f"UPDATE [tblHotel] SET [{guest_empty_col}]=? WHERE [{id_col}]=?", action == "checkout", rid)
                conn.commit()
            finally:conn.close()
            self._hotel_load_all()
            QMessageBox.information(self,"ثبت ورود/خروج", "تاریخ واقعی ورود ثبت شد." if action=="checkin" else "تاریخ واقعی خروج ثبت شد؛ سابقه اقامت حذف نشده است.")
        except Exception as exc: QMessageBox.critical(self,"خطای ثبت",str(exc))

    # ---------------------------------------------------------
    # انبار و تقاضای لوازم‌التحریر؛ تمام کنترل‌ها در main.ui تعریف شده‌اند.
    # ---------------------------------------------------------
    def setup_tahrir_tabs(self):
        for table_name in ("tblAnbarTahrirList", "tblMtoTahrirList"):
            table = getattr(self.ui, table_name)
            table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
            table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
            table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
            table.setAlternatingRowColors(True)
            table.verticalHeader().setVisible(False)
            table.verticalHeader().setDefaultSectionSize(30)
            table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
            table.horizontalHeader().setStretchLastSection(True)
        self._anbar_tahrir_id = None
        self._mto_tahrir_id = None
        self._anbar_tahrir_rows = []
        self._mto_tahrir_rows = []
        self.ui.btnAnbarTahrirNew.clicked.connect(self.clear_anbar_tahrir_form)
        self.ui.btnAnbarTahrirSave.clicked.connect(self.save_anbar_tahrir_item)
        self.ui.btnAnbarTahrirEdit.clicked.connect(self.edit_anbar_tahrir_item)
        self.ui.btnAnbarTahrirDelete.clicked.connect(self.delete_anbar_tahrir_item)
        self.ui.btnAnbarTahrirRefresh.clicked.connect(self.load_anbar_tahrir_items)
        self.ui.txtAnbarTahrirSearch.textChanged.connect(self.load_anbar_tahrir_items)
        self.ui.tblAnbarTahrirList.itemSelectionChanged.connect(self.select_anbar_tahrir_item)
        self.ui.btnMtoTahrirNew.clicked.connect(self.clear_mto_tahrir_form)
        self.ui.btnMtoTahrirSave.clicked.connect(self.save_mto_tahrir_request)
        self.ui.btnMtoTahrirEdit.clicked.connect(self.edit_mto_tahrir_request)
        self.ui.btnMtoTahrirDelete.clicked.connect(self.delete_mto_tahrir_request)
        # در این سامانه ثبت درخواست به معنی تحویل قطعی است؛ دکمه تحویل جداگانه استفاده نمی‌شود.
        self.ui.btnMtoTahrirDeliver.hide()
        self.ui.btnMtoTahrirRefresh.clicked.connect(self.load_mto_tahrir_requests)
        self.ui.txtMtoTahrirSearch.textChanged.connect(self.load_mto_tahrir_requests)
        # فیلتر بازه تاریخ؛ جستجو بر اساس شرح کالا نیز صریحاً حفظ می‌شود.
        for date_name in ("txtMtoTahrirFromDate", "txtMtoTahrirToDate"):
            date_widget = getattr(self.ui, date_name, None)
            if date_widget is not None:
                install_calendar_action(date_widget)
                # پس از کامل‌شدن تاریخ یا انتخاب از تقویم فیلتر کن؛ برای هر رقم پیام خطا نده.
                date_widget.textChanged.connect(self._mto_tahrir_date_filter_changed)
                date_widget.editingFinished.connect(self.load_mto_tahrir_requests)
        self.ui.tblMtoTahrirList.itemSelectionChanged.connect(self.select_mto_tahrir_request)
        self.ui.txtMtoTahrirRecorder.setReadOnly(True)
        self.ui.txtMtoTahrirEditor.setReadOnly(True)
        self.ui.cmbMtoTahrirVahed.setEditable(True)
        self.ui.cmbMtoTahrirTaeidkonandeh.setEditable(True)
        self.ui.cmbMtoTahrirTahvilgirandeh.setEditable(True)
        install_calendar_action(self.ui.txtMtoTahrirDate)
        self.ui.txtMtoTahrirDate.setText(self._tahrir_today())
        self.ui.txtMtoTahrirRecorder.setText(self.username)
        self.ui.txtMtoTahrirEditor.setText(self.username)
        self._ensure_mto_tahrir_recipient_column()
        self._load_mto_tahrir_combo_sources()
        self.ui.cmbMtoTahrirVahed.setCurrentText(self.user_vahed)
        # جستجو/تکمیل خودکار شرح کالا از موجودی انبار، همراه با پرکردن واحد.
        self._setup_tahrir_description_completer()
        self.load_anbar_tahrir_items()
        self.load_mto_tahrir_requests()

    def _setup_tahrir_description_completer(self):
        """پیشنهاد شرح کالاها هنگام تایپ، از اقلام ثبت‌شده در انبار."""
        self._tahrir_description_completer = QCompleter([], self)
        self._tahrir_description_completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self._tahrir_description_completer.setFilterMode(Qt.MatchFlag.MatchContains)
        self._tahrir_description_completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
        self.ui.txtMtoTahrirDescription.setCompleter(self._tahrir_description_completer)
        self._tahrir_description_completer.activated[str].connect(self._select_tahrir_stock_description)
        # نمایش پیشنهادهای شرح هنگام تایپ؛ جستجو در نام کالا با تطبیق بخشی از متن
        self.ui.txtMtoTahrirDescription.textEdited.connect(self._show_tahrir_description_suggestions)
        self._refresh_tahrir_description_completer()

    def _show_tahrir_description_suggestions(self, text):
        """بازگرداندن جستجوی زنده/تکمیل خودکار شرح کالا هنگام تایپ."""
        completer = getattr(self, "_tahrir_description_completer", None)
        if completer is None:
            return
        completer.setCompletionPrefix(str(text or ""))
        if text and completer.completionCount() > 0:
            completer.complete()

    def _refresh_tahrir_description_completer(self):
        if not hasattr(self, "_tahrir_description_completer"):
            return
        conn = None
        descriptions = []
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT DISTINCT [Description] FROM [TBL_Anbar_Tahrir] WHERE [Description] IS NOT NULL ORDER BY [Description]")
            descriptions = [str(row[0]).strip() for row in cur.fetchall() if str(row[0] or "").strip()]
        except Exception:
            descriptions = []
        finally:
            if conn is not None:
                conn.close()
        self._tahrir_description_completer.setModel(
            QStringListModel(descriptions, self._tahrir_description_completer)
        )

    def _select_tahrir_stock_description(self, description):
        description = str(description or "").strip()
        self.ui.txtMtoTahrirDescription.setText(description)
        conn = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT TOP 1 [Unit] FROM [TBL_Anbar_Tahrir] WHERE [Description]=? ORDER BY [ID]", (description,))
            row = cur.fetchone()
            if row and row[0] is not None:
                self.ui.txtMtoTahrirUnit.setText(str(row[0]).strip())
        except Exception as exc:
            self._tahrir_db_error("انتخاب کالای انبار", exc)
        finally:
            if conn is not None:
                conn.close()

    def _ensure_mto_tahrir_recipient_column(self):
        """ستون تحویل‌گیرنده را در دیتابیس‌های قدیمی، در صورت نبودن، اضافه می‌کند."""
        conn = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT TOP 1 * FROM [TBL_Mto_tahrir]")
            columns = {str(d[0]).casefold() for d in cur.description}
            if "tahvilgirandeh" not in columns:
                cur.execute("ALTER TABLE [TBL_Mto_tahrir] ADD COLUMN [Tahvilgirandeh] TEXT(255)")
                conn.commit()
        finally:
            if conn is not None:
                conn.close()

    def _load_mto_tahrir_combo_sources(self):
        """واحدها از فیلد فارسی vahed در tblkar و نام‌ها از tbluser بارگذاری می‌شوند؛ تایپ آزاد فعال است."""
        units, users = [], []
        conn = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            # منبع واحدها، جدول درخواست‌های تعمیرات است که نام واحدهای فارسی در آن ثبت شده.
            try:
                cur.execute("SELECT DISTINCT [vahed] FROM [tblkar] WHERE [vahed] IS NOT NULL ORDER BY [vahed]")
                units = [str(row[0]).strip() for row in cur.fetchall() if str(row[0] or "").strip()]
            except Exception:
                units = []
            cur.execute("SELECT [username] FROM [tbluser]")
            users = list(dict.fromkeys(str(row[0]).strip() for row in cur.fetchall() if str(row[0] or "").strip()))
        except Exception:
            pass
        finally:
            if conn is not None:
                conn.close()
        for combo, values in ((self.ui.cmbMtoTahrirVahed, units),
                              (self.ui.cmbMtoTahrirTaeidkonandeh, users),
                              (self.ui.cmbMtoTahrirTahvilgirandeh, users)):
            current = combo.currentText().strip()
            combo.clear()
            combo.addItems(list(dict.fromkeys(values)))
            combo.setEditable(True)
            if current:
                combo.setCurrentText(current)

    @staticmethod
    def _tahrir_today():
        try:
            d = jdatetime.date.today()
            return f"{d.year:04d}/{d.month:02d}/{d.day:02d}"
        except Exception:
            return ""

    @staticmethod
    def _tahrir_norm(value):
        """یکسان‌سازی ارقام و حروف فارسی/عربی برای جستجوی قابل‌اعتماد."""
        value = normalize_digits(str(value or "").strip())
        return (value.replace("ي", "ی").replace("ى", "ی").replace("ك", "ک")
                     .replace("‌", " ").replace("ـ", ""))

    def _tahrir_db_date(self, value):
        value = self._tahrir_norm(value).replace("/", "").replace("-", "")
        if not value:
            d = jdatetime.date.today()
            return int(f"{d.year:04d}{d.month:02d}{d.day:02d}")
        if not value.isdigit() or len(value) != 8:
            raise ValueError("تاریخ باید به صورت شمسی YYYY/MM/DD وارد شود؛ نمونه 1405/07/27")
        return int(value)

    @staticmethod
    def _tahrir_display_date(value):
        if value is None:
            return ""
        raw = str(value).strip().replace("/", "").replace("-", "")
        if raw.isdigit() and len(raw) == 8:
            return f"{raw[:4]}/{raw[4:6]}/{raw[6:]}"
        return str(value).strip()

    def _tahrir_db_error(self, title, exc):
        QMessageBox.critical(self, title, f"عملیات با دیتابیس Access ناموفق بود.\n\n{exc}")

    def load_anbar_tahrir_items(self, *_):
        table = self.ui.tblAnbarTahrirList
        selected = self._anbar_tahrir_id
        try:
            conn = get_connection(); cur = conn.cursor()
            cur.execute("SELECT [ID], [Description], [QTY], [Unit] FROM [TBL_Anbar_Tahrir] ORDER BY [Description]")
            rows = cur.fetchall(); conn.close()
            query = self._tahrir_norm(self.ui.txtAnbarTahrirSearch.text()).casefold()
            self._anbar_tahrir_rows = [tuple(r) for r in rows if not query or query in self._tahrir_norm(r[1]).casefold() or query in self._tahrir_norm(r[3]).casefold()]
            table.setRowCount(len(self._anbar_tahrir_rows))
            for i, row in enumerate(self._anbar_tahrir_rows):
                values = [i + 1, row[1], row[2], row[3]]
                for j, value in enumerate(values):
                    item = QTableWidgetItem("" if value is None else str(value))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    table.setItem(i, j, item)
            table.resizeColumnsToContents()
            if selected is not None:
                for i, row in enumerate(self._anbar_tahrir_rows):
                    if str(row[0]) == str(selected):
                        table.selectRow(i); break
        except Exception as exc:
            self._tahrir_db_error("انبار لوازم‌التحریر", exc)

    def clear_anbar_tahrir_form(self):
        self._anbar_tahrir_id = None
        self.ui.txtAnbarTahrirDescription.clear(); self.ui.txtAnbarTahrirQty.clear(); self.ui.txtAnbarTahrirUnit.clear()
        self.ui.tblAnbarTahrirList.clearSelection()
        self.ui.txtAnbarTahrirDescription.setFocus()

    def select_anbar_tahrir_item(self):
        row_index = self.ui.tblAnbarTahrirList.currentRow()
        if row_index < 0 or row_index >= len(self._anbar_tahrir_rows): return
        row = self._anbar_tahrir_rows[row_index]
        self._anbar_tahrir_id = row[0]
        self.ui.txtAnbarTahrirDescription.setText(str(row[1] or ""))
        self.ui.txtAnbarTahrirQty.setText(str(row[2] if row[2] is not None else 0))
        self.ui.txtAnbarTahrirUnit.setText(str(row[3] or ""))

    def _anbar_tahrir_values(self):
        description = self._tahrir_norm(self.ui.txtAnbarTahrirDescription.text())
        unit = self._tahrir_norm(self.ui.txtAnbarTahrirUnit.text())
        qty_text = self._tahrir_norm(self.ui.txtAnbarTahrirQty.text())
        if not description: raise ValueError("شرح کالا را وارد کنید.")
        if not qty_text: raise ValueError("موجودی را وارد کنید.")
        try: qty = float(qty_text.replace(",", "."))
        except Exception: raise ValueError("موجودی باید عددی باشد.")
        if qty < 0: raise ValueError("موجودی نمی‌تواند منفی باشد.")
        return description, qty, unit

    def save_anbar_tahrir_item(self):
        try:
            description, qty, unit = self._anbar_tahrir_values()
            conn = get_connection(); cur = conn.cursor()
            cur.execute("INSERT INTO [TBL_Anbar_Tahrir] ([Description], [QTY], [Unit]) VALUES (?, ?, ?)", (description, qty, unit))
            conn.commit(); conn.close()
            self.load_anbar_tahrir_items(); self.clear_anbar_tahrir_form()
            self._refresh_tahrir_description_completer()
            QMessageBox.information(self, "انبار لوازم‌التحریر", "کالا با موفقیت ثبت شد.")
        except Exception as exc:
            self._tahrir_db_error("ثبت کالای انبار", exc)

    def edit_anbar_tahrir_item(self):
        if self._anbar_tahrir_id is None:
            QMessageBox.warning(self, "ویرایش کالا", "ابتدا یک کالا را از جدول انتخاب کنید."); return
        try:
            description, qty, unit = self._anbar_tahrir_values()
            conn = get_connection(); cur = conn.cursor()
            cur.execute("UPDATE [TBL_Anbar_Tahrir] SET [Description]=?, [QTY]=?, [Unit]=? WHERE [ID]=?", (description, qty, unit, self._anbar_tahrir_id))
            conn.commit(); conn.close(); self.load_anbar_tahrir_items()
            self._refresh_tahrir_description_completer()
            QMessageBox.information(self, "انبار لوازم‌التحریر", "اطلاعات کالا ویرایش شد.")
        except Exception as exc: self._tahrir_db_error("ویرایش کالای انبار", exc)

    def delete_anbar_tahrir_item(self):
        if self._anbar_tahrir_id is None:
            QMessageBox.warning(self, "حذف کالا", "ابتدا یک کالا را از جدول انتخاب کنید."); return
        if QMessageBox.question(self, "حذف کالا", "آیا از حذف این کالا مطمئن هستید؟") != QMessageBox.StandardButton.Yes: return
        try:
            conn = get_connection(); cur = conn.cursor()
            cur.execute("DELETE FROM [TBL_Anbar_Tahrir] WHERE [ID]=?", (self._anbar_tahrir_id,))
            conn.commit(); conn.close(); self.clear_anbar_tahrir_form(); self.load_anbar_tahrir_items()
            self._refresh_tahrir_description_completer()
        except Exception as exc: self._tahrir_db_error("حذف کالای انبار", exc)

    def _mto_tahrir_date_filter_changed(self, *_args):
        """اعمال بازه تاریخ فقط وقتی هر دو فیلد خالی یا کامل باشند."""
        from_widget = getattr(self.ui, "txtMtoTahrirFromDate", None)
        to_widget = getattr(self.ui, "txtMtoTahrirToDate", None)
        values = [self._tahrir_norm(w.text()).replace("/", "").replace("-", "")
                  for w in (from_widget, to_widget) if w is not None]
        if all(not value or (value.isdigit() and len(value) == 8) for value in values):
            self.load_mto_tahrir_requests()

    def load_mto_tahrir_requests(self, *_):
        table = self.ui.tblMtoTahrirList; selected = self._mto_tahrir_id
        try:
            conn = get_connection(); cur = conn.cursor()
            cur.execute("SELECT [ID], [Date], [Description], [QTY], [Unit], [vahed], [Recorder], [Taeidkonandeh], [Tahvilgirandeh], [Editor] FROM [TBL_Mto_tahrir] ORDER BY [Date] DESC, [ID] DESC")
            rows = cur.fetchall(); conn.close()
            query = self._tahrir_norm(self.ui.txtMtoTahrirSearch.text()).casefold()
            from_text = self._tahrir_norm(getattr(self.ui, "txtMtoTahrirFromDate", None).text() if getattr(self.ui, "txtMtoTahrirFromDate", None) is not None else "")
            to_text = self._tahrir_norm(getattr(self.ui, "txtMtoTahrirToDate", None).text() if getattr(self.ui, "txtMtoTahrirToDate", None) is not None else "")
            # هنگام تایپ تاریخ، تا زمانی که هر ۸ رقم کامل نشده فیلتر اعمال نمی‌شود.
            # این کار جلوی خطاهای پیاپی برای ورودی‌هایی مثل 1405/0 را می‌گیرد.
            from_compact = from_text.replace("/", "").replace("-", "")
            to_compact = to_text.replace("/", "").replace("-", "")
            from_date = self._tahrir_db_date(from_text) if len(from_compact) == 8 else None
            to_date = self._tahrir_db_date(to_text) if len(to_compact) == 8 else None
            if from_date is not None and to_date is not None and from_date > to_date:
                raise ValueError("تاریخ شروع بازه نباید بعد از تاریخ پایان باشد.")
            filtered=[]
            for r in rows:
                # جستجو در شرح کالا و تمام ستون‌های اصلی درخواست (از جمله تاریخ و تعداد).
                searchable = [self._tahrir_norm(v).casefold() for v in r]
                if query and not any(query in value for value in searchable):
                    continue
                row_date_text = self._tahrir_norm(r[1]).replace("/", "").replace("-", "")
                # Access ممکن است تاریخ را به صورت عدد، متن یا datetime برگرداند.
                if len(row_date_text) >= 8 and row_date_text[:8].isdigit():
                    row_date = int(row_date_text[:8])
                else:
                    row_date = None
                if from_date is not None and (row_date is None or row_date < from_date):
                    continue
                if to_date is not None and (row_date is None or row_date > to_date):
                    continue
                filtered.append(tuple(r))
            self._mto_tahrir_rows=filtered; table.setRowCount(len(filtered))
            for i,r in enumerate(filtered):
                values=[i + 1, self._tahrir_display_date(r[1]), r[2], r[3], r[4], r[5], r[6], r[7], r[8]]
                for j,value in enumerate(values):
                    item=QTableWidgetItem("" if value is None else str(value)); item.setTextAlignment(Qt.AlignmentFlag.AlignCenter); table.setItem(i,j,item)
            table.resizeColumnsToContents()
            if selected is not None:
                for i,r in enumerate(filtered):
                    if str(r[0])==str(selected): table.selectRow(i); break
        except Exception as exc: self._tahrir_db_error("تقاضای لوازم‌التحریر", exc)

    def clear_mto_tahrir_form(self):
        self._mto_tahrir_id=None
        self.ui.txtMtoTahrirDate.setText(self._tahrir_today())
        self.ui.txtMtoTahrirDescription.clear(); self.ui.txtMtoTahrirQty.clear(); self.ui.txtMtoTahrirUnit.clear()
        self.ui.cmbMtoTahrirVahed.setCurrentText(self.user_vahed); self.ui.txtMtoTahrirRecorder.setText(self.username)
        self.ui.cmbMtoTahrirTaeidkonandeh.setCurrentText(""); self.ui.cmbMtoTahrirTahvilgirandeh.setCurrentText("")
        self.ui.txtMtoTahrirEditor.setText(self.username)
        self.ui.tblMtoTahrirList.clearSelection(); self.ui.txtMtoTahrirDescription.setFocus()

    def select_mto_tahrir_request(self):
        i=self.ui.tblMtoTahrirList.currentRow()
        if i<0 or i>=len(self._mto_tahrir_rows): return
        r=self._mto_tahrir_rows[i]; self._mto_tahrir_id=r[0]
        self.ui.txtMtoTahrirDate.setText(self._tahrir_display_date(r[1]))
        self.ui.txtMtoTahrirDescription.setText(str(r[2] or "")); self.ui.txtMtoTahrirQty.setText(str(r[3] if r[3] is not None else ""))
        self.ui.txtMtoTahrirUnit.setText(str(r[4] or "")); self.ui.cmbMtoTahrirVahed.setCurrentText(str(r[5] or ""))
        self.ui.txtMtoTahrirRecorder.setText(str(r[6] or "")); self.ui.cmbMtoTahrirTaeidkonandeh.setCurrentText(str(r[7] or ""))
        self.ui.cmbMtoTahrirTahvilgirandeh.setCurrentText(str(r[8] or ""))
        self.ui.txtMtoTahrirEditor.setText(str(r[9] or ""))

    def _mto_tahrir_values(self):
        date_value=self._tahrir_db_date(self.ui.txtMtoTahrirDate.text())
        desc=self._tahrir_norm(self.ui.txtMtoTahrirDescription.text())
        qty_text=self._tahrir_norm(self.ui.txtMtoTahrirQty.text())
        unit=self._tahrir_norm(self.ui.txtMtoTahrirUnit.text())
        vahed=self._tahrir_norm(self.ui.cmbMtoTahrirVahed.currentText())
        recorder=self._tahrir_norm(self.ui.txtMtoTahrirRecorder.text()) or self.username
        approver=self._tahrir_norm(self.ui.cmbMtoTahrirTaeidkonandeh.currentText())
        if not desc: raise ValueError("شرح کالای درخواستی را وارد کنید.")
        if not qty_text: raise ValueError("تعداد درخواستی را وارد کنید.")
        try: qty=float(qty_text.replace(",", "."))
        except Exception: raise ValueError("تعداد باید عددی باشد.")
        if qty<=0: raise ValueError("تعداد درخواست باید بیشتر از صفر باشد.")
        if not unit: raise ValueError("واحد کالا را وارد کنید.")
        if not vahed: raise ValueError("واحد سازمانی را وارد کنید.")
        editor=self.username
        return date_value,desc,qty,unit,vahed,recorder,approver,editor

    def _deduct_tahrir_stock(self, cur, description, unit, requested):
        """کسر اتمیک موجودی برای ثبت درخواست/تحویل؛ بدون توابع اختصاصی Access مثل Nz."""
        cur.execute(
            "SELECT [ID], [QTY] FROM [TBL_Anbar_Tahrir] "
            "WHERE [Description]=? AND [Unit]=? ORDER BY [ID]",
            (description, unit),
        )
        stocks = cur.fetchall()
        if not stocks:
            raise ValueError("این کالا با همین شرح و واحد در انبار تعریف نشده است.")
        available_total = sum(float(r[1] or 0) for r in stocks)
        if requested <= 0:
            raise ValueError("تعداد درخواست باید بیشتر از صفر باشد.")
        if available_total < requested:
            raise ValueError(
                f"موجودی کافی نیست. موجودی فعلی: {available_total:g}، مقدار درخواستی: {requested:g}"
            )
        remaining = float(requested)
        for stock_id, stock_qty in stocks:
            if remaining <= 0:
                break
            row_qty = float(stock_qty or 0)
            if row_qty <= 0:
                continue
            deduction = min(row_qty, remaining)
            cur.execute(
                "UPDATE [TBL_Anbar_Tahrir] SET [QTY]=? WHERE [ID]=?",
                (row_qty - deduction, stock_id),
            )
            remaining -= deduction

    def save_mto_tahrir_request(self):
        conn = None
        try:
            values = self._mto_tahrir_values()
            date_value, desc, qty, unit, vahed, recorder, approver, editor = values
            recipient = self._tahrir_norm(self.ui.cmbMtoTahrirTahvilgirandeh.currentText())
            if not recipient:
                raise ValueError("چون ثبت درخواست به معنی تحویل است، نام تحویل‌گیرنده را وارد یا انتخاب کنید.")
            conn = get_connection()
            cur = conn.cursor()
            # کسر موجودی و ثبت تحویل در یک تراکنش انجام می‌شوند.
            self._deduct_tahrir_stock(cur, desc, unit, qty)
            cur.execute(
                "INSERT INTO [TBL_Mto_tahrir] "
                "([Date],[Description],[QTY],[Unit],[vahed],[Recorder],[Taeidkonandeh],[Tahvilgirandeh],[Editor]) "
                "VALUES (?,?,?,?,?,?,?,?,?)",
                (date_value, desc, qty, unit, vahed, recorder, approver, recipient, editor),
            )
            conn.commit()
            conn.close()
            conn = None
            self.load_anbar_tahrir_items()
            self.load_mto_tahrir_requests()
            self.clear_mto_tahrir_form()
            QMessageBox.information(
                self, "تحویل لوازم‌التحریر",
                "درخواست ثبت شد، کالا تحویل‌شده محسوب شد و موجودی انبار کاهش یافت."
            )
        except Exception as exc:
            if conn is not None:
                try: conn.rollback()
                except Exception: pass
                try: conn.close()
                except Exception: pass
            self._tahrir_db_error("ثبت درخواست لوازم‌التحریر", exc)

    def edit_mto_tahrir_request(self):
        if self._mto_tahrir_id is None:
            QMessageBox.warning(self, "ویرایش درخواست", "ابتدا یک درخواست را از جدول انتخاب کنید.")
            return
        selected_row = next((r for r in self._mto_tahrir_rows if str(r[0]) == str(self._mto_tahrir_id)), None)
        if selected_row and str(selected_row[8] or "").strip():
            QMessageBox.warning(
                self, "ویرایش درخواست",
                "این درخواست قبلاً تحویل‌شده است و برای جلوگیری از مغایرت موجودی قابل ویرایش نیست."
            )
            return
        conn = None
        try:
            values = self._mto_tahrir_values()
            date_value, desc, qty, unit, vahed, recorder, approver, editor = values
            recipient = self._tahrir_norm(self.ui.cmbMtoTahrirTahvilgirandeh.currentText())
            if not recipient:
                raise ValueError("چون ثبت درخواست به معنی تحویل است، نام تحویل‌گیرنده را وارد یا انتخاب کنید.")
            conn = get_connection()
            cur = conn.cursor()
            # درخواست‌های قدیمیِ هنوز تحویل‌نشده، هنگام ذخیره ویرایش به تحویل قطعی تبدیل می‌شوند.
            self._deduct_tahrir_stock(cur, desc, unit, qty)
            cur.execute(
                "UPDATE [TBL_Mto_tahrir] SET [Date]=?,[Description]=?,[QTY]=?,[Unit]=?,"
                "[vahed]=?,[Recorder]=?,[Taeidkonandeh]=?,[Tahvilgirandeh]=?,[Editor]=? WHERE [ID]=?",
                (date_value, desc, qty, unit, vahed, recorder, approver, recipient, editor, self._mto_tahrir_id),
            )
            conn.commit()
            conn.close()
            conn = None
            self.load_anbar_tahrir_items()
            self.load_mto_tahrir_requests()
            QMessageBox.information(self, "تحویل لوازم‌التحریر", "درخواست ویرایش و تحویل ثبت شد؛ موجودی انبار کاهش یافت.")
        except Exception as exc:
            if conn is not None:
                try: conn.rollback()
                except Exception: pass
                try: conn.close()
                except Exception: pass
            self._tahrir_db_error("ویرایش درخواست لوازم‌التحریر", exc)

    def delete_mto_tahrir_request(self):
        if self._mto_tahrir_id is None:
            QMessageBox.warning(self,"حذف درخواست","ابتدا یک درخواست را از جدول انتخاب کنید."); return
        selected_row = next((r for r in self._mto_tahrir_rows if str(r[0]) == str(self._mto_tahrir_id)), None)
        if selected_row and str(selected_row[8] or "").strip():
            QMessageBox.warning(self, "حذف درخواست", "درخواست تحویل‌شده قابل حذف نیست؛ برای جلوگیری از مغایرت موجودی، ابتدا باید عملیات برگشت/اصلاح انبار تعریف شود.")
            return
        if QMessageBox.question(self,"حذف درخواست","آیا از حذف درخواست انتخاب‌شده مطمئن هستید؟") != QMessageBox.StandardButton.Yes: return
        try:
            conn=get_connection(); cur=conn.cursor(); cur.execute("DELETE FROM [TBL_Mto_tahrir] WHERE [ID]=?",(self._mto_tahrir_id,)); conn.commit(); conn.close()
            self.clear_mto_tahrir_form(); self.load_mto_tahrir_requests()
        except Exception as exc: self._tahrir_db_error("حذف درخواست لوازم‌التحریر",exc)

    def deliver_mto_tahrir_request(self):
        if self._mto_tahrir_id is None:
            QMessageBox.warning(self, "ثبت تحویل", "ابتدا یک درخواست را انتخاب کنید.")
            return
        selected = self.ui.tblMtoTahrirList.currentRow()
        if selected < 0 or selected >= len(self._mto_tahrir_rows):
            QMessageBox.warning(self, "ثبت تحویل", "درخواست انتخاب‌شده معتبر نیست.")
            return
        row = self._mto_tahrir_rows[selected]
        if str(row[8] or "").strip():
            QMessageBox.information(self, "ثبت تحویل", "این درخواست قبلاً تحویل شده است.")
            return
        recipient = self._tahrir_norm(self.ui.cmbMtoTahrirTahvilgirandeh.currentText())
        if not recipient:
            QMessageBox.warning(self, "ثبت تحویل", "نام تحویل‌گیرنده را در فرم وارد یا انتخاب کنید.")
            self.ui.cmbMtoTahrirTahvilgirandeh.setFocus()
            return
        if QMessageBox.question(
            self, "تأیید تحویل",
            f"آیا تحویل {row[3]} {row[4] or ''} از کالای «{row[2]}» را تأیید می‌کنید؟\n"
            "در صورت تأیید، موجودی انبار به همان میزان کاهش می‌یابد."
        ) != QMessageBox.StandardButton.Yes:
            return
        conn = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                "SELECT TOP 1 [ID], [QTY] FROM [TBL_Anbar_Tahrir] "
                "WHERE [Description]=? AND [Unit]=? ORDER BY [ID]",
                (str(row[2] or "").strip(), str(row[4] or "").strip())
            )
            stock = cur.fetchone()
            if stock is None:
                raise ValueError("این کالا با همین شرح و واحد در انبار تعریف نشده است؛ ابتدا کالا و موجودی آن را ثبت کنید.")
            available = float(stock[1] or 0)
            requested = float(row[3] or 0)
            if requested <= 0:
                raise ValueError("تعداد درخواست معتبر نیست.")
            if available < requested:
                raise ValueError(f"موجودی کافی نیست. موجودی فعلی: {available:g}، مقدار درخواست: {requested:g}")
            cur.execute(
                "UPDATE [TBL_Anbar_Tahrir] SET [QTY]=? WHERE [ID]=?",
                (available - requested, stock[0])
            )
            cur.execute(
                "UPDATE [TBL_Mto_tahrir] SET [Tahvilgirandeh]=?, [Editor]=? WHERE [ID]=?",
                (recipient, self.username, self._mto_tahrir_id)
            )
            conn.commit()
            conn.close()
            self.load_anbar_tahrir_items()
            self.load_mto_tahrir_requests()
            QMessageBox.information(self, "ثبت تحویل", "تحویل ثبت شد و موجودی انبار کاهش یافت.")
        except Exception as exc:
            if conn is not None:
                try: conn.rollback()
                except Exception: pass
                try: conn.close()
                except Exception: pass
            self._tahrir_db_error("ثبت تحویل لوازم‌التحریر", exc)

    # مدیریت اموال (جدول موجود Access با نام tblAmvall)
    # ---------------------------------------------------------
    def setup_amval_tab(self):
        """اتصال تب اموال به کنترل‌های موجود در main.ui؛ هیچ ویجتی در Python ساخته نمی‌شود."""
        table = self.ui.tblAmvalList
        table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        table.verticalHeader().setVisible(False)
        table.setAlternatingRowColors(True)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        table.horizontalHeader().setStretchLastSection(False)
        table.verticalHeader().setDefaultSectionSize(32)
        table.setStyleSheet("""
            QTableWidget { background: white; alternate-background-color: #F7F9FC;
                gridline-color: #D6DCE3; font-family: 'B Nazanin'; font-size: 11pt; }
            QHeaderView::section { background-color: #E8EEF5; color: #1F2937;
                font-family: 'B Nazanin'; font-size: 12pt; font-weight: bold;
                padding: 6px; border: 1px solid #C7D0DB; }
        """)
        self._amval_schema = None
        self._amval_rows = []
        self._amval_original_id = None

        for name, handler in (
            ("btnAmvalNew", self.new_amval_record),
            ("btnAmvalSave", self.save_amval_record),
            ("btnAmvalEdit", self.edit_amval_record),
            ("btnAmvalDelete", self.delete_amval_record),
            ("btnAmvalSearch", self.load_amval_data),
            ("btnAmvalClearFilter", self.clear_amval_filters),
            ("btnAmvalReport", self.export_amval_report),
            ("btnAmvalPrint", self.print_amval_report),
        ):
            getattr(self.ui, name).clicked.connect(handler)
        self.ui.txtAmvalSearch.textChanged.connect(self.load_amval_data)
        self.ui.cmbAmvalUnitFilter.currentIndexChanged.connect(self.load_amval_data)
        self.ui.cmbAmvalActiveFilter.currentIndexChanged.connect(self.load_amval_data)
        table.itemSelectionChanged.connect(self.on_amval_selection_changed)
        self.clear_amval_fields()
        self.load_amval_data()

    @staticmethod
    def _amval_text(value):
        if value is None:
            return ""
        if isinstance(value, (bytes, bytearray, memoryview)):
            try:
                return bytes(value).decode("utf-8", errors="replace")
            except Exception:
                return str(value)
        if hasattr(value, "strftime"):
            try:
                return value.strftime("%Y/%m/%d")
            except Exception:
                pass
        return str(value).strip()

    def _amval_get_schema(self, cursor):
        if self._amval_schema is not None:
            return self._amval_schema
        cursor.execute("SELECT TOP 1 * FROM [tblAmvall]")
        names = [d[0] for d in cursor.description]
        self._amval_schema = names
        return names

    def _amval_col(self, *aliases):
        schema = self._amval_schema or []
        folded = {str(x).casefold().replace(" ", ""): x for x in schema}
        for alias in aliases:
            key = str(alias).casefold().replace(" ", "")
            if key in folded:
                return folded[key]
        return None

    def _amval_field_value(self, row, field):
        if not field:
            return ""
        try:
            return self._amval_text(row.get(field))
        except Exception:
            return ""

    def _amval_row_dicts(self, cursor):
        schema = self._amval_get_schema(cursor)
        cursor.execute("SELECT * FROM [tblAmvall]")
        return [dict(zip(schema, row)) for row in cursor.fetchall()]

    def _amval_to_db(self, field, value):
        value = normalize_digits(str(value or "").strip())
        if not field:
            return None
        numeric = {"id", "assetno", "loccode", "invdate", "acqdate", "budgno", "code", "cd_vahed"}
        key = str(field).casefold().replace(" ", "")
        if key in numeric:
            if not value:
                return None
            digits = "".join(ch for ch in value if ch.isdigit())
            try:
                return int(digits) if digits else None
            except Exception:
                return None
        return value

    def _amval_filter_rows(self, rows):
        search = normalize_digits(self.ui.txtAmvalSearch.text().strip()).casefold()
        unit_code = str(self.ui.cmbAmvalUnitFilter.currentData() or "").strip()
        active = self.ui.cmbAmvalActiveFilter.currentText().strip()
        unit_col = self._amval_col("Cd_Vahed", "CD_VAHED")
        status_col = self._amval_col("Vazeiyat", "Vaziyat", "Status")
        filtered = []
        for row in rows:
            values = [self._amval_text(v) for v in row.values()]
            if search and not any(search in v.casefold() for v in values):
                continue
            if unit_code and self._amval_text(row.get(unit_col)) != unit_code:
                continue
            status = self._amval_text(row.get(status_col)) if status_col else ""
            status_norm = status.replace("ي", "ی").replace("ك", "ک").replace(" ", "").casefold()
            if active == "فعال" and status_norm == "غیرفعال":
                continue
            if active == "فعال" and status_norm == "فعال":
                pass
            elif active == "فعال" and status_col and status_norm not in ("فعال", "غیرفعال"):
                continue
            if active == "غیرفعال" and status_norm != "غیرفعال":
                continue
            filtered.append(row)
        return filtered

    def _amval_refresh_unit_filters(self, rows):
        unit_col = self._amval_col("Cd_Vahed", "CD_VAHED")
        name_col = self._amval_col("vahed", "VAHED")
        old = self.ui.cmbAmvalUnitFilter.currentData()
        self.ui.cmbAmvalUnitFilter.blockSignals(True)
        self.ui.cmbAmvalUnitFilter.clear()
        self.ui.cmbAmvalUnitFilter.addItem("همه واحدها", "")
        seen = set()
        for row in rows:
            code = self._amval_text(row.get(unit_col)) if unit_col else ""
            name = self._amval_text(row.get(name_col)) if name_col else ""
            if not code and not name:
                continue
            key = code or name
            if key in seen:
                continue
            seen.add(key)
            label = f"{code} - {name}" if code and name else (code or name)
            self.ui.cmbAmvalUnitFilter.addItem(label, code)
        if old is not None:
            idx = self.ui.cmbAmvalUnitFilter.findData(old)
            if idx >= 0:
                self.ui.cmbAmvalUnitFilter.setCurrentIndex(idx)
        self.ui.cmbAmvalUnitFilter.blockSignals(False)

    def load_amval_data(self, *_args):
        conn = cursor = None
        try:
            conn = get_connection(); cursor = conn.cursor()
            rows = self._amval_row_dicts(cursor)
            self._amval_refresh_unit_filters(rows)
            filtered = self._amval_filter_rows(rows)
            self._amval_rows = filtered
            table = self.ui.tblAmvalList
            table.setRowCount(len(filtered))
            cols = [
                lambda r, i: str(i + 1),
                lambda r, i: self._amval_text(r.get(self._amval_col("ID"))),
                lambda r, i: self._amval_text(r.get(self._amval_col("ASSETNO"))),
                lambda r, i: self._amval_text(r.get(self._amval_col("DESCRIPTION"))),
                lambda r, i: self._amval_text(r.get(self._amval_col("Loc Code"))),
                lambda r, i: self._amval_text(r.get(self._amval_col("Vazeiyat", "Vaziyat", "Status"))),
                lambda r, i: self._amval_text(r.get(self._amval_col("mahal"))),
                lambda r, i: self._amval_text(r.get(self._amval_col("SERIALNO", "SerialNo", "Serial", "شماره سریال"))),
                lambda r, i: self._amval_text(r.get(self._amval_col("MANUSERL"))),
                lambda r, i: self._amval_text(r.get(self._amval_col("INV DATE"))),
                lambda r, i: self._amval_text(r.get(self._amval_col("EXIT DATE", "ExitDate", "Exit Date"))),
                lambda r, i: self._amval_text(r.get(self._amval_col("LOC"))),
                lambda r, i: self._amval_text(r.get(self._amval_col("ACQ DATE"))),
                lambda r, i: self._amval_text(r.get(self._amval_col("BUDGNO"))),
                lambda r, i: self._amval_text(r.get(self._amval_col("NOTATIONS"))),
                lambda r, i: self._amval_text(r.get(self._amval_col("vahed"))),
                lambda r, i: self._amval_text(r.get(self._amval_col("Code"))),
                lambda r, i: self._amval_text(r.get(self._amval_col("Cd_Vahed"))),
                lambda r, i: self._amval_text(r.get(self._amval_col("Recorder"))),
                lambda r, i: self._amval_text(r.get(self._amval_col("Editor"))),
            ]
            for r, row in enumerate(filtered):
                for c, getter in enumerate(cols):
                    item = QTableWidgetItem(getter(row, r))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    if c == 1:
                        item.setData(Qt.ItemDataRole.UserRole, row.get(self._amval_col("ID")))
                    table.setItem(r, c, item)
            widths = [55, 70, 105, 220, 90, 110, 150, 120, 140, 105, 105, 120, 105, 120, 220, 150, 100, 100, 120, 120]
            for i, w in enumerate(widths):
                table.setColumnWidth(i, w)
        except Exception as exc:
            self.ui.tblAmvalList.setRowCount(0)
            QMessageBox.warning(self, "اموال", f"خواندن اطلاعات جدول tblAmvall انجام نشد:\n{exc}")
        finally:
            if cursor is not None:
                try: cursor.close()
                except Exception: pass
            if conn is not None:
                try: conn.close()
                except Exception: pass

    def clear_amval_fields(self):
        for name in ("txtAmvalID", "txtAmvalAssetNo", "txtAmvalDescription", "txtAmvalStatus", "txtAmvalMahal",
                     "txtAmvalSerial", "txtAmvalLocCode", "txtAmvalInvDate", "txtAmvalExitDate", "txtAmvalAcqDate",
                     "txtAmvalLoc", "txtAmvalBudget", "txtAmvalManUser", "txtAmvalCode",
                     "txtAmvalCdVahed", "txtAmvalRecorder", "txtAmvalEditor"):
            getattr(self.ui, name).clear()
        self.ui.txtAmvalNotes.clear()
        self.ui.cmbAmvalUnit.setCurrentIndex(-1)
        self.ui.cmbAmvalActive.setCurrentIndex(0)
        self._amval_original_id = None

    def clear_amval_filters(self):
        self.ui.txtAmvalSearch.clear()
        self.ui.cmbAmvalUnitFilter.setCurrentIndex(0)
        self.ui.cmbAmvalActiveFilter.setCurrentIndex(0)
        self.load_amval_data()

    def on_amval_selection_changed(self):
        row_index = self.ui.tblAmvalList.currentRow()
        if row_index < 0 or row_index >= len(self._amval_rows):
            return
        row = self._amval_rows[row_index]
        col = lambda *names: self._amval_col(*names)
        def set_line(name, *fields):
            field = col(*fields)
            getattr(self.ui, name).setText(self._amval_text(row.get(field)) if field else "")
        set_line("txtAmvalID", "ID")
        set_line("txtAmvalAssetNo", "ASSETNO")
        set_line("txtAmvalDescription", "DESCRIPTION")
        set_line("txtAmvalStatus", "Vazeiyat", "Vaziyat", "Status")
        set_line("txtAmvalMahal", "mahal")
        set_line("txtAmvalSerial", "SERIALNO", "SerialNo", "Serial", "شماره سریال")
        set_line("txtAmvalLocCode", "Loc Code")
        set_line("txtAmvalInvDate", "INV DATE")
        set_line("txtAmvalExitDate", "EXIT DATE", "ExitDate", "Exit Date")
        set_line("txtAmvalAcqDate", "ACQ DATE")
        set_line("txtAmvalLoc", "LOC")
        set_line("txtAmvalBudget", "BUDGNO")
        field = col("NOTATIONS")
        self.ui.txtAmvalNotes.setPlainText(self._amval_text(row.get(field)) if field else "")
        set_line("txtAmvalManUser", "MANUSERL")
        set_line("txtAmvalCode", "Code")
        set_line("txtAmvalCdVahed", "Cd_Vahed")
        set_line("txtAmvalRecorder", "Recorder")
        set_line("txtAmvalEditor", "Editor")
        unit_field = col("vahed")
        unit_value = self._amval_text(row.get(unit_field)) if unit_field else ""
        idx = self.ui.cmbAmvalUnit.findText(unit_value, Qt.MatchFlag.MatchExactly)
        if idx < 0 and unit_value:
            self.ui.cmbAmvalUnit.addItem(unit_value)
            idx = self.ui.cmbAmvalUnit.findText(unit_value, Qt.MatchFlag.MatchExactly)
        self.ui.cmbAmvalUnit.setCurrentIndex(idx)
        status = self.ui.txtAmvalStatus.text().strip().replace("ي", "ی").replace("ك", "ک").replace(" ", "").casefold()
        self.ui.cmbAmvalActive.setCurrentIndex(1 if status == "غیرفعال" else 0)
        self._amval_original_id = row.get(col("ID"))

    def _amval_collect(self):
        """فقط فیلدهای موجود در tblAmvall را جمع‌آوری می‌کند؛ فیلدهای UI بدون معادل DB ذخیره نمی‌شوند."""
        c = lambda *names: self._amval_col(*names)
        data = {
            c("ASSETNO"): self.ui.txtAmvalAssetNo.text(),
            c("DESCRIPTION"): self.ui.txtAmvalDescription.text(),
            c("Loc Code"): self.ui.txtAmvalLocCode.text(),
            c("Vazeiyat", "Vaziyat", "Status"): self.ui.txtAmvalStatus.text(),
            c("mahal"): self.ui.txtAmvalMahal.text(),
            c("SERIALNO", "SerialNo", "Serial", "شماره سریال"): self.ui.txtAmvalSerial.text(),
            c("INV DATE"): self.ui.txtAmvalInvDate.text(),
            c("EXIT DATE", "ExitDate", "Exit Date"): self.ui.txtAmvalExitDate.text(),
            c("LOC"): self.ui.txtAmvalLoc.text(),
            c("ACQ DATE"): self.ui.txtAmvalAcqDate.text(),
            c("BUDGNO"): self.ui.txtAmvalBudget.text(),
            c("NOTATIONS"): self.ui.txtAmvalNotes.toPlainText(),
            c("vahed"): self.ui.cmbAmvalUnit.currentText().strip(),
            c("Code"): self.ui.txtAmvalCode.text(),
            c("Cd_Vahed"): self.ui.txtAmvalCdVahed.text(),
            c("MANUSERL"): self.ui.txtAmvalManUser.text(),
            c("Recorder"): self.ui.txtAmvalRecorder.text() or self.username,
            c("Editor"): self.username,
        }
        return {field: self._amval_to_db(field, value) for field, value in data.items() if field}

    def new_amval_record(self):
        self.clear_amval_fields()
        self.ui.txtAmvalStatus.setText("فعال")
        self.ui.txtAmvalRecorder.setText(self.username)
        self.ui.txtAmvalAssetNo.setFocus()

    def save_amval_record(self):
        conn = cursor = None
        try:
            conn = get_connection(); cursor = conn.cursor()
            self._amval_get_schema(cursor)
            data = self._amval_collect()
            data.pop(self._amval_col("Recorder"), None)
            data.pop(self._amval_col("Editor"), None)
            if self._amval_col("Recorder"):
                data[self._amval_col("Recorder")] = self.username
            if self._amval_col("Editor"):
                data[self._amval_col("Editor")] = self.username
            asset_field = self._amval_col("ASSETNO")
            if asset_field and not data.get(asset_field):
                QMessageBox.information(self, "ثبت مال", "شماره اموال الزامی است.")
                self.ui.txtAmvalAssetNo.setFocus(); return
            fields = [f for f in data if f]
            if not fields:
                raise RuntimeError("هیچ فیلد قابل ذخیره‌ای در tblAmvall پیدا نشد.")
            names = ", ".join(f"[{f}]" for f in fields)
            marks = ", ".join("?" for _ in fields)
            cursor.execute(f"INSERT INTO [tblAmvall] ({names}) VALUES ({marks})", tuple(data[f] for f in fields))
            conn.commit()
            QMessageBox.information(self, "ثبت مال", "اطلاعات مال با موفقیت ثبت شد.")
            self.clear_amval_fields(); self.load_amval_data()
        except Exception as exc:
            if conn is not None:
                try: conn.rollback()
                except Exception: pass
            QMessageBox.warning(self, "ثبت مال", f"ثبت اطلاعات انجام نشد:\n{exc}")
        finally:
            if cursor is not None:
                try: cursor.close()
                except Exception: pass
            if conn is not None:
                try: conn.close()
                except Exception: pass

    def edit_amval_record(self):
        if self._amval_original_id in (None, ""):
            QMessageBox.information(self, "ویرایش مال", "ابتدا یک رکورد را از جدول انتخاب کنید.")
            return
        conn = cursor = None
        try:
            conn = get_connection(); cursor = conn.cursor()
            self._amval_get_schema(cursor)
            id_field = self._amval_col("ID")
            if not id_field:
                raise RuntimeError("فیلد ID در tblAmvall پیدا نشد.")
            data = self._amval_collect()
            if self._amval_col("Editor"):
                data[self._amval_col("Editor")] = self.username
            if self._amval_col("Recorder"):
                data.pop(self._amval_col("Recorder"), None)
            fields = [f for f in data if f and f != id_field]
            if not fields:
                raise RuntimeError("هیچ فیلد قابل ویرایشی پیدا نشد.")
            assignments = ", ".join(f"[{f}] = ?" for f in fields)
            cursor.execute(f"UPDATE [tblAmvall] SET {assignments} WHERE [{id_field}] = ?", tuple(data[f] for f in fields) + (self._amval_original_id,))
            conn.commit()
            QMessageBox.information(self, "ویرایش مال", "تغییرات با موفقیت ذخیره شد.")
            self.clear_amval_fields(); self.load_amval_data()
        except Exception as exc:
            if conn is not None:
                try: conn.rollback()
                except Exception: pass
            QMessageBox.warning(self, "ویرایش مال", f"ذخیره تغییرات انجام نشد:\n{exc}")
        finally:
            if cursor is not None:
                try: cursor.close()
                except Exception: pass
            if conn is not None:
                try: conn.close()
                except Exception: pass

    def delete_amval_record(self):
        if self._amval_original_id in (None, ""):
            QMessageBox.information(self, "حذف مال", "ابتدا یک رکورد را از جدول انتخاب کنید.")
            return
        answer = QMessageBox.question(self, "تأیید حذف", "آیا از حذف رکورد انتخاب‌شده مطمئن هستید؟",
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                      QMessageBox.StandardButton.No)
        if answer != QMessageBox.StandardButton.Yes:
            return
        conn = cursor = None
        try:
            conn = get_connection(); cursor = conn.cursor()
            id_field = self._amval_col("ID") or "ID"
            cursor.execute(f"DELETE FROM [tblAmvall] WHERE [{id_field}] = ?", (self._amval_original_id,))
            conn.commit()
            self.clear_amval_fields(); self.load_amval_data()
            QMessageBox.information(self, "حذف مال", "رکورد حذف شد.")
        except Exception as exc:
            if conn is not None:
                try: conn.rollback()
                except Exception: pass
            QMessageBox.warning(self, "حذف مال", f"حذف رکورد انجام نشد:\n{exc}")
        finally:
            if cursor is not None:
                try: cursor.close()
                except Exception: pass
            if conn is not None:
                try: conn.close()
                except Exception: pass

    def _amval_report_html(self):
        headers = [self.ui.tblAmvalList.horizontalHeaderItem(i).text() for i in range(self.ui.tblAmvalList.columnCount())]
        html = ["<html><head><meta charset='utf-8'></head><body dir='rtl'>",
                "<h2 style='text-align:center'>گزارش اموال</h2>",
                f"<p>تعداد رکورد: {self.ui.tblAmvalList.rowCount()}</p>",
                "<table border='1' cellspacing='0' cellpadding='4' style='border-collapse:collapse;width:100%;font-family:B Nazanin;font-size:9pt'>",
                "<tr>" + "".join(f"<th>{h}</th>" for h in headers) + "</tr>"]
        for r in range(self.ui.tblAmvalList.rowCount()):
            html.append("<tr>" + "".join(f"<td>{(self.ui.tblAmvalList.item(r,c).text() if self.ui.tblAmvalList.item(r,c) else '')}</td>" for c in range(self.ui.tblAmvalList.columnCount())) + "</tr>")
        html.append("</table></body></html>")
        return "".join(html)

    def export_amval_report(self):
        path, _ = QFileDialog.getSaveFileName(self, "ذخیره گزارش اموال", "گزارش_اموال.csv", "CSV (*.csv)")
        if not path:
            return
        import csv
        try:
            with open(path, "w", newline="", encoding="utf-8-sig") as f:
                writer = csv.writer(f)
                writer.writerow([self.ui.tblAmvalList.horizontalHeaderItem(i).text() for i in range(self.ui.tblAmvalList.columnCount())])
                for r in range(self.ui.tblAmvalList.rowCount()):
                    writer.writerow([self.ui.tblAmvalList.item(r,c).text() if self.ui.tblAmvalList.item(r,c) else "" for c in range(self.ui.tblAmvalList.columnCount())])
            QMessageBox.information(self, "گزارش اموال", f"گزارش با موفقیت ذخیره شد:\n{path}")
        except Exception as exc:
            QMessageBox.warning(self, "گزارش اموال", f"ذخیره گزارش انجام نشد:\n{exc}")

    def print_amval_report(self):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        dialog = QPrintDialog(printer, self)
        dialog.setWindowTitle("چاپ گزارش اموال")
        if dialog.exec() != QDialog.DialogCode.Accepted:
            return
        document = QTextDocument()
        document.setHtml(self._amval_report_html())
        document.print_(printer)

    # ---------------------------------------------------------
    # مدیریت کد کالاهای MESC (جدول موجود Access با نام mesc)
    # ---------------------------------------------------------
    def open_mesc_tab(self):
        """ورود به مدیریت MESC فقط برای SuperAdmin مجاز است."""
        if not self.is_master:
            QMessageBox.warning(self, "عدم دسترسی", "فقط SuperAdmin اجازه دسترسی به مدیریت کدهای MESC را دارد.")
            return
        self.open_page(self.ui.tabMesc)
        self.load_mesc_data()

    def setup_mesc_tab(self):
        """اتصال کنترل‌های طراحی‌شده در main.ui؛ هیچ ویجتی در کد ساخته نمی‌شود."""
        table = self.ui.tblMescList
        table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        table.verticalHeader().setVisible(False)
        table.setAlternatingRowColors(True)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        table.horizontalHeader().setStretchLastSection(True)
        table.verticalHeader().setDefaultSectionSize(32)
        table.setStyleSheet("QTableWidget { background: white; alternate-background-color: #F7F9FC; gridline-color: #D6DCE3; font-family: 'B Nazanin'; font-size: 12pt; } QHeaderView::section { background-color: #E8EEF5; color: #1F2937; font-family: 'B Nazanin'; font-size: 13pt; font-weight: bold; padding: 6px; }")
        for button_name, handler in (
            ("btnMescNew", self.new_mesc_record),
            ("btnMescSave", self.save_mesc_record),
            ("btnMescEdit", self.edit_mesc_record),
            ("btnMescDelete", self.delete_mesc_record),
            ("btnMescSearch", self.load_mesc_data),
        ):
            getattr(self.ui, button_name).clicked.connect(handler)
        self.ui.txtMescSearch.textChanged.connect(self.load_mesc_data)
        table.itemSelectionChanged.connect(self.on_mesc_selection_changed)
        self.ui.btnMescChoosePic.clicked.connect(self.choose_mesc_image)
        self.ui.btnMescRemovePic.clicked.connect(self.remove_mesc_image)
        self._mesc_image_data = None
        self._mesc_image_changed = False
        self._mesc_existing_image = False
        # فقط SuperAdmin می‌تواند این ماژول را باز کند یا عملیات انجام دهد.
        for name in ("btnMescNew", "btnMescSave", "btnMescEdit", "btnMescDelete", "btnMescSearch"):
            getattr(self.ui, name).setEnabled(self.is_master)
        self.clear_mesc_fields()
        self.load_mesc_data()

    @staticmethod
    def _mesc_text(value):
        if value is None:
            return ""
        if isinstance(value, (bytes, bytearray, memoryview)):
            return "دارد" if len(value) else "ندارد"
        return str(value)

    @staticmethod
    def _mesc_decode_image(data):
        """خواندن تصویر خام یا تصویری که در OLE Object همراه سربرگ ذخیره شده است."""
        if not data:
            return QPixmap()
        raw = bytes(data)
        pixmap = QPixmap()
        if pixmap.loadFromData(raw):
            return pixmap
        # برخی رکوردهای قدیمی Access سربرگ OLE قبل از محتوای واقعی دارند.
        signatures = (b"\x89PNG\r\n\x1a\n", b"\xff\xd8\xff", b"GIF87a", b"GIF89a", b"BM")
        for signature in signatures:
            offset = raw.find(signature)
            if offset >= 0:
                candidate = QPixmap()
                if candidate.loadFromData(raw[offset:]):
                    return candidate
        return QPixmap()

    def _mesc_show_image(self, data):
        pixmap = self._mesc_decode_image(data)
        preview = self.ui.lblMescPicPreview
        if pixmap.isNull():
            preview.setPixmap(QPixmap())
            preview.setText("تصویری انتخاب نشده" if not data else "قالب تصویر قابل نمایش نیست")
        else:
            preview.setText("")
            preview.setPixmap(pixmap.scaled(preview.size(), Qt.AspectRatioMode.KeepAspectRatio,
                                            Qt.TransformationMode.SmoothTransformation))

    def choose_mesc_image(self):
        if not self._mesc_guard():
            return
        path, _ = QFileDialog.getOpenFileName(
            self, "انتخاب تصویر کالا", "",
            "تصاویر (*.png *.jpg *.jpeg *.bmp *.gif *.webp);;همه فایل‌ها (*.*)"
        )
        if not path:
            return
        try:
            data = open(path, "rb").read()
            pixmap = self._mesc_decode_image(data)
            if pixmap.isNull():
                QMessageBox.warning(self, "تصویر کالا", "فایل انتخاب‌شده تصویر معتبر یا قابل پشتیبانی نیست.")
                return
            self._mesc_image_data = data
            self._mesc_image_changed = True
            self._mesc_existing_image = True
            self._mesc_show_image(data)
        except Exception as exc:
            QMessageBox.warning(self, "تصویر کالا", f"خواندن فایل تصویر ناموفق بود:\n{exc}")

    def remove_mesc_image(self):
        if not self._mesc_guard():
            return
        self._mesc_image_data = None
        self._mesc_image_changed = True
        self._mesc_existing_image = False
        self._mesc_show_image(None)

    def _mesc_guard(self):
        if not self.is_master:
            QMessageBox.warning(self, "عدم دسترسی", "فقط SuperAdmin اجازه انجام عملیات روی کدهای MESC را دارد.")
            return False
        return True

    def clear_mesc_fields(self):
        for name in ("txtMescCode", "txtMescShohazine", "txtMescSharh", "txtMescDescription", "txtMescUnit"):
            getattr(self.ui, name).clear()
        self.ui.txtMescSabtkonande.clear()
        self.ui.txtMescEditor.clear()
        self.ui.txtMescCode.setReadOnly(False)
        self._mesc_image_data = None
        self._mesc_image_changed = False
        self._mesc_existing_image = False
        self._mesc_show_image(None)
        self.ui.tblMescList.clearSelection()
        self._mesc_original_code = None

    def new_mesc_record(self):
        if not self._mesc_guard():
            return
        self.clear_mesc_fields()
        self.ui.txtMescCode.setFocus()

    def load_mesc_data(self, *_args):
        if not hasattr(self.ui, "tblMescList"):
            return
        table = self.ui.tblMescList
        # هیچ داده‌ای از جدول MESC برای کاربران غیرمجاز خوانده نمی‌شود.
        if not self.is_master:
            table.setRowCount(0)
            return
        conn = cursor = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT [mesc], [shohazine], [sharh], [Discription], [unit], [sabtkonande], [Editor], [pic] FROM [mesc]")
            rows = cursor.fetchall()
            search = self.ui.txtMescSearch.text().strip().casefold()
            filtered = []
            for row in rows:
                vals = [self._mesc_text(v) for v in row[:7]]
                vals.append("دارد" if row[7] else "ندارد")
                # تصویر فقط به‌صورت وضعیت نمایش داده می‌شود؛ جستجو روی فیلدهای متنی است.
                if search and not any(search in v.casefold() for v in vals[:7]):
                    continue
                filtered.append(vals)
            table.setRowCount(len(filtered))
            for r, values in enumerate(filtered):
                for c, value in enumerate(values):
                    item = QTableWidgetItem(value)
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    if c == 0:
                        item.setData(Qt.ItemDataRole.UserRole, values[0])
                    table.setItem(r, c, item)
            widths = [145, 125, 220, 220, 100, 130, 130, 130]
            for i, width in enumerate(widths):
                table.setColumnWidth(i, width)
        except Exception as exc:
            QMessageBox.warning(self, "مدیریت MESC", f"خواندن اطلاعات جدول mesc با خطا مواجه شد:\n{exc}")
        finally:
            if cursor is not None:
                try: cursor.close()
                except Exception: pass
            if conn is not None:
                try: conn.close()
                except Exception: pass

    def on_mesc_selection_changed(self):
        row = self.ui.tblMescList.currentRow()
        if row < 0:
            return
        values = []
        for col in range(7):
            item = self.ui.tblMescList.item(row, col)
            values.append(item.text() if item else "")
        names = ("txtMescCode", "txtMescShohazine", "txtMescSharh", "txtMescDescription", "txtMescUnit", "txtMescSabtkonande", "txtMescEditor")
        for name, value in zip(names, values):
            getattr(self.ui, name).setText(value)
        self._mesc_original_code = values[0]
        self.ui.txtMescCode.setReadOnly(False)
        self._mesc_image_data = None
        self._mesc_image_changed = False
        self._mesc_existing_image = False
        conn = cursor = None
        try:
            conn = get_connection(); cursor = conn.cursor()
            cursor.execute("SELECT [pic] FROM [mesc] WHERE [mesc]=?", (self._mesc_original_code,))
            image_row = cursor.fetchone()
            data = image_row[0] if image_row else None
            if data:
                self._mesc_existing_image = True
                self._mesc_image_data = bytes(data) if isinstance(data, (bytes, bytearray, memoryview)) else data
            self._mesc_show_image(self._mesc_image_data)
        except Exception as exc:
            self._mesc_show_image(None)
            QMessageBox.warning(self, "تصویر کالا", f"خواندن تصویر کالا انجام نشد:\n{exc}")
        finally:
            if cursor is not None:
                try: cursor.close()
                except Exception: pass
            if conn is not None:
                try: conn.close()
                except Exception: pass

    def _mesc_values(self):
        return (
            self.ui.txtMescCode.text().strip(),
            self.ui.txtMescShohazine.text().strip(),
            self.ui.txtMescSharh.text().strip(),
            self.ui.txtMescDescription.text().strip(),
            self.ui.txtMescUnit.text().strip(),
        )

    def _mesc_code_exists(self, cursor, code, exclude_code=None):
        if exclude_code is None:
            cursor.execute("SELECT COUNT(*) FROM [mesc] WHERE [mesc] = ?", (code,))
        else:
            cursor.execute("SELECT COUNT(*) FROM [mesc] WHERE [mesc] = ? AND [mesc] <> ?", (code, exclude_code))
        row = cursor.fetchone()
        return bool(row and int(row[0] or 0) > 0)

    def save_mesc_record(self):
        if not self._mesc_guard():
            return
        code, shohazine, sharh, description, unit = self._mesc_values()
        if not code:
            QMessageBox.information(self, "ثبت MESC", "وارد کردن کد MESC الزامی است.")
            self.ui.txtMescCode.setFocus()
            return
        conn = cursor = None
        try:
            conn = get_connection(); cursor = conn.cursor()
            if self._mesc_code_exists(cursor, code):
                QMessageBox.warning(self, "کد تکراری", f"کد MESC «{code}» قبلاً ثبت شده است. کد باید یکتا باشد.")
                return
            cursor.execute("INSERT INTO [mesc] ([mesc], [shohazine], [sharh], [Discription], [unit], [sabtkonande], [Editor], [pic]) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                           (code, shohazine, sharh, description, unit, self.username, "", self._mesc_image_data if self._mesc_image_data else None))
            conn.commit()
            QMessageBox.information(self, "ثبت MESC", "رکورد با موفقیت ثبت شد.")
            self.clear_mesc_fields(); self.load_mesc_data()
        except Exception as exc:
            if conn is not None:
                try: conn.rollback()
                except Exception: pass
            QMessageBox.warning(self, "ثبت MESC", f"ثبت اطلاعات انجام نشد:\n{exc}")
        finally:
            if cursor is not None:
                try: cursor.close()
                except Exception: pass
            if conn is not None:
                try: conn.close()
                except Exception: pass

    def edit_mesc_record(self):
        if not self._mesc_guard():
            return
        old_code = getattr(self, "_mesc_original_code", None)
        if not old_code:
            QMessageBox.information(self, "ویرایش MESC", "ابتدا یک رکورد را از جدول انتخاب کنید.")
            return
        code, shohazine, sharh, description, unit = self._mesc_values()
        if not code:
            QMessageBox.information(self, "ویرایش MESC", "کد MESC نمی‌تواند خالی باشد.")
            return
        conn = cursor = None
        try:
            conn = get_connection(); cursor = conn.cursor()
            if self._mesc_code_exists(cursor, code, old_code):
                QMessageBox.warning(self, "کد تکراری", f"کد MESC «{code}» متعلق به رکورد دیگری است.")
                return
            if self._mesc_image_changed:
                cursor.execute("UPDATE [mesc] SET [mesc]=?, [shohazine]=?, [sharh]=?, [Discription]=?, [unit]=?, [Editor]=?, [pic]=? WHERE [mesc]=?",
                               (code, shohazine, sharh, description, unit, self.username,
                                self._mesc_image_data if self._mesc_image_data else None, old_code))
            else:
                # اگر کاربر تصویر را تغییر نداده باشد، تصویر قبلی دست‌نخورده باقی می‌ماند.
                cursor.execute("UPDATE [mesc] SET [mesc]=?, [shohazine]=?, [sharh]=?, [Discription]=?, [unit]=?, [Editor]=? WHERE [mesc]=?",
                               (code, shohazine, sharh, description, unit, self.username, old_code))
            conn.commit()
            QMessageBox.information(self, "ویرایش MESC", "تغییرات با موفقیت ذخیره شد.")
            self.clear_mesc_fields(); self.load_mesc_data()
        except Exception as exc:
            if conn is not None:
                try: conn.rollback()
                except Exception: pass
            QMessageBox.warning(self, "ویرایش MESC", f"ذخیره تغییرات انجام نشد:\n{exc}")
        finally:
            if cursor is not None:
                try: cursor.close()
                except Exception: pass
            if conn is not None:
                try: conn.close()
                except Exception: pass

    def delete_mesc_record(self):
        if not self._mesc_guard():
            return
        row = self.ui.tblMescList.currentRow()
        item = self.ui.tblMescList.item(row, 0) if row >= 0 else None
        code = item.text().strip() if item else None
        if not code:
            QMessageBox.information(self, "حذف MESC", "ابتدا یک رکورد را از جدول انتخاب کنید.")
            return
        answer = QMessageBox.question(self, "تأیید حذف", f"آیا از حذف کد MESC «{code}» مطمئن هستید؟",
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                      QMessageBox.StandardButton.No)
        if answer != QMessageBox.StandardButton.Yes:
            return
        conn = cursor = None
        try:
            conn = get_connection(); cursor = conn.cursor()
            cursor.execute("DELETE FROM [mesc] WHERE [mesc] = ?", (code,))
            conn.commit()
            self.clear_mesc_fields(); self.load_mesc_data()
            QMessageBox.information(self, "حذف MESC", "رکورد حذف شد.")
        except Exception as exc:
            if conn is not None:
                try: conn.rollback()
                except Exception: pass
            QMessageBox.warning(self, "حذف MESC", f"حذف رکورد انجام نشد:\n{exc}")
        finally:
            if cursor is not None:
                try: cursor.close()
                except Exception: pass
            if conn is not None:
                try: conn.close()
                except Exception: pass


    def setup_report_tab(self):
        # هر فیلد تاریخ فقط یک آیکون تقویم داخلی دارد؛ دکمه تکراری ساخته نمی‌شود.
        for attr_name in ("txtReportFrom", "txtReportTo", "txtTrackingDate"):
            old_widget = getattr(self.ui, attr_name, None)
            if old_widget is None or isinstance(old_widget, JalaliDateLineEdit):
                continue

            parent = old_widget.parentWidget()
            layout = parent.layout() if parent is not None else None
            new_widget = JalaliDateLineEdit(parent)
            new_widget.setObjectName(attr_name)
            new_widget.setMinimumWidth(max(120, old_widget.minimumWidth()))
            new_widget.setSizePolicy(old_widget.sizePolicy())
            new_widget.setText(old_widget.text())

            if not replace_widget_in_layout(layout, old_widget, new_widget):
                new_widget.deleteLater()
                old_widget.setPlaceholderText("شمسی: 1405/07/18 - خالی = همه تاریخ‌ها")
                install_calendar_action(old_widget)
                continue

            old_widget.hide()
            old_widget.setParent(None)
            old_widget.deleteLater()
            setattr(self.ui, attr_name, new_widget)

        today = jdatetime.date.today().strftime("%Y/%m/%d")

        # فیلدهای بازه تاریخ می‌توانند QLineEdit یا QDateEdit باشند.
        # در حالت QLineEdit تاریخ شمسی به شکل 14050718 یا 1405/07/18 وارد می‌شود.
        for date_widget in (self.ui.txtReportFrom, self.ui.txtReportTo):
            if hasattr(date_widget, "setDate"):
                # QDateEdit: تاریخ خالی یعنی بدون محدودیت
                no_date = QDate(1900, 1, 1)
                if hasattr(date_widget, "setMinimumDate"):
                    date_widget.setMinimumDate(no_date)
                if hasattr(date_widget, "setSpecialValueText"):
                    date_widget.setSpecialValueText("بدون محدودیت")
                date_widget.setDate(no_date)
                if hasattr(date_widget, "setCalendarPopup"):
                    date_widget.setCalendarPopup(True)
            else:
                # QLineEdit: هیچ متد مخصوص تقویم صدا زده نمی‌شود.
                date_widget.clear()
                if hasattr(date_widget, "setPlaceholderText"):
                    date_widget.setPlaceholderText("شمسی: 1405/07/18 - خالی = همه تاریخ‌ها")

        self.ui.txtTrackingDate.setText(today)

        self.ui.cmbReportUnit.clear()
        self.ui.cmbReportUnit.addItem("همه واحدها")
        for unit in sorted(PERSIAN_UNITS):
            self.ui.cmbReportUnit.addItem(unit)

        # موضوع‌های موجود در tblkar برای فیلتر گزارش
        self.ui.cmbReportTopic.clear()
        self.ui.cmbReportTopic.addItem("همه موضوعات")
        topic_conn = None
        topic_cursor = None
        try:
            topic_conn = get_connection()
            topic_cursor = topic_conn.cursor()
            topic_cursor.execute(
                "SELECT DISTINCT [mozooe] FROM [tblkar] "
                "WHERE [mozooe] IS NOT NULL AND Trim([mozooe]) <> '' "
                "ORDER BY [mozooe]"
            )
            for topic_row in topic_cursor.fetchall():
                topic = str(topic_row[0] or "").strip()
                if topic:
                    self.ui.cmbReportTopic.addItem(topic)
        except Exception:
            pass
        finally:
            if topic_cursor is not None:
                try:
                    topic_cursor.close()
                except Exception:
                    pass
            if topic_conn is not None:
                try:
                    topic_conn.close()
                except Exception:
                    pass

        self.ui.cmbReportStatus.clear()
        self.ui.cmbReportStatus.addItems([
            "همه وضعیت‌ها",
            "ثبت نشده",
            "در انتظار بررسی",
            "در حال انجام",
            "متوقف شده",
            "پایان",
        ])

        self.ui.cmbTrackingStatus.clear()
        self.ui.cmbTrackingStatus.addItems([
            "در انتظار بررسی",
            "در حال انجام",
            "متوقف شده",
            "پایان",
        ])

        table = self.ui.tblReportList
        table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        table.verticalHeader().setVisible(False)
        table.setAlternatingRowColors(True)
        table.verticalHeader().setDefaultSectionSize(34)
        table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Interactive
        )
        table.horizontalHeader().setMinimumHeight(40)
        table.setStyleSheet("""
            QTableWidget {
                background: white;
                alternate-background-color: #F7F9FC;
                gridline-color: #D6DCE3;
                font-family: "B Nazanin";
                font-size: 12pt;
                selection-background-color: #B8D7F0;
                selection-color: #000000;
            }
            QHeaderView::section {
                background-color: #E8EEF5;
                color: #1F2937;
                font-family: "B Nazanin";
                font-size: 13pt;
                font-weight: bold;
                padding: 6px;
                border: 1px solid #C7D0DB;
            }
        """)

        self.ui.btnSaveTracking.setEnabled(self.can_manage_tracking())
        if not self.can_manage_tracking():
            self.ui.btnSaveTracking.setToolTip(
                "ثبت پیگیری و تکمیل کار فقط برای واحد تعمیرات عمومی یا SuperAdmin مجاز است."
            )

        self.ui.btnRefreshReport.clicked.connect(self.load_report_data)
        self.ui.btnClearReportFilters.clicked.connect(self.clear_report_filters)
        self.ui.txtReportSearch.textChanged.connect(self.load_report_data)
        self.ui.cmbReportUnit.currentIndexChanged.connect(self.load_report_data)
        self.ui.cmbReportTopic.currentIndexChanged.connect(self.load_report_data)
        self.ui.cmbReportStatus.currentIndexChanged.connect(self.load_report_data)
        # اتصال امن سیگنال‌ها برای QLineEdit و QDateEdit
        if hasattr(self.ui.txtReportFrom, "dateChanged"):
            self.ui.txtReportFrom.dateChanged.connect(self.load_report_data)
        else:
            self.ui.txtReportFrom.textChanged.connect(self.load_report_data)
        if hasattr(self.ui.txtReportTo, "dateChanged"):
            self.ui.txtReportTo.dateChanged.connect(self.load_report_data)
        else:
            self.ui.txtReportTo.textChanged.connect(self.load_report_data)
        self.ui.tblReportList.itemSelectionChanged.connect(
            self.on_report_selection_changed
        )
        self.ui.btnSaveTracking.clicked.connect(self.save_tracking)
        self.ui.btnViewTrackingHistory.clicked.connect(self.view_tracking_history)

    @staticmethod
    def _date_digits(value):
        value = normalize_digits(value).strip()
        return "".join(ch for ch in value if ch.isdigit())

    @staticmethod
    def _jalali_filter_date(qdate):
        """QDate میلادی را به YYYYMMDD شمسی تبدیل می‌کند؛ 1900/01/01 یعنی بدون فیلتر."""
        if qdate == QDate(1900, 1, 1):
            return ""
        gregorian_date = qdate.toPython()
        return jdatetime.date.fromgregorian(date=gregorian_date).strftime("%Y%m%d")

    @staticmethod
    def _read_report_filter_date(widget):
        """خواندن تاریخ فیلتر از QLineEdit یا QDateEdit و برگرداندن YYYYMMDD شمسی."""
        try:
            if hasattr(widget, "date"):
                qdate = widget.date()
                if qdate == QDate(1900, 1, 1):
                    return ""
                return MainWindow._jalali_filter_date(qdate)

            raw = normalize_digits(widget.text()).strip()
            digits = "".join(ch for ch in raw if ch.isdigit())
            if not digits:
                return ""
            if len(digits) != 8:
                return "INVALID"

            year, month, day = int(digits[:4]), int(digits[4:6]), int(digits[6:8])
            # اعتبارسنجی واقعی تاریخ شمسی؛ از ورود تاریخ نامعتبر جلوگیری می‌شود.
            jdatetime.date(year, month, day)
            return digits
        except Exception:
            return "INVALID"

    @staticmethod
    def _format_jalali_date(value):
        if value is None or value == "":
            return ""
        # فیلد Access ممکن است از نوع Date/Time باشد.
        if isinstance(value, datetime):
            try:
                jd = jdatetime.date.fromgregorian(date=value.date())
                return jd.strftime("%Y/%m/%d")
            except Exception:
                return str(value)
        if isinstance(value, py_date):
            try:
                jd = jdatetime.date.fromgregorian(date=value)
                return jd.strftime("%Y/%m/%d")
            except Exception:
                return str(value)
        text = str(value).strip()
        # اگر تاریخ متنی با اسلش ذخیره شده باشد، همان را استاندارد می‌کنیم.
        normalized = normalize_digits(text)
        digits = "".join(ch for ch in normalized if ch.isdigit())
        if len(digits) == 8:
            return f"{digits[:4]}/{digits[4:6]}/{digits[6:8]}"
        # پشتیبانی از تاریخ میلادی متنی در صورت وجود داده‌های قدیمی.
        for fmt in ("%Y-%m-%d", "%Y-%m-%d %H:%M:%S", "%m/%d/%Y"):
            try:
                gd = datetime.strptime(text[:19], fmt).date()
                return jdatetime.date.fromgregorian(date=gd).strftime("%Y/%m/%d")
            except Exception:
                pass
        return text

    @staticmethod
    def _completion_date_for_db(cursor, jalali_digits):
        """مقدار تاریخ پایان را متناسب با نوع فیلد tarikh در Access برمی‌گرداند."""
        year, month, day = int(jalali_digits[:4]), int(jalali_digits[4:6]), int(jalali_digits[6:8])
        jalali = jdatetime.date(year, month, day)
        gregorian = jalali.togregorian()
        try:
            for column in cursor.columns(table="tblkar"):
                if str(getattr(column, "column_name", "")).casefold() == "tarikh":
                    type_name = str(getattr(column, "type_name", "")).upper()
                    data_type = getattr(column, "data_type", None)
                    if any(word in type_name for word in ("DATE", "TIME")) or data_type in (91, 92, 93):
                        return datetime(gregorian.year, gregorian.month, gregorian.day)
                    if any(word in type_name for word in ("CHAR", "TEXT", "VARCHAR", "MEMO")):
                        return jalali.strftime("%Y/%m/%d")
                    if any(word in type_name for word in ("INT", "NUMERIC", "DECIMAL", "DOUBLE", "FLOAT", "REAL")) or data_type in (2, 3, 4, 5, 6, 7, 8):
                        return int(jalali_digits)
                    break
        except Exception:
            pass
        # مقدار پیش‌فرض برای فیلدهای متنی؛ از تبدیل اشتباه تاریخ شمسی به میلادی جلوگیری می‌کند.
        return jalali.strftime("%Y/%m/%d")

    def _get_latest_tracking(self):
        """آخرین وضعیت پیگیری را مستقیماً از فیلدهای tblkar می‌خواند."""
        latest = {}
        conn = None
        cursor = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT [wonumber], [vaziyat], [tarikh], [sharhepey], [editor]
                FROM [tblkar]
            """)
            for row in cursor.fetchall():
                number = str(row[0] or "").strip()
                if number:
                    latest[number] = {
                        "status": str(row[1] or "ثبت نشده").strip() or "ثبت نشده",
                        "date": row[2],
                        "by": str(row[4] or "").strip(),
                        "description": str(row[3] or "").strip(),
                    }
        except Exception:
            return latest
        finally:
            if cursor is not None:
                try:
                    cursor.close()
                except Exception:
                    pass
            if conn is not None:
                try:
                    conn.close()
                except Exception:
                    pass
        return latest

    def load_report_data(self, *_args):
        if not hasattr(self.ui, "tblReportList"):
            return

        conn = None
        cursor = None
        try:
            conn = get_connection()
            cursor = conn.cursor()

            sql = """
                SELECT [wonumber], [vahed], [tarikhdarkhast], [mozooe],
                       [mahalkarf], [mahalkara], [darkhastkonande], [sharh],
                       [vaziyat], [tarikh], [sharhepey], [payan]
                FROM [tblkar]
            """
            conditions = []
            params = []

            is_superadmin = self.usersecurity.casefold() == "superadmin"
            is_maintenance = self.is_maintenance_unit()

            # واحد تعمیرات عمومی باید همه درخواست‌ها را برای انجام کار ببیند.
            # سایر کاربران فقط محدوده مجاز خودشان را مشاهده می‌کنند.
            if not is_superadmin and not is_maintenance:
                if self.usersecurity.casefold() == "admin":
                    if self.user_vahed:
                        conditions.append("[vahed] = ?")
                        params.append(self.user_vahed)
                    else:
                        conditions.append("1 = 0")
                else:
                    conditions.append("[darkhastkonande] = ?")
                    params.append(self.username)

            selected_unit = self.ui.cmbReportUnit.currentText().strip()
            if selected_unit and selected_unit != "همه واحدها":
                conditions.append("[vahed] = ?")
                params.append(selected_unit)

            selected_topic = self.ui.cmbReportTopic.currentText().strip()
            if selected_topic and selected_topic != "همه موضوعات":
                conditions.append("[mozooe] = ?")
                params.append(selected_topic)

            if conditions:
                sql += " WHERE " + " AND ".join(conditions)
            sql += " ORDER BY [id] DESC"

            cursor.execute(sql, tuple(params))
            rows = cursor.fetchall()
        except Exception as exc:
            QMessageBox.warning(
                self, "گزارش کارها",
                f"دریافت گزارش با خطا مواجه شد:\n{exc}"
            )
            return
        finally:
            if cursor is not None:
                try:
                    cursor.close()
                except Exception:
                    pass
            if conn is not None:
                try:
                    conn.close()
                except Exception:
                    pass

        latest = self._get_latest_tracking()
        search = self.ui.txtReportSearch.text().strip().casefold()
        from_date = self._read_report_filter_date(self.ui.txtReportFrom)
        to_date = self._read_report_filter_date(self.ui.txtReportTo)
        if from_date == "INVALID" or to_date == "INVALID":
            return
        if from_date and to_date and from_date > to_date:
            return
        wanted_status = self.ui.cmbReportStatus.currentText()

        display_rows = []
        for row in rows:
            wonumber = str(row[0] or "").strip()
            unit = str(row[1] or "").strip()
            date_raw = str(row[2] or "").strip()
            date_digits = self._date_digits(date_raw)
            topic = str(row[3] or "").strip()
            area = str(row[4] or "").strip()
            sub_area = str(row[5] or "").strip()
            requester = str(row[6] or "").strip()
            request_description = str(row[7] or "").strip()
            raw_status = str(row[8] or "").strip()
            # در رکوردهای قدیمی ممکن است وضعیت خالی باشد، اما فیلد payan درست باشد.
            payan_value = row[11] if len(row) > 11 else False
            is_completed = payan_value is True or str(payan_value).strip().casefold() in ("true", "1", "-1", "yes")
            status = normalize_status(raw_status) or ("پایان" if is_completed else "ثبت نشده")
            if is_completed:
                status = "پایان"
            followup_date = str(row[9] or "").strip()
            followup_description = str(row[10] or "").strip()

            if from_date and len(date_digits) == 8 and date_digits < from_date:
                continue
            if to_date and len(date_digits) == 8 and date_digits > to_date:
                continue
            if wanted_status != "همه وضعیت‌ها":
                wanted_key = normalize_status(wanted_status)
                status_key = normalize_status(status)
                if wanted_key == "پایان":
                    # هم وضعیت جدید و هم رکوردهای قدیمی با payan=True را شامل می‌شود.
                    if not (is_completed or status_key == "پایان"):
                        continue
                elif status_key != wanted_key:
                    continue

            haystack = " ".join([
                wonumber, unit, date_raw, topic, area, sub_area,
                requester, request_description, status, followup_description,
            ]).casefold()
            if search and search not in haystack and normalize_digits(search) not in normalize_digits(haystack):
                continue

            display_rows.append((
                wonumber, unit, date_raw, topic, area, requester,
                request_description, status, followup_date, followup_description,
            ))

        table = self.ui.tblReportList
        table.setRowCount(len(display_rows))
        for row_index, row in enumerate(display_rows):
            values = [
                str(row_index + 1), row[0], row[1],
                self._format_jalali_date(row[2]), row[3], row[4],
                row[5], row[6], row[7],
                self._format_jalali_date(row[8]), row[9],
            ]
            for col, value in enumerate(values):
                item = QTableWidgetItem(str(value or ""))
                item.setTextAlignment(
                    Qt.AlignmentFlag.AlignCenter
                )
                if col == 1:
                    item.setData(Qt.ItemDataRole.UserRole, row[0])
                table.setItem(row_index, col, item)

        widths = [55, 105, 160, 115, 150, 150, 140, 320, 125, 125, 300]
        for col, width in enumerate(widths):
            table.setColumnWidth(col, width)

    def on_report_selection_changed(self):
        row = self.ui.tblReportList.currentRow()
        if row < 0:
            self.ui.lblSelectedWorkNo.setText("—")
            return
        item = self.ui.tblReportList.item(row, 1)
        number = item.data(Qt.ItemDataRole.UserRole) if item else ""
        if not number and item:
            number = item.text()
        self.ui.lblSelectedWorkNo.setText(str(number or "—"))

    def save_tracking(self):
        if not self.can_manage_tracking():
            QMessageBox.warning(
                self, "عدم دسترسی",
                "ثبت پیگیری و تکمیل کار فقط برای واحد تعمیرات عمومی یا SuperAdmin مجاز است."
            )
            return

        wonumber = self.ui.lblSelectedWorkNo.text().strip()
        if not wonumber or wonumber == "—":
            QMessageBox.warning(self, "انتخاب درخواست", "ابتدا یک درخواست از جدول گزارش انتخاب کنید.")
            return

        status = self.ui.cmbTrackingStatus.currentText().strip()
        date_text = self._date_digits(self.ui.txtTrackingDate.text())
        note = self.ui.txtTrackingNote.toPlainText().strip()
        is_completed = status.casefold() in ("پایان", "تکمیل شده")

        if is_completed:
            if len(date_text) != 8 or not date_text.isdigit():
                QMessageBox.warning(
                    self, "تاریخ پایان نامعتبر",
                    "برای پایان کار، تاریخ شمسی را به صورت ۸ رقمی وارد کنید؛ مثال: ۱۴۰۵۰۷۲۲"
                )
                return
            try:
                jdatetime.date(int(date_text[:4]), int(date_text[4:6]), int(date_text[6:8]))
            except ValueError:
                QMessageBox.warning(self, "تاریخ پایان نامعتبر", "تاریخ پایان کار معتبر نیست.")
                return

        if not note:
            QMessageBox.warning(self, "شرح پیگیری", "شرح پیگیری یا نتیجه انجام کار را وارد کنید.")
            return

        conn = None
        cursor = None
        try:
            conn = get_connection()
            cursor = conn.cursor()

            # تاریخ پایان فقط هنگام انتخاب وضعیت «پایان» تغییر می‌کند؛
            # با بازگرداندن کار به وضعیت دیگر، تاریخ قبلی حفظ می‌شود.
            if is_completed:
                completion_date = self._completion_date_for_db(cursor, date_text)
                cursor.execute("""
                    UPDATE [tblkar]
                    SET [vaziyat] = ?,
                        [payan] = ?,
                        [tarikh] = ?,
                        [editor] = ?,
                        [sharhepey] = ?
                    WHERE [wonumber] = ?
                """, ("پایان", True, completion_date, self.username, note, wonumber))
            else:
                cursor.execute("""
                    UPDATE [tblkar]
                    SET [vaziyat] = ?,
                        [payan] = ?,
                        [editor] = ?,
                        [sharhepey] = ?
                    WHERE [wonumber] = ?
                """, (status, False, self.username, note, wonumber))

            if cursor.rowcount == 0:
                QMessageBox.warning(
                    self, "ثبت پیگیری",
                    "درخواست موردنظر در tblkar پیدا نشد و اطلاعات ذخیره نشد."
                )
                conn.rollback()
                return

            conn.commit()
        except Exception as exc:
            if conn is not None:
                try:
                    conn.rollback()
                except Exception:
                    pass
            QMessageBox.critical(self, "ثبت پیگیری ناموفق", f"اطلاعات ذخیره نشد:\n{exc}")
            return
        finally:
            if cursor is not None:
                try:
                    cursor.close()
                except Exception:
                    pass
            if conn is not None:
                try:
                    conn.close()
                except Exception:
                    pass

        QMessageBox.information(
            self, "ثبت شد",
            "نتیجه پایان کار ثبت شد؛ فیلدهای payan، tarikh و editor نیز به‌روزرسانی شدند."
            if is_completed else "اطلاعات پیگیری با موفقیت ثبت شد."
        )
        self.ui.txtTrackingNote.clear()
        self.ui.txtTrackingDate.setText(jdatetime.date.today().strftime("%Y/%m/%d"))
        self.load_report_data()

    def view_tracking_history(self):
        wonumber = self.ui.lblSelectedWorkNo.text().strip()
        if not wonumber or wonumber == "—":
            QMessageBox.information(self, "سوابق پیگیری", "ابتدا یک درخواست را انتخاب کنید.")
            return

        conn = None
        cursor = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT [tarikh], [vaziyat], [sharhepey], [editor], [payan]
                FROM [tblkar]
                WHERE [wonumber] = ?
            """, (wonumber,))
            row = cursor.fetchone()
        except Exception as exc:
            QMessageBox.warning(self, "سوابق پیگیری", f"خواندن اطلاعات انجام نشد:\n{exc}")
            return
        finally:
            if cursor is not None:
                try:
                    cursor.close()
                except Exception:
                    pass
            if conn is not None:
                try:
                    conn.close()
                except Exception:
                    pass

        if not row:
            QMessageBox.information(self, "سوابق پیگیری", "برای این درخواست اطلاعاتی ثبت نشده است.")
            return

        completion_date, status, description, editor, is_completed = row
        date_display = self._format_jalali_date(completion_date) or "ثبت نشده"
        lines = [
            f"شماره درخواست: {wonumber}",
            f"وضعیت فعلی: {status or 'ثبت نشده'}",
            f"پایان کار: {'بله' if bool(is_completed) else 'خیر'}",
            f"تاریخ پایان: {date_display}",
            f"تغییردهنده وضعیت: {editor or 'ثبت نشده'}",
            f"شرح پیگیری / نتیجه کار: {description or ''}",
        ]
        QMessageBox.information(self, f"اطلاعات پیگیری درخواست {wonumber}", "\n".join(lines))

    def clear_report_filters(self):
        self.ui.txtReportSearch.clear()
        self.ui.cmbReportUnit.setCurrentIndex(0)
        self.ui.cmbReportTopic.setCurrentIndex(0)
        self.ui.cmbReportStatus.setCurrentIndex(0)
        for date_widget in (self.ui.txtReportFrom, self.ui.txtReportTo):
            if hasattr(date_widget, "setDate"):
                date_widget.setDate(QDate(1900, 1, 1))
            else:
                date_widget.clear()
        self.load_report_data()
