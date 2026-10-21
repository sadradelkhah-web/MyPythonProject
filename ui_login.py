# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(420, 280)
        login.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.verticalLayout = QVBoxLayout(login)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitle = QLabel(login)
        self.lblTitle.setObjectName(u"lblTitle")
        self.lblTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lblTitle)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lblUsername = QLabel(login)
        self.lblUsername.setObjectName(u"lblUsername")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblUsername)

        self.txtUsername = QLineEdit(login)
        self.txtUsername.setObjectName(u"txtUsername")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtUsername)

        self.lblPassword = QLabel(login)
        self.lblPassword.setObjectName(u"lblPassword")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblPassword)

        self.txtPassword = QLineEdit(login)
        self.txtPassword.setObjectName(u"txtPassword")
        self.txtPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtPassword)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayoutButtons = QHBoxLayout()
        self.horizontalLayoutButtons.setObjectName(u"horizontalLayoutButtons")
        self.btnLogin = QPushButton(login)
        self.btnLogin.setObjectName(u"btnLogin")

        self.horizontalLayoutButtons.addWidget(self.btnLogin)

        self.btnExit = QPushButton(login)
        self.btnExit.setObjectName(u"btnExit")

        self.horizontalLayoutButtons.addWidget(self.btnExit)


        self.verticalLayout.addLayout(self.horizontalLayoutButtons)


        self.retranslateUi(login)

        self.btnLogin.setDefault(True)


        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"\u0648\u0631\u0648\u062f \u0628\u0647 \u0633\u06cc\u0633\u062a\u0645", None))
        self.lblTitle.setText(QCoreApplication.translate("login", u"\u0648\u0631\u0648\u062f \u0628\u0647 \u0633\u06cc\u0633\u062a\u0645", None))
        self.lblUsername.setText(QCoreApplication.translate("login", u"\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc:", None))
        self.lblPassword.setText(QCoreApplication.translate("login", u"\u0631\u0645\u0632 \u0639\u0628\u0648\u0631:", None))
        self.btnLogin.setText(QCoreApplication.translate("login", u"\u0648\u0631\u0648\u062f", None))
        self.btnExit.setText(QCoreApplication.translate("login", u"\u062e\u0631\u0648\u062c", None))
    # retranslateUi

