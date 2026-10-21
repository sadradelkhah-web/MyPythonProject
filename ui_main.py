# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFormLayout, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 780)
        MainWindow.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.actionHome = QAction(MainWindow)
        self.actionHome.setObjectName(u"actionHome")
        self.actionPassword = QAction(MainWindow)
        self.actionPassword.setObjectName(u"actionPassword")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionUserManagement = QAction(MainWindow)
        self.actionUserManagement.setObjectName(u"actionUserManagement")
        self.actionRepairsRequest = QAction(MainWindow)
        self.actionRepairsRequest.setObjectName(u"actionRepairsRequest")
        self.actionRepairsHistory = QAction(MainWindow)
        self.actionRepairsHistory.setObjectName(u"actionRepairsHistory")
        self.actionEquipmentList = QAction(MainWindow)
        self.actionEquipmentList.setObjectName(u"actionEquipmentList")
        self.actionAssets = QAction(MainWindow)
        self.actionAssets.setObjectName(u"actionAssets")
        self.actionReportRepairs = QAction(MainWindow)
        self.actionReportRepairs.setObjectName(u"actionReportRepairs")
        self.actionReportEquipment = QAction(MainWindow)
        self.actionReportEquipment.setObjectName(u"actionReportEquipment")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionAnbarTahrir = QAction(MainWindow)
        self.actionAnbarTahrir.setObjectName(u"actionAnbarTahrir")
        self.actionMtoTahrir = QAction(MainWindow)
        self.actionMtoTahrir.setObjectName(u"actionMtoTahrir")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayoutApplication = QHBoxLayout(self.centralwidget)
        self.horizontalLayoutApplication.setSpacing(8)
        self.horizontalLayoutApplication.setObjectName(u"horizontalLayoutApplication")
        self.horizontalLayoutApplication.setContentsMargins(8, 8, 8, 8)
        self.navigationPanel = QFrame(self.centralwidget)
        self.navigationPanel.setObjectName(u"navigationPanel")
        self.navigationPanel.setMinimumSize(QSize(220, 0))
        self.navigationPanel.setMaximumSize(QSize(220, 16777215))
        self.navigationPanel.setFrameShape(QFrame.Shape.StyledPanel)
        self.navigationPanel.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayoutNavigation = QVBoxLayout(self.navigationPanel)
        self.verticalLayoutNavigation.setSpacing(8)
        self.verticalLayoutNavigation.setObjectName(u"verticalLayoutNavigation")
        self.verticalLayoutNavigation.setContentsMargins(12, 12, 12, 12)
        self.lblNavigationTitle = QLabel(self.navigationPanel)
        self.lblNavigationTitle.setObjectName(u"lblNavigationTitle")
        self.lblNavigationTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayoutNavigation.addWidget(self.lblNavigationTitle)

        self.lblNavigationUser = QLabel(self.navigationPanel)
        self.lblNavigationUser.setObjectName(u"lblNavigationUser")
        self.lblNavigationUser.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblNavigationUser.setWordWrap(True)

        self.verticalLayoutNavigation.addWidget(self.lblNavigationUser)

        self.navigationLine = QFrame(self.navigationPanel)
        self.navigationLine.setObjectName(u"navigationLine")
        self.navigationLine.setFrameShape(QFrame.Shape.HLine)
        self.navigationLine.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayoutNavigation.addWidget(self.navigationLine)

        self.btnHome = QPushButton(self.navigationPanel)
        self.btnHome.setObjectName(u"btnHome")
        self.btnHome.setMinimumSize(QSize(0, 42))

        self.verticalLayoutNavigation.addWidget(self.btnHome)

        self.btnPassword = QPushButton(self.navigationPanel)
        self.btnPassword.setObjectName(u"btnPassword")
        self.btnPassword.setMinimumSize(QSize(0, 42))

        self.verticalLayoutNavigation.addWidget(self.btnPassword)

        self.btnUsers = QPushButton(self.navigationPanel)
        self.btnUsers.setObjectName(u"btnUsers")
        self.btnUsers.setMinimumSize(QSize(0, 42))

        self.verticalLayoutNavigation.addWidget(self.btnUsers)

        self.btnTabPermissions = QPushButton(self.navigationPanel)
        self.btnTabPermissions.setObjectName(u"btnTabPermissions")
        self.btnTabPermissions.setMinimumSize(QSize(0, 42))

        self.verticalLayoutNavigation.addWidget(self.btnTabPermissions)

        self.btnRepairs = QPushButton(self.navigationPanel)
        self.btnRepairs.setObjectName(u"btnRepairs")
        self.btnRepairs.setMinimumSize(QSize(0, 42))

        self.verticalLayoutNavigation.addWidget(self.btnRepairs)

        self.btnEquipment = QPushButton(self.navigationPanel)
        self.btnEquipment.setObjectName(u"btnEquipment")
        self.btnEquipment.setMinimumSize(QSize(0, 42))

        self.verticalLayoutNavigation.addWidget(self.btnEquipment)

        self.btnAssets = QPushButton(self.navigationPanel)
        self.btnAssets.setObjectName(u"btnAssets")
        self.btnAssets.setMinimumSize(QSize(0, 42))

        self.verticalLayoutNavigation.addWidget(self.btnAssets)

        self.btnHotel = QPushButton(self.navigationPanel)
        self.btnHotel.setObjectName(u"btnHotel")
        self.btnHotel.setMinimumSize(QSize(0, 42))

        self.verticalLayoutNavigation.addWidget(self.btnHotel)

        self.btnReports = QPushButton(self.navigationPanel)
        self.btnReports.setObjectName(u"btnReports")
        self.btnReports.setMinimumSize(QSize(0, 42))

        self.verticalLayoutNavigation.addWidget(self.btnReports)

        self.btnAnbarTahrir = QPushButton(self.navigationPanel)
        self.btnAnbarTahrir.setObjectName(u"btnAnbarTahrir")
        self.btnAnbarTahrir.setMinimumSize(QSize(0, 42))

        self.verticalLayoutNavigation.addWidget(self.btnAnbarTahrir)

        self.btnMtoTahrir = QPushButton(self.navigationPanel)
        self.btnMtoTahrir.setObjectName(u"btnMtoTahrir")
        self.btnMtoTahrir.setMinimumSize(QSize(0, 42))

        self.verticalLayoutNavigation.addWidget(self.btnMtoTahrir)

        self.navigationVerticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayoutNavigation.addItem(self.navigationVerticalSpacer)

        self.btnExit = QPushButton(self.navigationPanel)
        self.btnExit.setObjectName(u"btnExit")
        self.btnExit.setMinimumSize(QSize(0, 42))

        self.verticalLayoutNavigation.addWidget(self.btnExit)


        self.horizontalLayoutApplication.addWidget(self.navigationPanel)

        self.tabMain = QTabWidget(self.centralwidget)
        self.tabMain.setObjectName(u"tabMain")
        sizePolicy.setHeightForWidth(self.tabMain.sizePolicy().hasHeightForWidth())
        self.tabMain.setSizePolicy(sizePolicy)
        self.tabMain.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.tabHome = QWidget()
        self.tabHome.setObjectName(u"tabHome")
        self.tabHome.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.verticalLayoutHome = QVBoxLayout(self.tabHome)
        self.verticalLayoutHome.setObjectName(u"verticalLayoutHome")
        self.lblHomeTitle = QLabel(self.tabHome)
        self.lblHomeTitle.setObjectName(u"lblHomeTitle")
        self.lblHomeTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayoutHome.addWidget(self.lblHomeTitle)

        self.gridLayoutHome = QGridLayout()
        self.gridLayoutHome.setObjectName(u"gridLayoutHome")
        self.btnOpenKar = QPushButton(self.tabHome)
        self.btnOpenKar.setObjectName(u"btnOpenKar")
        self.btnOpenKar.setMinimumSize(QSize(0, 70))

        self.gridLayoutHome.addWidget(self.btnOpenKar, 0, 0, 1, 1)

        self.btnOpenUsers = QPushButton(self.tabHome)
        self.btnOpenUsers.setObjectName(u"btnOpenUsers")
        self.btnOpenUsers.setMinimumSize(QSize(0, 70))

        self.gridLayoutHome.addWidget(self.btnOpenUsers, 0, 1, 1, 1)

        self.btnOpenPassword = QPushButton(self.tabHome)
        self.btnOpenPassword.setObjectName(u"btnOpenPassword")
        self.btnOpenPassword.setMinimumSize(QSize(0, 70))

        self.gridLayoutHome.addWidget(self.btnOpenPassword, 1, 0, 1, 1)

        self.btnOpenReports = QPushButton(self.tabHome)
        self.btnOpenReports.setObjectName(u"btnOpenReports")
        self.btnOpenReports.setMinimumSize(QSize(0, 70))

        self.gridLayoutHome.addWidget(self.btnOpenReports, 1, 1, 1, 1)

        self.btnOpenEquipment = QPushButton(self.tabHome)
        self.btnOpenEquipment.setObjectName(u"btnOpenEquipment")
        self.btnOpenEquipment.setMinimumSize(QSize(0, 70))

        self.gridLayoutHome.addWidget(self.btnOpenEquipment, 2, 0, 1, 1)

        self.btnOpenMesc = QPushButton(self.tabHome)
        self.btnOpenMesc.setObjectName(u"btnOpenMesc")
        self.btnOpenMesc.setMinimumSize(QSize(0, 70))

        self.gridLayoutHome.addWidget(self.btnOpenMesc, 2, 1, 1, 1)

        self.btnOpenAssets = QPushButton(self.tabHome)
        self.btnOpenAssets.setObjectName(u"btnOpenAssets")
        self.btnOpenAssets.setMinimumSize(QSize(0, 70))

        self.gridLayoutHome.addWidget(self.btnOpenAssets, 3, 0, 1, 1)

        self.btnOpenHotel = QPushButton(self.tabHome)
        self.btnOpenHotel.setObjectName(u"btnOpenHotel")
        self.btnOpenHotel.setMinimumSize(QSize(0, 70))

        self.gridLayoutHome.addWidget(self.btnOpenHotel, 3, 1, 1, 1)

        self.btnOpenAnbarTahrir = QPushButton(self.tabHome)
        self.btnOpenAnbarTahrir.setObjectName(u"btnOpenAnbarTahrir")
        self.btnOpenAnbarTahrir.setMinimumSize(QSize(0, 70))

        self.gridLayoutHome.addWidget(self.btnOpenAnbarTahrir, 4, 0, 1, 1)

        self.btnOpenMtoTahrir = QPushButton(self.tabHome)
        self.btnOpenMtoTahrir.setObjectName(u"btnOpenMtoTahrir")
        self.btnOpenMtoTahrir.setMinimumSize(QSize(0, 70))

        self.gridLayoutHome.addWidget(self.btnOpenMtoTahrir, 4, 1, 1, 1)


        self.verticalLayoutHome.addLayout(self.gridLayoutHome)

        self.verticalSpacerHome = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayoutHome.addItem(self.verticalSpacerHome)

        self.tabMain.addTab(self.tabHome, "")
        self.tabKar = QWidget()
        self.tabKar.setObjectName(u"tabKar")
        self.verticalLayoutKar = QVBoxLayout(self.tabKar)
        self.verticalLayoutKar.setObjectName(u"verticalLayoutKar")
        self.btnBackHomeKar = QPushButton(self.tabKar)
        self.btnBackHomeKar.setObjectName(u"btnBackHomeKar")
        self.btnBackHomeKar.setMinimumSize(QSize(170, 36))

        self.verticalLayoutKar.addWidget(self.btnBackHomeKar, 0, Qt.AlignmentFlag.AlignRight)

        self.horizontalLayoutKarTop = QHBoxLayout()
        self.horizontalLayoutKarTop.setObjectName(u"horizontalLayoutKarTop")
        self.formLayoutKar = QFormLayout()
        self.formLayoutKar.setObjectName(u"formLayoutKar")
        self.formLayoutKar.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_11 = QLabel(self.tabKar)
        self.label_11.setObjectName(u"label_11")

        self.formLayoutKar.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_11)

        self.lblWonumber = QLabel(self.tabKar)
        self.lblWonumber.setObjectName(u"lblWonumber")

        self.formLayoutKar.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lblWonumber)

        self.label_12 = QLabel(self.tabKar)
        self.label_12.setObjectName(u"label_12")

        self.formLayoutKar.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_12)

        self.cmbVahed = QComboBox(self.tabKar)
        self.cmbVahed.setObjectName(u"cmbVahed")

        self.formLayoutKar.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cmbVahed)

        self.label_13 = QLabel(self.tabKar)
        self.label_13.setObjectName(u"label_13")

        self.formLayoutKar.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_13)

        self.dateTarikhdarkhast = QLineEdit(self.tabKar)
        self.dateTarikhdarkhast.setObjectName(u"dateTarikhdarkhast")

        self.formLayoutKar.setWidget(2, QFormLayout.ItemRole.FieldRole, self.dateTarikhdarkhast)

        self.label_15 = QLabel(self.tabKar)
        self.label_15.setObjectName(u"label_15")

        self.formLayoutKar.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_15)

        self.cmbMozooe = QComboBox(self.tabKar)
        self.cmbMozooe.setObjectName(u"cmbMozooe")

        self.formLayoutKar.setWidget(3, QFormLayout.ItemRole.FieldRole, self.cmbMozooe)

        self.label_16 = QLabel(self.tabKar)
        self.label_16.setObjectName(u"label_16")

        self.formLayoutKar.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_16)

        self.txtMahalkarf = QLineEdit(self.tabKar)
        self.txtMahalkarf.setObjectName(u"txtMahalkarf")

        self.formLayoutKar.setWidget(4, QFormLayout.ItemRole.FieldRole, self.txtMahalkarf)

        self.label_17 = QLabel(self.tabKar)
        self.label_17.setObjectName(u"label_17")

        self.formLayoutKar.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_17)

        self.txtMahalkara = QLineEdit(self.tabKar)
        self.txtMahalkara.setObjectName(u"txtMahalkara")

        self.formLayoutKar.setWidget(5, QFormLayout.ItemRole.FieldRole, self.txtMahalkara)

        self.label_18 = QLabel(self.tabKar)
        self.label_18.setObjectName(u"label_18")

        self.formLayoutKar.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_18)

        self.lblDarkhastkonande = QLabel(self.tabKar)
        self.lblDarkhastkonande.setObjectName(u"lblDarkhastkonande")

        self.formLayoutKar.setWidget(6, QFormLayout.ItemRole.FieldRole, self.lblDarkhastkonande)


        self.horizontalLayoutKarTop.addLayout(self.formLayoutKar)

        self.verticalLayoutSharh = QVBoxLayout()
        self.verticalLayoutSharh.setObjectName(u"verticalLayoutSharh")
        self.label_14 = QLabel(self.tabKar)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayoutSharh.addWidget(self.label_14)

        self.txtSharh = QPlainTextEdit(self.tabKar)
        self.txtSharh.setObjectName(u"txtSharh")

        self.verticalLayoutSharh.addWidget(self.txtSharh)

        self.horizontalLayoutKarButtons = QHBoxLayout()
        self.horizontalLayoutKarButtons.setObjectName(u"horizontalLayoutKarButtons")
        self.btnSaveKar = QPushButton(self.tabKar)
        self.btnSaveKar.setObjectName(u"btnSaveKar")

        self.horizontalLayoutKarButtons.addWidget(self.btnSaveKar)

        self.btnNewKar = QPushButton(self.tabKar)
        self.btnNewKar.setObjectName(u"btnNewKar")

        self.horizontalLayoutKarButtons.addWidget(self.btnNewKar)

        self.btnClearKar = QPushButton(self.tabKar)
        self.btnClearKar.setObjectName(u"btnClearKar")

        self.horizontalLayoutKarButtons.addWidget(self.btnClearKar)


        self.verticalLayoutSharh.addLayout(self.horizontalLayoutKarButtons)


        self.horizontalLayoutKarTop.addLayout(self.verticalLayoutSharh)


        self.verticalLayoutKar.addLayout(self.horizontalLayoutKarTop)

        self.horizontalLayoutSearch = QHBoxLayout()
        self.horizontalLayoutSearch.setObjectName(u"horizontalLayoutSearch")
        self.lblSearch = QLabel(self.tabKar)
        self.lblSearch.setObjectName(u"lblSearch")

        self.horizontalLayoutSearch.addWidget(self.lblSearch)

        self.txtSearchKar = QLineEdit(self.tabKar)
        self.txtSearchKar.setObjectName(u"txtSearchKar")

        self.horizontalLayoutSearch.addWidget(self.txtSearchKar)


        self.verticalLayoutKar.addLayout(self.horizontalLayoutSearch)

        self.tblKarList = QTableWidget(self.tabKar)
        self.tblKarList.setObjectName(u"tblKarList")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.tblKarList.sizePolicy().hasHeightForWidth())
        self.tblKarList.setSizePolicy(sizePolicy1)

        self.verticalLayoutKar.addWidget(self.tblKarList)

        self.tabMain.addTab(self.tabKar, "")
        self.tabUserManagement = QWidget()
        self.tabUserManagement.setObjectName(u"tabUserManagement")
        self.verticalLayoutUsers = QVBoxLayout(self.tabUserManagement)
        self.verticalLayoutUsers.setObjectName(u"verticalLayoutUsers")
        self.btnBackHomeUsers = QPushButton(self.tabUserManagement)
        self.btnBackHomeUsers.setObjectName(u"btnBackHomeUsers")
        self.btnBackHomeUsers.setMinimumSize(QSize(170, 36))

        self.verticalLayoutUsers.addWidget(self.btnBackHomeUsers, 0, Qt.AlignmentFlag.AlignRight)

        self.horizontalLayoutUserForm = QHBoxLayout()
        self.horizontalLayoutUserForm.setObjectName(u"horizontalLayoutUserForm")
        self.formLayoutUser = QFormLayout()
        self.formLayoutUser.setObjectName(u"formLayoutUser")
        self.label_4 = QLabel(self.tabUserManagement)
        self.label_4.setObjectName(u"label_4")

        self.formLayoutUser.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.txtFullName = QLineEdit(self.tabUserManagement)
        self.txtFullName.setObjectName(u"txtFullName")

        self.formLayoutUser.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtFullName)

        self.label_5 = QLabel(self.tabUserManagement)
        self.label_5.setObjectName(u"label_5")

        self.formLayoutUser.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.txtUserLogin = QLineEdit(self.tabUserManagement)
        self.txtUserLogin.setObjectName(u"txtUserLogin")

        self.formLayoutUser.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtUserLogin)

        self.label_6 = QLabel(self.tabUserManagement)
        self.label_6.setObjectName(u"label_6")

        self.formLayoutUser.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.txtPassword = QLineEdit(self.tabUserManagement)
        self.txtPassword.setObjectName(u"txtPassword")
        self.txtPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayoutUser.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtPassword)

        self.label_7 = QLabel(self.tabUserManagement)
        self.label_7.setObjectName(u"label_7")

        self.formLayoutUser.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.txtPassword2 = QLineEdit(self.tabUserManagement)
        self.txtPassword2.setObjectName(u"txtPassword2")
        self.txtPassword2.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayoutUser.setWidget(3, QFormLayout.ItemRole.FieldRole, self.txtPassword2)

        self.label_8 = QLabel(self.tabUserManagement)
        self.label_8.setObjectName(u"label_8")

        self.formLayoutUser.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.txtSamat = QLineEdit(self.tabUserManagement)
        self.txtSamat.setObjectName(u"txtSamat")

        self.formLayoutUser.setWidget(4, QFormLayout.ItemRole.FieldRole, self.txtSamat)

        self.label_9 = QLabel(self.tabUserManagement)
        self.label_9.setObjectName(u"label_9")

        self.formLayoutUser.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.cmbUserVahed = QComboBox(self.tabUserManagement)
        self.cmbUserVahed.setObjectName(u"cmbUserVahed")

        self.formLayoutUser.setWidget(5, QFormLayout.ItemRole.FieldRole, self.cmbUserVahed)

        self.label_10 = QLabel(self.tabUserManagement)
        self.label_10.setObjectName(u"label_10")

        self.formLayoutUser.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.cmbUserLevel = QComboBox(self.tabUserManagement)
        self.cmbUserLevel.setObjectName(u"cmbUserLevel")

        self.formLayoutUser.setWidget(6, QFormLayout.ItemRole.FieldRole, self.cmbUserLevel)


        self.horizontalLayoutUserForm.addLayout(self.formLayoutUser)

        self.verticalLayoutUserButtons = QVBoxLayout()
        self.verticalLayoutUserButtons.setObjectName(u"verticalLayoutUserButtons")
        self.btnSaveUser = QPushButton(self.tabUserManagement)
        self.btnSaveUser.setObjectName(u"btnSaveUser")

        self.verticalLayoutUserButtons.addWidget(self.btnSaveUser)

        self.btnEditUser = QPushButton(self.tabUserManagement)
        self.btnEditUser.setObjectName(u"btnEditUser")

        self.verticalLayoutUserButtons.addWidget(self.btnEditUser)

        self.btnDeleteUser = QPushButton(self.tabUserManagement)
        self.btnDeleteUser.setObjectName(u"btnDeleteUser")

        self.verticalLayoutUserButtons.addWidget(self.btnDeleteUser)

        self.btnClear = QPushButton(self.tabUserManagement)
        self.btnClear.setObjectName(u"btnClear")

        self.verticalLayoutUserButtons.addWidget(self.btnClear)

        self.btnCancel = QPushButton(self.tabUserManagement)
        self.btnCancel.setObjectName(u"btnCancel")

        self.verticalLayoutUserButtons.addWidget(self.btnCancel)

        self.verticalSpacerUserButtons = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayoutUserButtons.addItem(self.verticalSpacerUserButtons)


        self.horizontalLayoutUserForm.addLayout(self.verticalLayoutUserButtons)


        self.verticalLayoutUsers.addLayout(self.horizontalLayoutUserForm)

        self.tblUsers = QTableWidget(self.tabUserManagement)
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

        self.verticalLayoutUsers.addWidget(self.tblUsers)

        self.tabMain.addTab(self.tabUserManagement, "")
        self.tabChangePassword = QWidget()
        self.tabChangePassword.setObjectName(u"tabChangePassword")
        self.verticalLayoutPassword = QVBoxLayout(self.tabChangePassword)
        self.verticalLayoutPassword.setObjectName(u"verticalLayoutPassword")
        self.btnBackHomePassword = QPushButton(self.tabChangePassword)
        self.btnBackHomePassword.setObjectName(u"btnBackHomePassword")
        self.btnBackHomePassword.setMinimumSize(QSize(170, 36))

        self.verticalLayoutPassword.addWidget(self.btnBackHomePassword, 0, Qt.AlignmentFlag.AlignRight)

        self.formLayoutPassword = QFormLayout()
        self.formLayoutPassword.setObjectName(u"formLayoutPassword")
        self.label = QLabel(self.tabChangePassword)
        self.label.setObjectName(u"label")

        self.formLayoutPassword.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.cmbChangeUser = QComboBox(self.tabChangePassword)
        self.cmbChangeUser.setObjectName(u"cmbChangeUser")

        self.formLayoutPassword.setWidget(0, QFormLayout.ItemRole.FieldRole, self.cmbChangeUser)

        self.label_2 = QLabel(self.tabChangePassword)
        self.label_2.setObjectName(u"label_2")

        self.formLayoutPassword.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.txtNewPassword = QLineEdit(self.tabChangePassword)
        self.txtNewPassword.setObjectName(u"txtNewPassword")
        self.txtNewPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayoutPassword.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtNewPassword)

        self.label_3 = QLabel(self.tabChangePassword)
        self.label_3.setObjectName(u"label_3")

        self.formLayoutPassword.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.txtNewPassword2 = QLineEdit(self.tabChangePassword)
        self.txtNewPassword2.setObjectName(u"txtNewPassword2")
        self.txtNewPassword2.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayoutPassword.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtNewPassword2)


        self.verticalLayoutPassword.addLayout(self.formLayoutPassword)

        self.horizontalLayoutPasswordButtons = QHBoxLayout()
        self.horizontalLayoutPasswordButtons.setObjectName(u"horizontalLayoutPasswordButtons")
        self.btnChangePassword = QPushButton(self.tabChangePassword)
        self.btnChangePassword.setObjectName(u"btnChangePassword")

        self.horizontalLayoutPasswordButtons.addWidget(self.btnChangePassword)

        self.btnCancelPassword = QPushButton(self.tabChangePassword)
        self.btnCancelPassword.setObjectName(u"btnCancelPassword")

        self.horizontalLayoutPasswordButtons.addWidget(self.btnCancelPassword)

        self.horizontalSpacerPassword = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutPasswordButtons.addItem(self.horizontalSpacerPassword)


        self.verticalLayoutPassword.addLayout(self.horizontalLayoutPasswordButtons)

        self.verticalSpacerPassword = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayoutPassword.addItem(self.verticalSpacerPassword)

        self.tabMain.addTab(self.tabChangePassword, "")
        self.tabReport = QWidget()
        self.tabReport.setObjectName(u"tabReport")
        self.verticalLayoutReport = QVBoxLayout(self.tabReport)
        self.verticalLayoutReport.setObjectName(u"verticalLayoutReport")
        self.btnBackHomeReport = QPushButton(self.tabReport)
        self.btnBackHomeReport.setObjectName(u"btnBackHomeReport")
        self.btnBackHomeReport.setMinimumSize(QSize(170, 36))

        self.verticalLayoutReport.addWidget(self.btnBackHomeReport, 0, Qt.AlignmentFlag.AlignRight)

        self.groupReportFilters = QGroupBox(self.tabReport)
        self.groupReportFilters.setObjectName(u"groupReportFilters")
        self.gridReportFilters = QGridLayout(self.groupReportFilters)
        self.gridReportFilters.setObjectName(u"gridReportFilters")
        self.lblReportSearch = QLabel(self.groupReportFilters)
        self.lblReportSearch.setObjectName(u"lblReportSearch")

        self.gridReportFilters.addWidget(self.lblReportSearch, 0, 0, 1, 1)

        self.txtReportSearch = QLineEdit(self.groupReportFilters)
        self.txtReportSearch.setObjectName(u"txtReportSearch")

        self.gridReportFilters.addWidget(self.txtReportSearch, 0, 1, 1, 1)

        self.lblReportUnit = QLabel(self.groupReportFilters)
        self.lblReportUnit.setObjectName(u"lblReportUnit")

        self.gridReportFilters.addWidget(self.lblReportUnit, 0, 2, 1, 1)

        self.cmbReportUnit = QComboBox(self.groupReportFilters)
        self.cmbReportUnit.setObjectName(u"cmbReportUnit")

        self.gridReportFilters.addWidget(self.cmbReportUnit, 0, 3, 1, 1)

        self.lblReportTopic = QLabel(self.groupReportFilters)
        self.lblReportTopic.setObjectName(u"lblReportTopic")

        self.gridReportFilters.addWidget(self.lblReportTopic, 0, 4, 1, 1)

        self.cmbReportTopic = QComboBox(self.groupReportFilters)
        self.cmbReportTopic.setObjectName(u"cmbReportTopic")

        self.gridReportFilters.addWidget(self.cmbReportTopic, 0, 5, 1, 1)

        self.lblReportStatus = QLabel(self.groupReportFilters)
        self.lblReportStatus.setObjectName(u"lblReportStatus")

        self.gridReportFilters.addWidget(self.lblReportStatus, 1, 0, 1, 1)

        self.cmbReportStatus = QComboBox(self.groupReportFilters)
        self.cmbReportStatus.setObjectName(u"cmbReportStatus")

        self.gridReportFilters.addWidget(self.cmbReportStatus, 1, 1, 1, 1)

        self.lblReportFrom = QLabel(self.groupReportFilters)
        self.lblReportFrom.setObjectName(u"lblReportFrom")

        self.gridReportFilters.addWidget(self.lblReportFrom, 1, 2, 1, 1)

        self.txtReportFrom = QLineEdit(self.groupReportFilters)
        self.txtReportFrom.setObjectName(u"txtReportFrom")

        self.gridReportFilters.addWidget(self.txtReportFrom, 1, 3, 1, 1)

        self.lblReportTo = QLabel(self.groupReportFilters)
        self.lblReportTo.setObjectName(u"lblReportTo")

        self.gridReportFilters.addWidget(self.lblReportTo, 1, 4, 1, 1)

        self.txtReportTo = QLineEdit(self.groupReportFilters)
        self.txtReportTo.setObjectName(u"txtReportTo")

        self.gridReportFilters.addWidget(self.txtReportTo, 1, 5, 1, 1)

        self.btnRefreshReport = QPushButton(self.groupReportFilters)
        self.btnRefreshReport.setObjectName(u"btnRefreshReport")

        self.gridReportFilters.addWidget(self.btnRefreshReport, 2, 4, 1, 1)

        self.btnClearReportFilters = QPushButton(self.groupReportFilters)
        self.btnClearReportFilters.setObjectName(u"btnClearReportFilters")

        self.gridReportFilters.addWidget(self.btnClearReportFilters, 2, 5, 1, 1)


        self.verticalLayoutReport.addWidget(self.groupReportFilters)

        self.tblReportList = QTableWidget(self.tabReport)
        if (self.tblReportList.columnCount() < 11):
            self.tblReportList.setColumnCount(11)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblReportList.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblReportList.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblReportList.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tblReportList.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tblReportList.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tblReportList.setHorizontalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tblReportList.setHorizontalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tblReportList.setHorizontalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tblReportList.setHorizontalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tblReportList.setHorizontalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tblReportList.setHorizontalHeaderItem(10, __qtablewidgetitem14)
        self.tblReportList.setObjectName(u"tblReportList")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(2)
        sizePolicy2.setHeightForWidth(self.tblReportList.sizePolicy().hasHeightForWidth())
        self.tblReportList.setSizePolicy(sizePolicy2)
        self.tblReportList.setColumnCount(11)
        self.tblReportList.setAlternatingRowColors(True)
        self.tblReportList.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblReportList.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        self.verticalLayoutReport.addWidget(self.tblReportList)

        self.groupTracking = QGroupBox(self.tabReport)
        self.groupTracking.setObjectName(u"groupTracking")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupTracking.sizePolicy().hasHeightForWidth())
        self.groupTracking.setSizePolicy(sizePolicy3)
        self.gridTracking = QGridLayout(self.groupTracking)
        self.gridTracking.setObjectName(u"gridTracking")
        self.lblSelectedWorkNoTitle = QLabel(self.groupTracking)
        self.lblSelectedWorkNoTitle.setObjectName(u"lblSelectedWorkNoTitle")

        self.gridTracking.addWidget(self.lblSelectedWorkNoTitle, 0, 0, 1, 1)

        self.lblSelectedWorkNo = QLabel(self.groupTracking)
        self.lblSelectedWorkNo.setObjectName(u"lblSelectedWorkNo")

        self.gridTracking.addWidget(self.lblSelectedWorkNo, 0, 1, 1, 1)

        self.lblTrackingStatusTitle = QLabel(self.groupTracking)
        self.lblTrackingStatusTitle.setObjectName(u"lblTrackingStatusTitle")

        self.gridTracking.addWidget(self.lblTrackingStatusTitle, 0, 2, 1, 1)

        self.cmbTrackingStatus = QComboBox(self.groupTracking)
        self.cmbTrackingStatus.setObjectName(u"cmbTrackingStatus")

        self.gridTracking.addWidget(self.cmbTrackingStatus, 0, 3, 1, 1)

        self.lblTrackingDateTitle = QLabel(self.groupTracking)
        self.lblTrackingDateTitle.setObjectName(u"lblTrackingDateTitle")

        self.gridTracking.addWidget(self.lblTrackingDateTitle, 0, 4, 1, 1)

        self.txtTrackingDate = QLineEdit(self.groupTracking)
        self.txtTrackingDate.setObjectName(u"txtTrackingDate")

        self.gridTracking.addWidget(self.txtTrackingDate, 0, 5, 1, 1)

        self.lblTrackingNoteTitle = QLabel(self.groupTracking)
        self.lblTrackingNoteTitle.setObjectName(u"lblTrackingNoteTitle")

        self.gridTracking.addWidget(self.lblTrackingNoteTitle, 1, 0, 1, 1)

        self.txtTrackingNote = QPlainTextEdit(self.groupTracking)
        self.txtTrackingNote.setObjectName(u"txtTrackingNote")
        self.txtTrackingNote.setMinimumSize(QSize(0, 45))
        self.txtTrackingNote.setMaximumSize(QSize(16777215, 65))

        self.gridTracking.addWidget(self.txtTrackingNote, 1, 1, 1, 5)

        self.btnSaveTracking = QPushButton(self.groupTracking)
        self.btnSaveTracking.setObjectName(u"btnSaveTracking")

        self.gridTracking.addWidget(self.btnSaveTracking, 2, 1, 1, 1)

        self.btnViewTrackingHistory = QPushButton(self.groupTracking)
        self.btnViewTrackingHistory.setObjectName(u"btnViewTrackingHistory")

        self.gridTracking.addWidget(self.btnViewTrackingHistory, 2, 2, 1, 1)


        self.verticalLayoutReport.addWidget(self.groupTracking)

        self.tabMain.addTab(self.tabReport, "")
        self.tabMesc = QWidget()
        self.tabMesc.setObjectName(u"tabMesc")
        self.tabMesc.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.verticalLayoutMesc = QVBoxLayout(self.tabMesc)
        self.verticalLayoutMesc.setObjectName(u"verticalLayoutMesc")
        self.btnBackHomeMesc = QPushButton(self.tabMesc)
        self.btnBackHomeMesc.setObjectName(u"btnBackHomeMesc")
        self.btnBackHomeMesc.setMinimumSize(QSize(170, 36))

        self.verticalLayoutMesc.addWidget(self.btnBackHomeMesc, 0, Qt.AlignmentFlag.AlignRight)

        self.groupMescFields = QGroupBox(self.tabMesc)
        self.groupMescFields.setObjectName(u"groupMescFields")
        self.gridLayoutMescFields = QGridLayout(self.groupMescFields)
        self.gridLayoutMescFields.setObjectName(u"gridLayoutMescFields")
        self.lblMescCode = QLabel(self.groupMescFields)
        self.lblMescCode.setObjectName(u"lblMescCode")

        self.gridLayoutMescFields.addWidget(self.lblMescCode, 0, 0, 1, 1)

        self.txtMescCode = QLineEdit(self.groupMescFields)
        self.txtMescCode.setObjectName(u"txtMescCode")

        self.gridLayoutMescFields.addWidget(self.txtMescCode, 0, 1, 1, 1)

        self.lblMescShohazine = QLabel(self.groupMescFields)
        self.lblMescShohazine.setObjectName(u"lblMescShohazine")

        self.gridLayoutMescFields.addWidget(self.lblMescShohazine, 0, 2, 1, 1)

        self.txtMescShohazine = QLineEdit(self.groupMescFields)
        self.txtMescShohazine.setObjectName(u"txtMescShohazine")

        self.gridLayoutMescFields.addWidget(self.txtMescShohazine, 0, 3, 1, 1)

        self.lblMescSharh = QLabel(self.groupMescFields)
        self.lblMescSharh.setObjectName(u"lblMescSharh")

        self.gridLayoutMescFields.addWidget(self.lblMescSharh, 1, 0, 1, 1)

        self.txtMescSharh = QLineEdit(self.groupMescFields)
        self.txtMescSharh.setObjectName(u"txtMescSharh")

        self.gridLayoutMescFields.addWidget(self.txtMescSharh, 1, 1, 1, 1)

        self.lblMescDescription = QLabel(self.groupMescFields)
        self.lblMescDescription.setObjectName(u"lblMescDescription")

        self.gridLayoutMescFields.addWidget(self.lblMescDescription, 1, 2, 1, 1)

        self.txtMescDescription = QLineEdit(self.groupMescFields)
        self.txtMescDescription.setObjectName(u"txtMescDescription")

        self.gridLayoutMescFields.addWidget(self.txtMescDescription, 1, 3, 1, 1)

        self.lblMescUnit = QLabel(self.groupMescFields)
        self.lblMescUnit.setObjectName(u"lblMescUnit")

        self.gridLayoutMescFields.addWidget(self.lblMescUnit, 2, 0, 1, 1)

        self.txtMescUnit = QLineEdit(self.groupMescFields)
        self.txtMescUnit.setObjectName(u"txtMescUnit")

        self.gridLayoutMescFields.addWidget(self.txtMescUnit, 2, 1, 1, 1)

        self.lblMescPic = QLabel(self.groupMescFields)
        self.lblMescPic.setObjectName(u"lblMescPic")

        self.gridLayoutMescFields.addWidget(self.lblMescPic, 2, 2, 1, 1)

        self.mescPicturePanel = QWidget(self.groupMescFields)
        self.mescPicturePanel.setObjectName(u"mescPicturePanel")
        self.horizontalLayoutMescPicture = QHBoxLayout(self.mescPicturePanel)
        self.horizontalLayoutMescPicture.setObjectName(u"horizontalLayoutMescPicture")
        self.horizontalLayoutMescPicture.setContentsMargins(0, 0, 0, 0)
        self.lblMescPicPreview = QLabel(self.mescPicturePanel)
        self.lblMescPicPreview.setObjectName(u"lblMescPicPreview")
        self.lblMescPicPreview.setMinimumSize(QSize(150, 110))
        self.lblMescPicPreview.setMaximumSize(QSize(150, 110))
        self.lblMescPicPreview.setFrameShape(QFrame.Shape.StyledPanel)
        self.lblMescPicPreview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblMescPicPreview.setWordWrap(True)

        self.horizontalLayoutMescPicture.addWidget(self.lblMescPicPreview)

        self.verticalLayoutMescPictureButtons = QVBoxLayout()
        self.verticalLayoutMescPictureButtons.setObjectName(u"verticalLayoutMescPictureButtons")
        self.btnMescChoosePic = QPushButton(self.mescPicturePanel)
        self.btnMescChoosePic.setObjectName(u"btnMescChoosePic")

        self.verticalLayoutMescPictureButtons.addWidget(self.btnMescChoosePic)

        self.btnMescRemovePic = QPushButton(self.mescPicturePanel)
        self.btnMescRemovePic.setObjectName(u"btnMescRemovePic")

        self.verticalLayoutMescPictureButtons.addWidget(self.btnMescRemovePic)


        self.horizontalLayoutMescPicture.addLayout(self.verticalLayoutMescPictureButtons)


        self.gridLayoutMescFields.addWidget(self.mescPicturePanel, 2, 3, 1, 1)

        self.lblMescSabtkonande = QLabel(self.groupMescFields)
        self.lblMescSabtkonande.setObjectName(u"lblMescSabtkonande")

        self.gridLayoutMescFields.addWidget(self.lblMescSabtkonande, 3, 0, 1, 1)

        self.txtMescSabtkonande = QLineEdit(self.groupMescFields)
        self.txtMescSabtkonande.setObjectName(u"txtMescSabtkonande")
        self.txtMescSabtkonande.setReadOnly(True)

        self.gridLayoutMescFields.addWidget(self.txtMescSabtkonande, 3, 1, 1, 1)

        self.lblMescEditor = QLabel(self.groupMescFields)
        self.lblMescEditor.setObjectName(u"lblMescEditor")

        self.gridLayoutMescFields.addWidget(self.lblMescEditor, 3, 2, 1, 1)

        self.txtMescEditor = QLineEdit(self.groupMescFields)
        self.txtMescEditor.setObjectName(u"txtMescEditor")
        self.txtMescEditor.setReadOnly(True)

        self.gridLayoutMescFields.addWidget(self.txtMescEditor, 3, 3, 1, 1)


        self.verticalLayoutMesc.addWidget(self.groupMescFields)

        self.horizontalLayoutMescActions = QHBoxLayout()
        self.horizontalLayoutMescActions.setObjectName(u"horizontalLayoutMescActions")
        self.btnMescNew = QPushButton(self.tabMesc)
        self.btnMescNew.setObjectName(u"btnMescNew")

        self.horizontalLayoutMescActions.addWidget(self.btnMescNew)

        self.btnMescSave = QPushButton(self.tabMesc)
        self.btnMescSave.setObjectName(u"btnMescSave")

        self.horizontalLayoutMescActions.addWidget(self.btnMescSave)

        self.btnMescEdit = QPushButton(self.tabMesc)
        self.btnMescEdit.setObjectName(u"btnMescEdit")

        self.horizontalLayoutMescActions.addWidget(self.btnMescEdit)

        self.btnMescDelete = QPushButton(self.tabMesc)
        self.btnMescDelete.setObjectName(u"btnMescDelete")

        self.horizontalLayoutMescActions.addWidget(self.btnMescDelete)

        self.horizontalSpacerMescActions = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutMescActions.addItem(self.horizontalSpacerMescActions)


        self.verticalLayoutMesc.addLayout(self.horizontalLayoutMescActions)

        self.horizontalLayoutMescSearch = QHBoxLayout()
        self.horizontalLayoutMescSearch.setObjectName(u"horizontalLayoutMescSearch")
        self.lblMescSearch = QLabel(self.tabMesc)
        self.lblMescSearch.setObjectName(u"lblMescSearch")

        self.horizontalLayoutMescSearch.addWidget(self.lblMescSearch)

        self.txtMescSearch = QLineEdit(self.tabMesc)
        self.txtMescSearch.setObjectName(u"txtMescSearch")

        self.horizontalLayoutMescSearch.addWidget(self.txtMescSearch)

        self.btnMescSearch = QPushButton(self.tabMesc)
        self.btnMescSearch.setObjectName(u"btnMescSearch")

        self.horizontalLayoutMescSearch.addWidget(self.btnMescSearch)


        self.verticalLayoutMesc.addLayout(self.horizontalLayoutMescSearch)

        self.tblMescList = QTableWidget(self.tabMesc)
        if (self.tblMescList.columnCount() < 8):
            self.tblMescList.setColumnCount(8)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tblMescList.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tblMescList.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tblMescList.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tblMescList.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tblMescList.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tblMescList.setHorizontalHeaderItem(5, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tblMescList.setHorizontalHeaderItem(6, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tblMescList.setHorizontalHeaderItem(7, __qtablewidgetitem22)
        self.tblMescList.setObjectName(u"tblMescList")
        self.tblMescList.setMinimumSize(QSize(0, 220))
        self.tblMescList.setAlternatingRowColors(True)
        self.tblMescList.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblMescList.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tblMescList.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblMescList.setRowCount(0)
        self.tblMescList.setColumnCount(8)

        self.verticalLayoutMesc.addWidget(self.tblMescList)

        self.tabMain.addTab(self.tabMesc, "")
        self.tabAmval = QWidget()
        self.tabAmval.setObjectName(u"tabAmval")
        self.tabAmval.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.verticalLayoutAmval = QVBoxLayout(self.tabAmval)
        self.verticalLayoutAmval.setObjectName(u"verticalLayoutAmval")
        self.btnBackHomeAmval = QPushButton(self.tabAmval)
        self.btnBackHomeAmval.setObjectName(u"btnBackHomeAmval")
        self.btnBackHomeAmval.setMinimumSize(QSize(170, 36))

        self.verticalLayoutAmval.addWidget(self.btnBackHomeAmval, 0, Qt.AlignmentFlag.AlignRight)

        self.groupAmvalFilter = QGroupBox(self.tabAmval)
        self.groupAmvalFilter.setObjectName(u"groupAmvalFilter")
        self.gridLayoutAmvalFilter = QGridLayout(self.groupAmvalFilter)
        self.gridLayoutAmvalFilter.setObjectName(u"gridLayoutAmvalFilter")
        self.lblAmvalSearch = QLabel(self.groupAmvalFilter)
        self.lblAmvalSearch.setObjectName(u"lblAmvalSearch")

        self.gridLayoutAmvalFilter.addWidget(self.lblAmvalSearch, 0, 0, 1, 1)

        self.txtAmvalSearch = QLineEdit(self.groupAmvalFilter)
        self.txtAmvalSearch.setObjectName(u"txtAmvalSearch")

        self.gridLayoutAmvalFilter.addWidget(self.txtAmvalSearch, 0, 1, 1, 3)

        self.lblAmvalUnitFilter = QLabel(self.groupAmvalFilter)
        self.lblAmvalUnitFilter.setObjectName(u"lblAmvalUnitFilter")

        self.gridLayoutAmvalFilter.addWidget(self.lblAmvalUnitFilter, 0, 4, 1, 1)

        self.cmbAmvalUnitFilter = QComboBox(self.groupAmvalFilter)
        self.cmbAmvalUnitFilter.setObjectName(u"cmbAmvalUnitFilter")

        self.gridLayoutAmvalFilter.addWidget(self.cmbAmvalUnitFilter, 0, 5, 1, 1)

        self.lblAmvalActiveFilter = QLabel(self.groupAmvalFilter)
        self.lblAmvalActiveFilter.setObjectName(u"lblAmvalActiveFilter")

        self.gridLayoutAmvalFilter.addWidget(self.lblAmvalActiveFilter, 0, 6, 1, 1)

        self.cmbAmvalActiveFilter = QComboBox(self.groupAmvalFilter)
        self.cmbAmvalActiveFilter.addItem("")
        self.cmbAmvalActiveFilter.addItem("")
        self.cmbAmvalActiveFilter.addItem("")
        self.cmbAmvalActiveFilter.setObjectName(u"cmbAmvalActiveFilter")

        self.gridLayoutAmvalFilter.addWidget(self.cmbAmvalActiveFilter, 0, 7, 1, 1)

        self.btnAmvalSearch = QPushButton(self.groupAmvalFilter)
        self.btnAmvalSearch.setObjectName(u"btnAmvalSearch")

        self.gridLayoutAmvalFilter.addWidget(self.btnAmvalSearch, 1, 4, 1, 1)

        self.btnAmvalClearFilter = QPushButton(self.groupAmvalFilter)
        self.btnAmvalClearFilter.setObjectName(u"btnAmvalClearFilter")

        self.gridLayoutAmvalFilter.addWidget(self.btnAmvalClearFilter, 1, 5, 1, 1)

        self.btnAmvalReport = QPushButton(self.groupAmvalFilter)
        self.btnAmvalReport.setObjectName(u"btnAmvalReport")

        self.gridLayoutAmvalFilter.addWidget(self.btnAmvalReport, 1, 6, 1, 1)

        self.btnAmvalPrint = QPushButton(self.groupAmvalFilter)
        self.btnAmvalPrint.setObjectName(u"btnAmvalPrint")

        self.gridLayoutAmvalFilter.addWidget(self.btnAmvalPrint, 1, 7, 1, 1)


        self.verticalLayoutAmval.addWidget(self.groupAmvalFilter)

        self.groupAmvalInfo = QGroupBox(self.tabAmval)
        self.groupAmvalInfo.setObjectName(u"groupAmvalInfo")
        self.gridLayoutAmvalInfo = QGridLayout(self.groupAmvalInfo)
        self.gridLayoutAmvalInfo.setObjectName(u"gridLayoutAmvalInfo")
        self.lblAmvalID = QLabel(self.groupAmvalInfo)
        self.lblAmvalID.setObjectName(u"lblAmvalID")

        self.gridLayoutAmvalInfo.addWidget(self.lblAmvalID, 0, 0, 1, 1)

        self.txtAmvalID = QLineEdit(self.groupAmvalInfo)
        self.txtAmvalID.setObjectName(u"txtAmvalID")
        self.txtAmvalID.setReadOnly(True)

        self.gridLayoutAmvalInfo.addWidget(self.txtAmvalID, 0, 1, 1, 1)

        self.lblAmvalAssetNo = QLabel(self.groupAmvalInfo)
        self.lblAmvalAssetNo.setObjectName(u"lblAmvalAssetNo")

        self.gridLayoutAmvalInfo.addWidget(self.lblAmvalAssetNo, 0, 2, 1, 1)

        self.txtAmvalAssetNo = QLineEdit(self.groupAmvalInfo)
        self.txtAmvalAssetNo.setObjectName(u"txtAmvalAssetNo")

        self.gridLayoutAmvalInfo.addWidget(self.txtAmvalAssetNo, 0, 3, 1, 1)

        self.lblAmvalDescription = QLabel(self.groupAmvalInfo)
        self.lblAmvalDescription.setObjectName(u"lblAmvalDescription")

        self.gridLayoutAmvalInfo.addWidget(self.lblAmvalDescription, 0, 4, 1, 1)

        self.txtAmvalDescription = QLineEdit(self.groupAmvalInfo)
        self.txtAmvalDescription.setObjectName(u"txtAmvalDescription")

        self.gridLayoutAmvalInfo.addWidget(self.txtAmvalDescription, 0, 5, 1, 3)

        self.lblAmvalStatus = QLabel(self.groupAmvalInfo)
        self.lblAmvalStatus.setObjectName(u"lblAmvalStatus")

        self.gridLayoutAmvalInfo.addWidget(self.lblAmvalStatus, 1, 0, 1, 1)

        self.txtAmvalStatus = QLineEdit(self.groupAmvalInfo)
        self.txtAmvalStatus.setObjectName(u"txtAmvalStatus")

        self.gridLayoutAmvalInfo.addWidget(self.txtAmvalStatus, 1, 1, 1, 1)

        self.lblAmvalUsePlace = QLabel(self.groupAmvalInfo)
        self.lblAmvalUsePlace.setObjectName(u"lblAmvalUsePlace")

        self.gridLayoutAmvalInfo.addWidget(self.lblAmvalUsePlace, 1, 2, 1, 1)

        self.txtAmvalMahal = QLineEdit(self.groupAmvalInfo)
        self.txtAmvalMahal.setObjectName(u"txtAmvalMahal")

        self.gridLayoutAmvalInfo.addWidget(self.txtAmvalMahal, 1, 3, 1, 1)

        self.lblAmvalSerial = QLabel(self.groupAmvalInfo)
        self.lblAmvalSerial.setObjectName(u"lblAmvalSerial")

        self.gridLayoutAmvalInfo.addWidget(self.lblAmvalSerial, 1, 4, 1, 1)

        self.txtAmvalSerial = QLineEdit(self.groupAmvalInfo)
        self.txtAmvalSerial.setObjectName(u"txtAmvalSerial")

        self.gridLayoutAmvalInfo.addWidget(self.txtAmvalSerial, 1, 5, 1, 1)

        self.lblAmvalLocCode = QLabel(self.groupAmvalInfo)
        self.lblAmvalLocCode.setObjectName(u"lblAmvalLocCode")

        self.gridLayoutAmvalInfo.addWidget(self.lblAmvalLocCode, 1, 6, 1, 1)

        self.txtAmvalLocCode = QLineEdit(self.groupAmvalInfo)
        self.txtAmvalLocCode.setObjectName(u"txtAmvalLocCode")

        self.gridLayoutAmvalInfo.addWidget(self.txtAmvalLocCode, 1, 7, 1, 1)

        self.lblAmvalInvDate = QLabel(self.groupAmvalInfo)
        self.lblAmvalInvDate.setObjectName(u"lblAmvalInvDate")

        self.gridLayoutAmvalInfo.addWidget(self.lblAmvalInvDate, 2, 0, 1, 1)

        self.txtAmvalInvDate = QLineEdit(self.groupAmvalInfo)
        self.txtAmvalInvDate.setObjectName(u"txtAmvalInvDate")

        self.gridLayoutAmvalInfo.addWidget(self.txtAmvalInvDate, 2, 1, 1, 1)

        self.lblAmvalExitDate = QLabel(self.groupAmvalInfo)
        self.lblAmvalExitDate.setObjectName(u"lblAmvalExitDate")

        self.gridLayoutAmvalInfo.addWidget(self.lblAmvalExitDate, 2, 2, 1, 1)

        self.txtAmvalExitDate = QLineEdit(self.groupAmvalInfo)
        self.txtAmvalExitDate.setObjectName(u"txtAmvalExitDate")

        self.gridLayoutAmvalInfo.addWidget(self.txtAmvalExitDate, 2, 3, 1, 1)

        self.lblAmvalAcqDate = QLabel(self.groupAmvalInfo)
        self.lblAmvalAcqDate.setObjectName(u"lblAmvalAcqDate")

        self.gridLayoutAmvalInfo.addWidget(self.lblAmvalAcqDate, 2, 4, 1, 1)

        self.txtAmvalAcqDate = QLineEdit(self.groupAmvalInfo)
        self.txtAmvalAcqDate.setObjectName(u"txtAmvalAcqDate")

        self.gridLayoutAmvalInfo.addWidget(self.txtAmvalAcqDate, 2, 5, 1, 1)

        self.lblAmvalLoc = QLabel(self.groupAmvalInfo)
        self.lblAmvalLoc.setObjectName(u"lblAmvalLoc")

        self.gridLayoutAmvalInfo.addWidget(self.lblAmvalLoc, 2, 6, 1, 1)

        self.txtAmvalLoc = QLineEdit(self.groupAmvalInfo)
        self.txtAmvalLoc.setObjectName(u"txtAmvalLoc")

        self.gridLayoutAmvalInfo.addWidget(self.txtAmvalLoc, 2, 7, 1, 1)

        self.lblAmvalBudget = QLabel(self.groupAmvalInfo)
        self.lblAmvalBudget.setObjectName(u"lblAmvalBudget")

        self.gridLayoutAmvalInfo.addWidget(self.lblAmvalBudget, 3, 0, 1, 1)

        self.txtAmvalBudget = QLineEdit(self.groupAmvalInfo)
        self.txtAmvalBudget.setObjectName(u"txtAmvalBudget")

        self.gridLayoutAmvalInfo.addWidget(self.txtAmvalBudget, 3, 1, 1, 1)

        self.lblAmvalNotes = QLabel(self.groupAmvalInfo)
        self.lblAmvalNotes.setObjectName(u"lblAmvalNotes")

        self.gridLayoutAmvalInfo.addWidget(self.lblAmvalNotes, 3, 2, 1, 1)

        self.txtAmvalNotes = QPlainTextEdit(self.groupAmvalInfo)
        self.txtAmvalNotes.setObjectName(u"txtAmvalNotes")
        self.txtAmvalNotes.setMinimumSize(QSize(0, 55))
        self.txtAmvalNotes.setMaximumSize(QSize(16777215, 80))

        self.gridLayoutAmvalInfo.addWidget(self.txtAmvalNotes, 3, 3, 1, 5)

        self.lblAmvalUnit = QLabel(self.groupAmvalInfo)
        self.lblAmvalUnit.setObjectName(u"lblAmvalUnit")

        self.gridLayoutAmvalInfo.addWidget(self.lblAmvalUnit, 4, 0, 1, 1)

        self.cmbAmvalUnit = QComboBox(self.groupAmvalInfo)
        self.cmbAmvalUnit.setObjectName(u"cmbAmvalUnit")

        self.gridLayoutAmvalInfo.addWidget(self.cmbAmvalUnit, 4, 1, 1, 1)

        self.lblAmvalUnitCode = QLabel(self.groupAmvalInfo)
        self.lblAmvalUnitCode.setObjectName(u"lblAmvalUnitCode")

        self.gridLayoutAmvalInfo.addWidget(self.lblAmvalUnitCode, 4, 2, 1, 1)

        self.txtAmvalUnitCode = QLineEdit(self.groupAmvalInfo)
        self.txtAmvalUnitCode.setObjectName(u"txtAmvalUnitCode")

        self.gridLayoutAmvalInfo.addWidget(self.txtAmvalUnitCode, 4, 3, 1, 1)

        self.lblAmvalActive = QLabel(self.groupAmvalInfo)
        self.lblAmvalActive.setObjectName(u"lblAmvalActive")

        self.gridLayoutAmvalInfo.addWidget(self.lblAmvalActive, 4, 4, 1, 1)

        self.cmbAmvalActive = QComboBox(self.groupAmvalInfo)
        self.cmbAmvalActive.addItem("")
        self.cmbAmvalActive.addItem("")
        self.cmbAmvalActive.setObjectName(u"cmbAmvalActive")

        self.gridLayoutAmvalInfo.addWidget(self.cmbAmvalActive, 4, 5, 1, 1)

        self.lblAmvalManUser = QLabel(self.groupAmvalInfo)
        self.lblAmvalManUser.setObjectName(u"lblAmvalManUser")

        self.gridLayoutAmvalInfo.addWidget(self.lblAmvalManUser, 4, 6, 1, 1)

        self.txtAmvalManUser = QLineEdit(self.groupAmvalInfo)
        self.txtAmvalManUser.setObjectName(u"txtAmvalManUser")

        self.gridLayoutAmvalInfo.addWidget(self.txtAmvalManUser, 4, 7, 1, 1)

        self.lblAmvalCode = QLabel(self.groupAmvalInfo)
        self.lblAmvalCode.setObjectName(u"lblAmvalCode")

        self.gridLayoutAmvalInfo.addWidget(self.lblAmvalCode, 5, 0, 1, 1)

        self.txtAmvalCode = QLineEdit(self.groupAmvalInfo)
        self.txtAmvalCode.setObjectName(u"txtAmvalCode")

        self.gridLayoutAmvalInfo.addWidget(self.txtAmvalCode, 5, 1, 1, 1)

        self.lblAmvalCdVahed = QLabel(self.groupAmvalInfo)
        self.lblAmvalCdVahed.setObjectName(u"lblAmvalCdVahed")

        self.gridLayoutAmvalInfo.addWidget(self.lblAmvalCdVahed, 5, 2, 1, 1)

        self.txtAmvalCdVahed = QLineEdit(self.groupAmvalInfo)
        self.txtAmvalCdVahed.setObjectName(u"txtAmvalCdVahed")

        self.gridLayoutAmvalInfo.addWidget(self.txtAmvalCdVahed, 5, 3, 1, 1)

        self.lblAmvalRecorder = QLabel(self.groupAmvalInfo)
        self.lblAmvalRecorder.setObjectName(u"lblAmvalRecorder")

        self.gridLayoutAmvalInfo.addWidget(self.lblAmvalRecorder, 5, 4, 1, 1)

        self.txtAmvalRecorder = QLineEdit(self.groupAmvalInfo)
        self.txtAmvalRecorder.setObjectName(u"txtAmvalRecorder")
        self.txtAmvalRecorder.setReadOnly(True)

        self.gridLayoutAmvalInfo.addWidget(self.txtAmvalRecorder, 5, 5, 1, 1)

        self.lblAmvalEditor = QLabel(self.groupAmvalInfo)
        self.lblAmvalEditor.setObjectName(u"lblAmvalEditor")

        self.gridLayoutAmvalInfo.addWidget(self.lblAmvalEditor, 5, 6, 1, 1)

        self.txtAmvalEditor = QLineEdit(self.groupAmvalInfo)
        self.txtAmvalEditor.setObjectName(u"txtAmvalEditor")
        self.txtAmvalEditor.setReadOnly(True)

        self.gridLayoutAmvalInfo.addWidget(self.txtAmvalEditor, 5, 7, 1, 1)


        self.verticalLayoutAmval.addWidget(self.groupAmvalInfo)

        self.horizontalLayoutAmvalActions = QHBoxLayout()
        self.horizontalLayoutAmvalActions.setObjectName(u"horizontalLayoutAmvalActions")
        self.btnAmvalNew = QPushButton(self.tabAmval)
        self.btnAmvalNew.setObjectName(u"btnAmvalNew")

        self.horizontalLayoutAmvalActions.addWidget(self.btnAmvalNew)

        self.btnAmvalSave = QPushButton(self.tabAmval)
        self.btnAmvalSave.setObjectName(u"btnAmvalSave")

        self.horizontalLayoutAmvalActions.addWidget(self.btnAmvalSave)

        self.btnAmvalEdit = QPushButton(self.tabAmval)
        self.btnAmvalEdit.setObjectName(u"btnAmvalEdit")

        self.horizontalLayoutAmvalActions.addWidget(self.btnAmvalEdit)

        self.btnAmvalDelete = QPushButton(self.tabAmval)
        self.btnAmvalDelete.setObjectName(u"btnAmvalDelete")

        self.horizontalLayoutAmvalActions.addWidget(self.btnAmvalDelete)

        self.horizontalSpacerAmvalActions = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutAmvalActions.addItem(self.horizontalSpacerAmvalActions)


        self.verticalLayoutAmval.addLayout(self.horizontalLayoutAmvalActions)

        self.tblAmvalList = QTableWidget(self.tabAmval)
        if (self.tblAmvalList.columnCount() < 20):
            self.tblAmvalList.setColumnCount(20)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tblAmvalList.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tblAmvalList.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tblAmvalList.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tblAmvalList.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tblAmvalList.setHorizontalHeaderItem(4, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tblAmvalList.setHorizontalHeaderItem(5, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tblAmvalList.setHorizontalHeaderItem(6, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tblAmvalList.setHorizontalHeaderItem(7, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tblAmvalList.setHorizontalHeaderItem(8, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tblAmvalList.setHorizontalHeaderItem(9, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tblAmvalList.setHorizontalHeaderItem(10, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tblAmvalList.setHorizontalHeaderItem(11, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tblAmvalList.setHorizontalHeaderItem(12, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tblAmvalList.setHorizontalHeaderItem(13, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tblAmvalList.setHorizontalHeaderItem(14, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tblAmvalList.setHorizontalHeaderItem(15, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tblAmvalList.setHorizontalHeaderItem(16, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tblAmvalList.setHorizontalHeaderItem(17, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tblAmvalList.setHorizontalHeaderItem(18, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tblAmvalList.setHorizontalHeaderItem(19, __qtablewidgetitem42)
        self.tblAmvalList.setObjectName(u"tblAmvalList")
        self.tblAmvalList.setMinimumSize(QSize(0, 250))
        self.tblAmvalList.setAlternatingRowColors(True)
        self.tblAmvalList.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblAmvalList.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tblAmvalList.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblAmvalList.setRowCount(0)
        self.tblAmvalList.setColumnCount(20)

        self.verticalLayoutAmval.addWidget(self.tblAmvalList)

        self.tabMain.addTab(self.tabAmval, "")
        self.tabHotel = QWidget()
        self.tabHotel.setObjectName(u"tabHotel")
        self.tabHotel.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.verticalLayoutHotel = QVBoxLayout(self.tabHotel)
        self.verticalLayoutHotel.setObjectName(u"verticalLayoutHotel")
        self.btnBackHomeHotel = QPushButton(self.tabHotel)
        self.btnBackHomeHotel.setObjectName(u"btnBackHomeHotel")
        self.btnBackHomeHotel.setMinimumSize(QSize(170, 36))

        self.verticalLayoutHotel.addWidget(self.btnBackHomeHotel)

        self.hotelSections = QTabWidget(self.tabHotel)
        self.hotelSections.setObjectName(u"hotelSections")
        self.hotelSections.setDocumentMode(True)
        self.hotelSections.setMovable(False)
        self.hotelSections.setTabPosition(QTabWidget.North)
        self.hotelRoomsPage = QWidget()
        self.hotelRoomsPage.setObjectName(u"hotelRoomsPage")
        self.hotelRoomsPageLayout = QVBoxLayout(self.hotelRoomsPage)
        self.hotelRoomsPageLayout.setSpacing(8)
        self.hotelRoomsPageLayout.setObjectName(u"hotelRoomsPageLayout")
        self.hotelRoomsPageLayout.setContentsMargins(8, 8, 8, 8)
        self.groupHotelSummary = QGroupBox(self.hotelRoomsPage)
        self.groupHotelSummary.setObjectName(u"groupHotelSummary")
        self.gridLayoutHotelSummary = QGridLayout(self.groupHotelSummary)
        self.gridLayoutHotelSummary.setObjectName(u"gridLayoutHotelSummary")
        self.lblHotelLaleh = QLabel(self.groupHotelSummary)
        self.lblHotelLaleh.setObjectName(u"lblHotelLaleh")
        self.lblHotelLaleh.setMinimumSize(QSize(0, 34))
        self.lblHotelLaleh.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayoutHotelSummary.addWidget(self.lblHotelLaleh, 0, 0, 1, 1)

        self.lblHotelLian = QLabel(self.groupHotelSummary)
        self.lblHotelLian.setObjectName(u"lblHotelLian")
        self.lblHotelLian.setMinimumSize(QSize(0, 34))
        self.lblHotelLian.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayoutHotelSummary.addWidget(self.lblHotelLian, 0, 1, 1, 1)

        self.lblHotelVacant = QLabel(self.groupHotelSummary)
        self.lblHotelVacant.setObjectName(u"lblHotelVacant")
        self.lblHotelVacant.setMinimumSize(QSize(0, 34))
        self.lblHotelVacant.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayoutHotelSummary.addWidget(self.lblHotelVacant, 0, 2, 1, 1)

        self.lblHotelOccupied = QLabel(self.groupHotelSummary)
        self.lblHotelOccupied.setObjectName(u"lblHotelOccupied")
        self.lblHotelOccupied.setMinimumSize(QSize(0, 34))
        self.lblHotelOccupied.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayoutHotelSummary.addWidget(self.lblHotelOccupied, 1, 0, 1, 1)

        self.lblHotelArrivals = QLabel(self.groupHotelSummary)
        self.lblHotelArrivals.setObjectName(u"lblHotelArrivals")
        self.lblHotelArrivals.setMinimumSize(QSize(0, 34))
        self.lblHotelArrivals.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayoutHotelSummary.addWidget(self.lblHotelArrivals, 1, 1, 1, 1)

        self.lblHotelDepartures = QLabel(self.groupHotelSummary)
        self.lblHotelDepartures.setObjectName(u"lblHotelDepartures")
        self.lblHotelDepartures.setMinimumSize(QSize(0, 34))
        self.lblHotelDepartures.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayoutHotelSummary.addWidget(self.lblHotelDepartures, 1, 2, 1, 1)


        self.hotelRoomsPageLayout.addWidget(self.groupHotelSummary)

        self.groupHotelRooms = QGroupBox(self.hotelRoomsPage)
        self.groupHotelRooms.setObjectName(u"groupHotelRooms")
        self.verticalLayoutHotelRooms = QVBoxLayout(self.groupHotelRooms)
        self.verticalLayoutHotelRooms.setObjectName(u"verticalLayoutHotelRooms")
        self.horizontalLayoutHotelBuilding = QHBoxLayout()
        self.horizontalLayoutHotelBuilding.setObjectName(u"horizontalLayoutHotelBuilding")
        self.btnHotelLaleh = QPushButton(self.groupHotelRooms)
        self.btnHotelLaleh.setObjectName(u"btnHotelLaleh")

        self.horizontalLayoutHotelBuilding.addWidget(self.btnHotelLaleh)

        self.btnHotelLian = QPushButton(self.groupHotelRooms)
        self.btnHotelLian.setObjectName(u"btnHotelLian")

        self.horizontalLayoutHotelBuilding.addWidget(self.btnHotelLian)

        self.btnHotelAll = QPushButton(self.groupHotelRooms)
        self.btnHotelAll.setObjectName(u"btnHotelAll")

        self.horizontalLayoutHotelBuilding.addWidget(self.btnHotelAll)


        self.verticalLayoutHotelRooms.addLayout(self.horizontalLayoutHotelBuilding)

        self.hotelRoomScroll = QScrollArea(self.groupHotelRooms)
        self.hotelRoomScroll.setObjectName(u"hotelRoomScroll")
        self.hotelRoomScroll.setWidgetResizable(True)
        self.hotelRoomScroll.setMinimumSize(QSize(0, 300))
        self.hotelRoomCardsHost = QWidget()
        self.hotelRoomCardsHost.setObjectName(u"hotelRoomCardsHost")
        self.hotelRoomCardsLayout = QGridLayout(self.hotelRoomCardsHost)
        self.hotelRoomCardsLayout.setSpacing(10)
        self.hotelRoomCardsLayout.setObjectName(u"hotelRoomCardsLayout")
        self.hotelRoomCardsLayout.setContentsMargins(6, 6, 6, 6)
        self.hotelRoomScroll.setWidget(self.hotelRoomCardsHost)

        self.verticalLayoutHotelRooms.addWidget(self.hotelRoomScroll)

        self.tblHotelRooms = QTableWidget(self.groupHotelRooms)
        if (self.tblHotelRooms.columnCount() < 8):
            self.tblHotelRooms.setColumnCount(8)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tblHotelRooms.setHorizontalHeaderItem(0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tblHotelRooms.setHorizontalHeaderItem(1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tblHotelRooms.setHorizontalHeaderItem(2, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tblHotelRooms.setHorizontalHeaderItem(3, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tblHotelRooms.setHorizontalHeaderItem(4, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tblHotelRooms.setHorizontalHeaderItem(5, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tblHotelRooms.setHorizontalHeaderItem(6, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tblHotelRooms.setHorizontalHeaderItem(7, __qtablewidgetitem50)
        self.tblHotelRooms.setObjectName(u"tblHotelRooms")
        self.tblHotelRooms.setMinimumSize(QSize(0, 175))
        self.tblHotelRooms.setAlternatingRowColors(True)
        self.tblHotelRooms.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblHotelRooms.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tblHotelRooms.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblHotelRooms.setColumnCount(8)
        self.tblHotelRooms.setRowCount(0)
        self.tblHotelRooms.setVisible(False)

        self.verticalLayoutHotelRooms.addWidget(self.tblHotelRooms)


        self.hotelRoomsPageLayout.addWidget(self.groupHotelRooms)

        self.hotelSections.addTab(self.hotelRoomsPage, "")
        self.hotelReceptionPage = QWidget()
        self.hotelReceptionPage.setObjectName(u"hotelReceptionPage")
        self.hotelReceptionPageLayout = QVBoxLayout(self.hotelReceptionPage)
        self.hotelReceptionPageLayout.setSpacing(8)
        self.hotelReceptionPageLayout.setObjectName(u"hotelReceptionPageLayout")
        self.hotelReceptionPageLayout.setContentsMargins(8, 8, 8, 8)
        self.groupHotelGuestForm = QGroupBox(self.hotelReceptionPage)
        self.groupHotelGuestForm.setObjectName(u"groupHotelGuestForm")
        self.gridLayoutHotelGuestForm = QGridLayout(self.groupHotelGuestForm)
        self.gridLayoutHotelGuestForm.setObjectName(u"gridLayoutHotelGuestForm")
        self.lblHotelNational = QLabel(self.groupHotelGuestForm)
        self.lblHotelNational.setObjectName(u"lblHotelNational")

        self.gridLayoutHotelGuestForm.addWidget(self.lblHotelNational, 0, 0, 1, 1)

        self.cmbHotelNational = QComboBox(self.groupHotelGuestForm)
        self.cmbHotelNational.setObjectName(u"cmbHotelNational")

        self.gridLayoutHotelGuestForm.addWidget(self.cmbHotelNational, 0, 1, 1, 1)

        self.lblHotelFirstName = QLabel(self.groupHotelGuestForm)
        self.lblHotelFirstName.setObjectName(u"lblHotelFirstName")

        self.gridLayoutHotelGuestForm.addWidget(self.lblHotelFirstName, 0, 2, 1, 1)

        self.txtHotelFirstName = QLineEdit(self.groupHotelGuestForm)
        self.txtHotelFirstName.setObjectName(u"txtHotelFirstName")

        self.gridLayoutHotelGuestForm.addWidget(self.txtHotelFirstName, 0, 3, 1, 1)

        self.lblHotelLastName = QLabel(self.groupHotelGuestForm)
        self.lblHotelLastName.setObjectName(u"lblHotelLastName")

        self.gridLayoutHotelGuestForm.addWidget(self.lblHotelLastName, 0, 4, 1, 1)

        self.txtHotelLastName = QLineEdit(self.groupHotelGuestForm)
        self.txtHotelLastName.setObjectName(u"txtHotelLastName")

        self.gridLayoutHotelGuestForm.addWidget(self.txtHotelLastName, 0, 5, 1, 1)

        self.lblHotelOrg = QLabel(self.groupHotelGuestForm)
        self.lblHotelOrg.setObjectName(u"lblHotelOrg")

        self.gridLayoutHotelGuestForm.addWidget(self.lblHotelOrg, 0, 6, 1, 1)

        self.cmbHotelOrg = QComboBox(self.groupHotelGuestForm)
        self.cmbHotelOrg.setObjectName(u"cmbHotelOrg")

        self.gridLayoutHotelGuestForm.addWidget(self.cmbHotelOrg, 0, 7, 1, 1)

        self.lblHotelPeople = QLabel(self.groupHotelGuestForm)
        self.lblHotelPeople.setObjectName(u"lblHotelPeople")

        self.gridLayoutHotelGuestForm.addWidget(self.lblHotelPeople, 0, 8, 1, 1)

        self.txtHotelPeople = QLineEdit(self.groupHotelGuestForm)
        self.txtHotelPeople.setObjectName(u"txtHotelPeople")

        self.gridLayoutHotelGuestForm.addWidget(self.txtHotelPeople, 0, 9, 1, 1)

        self.lblHotelBuilding = QLabel(self.groupHotelGuestForm)
        self.lblHotelBuilding.setObjectName(u"lblHotelBuilding")

        self.gridLayoutHotelGuestForm.addWidget(self.lblHotelBuilding, 1, 0, 1, 1)

        self.cmbHotelBuilding = QComboBox(self.groupHotelGuestForm)
        self.cmbHotelBuilding.setObjectName(u"cmbHotelBuilding")

        self.gridLayoutHotelGuestForm.addWidget(self.cmbHotelBuilding, 1, 1, 1, 1)

        self.lblHotelRoom = QLabel(self.groupHotelGuestForm)
        self.lblHotelRoom.setObjectName(u"lblHotelRoom")

        self.gridLayoutHotelGuestForm.addWidget(self.lblHotelRoom, 1, 2, 1, 1)

        self.cmbHotelRoom = QComboBox(self.groupHotelGuestForm)
        self.cmbHotelRoom.setObjectName(u"cmbHotelRoom")

        self.gridLayoutHotelGuestForm.addWidget(self.cmbHotelRoom, 1, 3, 1, 1)

        self.lblHotelArrival = QLabel(self.groupHotelGuestForm)
        self.lblHotelArrival.setObjectName(u"lblHotelArrival")

        self.gridLayoutHotelGuestForm.addWidget(self.lblHotelArrival, 1, 4, 1, 1)

        self.txtHotelArrival = QLineEdit(self.groupHotelGuestForm)
        self.txtHotelArrival.setObjectName(u"txtHotelArrival")

        self.gridLayoutHotelGuestForm.addWidget(self.txtHotelArrival, 1, 5, 1, 1)

        self.lblHotelDeparture = QLabel(self.groupHotelGuestForm)
        self.lblHotelDeparture.setObjectName(u"lblHotelDeparture")

        self.gridLayoutHotelGuestForm.addWidget(self.lblHotelDeparture, 1, 6, 1, 1)

        self.txtHotelDeparture = QLineEdit(self.groupHotelGuestForm)
        self.txtHotelDeparture.setObjectName(u"txtHotelDeparture")

        self.gridLayoutHotelGuestForm.addWidget(self.txtHotelDeparture, 1, 7, 1, 1)

        self.lblHotelEmployee = QLabel(self.groupHotelGuestForm)
        self.lblHotelEmployee.setObjectName(u"lblHotelEmployee")

        self.gridLayoutHotelGuestForm.addWidget(self.lblHotelEmployee, 1, 8, 1, 1)

        self.txtHotelEmployee = QLineEdit(self.groupHotelGuestForm)
        self.txtHotelEmployee.setObjectName(u"txtHotelEmployee")

        self.gridLayoutHotelGuestForm.addWidget(self.txtHotelEmployee, 1, 9, 1, 1)

        self.chkHotelBreakfast = QCheckBox(self.groupHotelGuestForm)
        self.chkHotelBreakfast.setObjectName(u"chkHotelBreakfast")

        self.gridLayoutHotelGuestForm.addWidget(self.chkHotelBreakfast, 2, 0, 1, 2)

        self.chkHotelLunch = QCheckBox(self.groupHotelGuestForm)
        self.chkHotelLunch.setObjectName(u"chkHotelLunch")

        self.gridLayoutHotelGuestForm.addWidget(self.chkHotelLunch, 2, 2, 1, 2)

        self.chkHotelDinner = QCheckBox(self.groupHotelGuestForm)
        self.chkHotelDinner.setObjectName(u"chkHotelDinner")

        self.gridLayoutHotelGuestForm.addWidget(self.chkHotelDinner, 2, 4, 1, 2)

        self.lblHotelActualArrival = QLabel(self.groupHotelGuestForm)
        self.lblHotelActualArrival.setObjectName(u"lblHotelActualArrival")

        self.gridLayoutHotelGuestForm.addWidget(self.lblHotelActualArrival, 3, 2, 1, 1)

        self.txtHotelActualArrival = QLineEdit(self.groupHotelGuestForm)
        self.txtHotelActualArrival.setObjectName(u"txtHotelActualArrival")
        self.txtHotelActualArrival.setClearButtonEnabled(True)

        self.gridLayoutHotelGuestForm.addWidget(self.txtHotelActualArrival, 3, 3, 1, 1)

        self.lblHotelActualDeparture = QLabel(self.groupHotelGuestForm)
        self.lblHotelActualDeparture.setObjectName(u"lblHotelActualDeparture")

        self.gridLayoutHotelGuestForm.addWidget(self.lblHotelActualDeparture, 4, 2, 1, 1)

        self.txtHotelActualDeparture = QLineEdit(self.groupHotelGuestForm)
        self.txtHotelActualDeparture.setObjectName(u"txtHotelActualDeparture")
        self.txtHotelActualDeparture.setClearButtonEnabled(True)

        self.gridLayoutHotelGuestForm.addWidget(self.txtHotelActualDeparture, 4, 3, 1, 1)


        self.hotelReceptionPageLayout.addWidget(self.groupHotelGuestForm)

        self.horizontalLayoutHotelActions = QHBoxLayout()
        self.horizontalLayoutHotelActions.setObjectName(u"horizontalLayoutHotelActions")
        self.btnHotelNew = QPushButton(self.hotelReceptionPage)
        self.btnHotelNew.setObjectName(u"btnHotelNew")

        self.horizontalLayoutHotelActions.addWidget(self.btnHotelNew)

        self.btnHotelEdit = QPushButton(self.hotelReceptionPage)
        self.btnHotelEdit.setObjectName(u"btnHotelEdit")

        self.horizontalLayoutHotelActions.addWidget(self.btnHotelEdit)

        self.btnHotelExtendStay = QPushButton(self.hotelReceptionPage)
        self.btnHotelExtendStay.setObjectName(u"btnHotelExtendStay")

        self.horizontalLayoutHotelActions.addWidget(self.btnHotelExtendStay)

        self.btnHotelSave = QPushButton(self.hotelReceptionPage)
        self.btnHotelSave.setObjectName(u"btnHotelSave")

        self.horizontalLayoutHotelActions.addWidget(self.btnHotelSave)

        self.btnHotelCheckIn = QPushButton(self.hotelReceptionPage)
        self.btnHotelCheckIn.setObjectName(u"btnHotelCheckIn")

        self.horizontalLayoutHotelActions.addWidget(self.btnHotelCheckIn)

        self.btnHotelCheckOut = QPushButton(self.hotelReceptionPage)
        self.btnHotelCheckOut.setObjectName(u"btnHotelCheckOut")

        self.horizontalLayoutHotelActions.addWidget(self.btnHotelCheckOut)

        self.btnHotelRefresh = QPushButton(self.hotelReceptionPage)
        self.btnHotelRefresh.setObjectName(u"btnHotelRefresh")

        self.horizontalLayoutHotelActions.addWidget(self.btnHotelRefresh)


        self.hotelReceptionPageLayout.addLayout(self.horizontalLayoutHotelActions)

        self.hotelSections.addTab(self.hotelReceptionPage, "")
        self.hotelMovementsPage = QWidget()
        self.hotelMovementsPage.setObjectName(u"hotelMovementsPage")
        self.hotelMovementsPageLayout = QVBoxLayout(self.hotelMovementsPage)
        self.hotelMovementsPageLayout.setSpacing(8)
        self.hotelMovementsPageLayout.setObjectName(u"hotelMovementsPageLayout")
        self.hotelMovementsPageLayout.setContentsMargins(8, 8, 8, 8)
        self.lblHotelMovementInfo = QLabel(self.hotelMovementsPage)
        self.lblHotelMovementInfo.setObjectName(u"lblHotelMovementInfo")

        self.hotelMovementsPageLayout.addWidget(self.lblHotelMovementInfo)

        self.tblHotelToday = QTableWidget(self.hotelMovementsPage)
        if (self.tblHotelToday.columnCount() < 7):
            self.tblHotelToday.setColumnCount(7)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tblHotelToday.setHorizontalHeaderItem(0, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tblHotelToday.setHorizontalHeaderItem(1, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tblHotelToday.setHorizontalHeaderItem(2, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tblHotelToday.setHorizontalHeaderItem(3, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tblHotelToday.setHorizontalHeaderItem(4, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tblHotelToday.setHorizontalHeaderItem(5, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tblHotelToday.setHorizontalHeaderItem(6, __qtablewidgetitem57)
        self.tblHotelToday.setObjectName(u"tblHotelToday")
        self.tblHotelToday.setMinimumSize(QSize(0, 250))
        self.tblHotelToday.setColumnCount(7)
        self.tblHotelToday.setRowCount(0)

        self.hotelMovementsPageLayout.addWidget(self.tblHotelToday)

        self.hotelSections.addTab(self.hotelMovementsPage, "")
        self.hotelHistoryPage = QWidget()
        self.hotelHistoryPage.setObjectName(u"hotelHistoryPage")
        self.hotelHistoryPageLayout = QVBoxLayout(self.hotelHistoryPage)
        self.hotelHistoryPageLayout.setSpacing(8)
        self.hotelHistoryPageLayout.setObjectName(u"hotelHistoryPageLayout")
        self.hotelHistoryPageLayout.setContentsMargins(8, 8, 8, 8)
        self.groupHotelHistory = QGroupBox(self.hotelHistoryPage)
        self.groupHotelHistory.setObjectName(u"groupHotelHistory")
        self.verticalLayoutHotelHistory = QVBoxLayout(self.groupHotelHistory)
        self.verticalLayoutHotelHistory.setObjectName(u"verticalLayoutHotelHistory")
        self.tblHotelHistory = QTableWidget(self.groupHotelHistory)
        if (self.tblHotelHistory.columnCount() < 11):
            self.tblHotelHistory.setColumnCount(11)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tblHotelHistory.setHorizontalHeaderItem(0, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tblHotelHistory.setHorizontalHeaderItem(1, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tblHotelHistory.setHorizontalHeaderItem(2, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tblHotelHistory.setHorizontalHeaderItem(3, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tblHotelHistory.setHorizontalHeaderItem(4, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tblHotelHistory.setHorizontalHeaderItem(5, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tblHotelHistory.setHorizontalHeaderItem(6, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tblHotelHistory.setHorizontalHeaderItem(7, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tblHotelHistory.setHorizontalHeaderItem(8, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tblHotelHistory.setHorizontalHeaderItem(9, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tblHotelHistory.setHorizontalHeaderItem(10, __qtablewidgetitem68)
        self.tblHotelHistory.setObjectName(u"tblHotelHistory")
        self.tblHotelHistory.setMinimumSize(QSize(0, 150))
        self.tblHotelHistory.setAlternatingRowColors(True)
        self.tblHotelHistory.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblHotelHistory.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tblHotelHistory.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblHotelHistory.setColumnCount(11)
        self.tblHotelHistory.setRowCount(0)

        self.verticalLayoutHotelHistory.addWidget(self.tblHotelHistory)


        self.hotelHistoryPageLayout.addWidget(self.groupHotelHistory)

        self.horizontalLayoutHotelSearch = QHBoxLayout()
        self.horizontalLayoutHotelSearch.setObjectName(u"horizontalLayoutHotelSearch")
        self.lblHotelSearch = QLabel(self.hotelHistoryPage)
        self.lblHotelSearch.setObjectName(u"lblHotelSearch")

        self.horizontalLayoutHotelSearch.addWidget(self.lblHotelSearch)

        self.txtHotelSearch = QLineEdit(self.hotelHistoryPage)
        self.txtHotelSearch.setObjectName(u"txtHotelSearch")

        self.horizontalLayoutHotelSearch.addWidget(self.txtHotelSearch)


        self.hotelHistoryPageLayout.addLayout(self.horizontalLayoutHotelSearch)

        self.hotelSections.addTab(self.hotelHistoryPage, "")

        self.verticalLayoutHotel.addWidget(self.hotelSections)

        self.tabMain.addTab(self.tabHotel, "")
        self.tabAnbarTahrir = QWidget()
        self.tabAnbarTahrir.setObjectName(u"tabAnbarTahrir")
        self.tabAnbarTahrir.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.verticalLayoutAnbarTahrir = QVBoxLayout(self.tabAnbarTahrir)
        self.verticalLayoutAnbarTahrir.setObjectName(u"verticalLayoutAnbarTahrir")
        self.btnBackHomeAnbarTahrir = QPushButton(self.tabAnbarTahrir)
        self.btnBackHomeAnbarTahrir.setObjectName(u"btnBackHomeAnbarTahrir")
        self.btnBackHomeAnbarTahrir.setMinimumSize(QSize(170, 36))

        self.verticalLayoutAnbarTahrir.addWidget(self.btnBackHomeAnbarTahrir, 0, Qt.AlignmentFlag.AlignRight)

        self.groupAnbarTahrirSearch = QGroupBox(self.tabAnbarTahrir)
        self.groupAnbarTahrirSearch.setObjectName(u"groupAnbarTahrirSearch")
        self.gridAnbarTahrirSearch = QGridLayout(self.groupAnbarTahrirSearch)
        self.gridAnbarTahrirSearch.setObjectName(u"gridAnbarTahrirSearch")
        self.lblAnbarTahrirSearch = QLabel(self.groupAnbarTahrirSearch)
        self.lblAnbarTahrirSearch.setObjectName(u"lblAnbarTahrirSearch")

        self.gridAnbarTahrirSearch.addWidget(self.lblAnbarTahrirSearch, 0, 0, 1, 1)

        self.txtAnbarTahrirSearch = QLineEdit(self.groupAnbarTahrirSearch)
        self.txtAnbarTahrirSearch.setObjectName(u"txtAnbarTahrirSearch")

        self.gridAnbarTahrirSearch.addWidget(self.txtAnbarTahrirSearch, 0, 1, 1, 3)

        self.lblAnbarTahrirDescription = QLabel(self.groupAnbarTahrirSearch)
        self.lblAnbarTahrirDescription.setObjectName(u"lblAnbarTahrirDescription")

        self.gridAnbarTahrirSearch.addWidget(self.lblAnbarTahrirDescription, 1, 0, 1, 1)

        self.txtAnbarTahrirDescription = QLineEdit(self.groupAnbarTahrirSearch)
        self.txtAnbarTahrirDescription.setObjectName(u"txtAnbarTahrirDescription")

        self.gridAnbarTahrirSearch.addWidget(self.txtAnbarTahrirDescription, 1, 1, 1, 1)

        self.lblAnbarTahrirQty = QLabel(self.groupAnbarTahrirSearch)
        self.lblAnbarTahrirQty.setObjectName(u"lblAnbarTahrirQty")

        self.gridAnbarTahrirSearch.addWidget(self.lblAnbarTahrirQty, 1, 2, 1, 1)

        self.txtAnbarTahrirQty = QLineEdit(self.groupAnbarTahrirSearch)
        self.txtAnbarTahrirQty.setObjectName(u"txtAnbarTahrirQty")

        self.gridAnbarTahrirSearch.addWidget(self.txtAnbarTahrirQty, 1, 3, 1, 1)

        self.lblAnbarTahrirUnit = QLabel(self.groupAnbarTahrirSearch)
        self.lblAnbarTahrirUnit.setObjectName(u"lblAnbarTahrirUnit")

        self.gridAnbarTahrirSearch.addWidget(self.lblAnbarTahrirUnit, 1, 4, 1, 1)

        self.txtAnbarTahrirUnit = QLineEdit(self.groupAnbarTahrirSearch)
        self.txtAnbarTahrirUnit.setObjectName(u"txtAnbarTahrirUnit")

        self.gridAnbarTahrirSearch.addWidget(self.txtAnbarTahrirUnit, 1, 5, 1, 1)


        self.verticalLayoutAnbarTahrir.addWidget(self.groupAnbarTahrirSearch)

        self.horizontalLayoutAnbarTahrirActions = QHBoxLayout()
        self.horizontalLayoutAnbarTahrirActions.setObjectName(u"horizontalLayoutAnbarTahrirActions")
        self.btnAnbarTahrirNew = QPushButton(self.tabAnbarTahrir)
        self.btnAnbarTahrirNew.setObjectName(u"btnAnbarTahrirNew")

        self.horizontalLayoutAnbarTahrirActions.addWidget(self.btnAnbarTahrirNew)

        self.btnAnbarTahrirSave = QPushButton(self.tabAnbarTahrir)
        self.btnAnbarTahrirSave.setObjectName(u"btnAnbarTahrirSave")

        self.horizontalLayoutAnbarTahrirActions.addWidget(self.btnAnbarTahrirSave)

        self.btnAnbarTahrirEdit = QPushButton(self.tabAnbarTahrir)
        self.btnAnbarTahrirEdit.setObjectName(u"btnAnbarTahrirEdit")

        self.horizontalLayoutAnbarTahrirActions.addWidget(self.btnAnbarTahrirEdit)

        self.btnAnbarTahrirDelete = QPushButton(self.tabAnbarTahrir)
        self.btnAnbarTahrirDelete.setObjectName(u"btnAnbarTahrirDelete")

        self.horizontalLayoutAnbarTahrirActions.addWidget(self.btnAnbarTahrirDelete)

        self.btnAnbarTahrirRefresh = QPushButton(self.tabAnbarTahrir)
        self.btnAnbarTahrirRefresh.setObjectName(u"btnAnbarTahrirRefresh")

        self.horizontalLayoutAnbarTahrirActions.addWidget(self.btnAnbarTahrirRefresh)


        self.verticalLayoutAnbarTahrir.addLayout(self.horizontalLayoutAnbarTahrirActions)

        self.tblAnbarTahrirList = QTableWidget(self.tabAnbarTahrir)
        if (self.tblAnbarTahrirList.columnCount() < 4):
            self.tblAnbarTahrirList.setColumnCount(4)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tblAnbarTahrirList.setHorizontalHeaderItem(0, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tblAnbarTahrirList.setHorizontalHeaderItem(1, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.tblAnbarTahrirList.setHorizontalHeaderItem(2, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.tblAnbarTahrirList.setHorizontalHeaderItem(3, __qtablewidgetitem72)
        self.tblAnbarTahrirList.setObjectName(u"tblAnbarTahrirList")
        self.tblAnbarTahrirList.setColumnCount(4)
        self.tblAnbarTahrirList.setRowCount(0)

        self.verticalLayoutAnbarTahrir.addWidget(self.tblAnbarTahrirList)

        self.tabMain.addTab(self.tabAnbarTahrir, "")
        self.tabMtoTahrir = QWidget()
        self.tabMtoTahrir.setObjectName(u"tabMtoTahrir")
        self.tabMtoTahrir.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.verticalLayoutMtoTahrir = QVBoxLayout(self.tabMtoTahrir)
        self.verticalLayoutMtoTahrir.setObjectName(u"verticalLayoutMtoTahrir")
        self.btnBackHomeMtoTahrir = QPushButton(self.tabMtoTahrir)
        self.btnBackHomeMtoTahrir.setObjectName(u"btnBackHomeMtoTahrir")
        self.btnBackHomeMtoTahrir.setMinimumSize(QSize(170, 36))

        self.verticalLayoutMtoTahrir.addWidget(self.btnBackHomeMtoTahrir, 0, Qt.AlignmentFlag.AlignRight)

        self.groupMtoTahrirFilters = QGroupBox(self.tabMtoTahrir)
        self.groupMtoTahrirFilters.setObjectName(u"groupMtoTahrirFilters")
        self.gridMtoTahrirFilters = QGridLayout(self.groupMtoTahrirFilters)
        self.gridMtoTahrirFilters.setObjectName(u"gridMtoTahrirFilters")
        self.lblMtoTahrirSearch = QLabel(self.groupMtoTahrirFilters)
        self.lblMtoTahrirSearch.setObjectName(u"lblMtoTahrirSearch")

        self.gridMtoTahrirFilters.addWidget(self.lblMtoTahrirSearch, 0, 0, 1, 1)

        self.txtMtoTahrirSearch = QLineEdit(self.groupMtoTahrirFilters)
        self.txtMtoTahrirSearch.setObjectName(u"txtMtoTahrirSearch")

        self.gridMtoTahrirFilters.addWidget(self.txtMtoTahrirSearch, 0, 1, 1, 5)

        self.lblMtoTahrirFromDate = QLabel(self.groupMtoTahrirFilters)
        self.lblMtoTahrirFromDate.setObjectName(u"lblMtoTahrirFromDate")

        self.gridMtoTahrirFilters.addWidget(self.lblMtoTahrirFromDate, 1, 0, 1, 1)

        self.txtMtoTahrirFromDate = QLineEdit(self.groupMtoTahrirFilters)
        self.txtMtoTahrirFromDate.setObjectName(u"txtMtoTahrirFromDate")

        self.gridMtoTahrirFilters.addWidget(self.txtMtoTahrirFromDate, 1, 1, 1, 1)

        self.lblMtoTahrirToDate = QLabel(self.groupMtoTahrirFilters)
        self.lblMtoTahrirToDate.setObjectName(u"lblMtoTahrirToDate")

        self.gridMtoTahrirFilters.addWidget(self.lblMtoTahrirToDate, 1, 2, 1, 1)

        self.txtMtoTahrirToDate = QLineEdit(self.groupMtoTahrirFilters)
        self.txtMtoTahrirToDate.setObjectName(u"txtMtoTahrirToDate")

        self.gridMtoTahrirFilters.addWidget(self.txtMtoTahrirToDate, 1, 3, 1, 1)


        self.verticalLayoutMtoTahrir.addWidget(self.groupMtoTahrirFilters)

        self.groupMtoTahrirInfo = QGroupBox(self.tabMtoTahrir)
        self.groupMtoTahrirInfo.setObjectName(u"groupMtoTahrirInfo")
        self.gridMtoTahrirInfo = QGridLayout(self.groupMtoTahrirInfo)
        self.gridMtoTahrirInfo.setObjectName(u"gridMtoTahrirInfo")
        self.lblMtoTahrirDate = QLabel(self.groupMtoTahrirInfo)
        self.lblMtoTahrirDate.setObjectName(u"lblMtoTahrirDate")

        self.gridMtoTahrirInfo.addWidget(self.lblMtoTahrirDate, 0, 0, 1, 1)

        self.txtMtoTahrirDate = QLineEdit(self.groupMtoTahrirInfo)
        self.txtMtoTahrirDate.setObjectName(u"txtMtoTahrirDate")

        self.gridMtoTahrirInfo.addWidget(self.txtMtoTahrirDate, 0, 1, 1, 1)

        self.lblMtoTahrirDescription = QLabel(self.groupMtoTahrirInfo)
        self.lblMtoTahrirDescription.setObjectName(u"lblMtoTahrirDescription")

        self.gridMtoTahrirInfo.addWidget(self.lblMtoTahrirDescription, 0, 2, 1, 1)

        self.txtMtoTahrirDescription = QLineEdit(self.groupMtoTahrirInfo)
        self.txtMtoTahrirDescription.setObjectName(u"txtMtoTahrirDescription")

        self.gridMtoTahrirInfo.addWidget(self.txtMtoTahrirDescription, 0, 3, 1, 5)

        self.lblMtoTahrirQty = QLabel(self.groupMtoTahrirInfo)
        self.lblMtoTahrirQty.setObjectName(u"lblMtoTahrirQty")

        self.gridMtoTahrirInfo.addWidget(self.lblMtoTahrirQty, 1, 0, 1, 1)

        self.txtMtoTahrirQty = QLineEdit(self.groupMtoTahrirInfo)
        self.txtMtoTahrirQty.setObjectName(u"txtMtoTahrirQty")

        self.gridMtoTahrirInfo.addWidget(self.txtMtoTahrirQty, 1, 1, 1, 1)

        self.lblMtoTahrirUnit = QLabel(self.groupMtoTahrirInfo)
        self.lblMtoTahrirUnit.setObjectName(u"lblMtoTahrirUnit")

        self.gridMtoTahrirInfo.addWidget(self.lblMtoTahrirUnit, 1, 2, 1, 1)

        self.txtMtoTahrirUnit = QLineEdit(self.groupMtoTahrirInfo)
        self.txtMtoTahrirUnit.setObjectName(u"txtMtoTahrirUnit")

        self.gridMtoTahrirInfo.addWidget(self.txtMtoTahrirUnit, 1, 3, 1, 1)

        self.lblMtoTahrirVahed = QLabel(self.groupMtoTahrirInfo)
        self.lblMtoTahrirVahed.setObjectName(u"lblMtoTahrirVahed")

        self.gridMtoTahrirInfo.addWidget(self.lblMtoTahrirVahed, 1, 4, 1, 1)

        self.cmbMtoTahrirVahed = QComboBox(self.groupMtoTahrirInfo)
        self.cmbMtoTahrirVahed.setObjectName(u"cmbMtoTahrirVahed")
        self.cmbMtoTahrirVahed.setEditable(True)
        self.cmbMtoTahrirVahed.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)

        self.gridMtoTahrirInfo.addWidget(self.cmbMtoTahrirVahed, 1, 5, 1, 1)

        self.lblMtoTahrirRecorder = QLabel(self.groupMtoTahrirInfo)
        self.lblMtoTahrirRecorder.setObjectName(u"lblMtoTahrirRecorder")

        self.gridMtoTahrirInfo.addWidget(self.lblMtoTahrirRecorder, 2, 0, 1, 1)

        self.txtMtoTahrirRecorder = QLineEdit(self.groupMtoTahrirInfo)
        self.txtMtoTahrirRecorder.setObjectName(u"txtMtoTahrirRecorder")

        self.gridMtoTahrirInfo.addWidget(self.txtMtoTahrirRecorder, 2, 1, 1, 1)

        self.lblMtoTahrirTaeidkonandeh = QLabel(self.groupMtoTahrirInfo)
        self.lblMtoTahrirTaeidkonandeh.setObjectName(u"lblMtoTahrirTaeidkonandeh")

        self.gridMtoTahrirInfo.addWidget(self.lblMtoTahrirTaeidkonandeh, 2, 2, 1, 1)

        self.cmbMtoTahrirTaeidkonandeh = QComboBox(self.groupMtoTahrirInfo)
        self.cmbMtoTahrirTaeidkonandeh.setObjectName(u"cmbMtoTahrirTaeidkonandeh")
        self.cmbMtoTahrirTaeidkonandeh.setEditable(True)
        self.cmbMtoTahrirTaeidkonandeh.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)

        self.gridMtoTahrirInfo.addWidget(self.cmbMtoTahrirTaeidkonandeh, 2, 3, 1, 1)

        self.lblMtoTahrirEditor = QLabel(self.groupMtoTahrirInfo)
        self.lblMtoTahrirEditor.setObjectName(u"lblMtoTahrirEditor")

        self.gridMtoTahrirInfo.addWidget(self.lblMtoTahrirEditor, 2, 4, 1, 1)

        self.txtMtoTahrirEditor = QLineEdit(self.groupMtoTahrirInfo)
        self.txtMtoTahrirEditor.setObjectName(u"txtMtoTahrirEditor")

        self.gridMtoTahrirInfo.addWidget(self.txtMtoTahrirEditor, 2, 5, 1, 1)

        self.lblMtoTahrirTahvilGirandeh = QLabel(self.groupMtoTahrirInfo)
        self.lblMtoTahrirTahvilGirandeh.setObjectName(u"lblMtoTahrirTahvilGirandeh")

        self.gridMtoTahrirInfo.addWidget(self.lblMtoTahrirTahvilGirandeh, 2, 6, 1, 1)

        self.cmbMtoTahrirTahvilgirandeh = QComboBox(self.groupMtoTahrirInfo)
        self.cmbMtoTahrirTahvilgirandeh.setObjectName(u"cmbMtoTahrirTahvilgirandeh")
        self.cmbMtoTahrirTahvilgirandeh.setEditable(True)
        self.cmbMtoTahrirTahvilgirandeh.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)

        self.gridMtoTahrirInfo.addWidget(self.cmbMtoTahrirTahvilgirandeh, 2, 7, 1, 1)


        self.verticalLayoutMtoTahrir.addWidget(self.groupMtoTahrirInfo)

        self.horizontalLayoutMtoTahrirActions = QHBoxLayout()
        self.horizontalLayoutMtoTahrirActions.setObjectName(u"horizontalLayoutMtoTahrirActions")
        self.btnMtoTahrirNew = QPushButton(self.tabMtoTahrir)
        self.btnMtoTahrirNew.setObjectName(u"btnMtoTahrirNew")

        self.horizontalLayoutMtoTahrirActions.addWidget(self.btnMtoTahrirNew)

        self.btnMtoTahrirSave = QPushButton(self.tabMtoTahrir)
        self.btnMtoTahrirSave.setObjectName(u"btnMtoTahrirSave")

        self.horizontalLayoutMtoTahrirActions.addWidget(self.btnMtoTahrirSave)

        self.btnMtoTahrirEdit = QPushButton(self.tabMtoTahrir)
        self.btnMtoTahrirEdit.setObjectName(u"btnMtoTahrirEdit")

        self.horizontalLayoutMtoTahrirActions.addWidget(self.btnMtoTahrirEdit)

        self.btnMtoTahrirDelete = QPushButton(self.tabMtoTahrir)
        self.btnMtoTahrirDelete.setObjectName(u"btnMtoTahrirDelete")

        self.horizontalLayoutMtoTahrirActions.addWidget(self.btnMtoTahrirDelete)

        self.btnMtoTahrirDeliver = QPushButton(self.tabMtoTahrir)
        self.btnMtoTahrirDeliver.setObjectName(u"btnMtoTahrirDeliver")

        self.horizontalLayoutMtoTahrirActions.addWidget(self.btnMtoTahrirDeliver)

        self.btnMtoTahrirRefresh = QPushButton(self.tabMtoTahrir)
        self.btnMtoTahrirRefresh.setObjectName(u"btnMtoTahrirRefresh")

        self.horizontalLayoutMtoTahrirActions.addWidget(self.btnMtoTahrirRefresh)


        self.verticalLayoutMtoTahrir.addLayout(self.horizontalLayoutMtoTahrirActions)

        self.tblMtoTahrirList = QTableWidget(self.tabMtoTahrir)
        if (self.tblMtoTahrirList.columnCount() < 9):
            self.tblMtoTahrirList.setColumnCount(9)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.tblMtoTahrirList.setHorizontalHeaderItem(0, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tblMtoTahrirList.setHorizontalHeaderItem(1, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.tblMtoTahrirList.setHorizontalHeaderItem(2, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.tblMtoTahrirList.setHorizontalHeaderItem(3, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.tblMtoTahrirList.setHorizontalHeaderItem(4, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.tblMtoTahrirList.setHorizontalHeaderItem(5, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.tblMtoTahrirList.setHorizontalHeaderItem(6, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tblMtoTahrirList.setHorizontalHeaderItem(7, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tblMtoTahrirList.setHorizontalHeaderItem(8, __qtablewidgetitem81)
        self.tblMtoTahrirList.setObjectName(u"tblMtoTahrirList")
        self.tblMtoTahrirList.setColumnCount(9)
        self.tblMtoTahrirList.setRowCount(0)

        self.verticalLayoutMtoTahrir.addWidget(self.tblMtoTahrirList)

        self.tabMain.addTab(self.tabMtoTahrir, "")

        self.horizontalLayoutApplication.addWidget(self.tabMain)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 22))
        self.menuSystem = QMenu(self.menubar)
        self.menuSystem.setObjectName(u"menuSystem")
        self.menuUsers = QMenu(self.menubar)
        self.menuUsers.setObjectName(u"menuUsers")
        self.menuRepairs = QMenu(self.menubar)
        self.menuRepairs.setObjectName(u"menuRepairs")
        self.menuEquipment = QMenu(self.menubar)
        self.menuEquipment.setObjectName(u"menuEquipment")
        self.menuStationery = QMenu(self.menubar)
        self.menuStationery.setObjectName(u"menuStationery")
        self.menuReports = QMenu(self.menubar)
        self.menuReports.setObjectName(u"menuReports")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.lblStatusUser = QLabel(self.statusBar)
        self.lblStatusUser.setObjectName(u"lblStatusUser")
        self.lblStatusUser.setMinimumSize(QSize(145, 27))
        self.lblStatusUser.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStatusUnit = QLabel(self.statusBar)
        self.lblStatusUnit.setObjectName(u"lblStatusUnit")
        self.lblStatusUnit.setMinimumSize(QSize(165, 27))
        self.lblStatusUnit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStatusSecurity = QLabel(self.statusBar)
        self.lblStatusSecurity.setObjectName(u"lblStatusSecurity")
        self.lblStatusSecurity.setMinimumSize(QSize(135, 27))
        self.lblStatusSecurity.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStatusLevel = QLabel(self.statusBar)
        self.lblStatusLevel.setObjectName(u"lblStatusLevel")
        self.lblStatusLevel.setMinimumSize(QSize(125, 27))
        self.lblStatusLevel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStatusWeekday = QLabel(self.statusBar)
        self.lblStatusWeekday.setObjectName(u"lblStatusWeekday")
        self.lblStatusWeekday.setMinimumSize(QSize(85, 27))
        self.lblStatusWeekday.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStatusDate = QLabel(self.statusBar)
        self.lblStatusDate.setObjectName(u"lblStatusDate")
        self.lblStatusDate.setMinimumSize(QSize(105, 27))
        self.lblStatusDate.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblStatusTime = QLabel(self.statusBar)
        self.lblStatusTime.setObjectName(u"lblStatusTime")
        self.lblStatusTime.setMinimumSize(QSize(100, 27))
        self.lblStatusTime.setAlignment(Qt.AlignmentFlag.AlignCenter)
        MainWindow.setStatusBar(self.statusBar)

        self.menubar.addAction(self.menuSystem.menuAction())
        self.menubar.addAction(self.menuUsers.menuAction())
        self.menubar.addAction(self.menuRepairs.menuAction())
        self.menubar.addAction(self.menuEquipment.menuAction())
        self.menubar.addAction(self.menuStationery.menuAction())
        self.menubar.addAction(self.menuReports.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuSystem.addAction(self.actionHome)
        self.menuSystem.addAction(self.actionPassword)
        self.menuSystem.addSeparator()
        self.menuSystem.addAction(self.actionExit)
        self.menuUsers.addAction(self.actionUserManagement)
        self.menuRepairs.addAction(self.actionRepairsRequest)
        self.menuRepairs.addAction(self.actionRepairsHistory)
        self.menuEquipment.addAction(self.actionEquipmentList)
        self.menuEquipment.addAction(self.actionAssets)
        self.menuStationery.addAction(self.actionAnbarTahrir)
        self.menuStationery.addAction(self.actionMtoTahrir)
        self.menuReports.addAction(self.actionReportRepairs)
        self.menuReports.addAction(self.actionReportEquipment)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.tabMain.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0633\u06cc\u0633\u062a\u0645 \u0645\u062f\u06cc\u0631\u06cc\u062a \u062f\u0631\u062e\u0648\u0627\u0633\u062a\u200c\u0647\u0627\u06cc \u062a\u0639\u0645\u06cc\u0631\u0627\u062a", None))
        MainWindow.setStyleSheet(QCoreApplication.translate("MainWindow", u"QFrame#navigationPanel { background: #F1F5F9; border: 1px solid #D7E0EA; border-radius: 8px; }\n"
"QFrame#navigationPanel QLabel { color: #243447; font-size: 11pt; }\n"
"QPushButton { min-height: 38px; padding: 5px 8px; border: 1px solid #C7D0DB; border-radius: 5px; background: white; color: #263445; font-size: 11pt; }\n"
"QPushButton:hover { background: #DCEAF8; border-color: #7EA9D6; }\n"
"QPushButton:pressed { background: #C4DCF3; }\n"
"QTabBar::tab { font-family: \"B Nazanin\"; font-size: 14pt; font-weight: bold; min-height: 42px; padding: 6px 15px; background: #E8EEF5; color: #263445; border: 1px solid #C7D0DB; }\n"
"QTabBar::tab:selected { background: white; color: #1565A8; border-top: 3px solid #1976D2; }\n"
"QTabWidget::pane { border: 1px solid #C7D0DB; background: white; }\n"
"\n"
"/* \u06a9\u0627\u0631\u062a\u200c\u0647\u0627\u06cc \u0627\u062a\u0627\u0642: \u0633\u0627\u062e\u062a\u0627\u0631 \u0648 \u0638\u0627\u0647\u0631 \u062b\u0627\u0628\u062a \u062f\u0631 main.ui\u061b Python \u0641\u0642\u0637"
                        " \u0648\u0636\u0639\u06cc\u062a/\u0645\u062a\u0646 \u0647\u0631 \u06a9\u0627\u0631\u062a \u0631\u0627 \u062a\u0639\u06cc\u06cc\u0646 \u0645\u06cc\u200c\u06a9\u0646\u062f. */\n"
"QPushButton#hotelRoomCardButton { text-align: center; padding: 9px; border: 1px solid #C9CED4; border-radius: 10px; color: #667085; background: #F1F3F5; font-family: \"B Nazanin\"; font-size: 11pt; font-weight: bold; }\n"
"QPushButton#hotelRoomCardButton[hotelStatus=\"vacant\"] { background: #F0F9F3; border-color: #8CC9A0; color: #21864B; }\n"
"QPushButton#hotelRoomCardButton[hotelStatus=\"occupied\"] { background: #FFF3F1; border-color: #E6A39B; color: #B9382B; }\n"
"QPushButton#hotelRoomCardButton[hotelStatus=\"reserved\"] { background: #FFF7E8; border-color: #E7C078; color: #996515; }\n"
"QPushButton#hotelRoomCardButton:hover { border-width: 2px; }\n"
"", None))
        self.actionHome.setText(QCoreApplication.translate("MainWindow", u"\u0635\u0641\u062d\u0647 \u0627\u0635\u0644\u06cc", None))
        self.actionPassword.setText(QCoreApplication.translate("MainWindow", u"\u062a\u063a\u06cc\u06cc\u0631 \u0631\u0645\u0632 \u0639\u0628\u0648\u0631", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0631\u0648\u062c", None))
        self.actionUserManagement.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062f\u06cc\u0631\u06cc\u062a \u06a9\u0627\u0631\u0628\u0631\u0627\u0646", None))
        self.actionRepairsRequest.setText(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a \u06a9\u0627\u0631 \u062a\u0639\u0645\u06cc\u0631\u0627\u062a\u06cc", None))
        self.actionRepairsHistory.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0648\u0627\u0628\u0642 \u062a\u0639\u0645\u06cc\u0631\u0627\u062a", None))
        self.actionEquipmentList.setText(QCoreApplication.translate("MainWindow", u"\u0641\u0647\u0631\u0633\u062a \u062a\u062c\u0647\u06cc\u0632\u0627\u062a", None))
        self.actionAssets.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0645\u0648\u0627\u0644", None))
        self.actionReportRepairs.setText(QCoreApplication.translate("MainWindow", u"\u06af\u0632\u0627\u0631\u0634 \u062a\u0639\u0645\u06cc\u0631\u0627\u062a", None))
        self.actionReportEquipment.setText(QCoreApplication.translate("MainWindow", u"\u06af\u0632\u0627\u0631\u0634 \u062a\u062c\u0647\u06cc\u0632\u0627\u062a", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0631\u0628\u0627\u0631\u0647 \u0628\u0631\u0646\u0627\u0645\u0647", None))
        self.actionAnbarTahrir.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0646\u0628\u0627\u0631 \u0644\u0648\u0627\u0632\u0645\u200c\u0627\u0644\u062a\u062d\u0631\u06cc\u0631", None))
        self.actionMtoTahrir.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0642\u0627\u0636\u0627\u06cc \u0644\u0648\u0627\u0632\u0645\u200c\u0627\u0644\u062a\u062d\u0631\u06cc\u0631", None))
        self.lblNavigationTitle.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0627\u0645\u0627\u0646\u0647 \u0645\u062f\u06cc\u0631\u06cc\u062a", None))
        self.lblNavigationUser.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0648\u0634 \u0622\u0645\u062f\u06cc\u062f", None))
        self.btnHome.setText(QCoreApplication.translate("MainWindow", u"\u0635\u0641\u062d\u0647 \u0627\u0635\u0644\u06cc", None))
        self.btnPassword.setText(QCoreApplication.translate("MainWindow", u"\u062a\u063a\u06cc\u06cc\u0631 \u0631\u0645\u0632 \u0639\u0628\u0648\u0631", None))
        self.btnUsers.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062f\u06cc\u0631\u06cc\u062a \u06a9\u0627\u0631\u0628\u0631\u0627\u0646", None))
#if QT_CONFIG(tooltip)
        self.btnTabPermissions.setToolTip(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u06cc\u06cc\u0646 \u0627\u06cc\u0646\u06a9\u0647 \u0647\u0631 \u06a9\u0627\u0631\u0628\u0631 \u0628\u0647 \u06a9\u062f\u0627\u0645 \u062a\u0628\u200c\u0647\u0627\u06cc \u0633\u0627\u0645\u0627\u0646\u0647 \u062f\u0633\u062a\u0631\u0633\u06cc \u062f\u0627\u0634\u062a\u0647 \u0628\u0627\u0634\u062f", None))
#endif // QT_CONFIG(tooltip)
        self.btnTabPermissions.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u06cc\u06cc\u0646 \u062f\u0633\u062a\u0631\u0633\u06cc \u062a\u0628\u200c\u0647\u0627", None))
        self.btnRepairs.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0631\u062e\u0648\u0627\u0633\u062a \u06a9\u0627\u0631", None))
        self.btnEquipment.setText(QCoreApplication.translate("MainWindow", u"\u062a\u062c\u0647\u06cc\u0632\u0627\u062a", None))
        self.btnAssets.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0645\u0648\u0627\u0644", None))
        self.btnHotel.setText(QCoreApplication.translate("MainWindow", u"\u0627\u062a\u0627\u0642\u200c\u062f\u0627\u0631\u06cc", None))
        self.btnReports.setText(QCoreApplication.translate("MainWindow", u"\u06af\u0632\u0627\u0631\u0634 \u0648 \u067e\u06cc\u06af\u06cc\u0631\u06cc", None))
        self.btnAnbarTahrir.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0646\u0628\u0627\u0631 \u0644\u0648\u0627\u0632\u0645\u200c\u0627\u0644\u062a\u062d\u0631\u06cc\u0631", None))
        self.btnMtoTahrir.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0642\u0627\u0636\u0627\u06cc \u0644\u0648\u0627\u0632\u0645\u200c\u0627\u0644\u062a\u062d\u0631\u06cc\u0631", None))
        self.btnExit.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0631\u0648\u062c \u0627\u0632 \u0628\u0631\u0646\u0627\u0645\u0647", None))
        self.lblHomeTitle.setText(QCoreApplication.translate("MainWindow", u"\u0633\u06cc\u0633\u062a\u0645 \u0645\u062f\u06cc\u0631\u06cc\u062a \u062f\u0631\u062e\u0648\u0627\u0633\u062a\u200c\u0647\u0627\u06cc \u062a\u0639\u0645\u06cc\u0631\u0627\u062a", None))
        self.btnOpenKar.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0631\u062e\u0648\u0627\u0633\u062a \u06a9\u0627\u0631", None))
        self.btnOpenUsers.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062f\u06cc\u0631\u06cc\u062a \u06a9\u0627\u0631\u0628\u0631\u0627\u0646", None))
        self.btnOpenPassword.setText(QCoreApplication.translate("MainWindow", u"\u062a\u063a\u06cc\u06cc\u0631 \u0631\u0645\u0632 \u0639\u0628\u0648\u0631", None))
        self.btnOpenReports.setText(QCoreApplication.translate("MainWindow", u"\u06af\u0632\u0627\u0631\u0634 \u0648 \u067e\u06cc\u06af\u06cc\u0631\u06cc", None))
        self.btnOpenEquipment.setText(QCoreApplication.translate("MainWindow", u"\u062a\u062c\u0647\u06cc\u0632\u0627\u062a", None))
        self.btnOpenMesc.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062f\u06cc\u0631\u06cc\u062a \u06a9\u062f \u06a9\u0627\u0644\u0627\u0647\u0627\u06cc MESC", None))
        self.btnOpenAssets.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0645\u0648\u0627\u0644", None))
        self.btnOpenHotel.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062f\u06cc\u0631\u06cc\u062a \u0627\u062a\u0627\u0642\u200c\u062f\u0627\u0631\u06cc", None))
        self.btnOpenAnbarTahrir.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0646\u0628\u0627\u0631 \u0644\u0648\u0627\u0632\u0645\u200c\u0627\u0644\u062a\u062d\u0631\u06cc\u0631", None))
        self.btnOpenMtoTahrir.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0642\u0627\u0636\u0627\u06cc \u0644\u0648\u0627\u0632\u0645\u200c\u0627\u0644\u062a\u062d\u0631\u06cc\u0631", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabHome), QCoreApplication.translate("MainWindow", u"\u0635\u0641\u062d\u0647 \u0627\u0635\u0644\u06cc", None))
        self.btnBackHomeKar.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0631\u0648\u062c \u0627\u0632 \u0627\u06cc\u0646 \u062a\u0628", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u062f\u0631\u062e\u0648\u0627\u0633\u062a:", None))
        self.lblWonumber.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0627\u062d\u062f \u062f\u0631\u062e\u0648\u0627\u0633\u062a\u200c\u06a9\u0646\u0646\u062f\u0647:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627\u0631\u06cc\u062e \u062f\u0631\u062e\u0648\u0627\u0633\u062a:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0648\u0636\u0648\u0639:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0646\u0637\u0642\u0647 \u06a9\u0627\u0631:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062d\u0644 \u06a9\u0627\u0631:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a\u200c\u06a9\u0646\u0646\u062f\u0647:", None))
        self.lblDarkhastkonande.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0631\u062d \u06a9\u0627\u0631:", None))
        self.btnSaveKar.setText(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a \u062f\u0631\u062e\u0648\u0627\u0633\u062a", None))
        self.btnNewKar.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0631\u062e\u0648\u0627\u0633\u062a \u062c\u062f\u06cc\u062f", None))
        self.btnClearKar.setText(QCoreApplication.translate("MainWindow", u"\u067e\u0627\u06a9 \u06a9\u0631\u062f\u0646 \u0641\u0631\u0645", None))
        self.lblSearch.setText(QCoreApplication.translate("MainWindow", u"\u062c\u0633\u062a\u062c\u0648:", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabKar), QCoreApplication.translate("MainWindow", u"\u062f\u0631\u062e\u0648\u0627\u0633\u062a \u06a9\u0627\u0631", None))
        self.btnBackHomeUsers.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0631\u0648\u062c \u0627\u0632 \u0627\u06cc\u0646 \u062a\u0628", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u0648 \u0646\u0627\u0645 \u062e\u0627\u0646\u0648\u0627\u062f\u06af\u06cc:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0645\u0632 \u0639\u0628\u0648\u0631:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u062a\u06a9\u0631\u0627\u0631 \u0631\u0645\u0632 \u0639\u0628\u0648\u0631:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0645\u062a:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0627\u062d\u062f:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0637\u062d \u062f\u0633\u062a\u0631\u0633\u06cc:", None))
        self.btnSaveUser.setText(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a \u06a9\u0627\u0631\u0628\u0631", None))
        self.btnEditUser.setText(QCoreApplication.translate("MainWindow", u"\u0648\u06cc\u0631\u0627\u06cc\u0634", None))
        self.btnDeleteUser.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0630\u0641 \u06a9\u0627\u0631\u0628\u0631", None))
        self.btnClear.setText(QCoreApplication.translate("MainWindow", u"\u067e\u0627\u06a9 \u06a9\u0631\u062f\u0646", None))
        self.btnCancel.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0627\u0632\u06af\u0634\u062a", None))
        ___qtablewidgetitem = self.tblUsers.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc", None))
        ___qtablewidgetitem1 = self.tblUsers.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645", None))
        ___qtablewidgetitem2 = self.tblUsers.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0627\u062d\u062f", None))
        ___qtablewidgetitem3 = self.tblUsers.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0637\u062d \u062f\u0633\u062a\u0631\u0633\u06cc", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabUserManagement), QCoreApplication.translate("MainWindow", u"\u062a\u0639\u0631\u06cc\u0641 \u0648 \u0645\u062f\u06cc\u0631\u06cc\u062a \u06a9\u0627\u0631\u0628\u0631\u0627\u0646", None))
        self.btnBackHomePassword.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0631\u0648\u062c \u0627\u0632 \u0627\u06cc\u0646 \u062a\u0628", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0646\u062a\u062e\u0627\u0628 \u06a9\u0627\u0631\u0628\u0631:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0645\u0632 \u062c\u062f\u06cc\u062f:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u062a\u06a9\u0631\u0627\u0631 \u0631\u0645\u0632 \u062c\u062f\u06cc\u062f:", None))
        self.btnChangePassword.setText(QCoreApplication.translate("MainWindow", u"\u062a\u063a\u06cc\u06cc\u0631 \u0631\u0645\u0632", None))
        self.btnCancelPassword.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0646\u0635\u0631\u0627\u0641", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabChangePassword), QCoreApplication.translate("MainWindow", u"\u062a\u063a\u06cc\u06cc\u0631 \u0631\u0645\u0632 \u0639\u0628\u0648\u0631", None))
        self.btnBackHomeReport.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0631\u0648\u062c \u0627\u0632 \u0627\u06cc\u0646 \u062a\u0628", None))
        self.groupReportFilters.setTitle(QCoreApplication.translate("MainWindow", u"\u0641\u06cc\u0644\u062a\u0631 \u06af\u0632\u0627\u0631\u0634", None))
        self.lblReportSearch.setText(QCoreApplication.translate("MainWindow", u"\u062c\u0633\u062a\u062c\u0648:", None))
        self.lblReportUnit.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0627\u062d\u062f \u062f\u0631\u062e\u0648\u0627\u0633\u062a\u200c\u06a9\u0646\u0646\u062f\u0647:", None))
        self.lblReportTopic.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0648\u0636\u0648\u0639 \u062f\u0631\u062e\u0648\u0627\u0633\u062a:", None))
        self.lblReportStatus.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0636\u0639\u06cc\u062a \u06a9\u0627\u0631:", None))
        self.lblReportFrom.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0632 \u062a\u0627\u0631\u06cc\u062e (\u0634\u0645\u0633\u06cc):", None))
        self.lblReportTo.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627 \u062a\u0627\u0631\u06cc\u062e (\u0634\u0645\u0633\u06cc):", None))
        self.btnRefreshReport.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0645\u0627\u06cc\u0634 \u06af\u0632\u0627\u0631\u0634", None))
        self.btnClearReportFilters.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0630\u0641 \u0641\u06cc\u0644\u062a\u0631\u0647\u0627", None))
        ___qtablewidgetitem4 = self.tblReportList.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0631\u062f\u06cc\u0641", None))
        ___qtablewidgetitem5 = self.tblReportList.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u062f\u0631\u062e\u0648\u0627\u0633\u062a", None))
        ___qtablewidgetitem6 = self.tblReportList.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0627\u062d\u062f", None))
        ___qtablewidgetitem7 = self.tblReportList.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627\u0631\u06cc\u062e \u062f\u0631\u062e\u0648\u0627\u0633\u062a", None))
        ___qtablewidgetitem8 = self.tblReportList.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0648\u0636\u0648\u0639 \u062f\u0631\u062e\u0648\u0627\u0633\u062a", None))
        ___qtablewidgetitem9 = self.tblReportList.horizontalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062d\u0644 \u06a9\u0627\u0631", None))
        ___qtablewidgetitem10 = self.tblReportList.horizontalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0631\u062e\u0648\u0627\u0633\u062a\u200c\u06a9\u0646\u0646\u062f\u0647", None))
        ___qtablewidgetitem11 = self.tblReportList.horizontalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0631\u062d \u062f\u0631\u062e\u0648\u0627\u0633\u062a", None))
        ___qtablewidgetitem12 = self.tblReportList.horizontalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0636\u0639\u06cc\u062a", None))
        ___qtablewidgetitem13 = self.tblReportList.horizontalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u0622\u062e\u0631\u06cc\u0646 \u062a\u0627\u0631\u06cc\u062e \u067e\u06cc\u06af\u06cc\u0631\u06cc", None))
        ___qtablewidgetitem14 = self.tblReportList.horizontalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u0622\u062e\u0631\u06cc\u0646 \u062a\u0648\u0636\u06cc\u062d\u0627\u062a", None))
        self.groupTracking.setTitle(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a \u067e\u06cc\u06af\u06cc\u0631\u06cc \u0648 \u0646\u062a\u06cc\u062c\u0647 \u06a9\u0627\u0631", None))
        self.lblSelectedWorkNoTitle.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u062f\u0631\u062e\u0648\u0627\u0633\u062a \u0627\u0646\u062a\u062e\u0627\u0628\u200c\u0634\u062f\u0647:", None))
        self.lblSelectedWorkNo.setText(QCoreApplication.translate("MainWindow", u"\u2014", None))
        self.lblTrackingStatusTitle.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0636\u0639\u06cc\u062a \u062c\u062f\u06cc\u062f:", None))
        self.lblTrackingDateTitle.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627\u0631\u06cc\u062e \u067e\u06cc\u06af\u06cc\u0631\u06cc:", None))
        self.lblTrackingNoteTitle.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0631\u062d \u067e\u06cc\u06af\u06cc\u0631\u06cc / \u0646\u062a\u06cc\u062c\u0647 \u0627\u0646\u062c\u0627\u0645 \u06a9\u0627\u0631:", None))
        self.btnSaveTracking.setText(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a \u067e\u06cc\u06af\u06cc\u0631\u06cc / \u062a\u06a9\u0645\u06cc\u0644 \u06a9\u0627\u0631", None))
        self.btnViewTrackingHistory.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0634\u0627\u0647\u062f\u0647 \u0633\u0648\u0627\u0628\u0642 \u067e\u06cc\u06af\u06cc\u0631\u06cc", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabReport), QCoreApplication.translate("MainWindow", u"\u06af\u0632\u0627\u0631\u0634 \u0648 \u067e\u06cc\u06af\u06cc\u0631\u06cc \u06a9\u0627\u0631\u0647\u0627", None))
        self.btnBackHomeMesc.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0631\u0648\u062c \u0627\u0632 \u0627\u06cc\u0646 \u062a\u0628", None))
        self.groupMescFields.setTitle(QCoreApplication.translate("MainWindow", u"\u0627\u0637\u0644\u0627\u0639\u0627\u062a \u06a9\u062f \u06a9\u0627\u0644\u0627", None))
        self.lblMescCode.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u062f MESC:", None))
        self.txtMescCode.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u06a9\u062f \u06cc\u06a9\u062a\u0627\u06cc \u06a9\u0627\u0644\u0627", None))
        self.lblMescShohazine.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u0647\u0632\u06cc\u0646\u0647:", None))
        self.lblMescSharh.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0631\u062d:", None))
        self.lblMescDescription.setText(QCoreApplication.translate("MainWindow", u"Discription:", None))
        self.lblMescUnit.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0627\u062d\u062f:", None))
        self.lblMescPic.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0635\u0648\u06cc\u0631 \u06a9\u0627\u0644\u0627 (\u0627\u062e\u062a\u06cc\u0627\u0631\u06cc):", None))
        self.lblMescPicPreview.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0635\u0648\u06cc\u0631\u06cc \u0627\u0646\u062a\u062e\u0627\u0628 \u0646\u0634\u062f\u0647", None))
        self.btnMescChoosePic.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0646\u062a\u062e\u0627\u0628 \u062a\u0635\u0648\u06cc\u0631", None))
        self.btnMescRemovePic.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0630\u0641 \u062a\u0635\u0648\u06cc\u0631", None))
        self.lblMescSabtkonande.setText(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a\u200c\u06a9\u0646\u0646\u062f\u0647:", None))
        self.lblMescEditor.setText(QCoreApplication.translate("MainWindow", u"\u0622\u062e\u0631\u06cc\u0646 \u0648\u06cc\u0631\u0627\u06cc\u0634\u06af\u0631:", None))
        self.btnMescNew.setText(QCoreApplication.translate("MainWindow", u"\u0631\u06a9\u0648\u0631\u062f \u062c\u062f\u06cc\u062f", None))
        self.btnMescSave.setText(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a \u0627\u0637\u0644\u0627\u0639\u0627\u062a", None))
        self.btnMescEdit.setText(QCoreApplication.translate("MainWindow", u"\u0630\u062e\u06cc\u0631\u0647 \u0648\u06cc\u0631\u0627\u06cc\u0634", None))
        self.btnMescDelete.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0630\u0641 \u0631\u06a9\u0648\u0631\u062f", None))
        self.lblMescSearch.setText(QCoreApplication.translate("MainWindow", u"\u062c\u0633\u062a\u062c\u0648 \u062f\u0631 \u06a9\u062f\u060c \u0634\u0631\u062d\u060c \u0634\u0645\u0627\u0631\u0647 \u0647\u0632\u06cc\u0646\u0647 \u06cc\u0627 \u0648\u0627\u062d\u062f:", None))
        self.txtMescSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0639\u0628\u0627\u0631\u062a \u062c\u0633\u062a\u062c\u0648 \u0631\u0627 \u0648\u0627\u0631\u062f \u06a9\u0646\u06cc\u062f...", None))
        self.btnMescSearch.setText(QCoreApplication.translate("MainWindow", u"\u062c\u0633\u062a\u062c\u0648", None))
        ___qtablewidgetitem15 = self.tblMescList.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u062f MESC", None))
        ___qtablewidgetitem16 = self.tblMescList.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u0647\u0632\u06cc\u0646\u0647", None))
        ___qtablewidgetitem17 = self.tblMescList.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0631\u062d", None))
        ___qtablewidgetitem18 = self.tblMescList.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Discription", None))
        ___qtablewidgetitem19 = self.tblMescList.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0627\u062d\u062f", None))
        ___qtablewidgetitem20 = self.tblMescList.horizontalHeaderItem(5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a\u200c\u06a9\u0646\u0646\u062f\u0647", None))
        ___qtablewidgetitem21 = self.tblMescList.horizontalHeaderItem(6)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u0648\u06cc\u0631\u0627\u06cc\u0634\u06af\u0631", None))
        ___qtablewidgetitem22 = self.tblMescList.horizontalHeaderItem(7)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0635\u0648\u06cc\u0631", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabMesc), QCoreApplication.translate("MainWindow", u"\u0645\u062f\u06cc\u0631\u06cc\u062a \u06a9\u062f \u06a9\u0627\u0644\u0627\u0647\u0627\u06cc MESC", None))
        self.btnBackHomeAmval.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0631\u0648\u062c \u0627\u0632 \u0627\u06cc\u0646 \u062a\u0628", None))
        self.groupAmvalFilter.setTitle(QCoreApplication.translate("MainWindow", u"\u062c\u0633\u062a\u062c\u0648 \u0648 \u0641\u06cc\u0644\u062a\u0631 \u0627\u0645\u0648\u0627\u0644", None))
        self.lblAmvalSearch.setText(QCoreApplication.translate("MainWindow", u"\u062c\u0633\u062a\u062c\u0648:", None))
        self.txtAmvalSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u0627\u0645\u0648\u0627\u0644\u060c \u0634\u0631\u062d\u060c \u0634\u0645\u0627\u0631\u0647 \u0633\u0631\u06cc\u0627\u0644\u060c \u0645\u062d\u0644\u060c \u0634\u0645\u0627\u0631\u0647 \u0628\u0648\u062f\u062c\u0647 \u06cc\u0627 \u062a\u0648\u0636\u06cc\u062d\u0627\u062a...", None))
        self.lblAmvalUnitFilter.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0627\u062d\u062f:", None))
#if QT_CONFIG(tooltip)
        self.cmbAmvalUnitFilter.setToolTip(QCoreApplication.translate("MainWindow", u"\u0641\u06cc\u0644\u062a\u0631 \u0627\u0645\u0648\u0627\u0644 \u0628\u0631 \u0627\u0633\u0627\u0633 \u06a9\u062f \u0648\u0627\u062d\u062f\u061b \u0646\u0645\u0648\u0646\u0647: 5121 \u0628\u0631\u0627\u06cc \u062a\u0639\u0645\u06cc\u0631\u0627\u062a", None))
#endif // QT_CONFIG(tooltip)
        self.lblAmvalActiveFilter.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0636\u0639\u06cc\u062a \u0641\u0639\u0627\u0644:", None))
        self.cmbAmvalActiveFilter.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0647\u0645\u0647", None))
        self.cmbAmvalActiveFilter.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0641\u0639\u0627\u0644", None))
        self.cmbAmvalActiveFilter.setItemText(2, QCoreApplication.translate("MainWindow", u"\u063a\u06cc\u0631\u0641\u0639\u0627\u0644", None))

        self.btnAmvalSearch.setText(QCoreApplication.translate("MainWindow", u"\u062c\u0633\u062a\u062c\u0648", None))
        self.btnAmvalClearFilter.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0630\u0641 \u0641\u06cc\u0644\u062a\u0631", None))
        self.btnAmvalReport.setText(QCoreApplication.translate("MainWindow", u"\u06af\u0632\u0627\u0631\u0634 \u0627\u0645\u0648\u0627\u0644", None))
        self.btnAmvalPrint.setText(QCoreApplication.translate("MainWindow", u"\u0686\u0627\u067e \u06af\u0632\u0627\u0631\u0634", None))
        self.groupAmvalInfo.setTitle(QCoreApplication.translate("MainWindow", u"\u0627\u0637\u0644\u0627\u0639\u0627\u062a \u0645\u0627\u0644", None))
        self.lblAmvalID.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0646\u0627\u0633\u0647:", None))
        self.lblAmvalAssetNo.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u0627\u0645\u0648\u0627\u0644:", None))
        self.lblAmvalDescription.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0631\u062d:", None))
        self.lblAmvalStatus.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0636\u0639\u06cc\u062a:", None))
        self.lblAmvalUsePlace.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062d\u0644 \u0627\u0633\u062a\u0641\u0627\u062f\u0647:", None))
        self.lblAmvalSerial.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u0633\u0631\u06cc\u0627\u0644:", None))
        self.lblAmvalLocCode.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u062f \u0645\u062d\u0644 (Loc Code):", None))
        self.lblAmvalInvDate.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627\u0631\u06cc\u062e \u0648\u0631\u0648\u062f:", None))
        self.txtAmvalInvDate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0633\u06cc: 1405/07/18", None))
        self.lblAmvalExitDate.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627\u0631\u06cc\u062e \u062e\u0631\u0648\u062c:", None))
        self.txtAmvalExitDate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0633\u06cc: 1405/07/18", None))
        self.lblAmvalAcqDate.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627\u0631\u06cc\u062e \u062a\u062d\u0635\u06cc\u0644 (ACQ DATE):", None))
        self.lblAmvalLoc.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062d\u0644 (LOC):", None))
        self.lblAmvalBudget.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u0628\u0648\u062f\u062c\u0647:", None))
        self.lblAmvalNotes.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0648\u0636\u06cc\u062d\u0627\u062a:", None))
        self.lblAmvalUnit.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0627\u062d\u062f:", None))
        self.lblAmvalUnitCode.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u062f \u0648\u0627\u062d\u062f:", None))
        self.txtAmvalUnitCode.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0645\u062b\u0627\u0644: 5121 = \u062a\u0639\u0645\u06cc\u0631\u0627\u062a", None))
        self.lblAmvalActive.setText(QCoreApplication.translate("MainWindow", u"\u0641\u0639\u0627\u0644 / \u063a\u06cc\u0631\u0641\u0639\u0627\u0644:", None))
        self.cmbAmvalActive.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0641\u0639\u0627\u0644", None))
        self.cmbAmvalActive.setItemText(1, QCoreApplication.translate("MainWindow", u"\u063a\u06cc\u0631\u0641\u0639\u0627\u0644", None))

        self.lblAmvalManUser.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u062a\u0641\u0627\u062f\u0647\u200c\u06a9\u0646\u0646\u062f\u0647 (MANUSERL):", None))
        self.lblAmvalCode.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u062f (Code):", None))
        self.lblAmvalCdVahed.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u062f \u0648\u0627\u062d\u062f (Cd_Vahed):", None))
        self.lblAmvalRecorder.setText(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a\u200c\u06a9\u0646\u0646\u062f\u0647:", None))
        self.lblAmvalEditor.setText(QCoreApplication.translate("MainWindow", u"\u0648\u06cc\u0631\u0627\u06cc\u0634\u06af\u0631:", None))
        self.btnAmvalNew.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0627\u0644 \u062c\u062f\u06cc\u062f", None))
        self.btnAmvalSave.setText(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a \u0627\u0637\u0644\u0627\u0639\u0627\u062a", None))
        self.btnAmvalEdit.setText(QCoreApplication.translate("MainWindow", u"\u0630\u062e\u06cc\u0631\u0647 \u0648\u06cc\u0631\u0627\u06cc\u0634", None))
        self.btnAmvalDelete.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0630\u0641", None))
        ___qtablewidgetitem23 = self.tblAmvalList.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"\u0631\u062f\u06cc\u0641", None))
        ___qtablewidgetitem24 = self.tblAmvalList.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0646\u0627\u0633\u0647", None))
        ___qtablewidgetitem25 = self.tblAmvalList.horizontalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u0627\u0645\u0648\u0627\u0644", None))
        ___qtablewidgetitem26 = self.tblAmvalList.horizontalHeaderItem(3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0631\u062d", None))
        ___qtablewidgetitem27 = self.tblAmvalList.horizontalHeaderItem(4)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u062f \u0645\u062d\u0644", None))
        ___qtablewidgetitem28 = self.tblAmvalList.horizontalHeaderItem(5)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0636\u0639\u06cc\u062a", None))
        ___qtablewidgetitem29 = self.tblAmvalList.horizontalHeaderItem(6)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062d\u0644 \u0627\u0633\u062a\u0641\u0627\u062f\u0647", None))
        ___qtablewidgetitem30 = self.tblAmvalList.horizontalHeaderItem(7)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u0633\u0631\u06cc\u0627\u0644", None))
        ___qtablewidgetitem31 = self.tblAmvalList.horizontalHeaderItem(8)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u062a\u0641\u0627\u062f\u0647\u200c\u06a9\u0646\u0646\u062f\u0647", None))
        ___qtablewidgetitem32 = self.tblAmvalList.horizontalHeaderItem(9)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627\u0631\u06cc\u062e \u0648\u0631\u0648\u062f", None))
        ___qtablewidgetitem33 = self.tblAmvalList.horizontalHeaderItem(10)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627\u0631\u06cc\u062e \u062e\u0631\u0648\u062c", None))
        ___qtablewidgetitem34 = self.tblAmvalList.horizontalHeaderItem(11)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062d\u0644 (LOC)", None))
        ___qtablewidgetitem35 = self.tblAmvalList.horizontalHeaderItem(12)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627\u0631\u06cc\u062e \u062a\u062d\u0635\u06cc\u0644", None))
        ___qtablewidgetitem36 = self.tblAmvalList.horizontalHeaderItem(13)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u0628\u0648\u062f\u062c\u0647", None))
        ___qtablewidgetitem37 = self.tblAmvalList.horizontalHeaderItem(14)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0648\u0636\u06cc\u062d\u0627\u062a", None))
        ___qtablewidgetitem38 = self.tblAmvalList.horizontalHeaderItem(15)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0627\u062d\u062f", None))
        ___qtablewidgetitem39 = self.tblAmvalList.horizontalHeaderItem(16)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u062f", None))
        ___qtablewidgetitem40 = self.tblAmvalList.horizontalHeaderItem(17)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u062f \u0648\u0627\u062d\u062f", None))
        ___qtablewidgetitem41 = self.tblAmvalList.horizontalHeaderItem(18)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a\u200c\u06a9\u0646\u0646\u062f\u0647", None))
        ___qtablewidgetitem42 = self.tblAmvalList.horizontalHeaderItem(19)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"\u0648\u06cc\u0631\u0627\u06cc\u0634\u06af\u0631", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabAmval), QCoreApplication.translate("MainWindow", u"\u0627\u0645\u0648\u0627\u0644", None))
        self.tabHotel.setStyleSheet(QCoreApplication.translate("MainWindow", u"QGroupBox { font-family: \"B Nazanin\"; font-size: 12pt; font-weight: bold; border: 1px solid #D6DEE8; border-radius: 8px; margin-top: 12px; padding-top: 10px; } QGroupBox::title { subcontrol-origin: margin; right: 12px; padding: 0 6px; } QLineEdit, QComboBox { min-height: 32px; padding: 3px 7px; border: 1px solid #C7D2DF; border-radius: 5px; } QTableWidget { gridline-color: #E3E8EF; alternate-background-color: #F5F8FC; selection-background-color: #D7E9FA; selection-color: #17324D; } QPushButton#hotelRoomCardButton { min-width: 155px; min-height: 128px; max-width: 280px; text-align: center; border: 1px solid #C9CED4; border-radius: 10px; padding: 9px; font-family: \"B Nazanin\"; font-size: 11pt; font-weight: bold; } QPushButton#hotelRoomCardButton[roomStatus=\"\u062e\u0627\u0644\u06cc\"] { background: #F0F9F3; border-color: #8CC9A0; color: #21864B; } QPushButton#hotelRoomCardButton[roomStatus=\"\u0627\u0634\u063a\u0627\u0644\"] { background: #FFF3F1; border-color: #E6A39B; color: #B9382B; } QPushButton#hotelRo"
                        "omCardButton[roomStatus=\"\u0631\u0632\u0631\u0648\"] { background: #FFF7E8; border-color: #E7C078; color: #996515; } QPushButton#hotelRoomCardButton[roomStatus=\"\u0633\u0627\u06cc\u0631\"] { background: #F1F3F5; border-color: #C9CED4; color: #667085; } QPushButton#hotelRoomCardButton:hover { border-width: 2px; }", None))
        self.btnBackHomeHotel.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0627\u0632\u06af\u0634\u062a \u0628\u0647 \u0635\u0641\u062d\u0647 \u0627\u0635\u0644\u06cc", None))
        self.hotelSections.setStyleSheet(QCoreApplication.translate("MainWindow", u"QTabBar::tab { min-height: 42px; padding: 7px 18px; font-family: \"B Nazanin\"; font-size: 13pt; font-weight: bold; }", None))
        self.groupHotelSummary.setTitle(QCoreApplication.translate("MainWindow", u"\u0648\u0636\u0639\u06cc\u062a \u06a9\u0644\u06cc \u0627\u0642\u0627\u0645\u062a\u06af\u0627\u0647", None))
        self.lblHotelLaleh.setText(QCoreApplication.translate("MainWindow", u"\u0644\u0627\u0644\u0647: \u06f2\u06f4 \u0627\u062a\u0627\u0642", None))
        self.lblHotelLian.setText(QCoreApplication.translate("MainWindow", u"\u0644\u06cc\u0627\u0646: \u06f6 \u0633\u0648\u0626\u06cc\u062a", None))
        self.lblHotelVacant.setText(QCoreApplication.translate("MainWindow", u"\u0627\u062a\u0627\u0642 \u062e\u0627\u0644\u06cc: \u2014", None))
        self.lblHotelOccupied.setText(QCoreApplication.translate("MainWindow", u"\u0627\u062a\u0627\u0642 \u0627\u0634\u063a\u0627\u0644: \u2014", None))
        self.lblHotelArrivals.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0631\u0648\u062f \u0627\u0645\u0631\u0648\u0632: \u2014", None))
        self.lblHotelDepartures.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0631\u0648\u062c \u0627\u0645\u0631\u0648\u0632: \u2014", None))
        self.groupHotelRooms.setTitle(QCoreApplication.translate("MainWindow", u"\u0648\u0636\u0639\u06cc\u062a \u0627\u062a\u0627\u0642\u200c\u0647\u0627 \u0648 \u0633\u0648\u0626\u06cc\u062a\u200c\u0647\u0627", None))
        self.btnHotelLaleh.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0627\u062e\u062a\u0645\u0627\u0646 \u0644\u0627\u0644\u0647", None))
        self.btnHotelLian.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0627\u062e\u062a\u0645\u0627\u0646 \u0644\u06cc\u0627\u0646", None))
        self.btnHotelAll.setText(QCoreApplication.translate("MainWindow", u"\u0647\u0645\u0647 \u0627\u062a\u0627\u0642\u200c\u0647\u0627", None))
        ___qtablewidgetitem43 = self.tblHotelRooms.horizontalHeaderItem(0)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0627\u062e\u062a\u0645\u0627\u0646", None))
        ___qtablewidgetitem44 = self.tblHotelRooms.horizontalHeaderItem(1)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"\u0627\u062a\u0627\u0642 / \u0633\u0648\u0626\u06cc\u062a", None))
        ___qtablewidgetitem45 = self.tblHotelRooms.horizontalHeaderItem(2)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0636\u0639\u06cc\u062a", None))
        ___qtablewidgetitem46 = self.tblHotelRooms.horizontalHeaderItem(3)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u0645\u0647\u0645\u0627\u0646", None))
        ___qtablewidgetitem47 = self.tblHotelRooms.horizontalHeaderItem(4)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u0627\u062f \u0646\u0641\u0631\u0627\u062a", None))
        ___qtablewidgetitem48 = self.tblHotelRooms.horizontalHeaderItem(5)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0631\u0648\u062f", None))
        ___qtablewidgetitem49 = self.tblHotelRooms.horizontalHeaderItem(6)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0631\u0648\u062c", None))
        ___qtablewidgetitem50 = self.tblHotelRooms.horizontalHeaderItem(7)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062f\u062a \u0627\u0642\u0627\u0645\u062a", None))
        self.hotelSections.setTabText(self.hotelSections.indexOf(self.hotelRoomsPage), QCoreApplication.translate("MainWindow", u"\u0648\u0636\u0639\u06cc\u062a \u0627\u062a\u0627\u0642\u200c\u0647\u0627", None))
        self.groupHotelGuestForm.setTitle(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a \u0627\u0642\u0627\u0645\u062a \u0645\u0647\u0645\u0627\u0646", None))
        self.lblHotelNational.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u062f \u0645\u0644\u06cc:", None))
        self.lblHotelFirstName.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645:", None))
        self.lblHotelLastName.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u062e\u0627\u0646\u0648\u0627\u062f\u06af\u06cc:", None))
        self.lblHotelOrg.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0627\u0632\u0645\u0627\u0646:", None))
        self.lblHotelPeople.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u0627\u062f \u0646\u0641\u0631\u0627\u062a:", None))
        self.lblHotelBuilding.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0627\u062e\u062a\u0645\u0627\u0646:", None))
        self.lblHotelRoom.setText(QCoreApplication.translate("MainWindow", u"\u0627\u062a\u0627\u0642 / \u0633\u0648\u0626\u06cc\u062a:", None))
        self.lblHotelArrival.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627\u0631\u06cc\u062e \u0648\u0631\u0648\u062f \u0628\u0631\u0646\u0627\u0645\u0647\u200c\u0631\u06cc\u0632\u06cc\u200c\u0634\u062f\u0647:", None))
        self.txtHotelArrival.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0633\u06cc: 1405/07/18", None))
        self.lblHotelDeparture.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627\u0631\u06cc\u062e \u062e\u0631\u0648\u062c \u0628\u0631\u0646\u0627\u0645\u0647\u200c\u0631\u06cc\u0632\u06cc\u200c\u0634\u062f\u0647:", None))
        self.txtHotelDeparture.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0633\u06cc: 1405/07/18", None))
        self.lblHotelEmployee.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u062f \u067e\u0631\u0633\u0646\u0644\u06cc:", None))
        self.chkHotelBreakfast.setText(QCoreApplication.translate("MainWindow", u"\u0635\u0628\u062d\u0627\u0646\u0647", None))
        self.chkHotelLunch.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0647\u0627\u0631", None))
        self.chkHotelDinner.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0627\u0645", None))
        self.lblHotelActualArrival.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0631\u0648\u062f \u0648\u0627\u0642\u0639\u06cc", None))
#if QT_CONFIG(tooltip)
        self.txtHotelActualArrival.setToolTip(QCoreApplication.translate("MainWindow", u"\u062a\u0627\u0631\u06cc\u062e \u0648\u0627\u0642\u0639\u06cc \u0648\u0631\u0648\u062f \u0645\u0647\u0645\u0627\u0646\u061b \u062e\u0627\u0644\u06cc \u0628\u0645\u0627\u0646\u062f \u062a\u0627 \u062a\u0627\u0631\u06cc\u062e \u0627\u0645\u0631\u0648\u0632 \u062b\u0628\u062a \u0634\u0648\u062f.", None))
#endif // QT_CONFIG(tooltip)
        self.txtHotelActualArrival.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0633\u06cc: 1405/07/18", None))
        self.txtHotelActualArrival.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0633\u06cc: 1405/07/18", None))
        self.lblHotelActualDeparture.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0631\u0648\u062c \u0648\u0627\u0642\u0639\u06cc", None))
#if QT_CONFIG(tooltip)
        self.txtHotelActualDeparture.setToolTip(QCoreApplication.translate("MainWindow", u"\u062a\u0627\u0631\u06cc\u062e \u0648\u0627\u0642\u0639\u06cc \u062e\u0631\u0648\u062c\u061b \u0641\u0642\u0637 \u067e\u0633 \u0627\u0632 \u062b\u0628\u062a \u0648\u0631\u0648\u062f \u0648\u0627\u0642\u0639\u06cc \u0642\u0627\u0628\u0644 \u062b\u0628\u062a \u0627\u0633\u062a.", None))
#endif // QT_CONFIG(tooltip)
        self.txtHotelActualDeparture.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0633\u06cc: 1405/07/18", None))
        self.txtHotelActualDeparture.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0633\u06cc: 1405/07/18", None))
        self.btnHotelNew.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0647\u0645\u0627\u0646 \u062c\u062f\u06cc\u062f", None))
        self.btnHotelEdit.setText(QCoreApplication.translate("MainWindow", u"\u0648\u06cc\u0631\u0627\u06cc\u0634 \u0627\u0642\u0627\u0645\u062a", None))
#if QT_CONFIG(tooltip)
        self.btnHotelExtendStay.setToolTip(QCoreApplication.translate("MainWindow", u"\u062a\u0645\u062f\u06cc\u062f \u062a\u0627\u0631\u06cc\u062e \u062e\u0631\u0648\u062c \u0645\u0648\u0631\u062f \u0627\u0646\u062a\u0638\u0627\u0631 \u0645\u0647\u0645\u0627\u0646 \u0633\u0627\u06a9\u0646\u061b \u062a\u0627\u0631\u06cc\u062e \u062e\u0631\u0648\u062c \u0648\u0627\u0642\u0639\u06cc \u062a\u063a\u06cc\u06cc\u0631 \u0646\u0645\u06cc\u200c\u06a9\u0646\u062f.", None))
#endif // QT_CONFIG(tooltip)
        self.btnHotelExtendStay.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0645\u062f\u06cc\u062f \u0627\u0642\u0627\u0645\u062a", None))
        self.btnHotelSave.setText(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a \u0627\u0642\u0627\u0645\u062a", None))
#if QT_CONFIG(tooltip)
        self.btnHotelCheckIn.setToolTip(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a \u062a\u0627\u0631\u06cc\u062e \u0648\u0627\u0642\u0639\u06cc \u0648\u0631\u0648\u062f \u0645\u0647\u0645\u0627\u0646 \u0627\u0646\u062a\u062e\u0627\u0628\u200c\u0634\u062f\u0647", None))
#endif // QT_CONFIG(tooltip)
        self.btnHotelCheckIn.setText(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a \u0648\u0631\u0648\u062f \u0648\u0627\u0642\u0639\u06cc", None))
#if QT_CONFIG(tooltip)
        self.btnHotelCheckOut.setToolTip(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a \u062a\u0627\u0631\u06cc\u062e \u0648\u0627\u0642\u0639\u06cc \u062e\u0631\u0648\u062c \u0645\u0647\u0645\u0627\u0646 \u0627\u0646\u062a\u062e\u0627\u0628\u200c\u0634\u062f\u0647\u061b \u0627\u0628\u062a\u062f\u0627 \u0648\u0631\u0648\u062f \u0628\u0627\u06cc\u062f \u062b\u0628\u062a \u0634\u062f\u0647 \u0628\u0627\u0634\u062f", None))
#endif // QT_CONFIG(tooltip)
        self.btnHotelCheckOut.setText(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a \u062e\u0631\u0648\u062c \u0648\u0627\u0642\u0639\u06cc", None))
        self.btnHotelRefresh.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0631\u0648\u0632\u0631\u0633\u0627\u0646\u06cc", None))
        self.hotelSections.setTabText(self.hotelSections.indexOf(self.hotelReceptionPage), QCoreApplication.translate("MainWindow", u"\u067e\u0630\u06cc\u0631\u0634 \u0648 \u0631\u0632\u0631\u0648", None))
        self.lblHotelMovementInfo.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0631\u0648\u062f\u0647\u0627 \u0648 \u062e\u0631\u0648\u062c\u200c\u0647\u0627\u06cc \u0628\u0631\u0646\u0627\u0645\u0647\u200c\u0631\u06cc\u0632\u06cc\u200c\u0634\u062f\u0647 \u0627\u0645\u0631\u0648\u0632\u061b \u0628\u0631\u0627\u06cc \u062b\u0628\u062a \u0648\u0631\u0648\u062f \u06cc\u0627 \u062e\u0631\u0648\u062c\u060c \u0631\u062f\u06cc\u0641 \u0645\u0647\u0645\u0627\u0646 \u0631\u0627 \u0627\u0646\u062a\u062e\u0627\u0628 \u06a9\u0646\u06cc\u062f.", None))
        ___qtablewidgetitem51 = self.tblHotelToday.horizontalHeaderItem(0)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0646\u0627\u0633\u0647", None))
        ___qtablewidgetitem52 = self.tblHotelToday.horizontalHeaderItem(1)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"\u0639\u0645\u0644\u06cc\u0627\u062a", None))
        ___qtablewidgetitem53 = self.tblHotelToday.horizontalHeaderItem(2)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0627\u062e\u062a\u0645\u0627\u0646", None))
        ___qtablewidgetitem54 = self.tblHotelToday.horizontalHeaderItem(3)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"\u0627\u062a\u0627\u0642", None))
        ___qtablewidgetitem55 = self.tblHotelToday.horizontalHeaderItem(4)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u0645\u0647\u0645\u0627\u0646", None))
        ___qtablewidgetitem56 = self.tblHotelToday.horizontalHeaderItem(5)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0641\u0631\u0627\u062a", None))
        ___qtablewidgetitem57 = self.tblHotelToday.horizontalHeaderItem(6)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627\u0631\u06cc\u062e \u0628\u0631\u0646\u0627\u0645\u0647\u200c\u0631\u06cc\u0632\u06cc\u200c\u0634\u062f\u0647", None))
        self.hotelSections.setTabText(self.hotelSections.indexOf(self.hotelMovementsPage), QCoreApplication.translate("MainWindow", u"\u0648\u0631\u0648\u062f \u0648 \u062e\u0631\u0648\u062c \u0627\u0645\u0631\u0648\u0632", None))
        self.groupHotelHistory.setTitle(QCoreApplication.translate("MainWindow", u"\u0633\u0648\u0627\u0628\u0642 \u0627\u0642\u0627\u0645\u062a (\u0627\u0637\u0644\u0627\u0639\u0627\u062a \u062d\u0630\u0641 \u0646\u0645\u06cc\u200c\u0634\u0648\u062f)", None))
        ___qtablewidgetitem58 = self.tblHotelHistory.horizontalHeaderItem(0)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0646\u0627\u0633\u0647", None))
        ___qtablewidgetitem59 = self.tblHotelHistory.horizontalHeaderItem(1)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u0645\u0647\u0645\u0627\u0646", None))
        ___qtablewidgetitem60 = self.tblHotelHistory.horizontalHeaderItem(2)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u062f \u0645\u0644\u06cc", None))
        ___qtablewidgetitem61 = self.tblHotelHistory.horizontalHeaderItem(3)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0627\u062e\u062a\u0645\u0627\u0646", None))
        ___qtablewidgetitem62 = self.tblHotelHistory.horizontalHeaderItem(4)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"\u0627\u062a\u0627\u0642", None))
        ___qtablewidgetitem63 = self.tblHotelHistory.horizontalHeaderItem(5)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0641\u0631\u0627\u062a", None))
        ___qtablewidgetitem64 = self.tblHotelHistory.horizontalHeaderItem(6)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0631\u0648\u062f \u0628\u0631\u0646\u0627\u0645\u0647\u200c\u0631\u06cc\u0632\u06cc\u200c\u0634\u062f\u0647", None))
        ___qtablewidgetitem65 = self.tblHotelHistory.horizontalHeaderItem(7)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0631\u0648\u062c \u0628\u0631\u0646\u0627\u0645\u0647\u200c\u0631\u06cc\u0632\u06cc\u200c\u0634\u062f\u0647", None))
        ___qtablewidgetitem66 = self.tblHotelHistory.horizontalHeaderItem(8)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0631\u0648\u062f \u0648\u0627\u0642\u0639\u06cc", None))
        ___qtablewidgetitem67 = self.tblHotelHistory.horizontalHeaderItem(9)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0631\u0648\u062c \u0648\u0627\u0642\u0639\u06cc", None))
        ___qtablewidgetitem68 = self.tblHotelHistory.horizontalHeaderItem(10)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062f\u062a \u0627\u0642\u0627\u0645\u062a", None))
        self.lblHotelSearch.setText(QCoreApplication.translate("MainWindow", u"\u062c\u0633\u062a\u062c\u0648\u06cc \u0633\u0648\u0627\u0628\u0642:", None))
        self.txtHotelSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645\u060c \u0646\u0627\u0645 \u062e\u0627\u0646\u0648\u0627\u062f\u06af\u06cc\u060c \u06a9\u062f \u0645\u0644\u06cc\u060c \u0633\u0627\u0632\u0645\u0627\u0646 \u06cc\u0627 \u0627\u062a\u0627\u0642...", None))
        self.hotelSections.setTabText(self.hotelSections.indexOf(self.hotelHistoryPage), QCoreApplication.translate("MainWindow", u"\u0633\u0648\u0627\u0628\u0642 \u0627\u0642\u0627\u0645\u062a", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabHotel), QCoreApplication.translate("MainWindow", u"\u0627\u062a\u0627\u0642\u200c\u062f\u0627\u0631\u06cc", None))
        self.btnBackHomeAnbarTahrir.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0631\u0648\u062c \u0627\u0632 \u0627\u06cc\u0646 \u062a\u0628", None))
        self.groupAnbarTahrirSearch.setTitle(QCoreApplication.translate("MainWindow", u"\u062c\u0633\u062a\u062c\u0648 \u0648 \u0627\u0637\u0644\u0627\u0639\u0627\u062a \u06a9\u0627\u0644\u0627", None))
        self.lblAnbarTahrirSearch.setText(QCoreApplication.translate("MainWindow", u"\u062c\u0633\u062a\u062c\u0648:", None))
        self.txtAnbarTahrirSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0634\u0631\u062d \u06a9\u0627\u0644\u0627 \u06cc\u0627 \u0648\u0627\u062d\u062f...", None))
        self.lblAnbarTahrirDescription.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0631\u062d \u06a9\u0627\u0644\u0627:", None))
        self.txtAnbarTahrirDescription.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0645\u062b\u0644\u0627\u064b \u062e\u0648\u062f\u06a9\u0627\u0631\u060c \u06a9\u0627\u063a\u0630\u060c \u067e\u0648\u0634\u0647...", None))
        self.lblAnbarTahrirQty.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0648\u062c\u0648\u062f\u06cc:", None))
        self.txtAnbarTahrirQty.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u0627\u062f \u0645\u0648\u062c\u0648\u062f", None))
        self.lblAnbarTahrirUnit.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0627\u062d\u062f:", None))
        self.txtAnbarTahrirUnit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0639\u062f\u062f\u060c \u0628\u0633\u062a\u0647\u060c \u06a9\u0627\u0631\u062a\u0646...", None))
        self.btnAnbarTahrirNew.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u0627\u0644\u0627\u06cc \u062c\u062f\u06cc\u062f", None))
        self.btnAnbarTahrirSave.setText(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a", None))
        self.btnAnbarTahrirEdit.setText(QCoreApplication.translate("MainWindow", u"\u0630\u062e\u06cc\u0631\u0647 \u0648\u06cc\u0631\u0627\u06cc\u0634", None))
        self.btnAnbarTahrirDelete.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0630\u0641", None))
        self.btnAnbarTahrirRefresh.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0627\u0632\u062e\u0648\u0627\u0646\u06cc", None))
        ___qtablewidgetitem69 = self.tblAnbarTahrirList.horizontalHeaderItem(0)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"\u0631\u062f\u06cc\u0641", None))
        ___qtablewidgetitem70 = self.tblAnbarTahrirList.horizontalHeaderItem(1)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0631\u062d \u06a9\u0627\u0644\u0627", None))
        ___qtablewidgetitem71 = self.tblAnbarTahrirList.horizontalHeaderItem(2)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0648\u062c\u0648\u062f\u06cc", None))
        ___qtablewidgetitem72 = self.tblAnbarTahrirList.horizontalHeaderItem(3)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0627\u062d\u062f", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabAnbarTahrir), QCoreApplication.translate("MainWindow", u"\u0627\u0646\u0628\u0627\u0631 \u0644\u0648\u0627\u0632\u0645\u200c\u0627\u0644\u062a\u062d\u0631\u06cc\u0631", None))
        self.btnBackHomeMtoTahrir.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0631\u0648\u062c \u0627\u0632 \u0627\u06cc\u0646 \u062a\u0628", None))
        self.groupMtoTahrirFilters.setTitle(QCoreApplication.translate("MainWindow", u"\u062c\u0633\u062a\u062c\u0648 \u0648 \u0641\u06cc\u0644\u062a\u0631 \u062f\u0631\u062e\u0648\u0627\u0633\u062a\u200c\u0647\u0627", None))
        self.lblMtoTahrirSearch.setText(QCoreApplication.translate("MainWindow", u"\u062c\u0633\u062a\u062c\u0648:", None))
        self.txtMtoTahrirSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u062c\u0633\u062a\u062c\u0648 \u062f\u0631 \u0634\u0631\u062d \u06a9\u0627\u0644\u0627\u060c \u062b\u0628\u062a\u200c\u06a9\u0646\u0646\u062f\u0647\u060c \u0648\u0627\u062d\u062f \u0648 \u0633\u0627\u06cc\u0631 \u0645\u0634\u062e\u0635\u0627\u062a...", None))
        self.lblMtoTahrirFromDate.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0632 \u062a\u0627\u0631\u06cc\u062e:", None))
        self.txtMtoTahrirFromDate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0633\u06cc: 1405/07/01", None))
        self.lblMtoTahrirToDate.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627 \u062a\u0627\u0631\u06cc\u062e:", None))
        self.txtMtoTahrirToDate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0633\u06cc: 1405/07/30", None))
        self.groupMtoTahrirInfo.setTitle(QCoreApplication.translate("MainWindow", u"\u0627\u0637\u0644\u0627\u0639\u0627\u062a \u062f\u0631\u062e\u0648\u0627\u0633\u062a", None))
        self.lblMtoTahrirDate.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627\u0631\u06cc\u062e \u0634\u0645\u0633\u06cc:", None))
        self.txtMtoTahrirDate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0645\u062b\u0644\u0627\u064b 1405/07/27", None))
        self.lblMtoTahrirDescription.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0631\u062d \u06a9\u0627\u0644\u0627:", None))
        self.txtMtoTahrirDescription.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0634\u0631\u062d \u06a9\u0627\u0644\u0627\u06cc \u062f\u0631\u062e\u0648\u0627\u0633\u062a\u06cc", None))
        self.lblMtoTahrirQty.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u0627\u062f:", None))
        self.txtMtoTahrirQty.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u0627\u062f \u062f\u0631\u062e\u0648\u0627\u0633\u062a\u06cc", None))
        self.lblMtoTahrirUnit.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0627\u062d\u062f:", None))
        self.txtMtoTahrirUnit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0639\u062f\u062f\u060c \u0628\u0633\u062a\u0647...", None))
        self.lblMtoTahrirVahed.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0627\u062d\u062f \u0633\u0627\u0632\u0645\u0627\u0646\u06cc:", None))
        self.cmbMtoTahrirVahed.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0648\u0627\u062d\u062f \u0633\u0627\u0632\u0645\u0627\u0646\u06cc\u061b \u0627\u0632 \u0641\u0647\u0631\u0633\u062a \u0627\u0646\u062a\u062e\u0627\u0628 \u06a9\u0646\u06cc\u062f \u06cc\u0627 \u0628\u0646\u0648\u06cc\u0633\u06cc\u062f", None))
        self.lblMtoTahrirRecorder.setText(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a\u200c\u06a9\u0646\u0646\u062f\u0647:", None))
        self.txtMtoTahrirRecorder.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631 \u062b\u0628\u062a\u200c\u06a9\u0646\u0646\u062f\u0647", None))
        self.lblMtoTahrirTaeidkonandeh.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0623\u06cc\u06cc\u062f\u06a9\u0646\u0646\u062f\u0647:", None))
        self.cmbMtoTahrirTaeidkonandeh.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u062a\u0623\u06cc\u06cc\u062f\u06a9\u0646\u0646\u062f\u0647\u061b \u0627\u0646\u062a\u062e\u0627\u0628 \u06cc\u0627 \u0648\u0631\u0648\u062f \u0646\u0627\u0645", None))
        self.lblMtoTahrirEditor.setText(QCoreApplication.translate("MainWindow", u"\u0622\u062e\u0631\u06cc\u0646 \u0648\u06cc\u0631\u0627\u06cc\u0634:", None))
        self.txtMtoTahrirEditor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u0648\u06cc\u0631\u0627\u06cc\u0634\u200c\u06a9\u0646\u0646\u062f\u0647", None))
        self.lblMtoTahrirTahvilGirandeh.setText(QCoreApplication.translate("MainWindow", u"\u062a\u062d\u0648\u06cc\u0644\u200c\u06af\u06cc\u0631\u0646\u062f\u0647:", None))
        self.cmbMtoTahrirTahvilgirandeh.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u062a\u062d\u0648\u06cc\u0644\u200c\u06af\u06cc\u0631\u0646\u062f\u0647", None))
        self.btnMtoTahrirNew.setText(QCoreApplication.translate("MainWindow", u"\u062f\u0631\u062e\u0648\u0627\u0633\u062a \u062c\u062f\u06cc\u062f", None))
        self.btnMtoTahrirSave.setText(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a \u062f\u0631\u062e\u0648\u0627\u0633\u062a", None))
        self.btnMtoTahrirEdit.setText(QCoreApplication.translate("MainWindow", u"\u0630\u062e\u06cc\u0631\u0647 \u0648\u06cc\u0631\u0627\u06cc\u0634", None))
        self.btnMtoTahrirDelete.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0630\u0641 \u062f\u0631\u062e\u0648\u0627\u0633\u062a", None))
        self.btnMtoTahrirDeliver.setText(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a \u062a\u062d\u0648\u06cc\u0644", None))
        self.btnMtoTahrirRefresh.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0627\u0632\u062e\u0648\u0627\u0646\u06cc", None))
        ___qtablewidgetitem73 = self.tblMtoTahrirList.horizontalHeaderItem(0)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"\u0631\u062f\u06cc\u0641", None))
        ___qtablewidgetitem74 = self.tblMtoTahrirList.horizontalHeaderItem(1)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627\u0631\u06cc\u062e", None))
        ___qtablewidgetitem75 = self.tblMtoTahrirList.horizontalHeaderItem(2)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0631\u062d \u06a9\u0627\u0644\u0627", None))
        ___qtablewidgetitem76 = self.tblMtoTahrirList.horizontalHeaderItem(3)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u0627\u062f", None))
        ___qtablewidgetitem77 = self.tblMtoTahrirList.horizontalHeaderItem(4)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0627\u062d\u062f", None))
        ___qtablewidgetitem78 = self.tblMtoTahrirList.horizontalHeaderItem(5)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0627\u062d\u062f \u0633\u0627\u0632\u0645\u0627\u0646\u06cc", None))
        ___qtablewidgetitem79 = self.tblMtoTahrirList.horizontalHeaderItem(6)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a\u200c\u06a9\u0646\u0646\u062f\u0647", None))
        ___qtablewidgetitem80 = self.tblMtoTahrirList.horizontalHeaderItem(7)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0623\u06cc\u06cc\u062f\u06a9\u0646\u0646\u062f\u0647", None))
        ___qtablewidgetitem81 = self.tblMtoTahrirList.horizontalHeaderItem(8)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"\u062a\u062d\u0648\u06cc\u0644\u200c\u06af\u06cc\u0631\u0646\u062f\u0647", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabMtoTahrir), QCoreApplication.translate("MainWindow", u"\u062a\u0642\u0627\u0636\u0627\u06cc \u0644\u0648\u0627\u0632\u0645\u200c\u0627\u0644\u062a\u062d\u0631\u06cc\u0631", None))
        self.menuSystem.setTitle(QCoreApplication.translate("MainWindow", u"\u0633\u06cc\u0633\u062a\u0645", None))
        self.menuUsers.setTitle(QCoreApplication.translate("MainWindow", u"\u06a9\u0627\u0631\u0628\u0631\u0627\u0646", None))
        self.menuRepairs.setTitle(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u0645\u06cc\u0631\u0627\u062a", None))
        self.menuEquipment.setTitle(QCoreApplication.translate("MainWindow", u"\u062a\u062c\u0647\u06cc\u0632\u0627\u062a \u0648 \u0627\u0645\u0648\u0627\u0644", None))
        self.menuStationery.setTitle(QCoreApplication.translate("MainWindow", u"\u0644\u0648\u0627\u0632\u0645\u200c\u0627\u0644\u062a\u062d\u0631\u06cc\u0631", None))
        self.menuReports.setTitle(QCoreApplication.translate("MainWindow", u"\u06af\u0632\u0627\u0631\u0634\u200c\u0647\u0627", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"\u0631\u0627\u0647\u0646\u0645\u0627", None))
        self.lblStatusUser.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u0627\u0631\u0628\u0631: \u2014", None))
        self.lblStatusUnit.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0627\u062d\u062f: \u2014", None))
        self.lblStatusSecurity.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0648\u0639 \u06a9\u0627\u0631\u0628\u0631: \u2014", None))
        self.lblStatusLevel.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0637\u062d \u062f\u0633\u062a\u0631\u0633\u06cc: \u2014", None))
        self.lblStatusWeekday.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0648\u0632 \u0647\u0641\u062a\u0647", None))
        self.lblStatusDate.setText(QCoreApplication.translate("MainWindow", u"1405/07/24", None))
        self.lblStatusTime.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
    # retranslateUi

