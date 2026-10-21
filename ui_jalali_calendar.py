# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'jalali_calendar.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_JalaliCalendarDialog(object):
    def setupUi(self, JalaliCalendarDialog):
        if not JalaliCalendarDialog.objectName():
            JalaliCalendarDialog.setObjectName(u"JalaliCalendarDialog")
        JalaliCalendarDialog.setMinimumSize(QSize(350, 260))
        JalaliCalendarDialog.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.rootLayout = QVBoxLayout(JalaliCalendarDialog)
        self.rootLayout.setSpacing(8)
        self.rootLayout.setObjectName(u"rootLayout")
        self.rootLayout.setContentsMargins(10, 10, 10, 10)
        self.navigationLayout = QHBoxLayout()
        self.navigationLayout.setObjectName(u"navigationLayout")
        self.prev_button = QPushButton(JalaliCalendarDialog)
        self.prev_button.setObjectName(u"prev_button")

        self.navigationLayout.addWidget(self.prev_button)

        self.month_label = QLabel(JalaliCalendarDialog)
        self.month_label.setObjectName(u"month_label")
        self.month_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.navigationLayout.addWidget(self.month_label)

        self.next_button = QPushButton(JalaliCalendarDialog)
        self.next_button.setObjectName(u"next_button")

        self.navigationLayout.addWidget(self.next_button)


        self.rootLayout.addLayout(self.navigationLayout)

        self.days_grid = QGridLayout()
        self.days_grid.setSpacing(4)
        self.days_grid.setObjectName(u"days_grid")

        self.rootLayout.addLayout(self.days_grid)

        self.bottomLayout = QHBoxLayout()
        self.bottomLayout.setObjectName(u"bottomLayout")
        self.today_button = QPushButton(JalaliCalendarDialog)
        self.today_button.setObjectName(u"today_button")

        self.bottomLayout.addWidget(self.today_button)

        self.clear_button = QPushButton(JalaliCalendarDialog)
        self.clear_button.setObjectName(u"clear_button")

        self.bottomLayout.addWidget(self.clear_button)


        self.rootLayout.addLayout(self.bottomLayout)


        self.retranslateUi(JalaliCalendarDialog)

        QMetaObject.connectSlotsByName(JalaliCalendarDialog)
    # setupUi

    def retranslateUi(self, JalaliCalendarDialog):
        JalaliCalendarDialog.setWindowTitle(QCoreApplication.translate("JalaliCalendarDialog", u"\u0627\u0646\u062a\u062e\u0627\u0628 \u062a\u0627\u0631\u06cc\u062e \u0634\u0645\u0633\u06cc", None))
        JalaliCalendarDialog.setStyleSheet(QCoreApplication.translate("JalaliCalendarDialog", u"QDialog { background: white; border: 1px solid #9AA8B7; }\n"
"QPushButton { min-width: 32px; min-height: 30px; padding: 3px; }\n"
"QPushButton:hover { background: #DCEBFA; }\n"
"QLabel#month_label { font-weight: bold; font-size: 14pt; }\n"
"QLabel[weekdayHeader=\"true\"] { font-weight: bold; color: #245B87; }\n"
"QPushButton[calendarToday=\"true\"] { background: #1976D2; color: white; font-weight: bold; }", None))
        self.prev_button.setText(QCoreApplication.translate("JalaliCalendarDialog", u"\u0645\u0627\u0647 \u0642\u0628\u0644 \u25c0", None))
        self.month_label.setText(QCoreApplication.translate("JalaliCalendarDialog", u"\u0645\u0627\u0647 \u0648 \u0633\u0627\u0644", None))
        self.next_button.setText(QCoreApplication.translate("JalaliCalendarDialog", u"\u25b6 \u0645\u0627\u0647 \u0628\u0639\u062f", None))
        self.today_button.setText(QCoreApplication.translate("JalaliCalendarDialog", u"\u0627\u0645\u0631\u0648\u0632", None))
        self.clear_button.setText(QCoreApplication.translate("JalaliCalendarDialog", u"\u067e\u0627\u06a9 \u06a9\u0631\u062f\u0646", None))
    # retranslateUi

