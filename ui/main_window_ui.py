# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSplitter, QTabWidget,
    QToolBox, QVBoxLayout, QWidget)
from static import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1427, 721)
        MainWindow.setMaximumSize(QSize(1427, 721))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(0)
        self.menue_widget = QWidget(self.splitter)
        self.menue_widget.setObjectName(u"menue_widget")
        self.menue_widget.setMinimumSize(QSize(250, 0))
        self.menue_widget.setStyleSheet(u"background: #29323c;\n"
"color: #fff;\n"
"border: none")
        self.gridLayout = QGridLayout(self.menue_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.toolBox = QToolBox(self.menue_widget)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"#toolBox {\n"
"	color:#fff;\n"
"}\n"
"\n"
"#toolBox::tab {\n"
"	padding-left:5px;\n"
"	text-align:left;\n"
"    border-radius:2px;\n"
"}\n"
"\n"
"#toolBox::tab:selected {\n"
"	background-color: #485563;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"#toolBox QPushButton {\n"
"	padding: 5px 0px 5px 20px;\n"
"	text-align: left;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"#toolBox QPushButton:hover {\n"
"	background-color: #485563;\n"
"}\n"
"\n"
"#toolBox QPushButton:checked {\n"
"	background-color: #4398d8;\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 238, 619))
        self.page.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(self.page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.homeButton = QPushButton(self.page)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setMinimumSize(QSize(0, 0))
        self.homeButton.setMaximumSize(QSize(12121212, 16777215))
        self.homeButton.setFocusPolicy(Qt.NoFocus)
        self.homeButton.setCheckable(True)

        self.verticalLayout.addWidget(self.homeButton)

        self.pushButton_2 = QPushButton(self.page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 0))
        self.pushButton_2.setMaximumSize(QSize(12121121, 16777215))
        self.pushButton_2.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout.addWidget(self.pushButton_2)

        self.verticalSpacer = QSpacerItem(20, 494, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        icon = QIcon()
        icon.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page, icon, u"General")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 238, 619))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/book-open.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_2, icon1, u"Recipes")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 238, 619))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_3, icon2, u"About")

        self.gridLayout.addWidget(self.toolBox, 0, 0, 1, 1)

        self.splitter.addWidget(self.menue_widget)
        self.main_widget = QWidget(self.splitter)
        self.main_widget.setObjectName(u"main_widget")
        self.gridLayout_2 = QGridLayout(self.main_widget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.search_widget = QWidget(self.main_widget)
        self.search_widget.setObjectName(u"search_widget")
        self.search_widget.setStyleSheet(u"#search_widget {\n"
"	background-color: #29323c ;\n"
"}\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(self.search_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_3 = QPushButton(self.search_widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(30, 30))
        self.pushButton_3.setMaximumSize(QSize(30, 30))
        self.pushButton_3.setStyleSheet(u"background-color: #29323c ;\n"
"border: none;")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/arrow-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icons/icons/arrow-right.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QSize(24, 24))
        self.pushButton_3.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.horizontalSpacer = QSpacerItem(334, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.search_frame = QFrame(self.search_widget)
        self.search_frame.setObjectName(u"search_frame")
        self.search_frame.setMinimumSize(QSize(500, 0))
        self.search_frame.setStyleSheet(u"#search_frame {\n"
"	border: 1px solid #485563;\n"
"	border-radius: 20px;\n"
"	background-color: #fff;\n"
"}\n"
"#search_frame QPushButton {\n"
"	padding: 5px 5px;\n"
"	border-radius: 15px;\n"
"}\n"
"#search_frame QPushButton:pressed {\n"
"	padding-left: 10px;\n"
"}\n"
"#search_frame QLineEdit {\n"
" 	border: none;\n"
"}")
        self.search_frame.setFrameShape(QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.search_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, 10, 5, -1)
        self.lineEdit = QLineEdit(self.search_frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(300, 0))
        self.lineEdit.setMaximumSize(QSize(16777215, 1212121))

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_4 = QPushButton(self.search_frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(50, 0))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon4)

        self.horizontalLayout.addWidget(self.pushButton_4)


        self.horizontalLayout_2.addWidget(self.search_frame)

        self.horizontalSpacer_2 = QSpacerItem(334, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.user_label = QLabel(self.search_widget)
        self.user_label.setObjectName(u"user_label")
        self.user_label.setMinimumSize(QSize(30, 30))
        self.user_label.setMaximumSize(QSize(30, 30))
        self.user_label.setStyleSheet(u"#user_label {\n"
"	background-color: #fff;\n"
"	border: 1px solid #F2F4F4;\n"
"	padding: 5px 5px;\n"
"	border-radius: 15%;\n"
"}")
        self.user_label.setPixmap(QPixmap(u":/icons/icons/user.svg"))
        self.user_label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.user_label)


        self.gridLayout_2.addWidget(self.search_widget, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(self.main_widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"#tabWidget {\n"
"	background-color: #fff;\n"
"}\n"
"\n"
"QTabBar::close-button {\n"
"	margin-left: 3px;\n"
"	image: url(:/icons/icons/x-circle (1).svg);\n"
"}\n"
"\n"
"QTabBar::close-button:hover {\n"
"	margin-left: 3px;\n"
"	image: url(:/icons/icons/x-circle-red.svg);\n"
"}\n"
"")
        self.tabWidget.setTabsClosable(True)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")

        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.splitter.addWidget(self.main_widget)

        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_3.toggled.connect(self.menue_widget.setHidden)

        self.toolBox.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"General", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Recipes", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"About", None))
        self.pushButton_3.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search recipe...", None))
        self.pushButton_4.setText("")
        self.user_label.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
    # retranslateUi

