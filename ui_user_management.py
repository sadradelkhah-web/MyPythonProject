# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_management.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDialog,
    QFormLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_user_managment(object):
    def setupUi(self, user_managment):
        if not user_managment.objectName():
            user_managment.setObjectName(u"user_managment")
        user_managment.resize(860, 670)
        user_managment.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.verticalLayoutDialog = QVBoxLayout(user_managment)
        self.verticalLayoutDialog.setObjectName(u"verticalLayoutDialog")
        self.lblUserFormNote = QLabel(user_managment)
        self.lblUserFormNote.setObjectName(u"lblUserFormNote")
        self.lblUserFormNote.setWordWrap(True)

        self.verticalLayoutDialog.addWidget(self.lblUserFormNote)

        self.tabUserPages = QTabWidget(user_managment)
        self.tabUserPages.setObjectName(u"tabUserPages")
        self.tabUserPages.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayoutTab1 = QVBoxLayout(self.tab)
        self.verticalLayoutTab1.setObjectName(u"verticalLayoutTab1")
        self.horizontalLayoutUserForm = QHBoxLayout()
        self.horizontalLayoutUserForm.setObjectName(u"horizontalLayoutUserForm")
        self.formLayoutUser = QFormLayout()
        self.formLayoutUser.setObjectName(u"formLayoutUser")
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.formLayoutUser.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.txtFullName = QLineEdit(self.tab)
        self.txtFullName.setObjectName(u"txtFullName")

        self.formLayoutUser.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtFullName)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")

        self.formLayoutUser.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.txtUserLogin = QLineEdit(self.tab)
        self.txtUserLogin.setObjectName(u"txtUserLogin")

        self.formLayoutUser.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtUserLogin)

        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")

        self.formLayoutUser.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.txtPassword = QLineEdit(self.tab)
        self.txtPassword.setObjectName(u"txtPassword")
        self.txtPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayoutUser.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtPassword)

        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")

        self.formLayoutUser.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.txtPassword2 = QLineEdit(self.tab)
        self.txtPassword2.setObjectName(u"txtPassword2")
        self.txtPassword2.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayoutUser.setWidget(3, QFormLayout.ItemRole.FieldRole, self.txtPassword2)

        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")

        self.formLayoutUser.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.txtSamat = QLineEdit(self.tab)
        self.txtSamat.setObjectName(u"txtSamat")

        self.formLayoutUser.setWidget(4, QFormLayout.ItemRole.FieldRole, self.txtSamat)

        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")

        self.formLayoutUser.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.cmbUserVahed = QComboBox(self.tab)
        self.cmbUserVahed.setObjectName(u"cmbUserVahed")

        self.formLayoutUser.setWidget(5, QFormLayout.ItemRole.FieldRole, self.cmbUserVahed)

        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")

        self.formLayoutUser.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.cmbUserLevel = QComboBox(self.tab)
        self.cmbUserLevel.setObjectName(u"cmbUserLevel")

        self.formLayoutUser.setWidget(6, QFormLayout.ItemRole.FieldRole, self.cmbUserLevel)


        self.horizontalLayoutUserForm.addLayout(self.formLayoutUser)

        self.verticalLayoutUserButtons = QVBoxLayout()
        self.verticalLayoutUserButtons.setObjectName(u"verticalLayoutUserButtons")
        self.btnSaveUser = QPushButton(self.tab)
        self.btnSaveUser.setObjectName(u"btnSaveUser")

        self.verticalLayoutUserButtons.addWidget(self.btnSaveUser)

        self.btnEditUser = QPushButton(self.tab)
        self.btnEditUser.setObjectName(u"btnEditUser")

        self.verticalLayoutUserButtons.addWidget(self.btnEditUser)

        self.btnDeleteUser = QPushButton(self.tab)
        self.btnDeleteUser.setObjectName(u"btnDeleteUser")

        self.verticalLayoutUserButtons.addWidget(self.btnDeleteUser)

        self.btnClear = QPushButton(self.tab)
        self.btnClear.setObjectName(u"btnClear")

        self.verticalLayoutUserButtons.addWidget(self.btnClear)

        self.btnCancel = QPushButton(self.tab)
        self.btnCancel.setObjectName(u"btnCancel")

        self.verticalLayoutUserButtons.addWidget(self.btnCancel)

        self.verticalSpacerButtons = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayoutUserButtons.addItem(self.verticalSpacerButtons)


        self.horizontalLayoutUserForm.addLayout(self.verticalLayoutUserButtons)


        self.verticalLayoutTab1.addLayout(self.horizontalLayoutUserForm)

        self.tblUsers = QTableWidget(self.tab)
        if (self.tblUsers.columnCount() < 4):
            self.tblUsers.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblUsers.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblUsers.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblUsers.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblUsers.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tblUsers.setObjectName(u"tblUsers")
        self.tblUsers.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayoutTab1.addWidget(self.tblUsers)

        self.tabUserPages.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayoutTab2 = QVBoxLayout(self.tab_2)
        self.verticalLayoutTab2.setObjectName(u"verticalLayoutTab2")
        self.formLayoutPassword = QFormLayout()
        self.formLayoutPassword.setObjectName(u"formLayoutPassword")
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")

        self.formLayoutPassword.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.cmbChangeUser = QComboBox(self.tab_2)
        self.cmbChangeUser.setObjectName(u"cmbChangeUser")

        self.formLayoutPassword.setWidget(0, QFormLayout.ItemRole.FieldRole, self.cmbChangeUser)

        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")

        self.formLayoutPassword.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.txtNewPassword = QLineEdit(self.tab_2)
        self.txtNewPassword.setObjectName(u"txtNewPassword")
        self.txtNewPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayoutPassword.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtNewPassword)

        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayoutPassword.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.txtNewPassword2 = QLineEdit(self.tab_2)
        self.txtNewPassword2.setObjectName(u"txtNewPassword2")
        self.txtNewPassword2.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayoutPassword.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtNewPassword2)


        self.verticalLayoutTab2.addLayout(self.formLayoutPassword)

        self.horizontalLayoutPasswordButtons = QHBoxLayout()
        self.horizontalLayoutPasswordButtons.setObjectName(u"horizontalLayoutPasswordButtons")
        self.btnChangePassword = QPushButton(self.tab_2)
        self.btnChangePassword.setObjectName(u"btnChangePassword")

        self.horizontalLayoutPasswordButtons.addWidget(self.btnChangePassword)

        self.btnCancelPassword = QPushButton(self.tab_2)
        self.btnCancelPassword.setObjectName(u"btnCancelPassword")

        self.horizontalLayoutPasswordButtons.addWidget(self.btnCancelPassword)

        self.horizontalSpacerPassword = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutPasswordButtons.addItem(self.horizontalSpacerPassword)


        self.verticalLayoutTab2.addLayout(self.horizontalLayoutPasswordButtons)

        self.verticalSpacerPassword = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayoutTab2.addItem(self.verticalSpacerPassword)

        self.tabUserPages.addTab(self.tab_2, "")

        self.verticalLayoutDialog.addWidget(self.tabUserPages)


        self.retranslateUi(user_managment)

        self.tabUserPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(user_managment)
    # setupUi

    def retranslateUi(self, user_managment):
        user_managment.setWindowTitle(QCoreApplication.translate("user_managment", u"\u0645\u062f\u06cc\u0631\u06cc\u062a \u06a9\u0627\u0631\u0628\u0631\u0627\u0646", None))
        self.lblUserFormNote.setText(QCoreApplication.translate("user_managment", u"\u0627\u06cc\u0646 \u0641\u0631\u0645 \u0628\u0631\u0627\u06cc \u0648\u06cc\u0631\u0627\u06cc\u0634 \u062f\u0631 Qt Designer \u0646\u06af\u0647\u062f\u0627\u0631\u06cc \u0645\u06cc\u200c\u0634\u0648\u062f. \u0627\u062c\u0631\u0627\u06cc \u0628\u0631\u0646\u0627\u0645\u0647 \u0627\u0632 \u062a\u0628\u200c\u0647\u0627\u06cc \u0641\u0631\u0645 \u0627\u0635\u0644\u06cc \u0627\u0633\u062a.", None))
        self.label_4.setText(QCoreApplication.translate("user_managment", u"\u0646\u0627\u0645 \u0648 \u0646\u0627\u0645 \u062e\u0627\u0646\u0648\u0627\u062f\u06af\u06cc:", None))
        self.label_5.setText(QCoreApplication.translate("user_managment", u"\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc:", None))
        self.label_6.setText(QCoreApplication.translate("user_managment", u"\u0631\u0645\u0632 \u0639\u0628\u0648\u0631:", None))
        self.label_7.setText(QCoreApplication.translate("user_managment", u"\u062a\u06a9\u0631\u0627\u0631 \u0631\u0645\u0632 \u0639\u0628\u0648\u0631:", None))
        self.label_8.setText(QCoreApplication.translate("user_managment", u"\u0633\u0645\u062a:", None))
        self.label_9.setText(QCoreApplication.translate("user_managment", u"\u0648\u0627\u062d\u062f:", None))
        self.label_10.setText(QCoreApplication.translate("user_managment", u"\u0633\u0637\u062d \u062f\u0633\u062a\u0631\u0633\u06cc:", None))
        self.btnSaveUser.setText(QCoreApplication.translate("user_managment", u"\u062b\u0628\u062a \u06a9\u0627\u0631\u0628\u0631", None))
        self.btnEditUser.setText(QCoreApplication.translate("user_managment", u"\u0648\u06cc\u0631\u0627\u06cc\u0634", None))
        self.btnDeleteUser.setText(QCoreApplication.translate("user_managment", u"\u062d\u0630\u0641 \u06a9\u0627\u0631\u0628\u0631", None))
        self.btnClear.setText(QCoreApplication.translate("user_managment", u"\u067e\u0627\u06a9 \u06a9\u0631\u062f\u0646", None))
        self.btnCancel.setText(QCoreApplication.translate("user_managment", u"\u0628\u0627\u0632\u06af\u0634\u062a", None))
        ___qtablewidgetitem = self.tblUsers.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("user_managment", u"\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc", None))
        ___qtablewidgetitem1 = self.tblUsers.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("user_managment", u"\u0646\u0627\u0645", None))
        ___qtablewidgetitem2 = self.tblUsers.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("user_managment", u"\u0648\u0627\u062d\u062f", None))
        ___qtablewidgetitem3 = self.tblUsers.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("user_managment", u"\u0633\u0637\u062d \u062f\u0633\u062a\u0631\u0633\u06cc", None))
        self.tabUserPages.setTabText(self.tabUserPages.indexOf(self.tab), QCoreApplication.translate("user_managment", u"\u062a\u0639\u0631\u06cc\u0641 \u06a9\u0627\u0631\u0628\u0631 \u062c\u062f\u06cc\u062f", None))
        self.label.setText(QCoreApplication.translate("user_managment", u"\u0627\u0646\u062a\u062e\u0627\u0628 \u06a9\u0627\u0631\u0628\u0631:", None))
        self.label_2.setText(QCoreApplication.translate("user_managment", u"\u0631\u0645\u0632 \u062c\u062f\u06cc\u062f:", None))
        self.label_3.setText(QCoreApplication.translate("user_managment", u"\u062a\u06a9\u0631\u0627\u0631 \u0631\u0645\u0632 \u062c\u062f\u06cc\u062f:", None))
        self.btnChangePassword.setText(QCoreApplication.translate("user_managment", u"\u062a\u063a\u06cc\u06cc\u0631 \u0631\u0645\u0632", None))
        self.btnCancelPassword.setText(QCoreApplication.translate("user_managment", u"\u0627\u0646\u0635\u0631\u0627\u0641", None))
        self.tabUserPages.setTabText(self.tabUserPages.indexOf(self.tab_2), QCoreApplication.translate("user_managment", u"\u062a\u063a\u06cc\u06cc\u0631 \u0631\u0645\u0632 \u0639\u0628\u0648\u0631", None))
    # retranslateUi

