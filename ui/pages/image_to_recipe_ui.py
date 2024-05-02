# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'image_to_recipe_ui.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)
from static import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(899, 538)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.top_frame = QFrame(Form)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(172, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.imagga_search_frame = QFrame(self.top_frame)
        self.imagga_search_frame.setObjectName(u"imagga_search_frame")
        self.imagga_search_frame.setMinimumSize(QSize(500, 0))
        self.imagga_search_frame.setStyleSheet(u"#imagga_search_frame {\n"
"	border-bottom: 1px solid black;\n"
"	background-color: #fff;\n"
"}\n"
"#imagga_search_frame QPushButton {\n"
"	padding: 5px 5px;\n"
"	border-radius: 15px;\n"
"}\n"
"#imagga_search_frame QPushButton:pressed {\n"
"	padding-left: 10px;\n"
"}\n"
"#imagga_search_frame QLineEdit {\n"
" 	border: none;\n"
"}")
        self.imagga_search_frame.setFrameShape(QFrame.StyledPanel)
        self.imagga_search_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.imagga_search_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.input_imageUrl = QLineEdit(self.imagga_search_frame)
        self.input_imageUrl.setObjectName(u"input_imageUrl")

        self.horizontalLayout.addWidget(self.input_imageUrl)

        self.imagga_searchButton = QPushButton(self.imagga_search_frame)
        self.imagga_searchButton.setObjectName(u"imagga_searchButton")
        self.imagga_searchButton.setMinimumSize(QSize(46, 0))
        font = QFont()
        font.setBold(False)
        self.imagga_searchButton.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.imagga_searchButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.imagga_searchButton)


        self.horizontalLayout_2.addWidget(self.imagga_search_frame)

        self.horizontalSpacer_2 = QSpacerItem(171, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout.addWidget(self.top_frame, 0, 0, 1, 1)

        self.middle_frame = QFrame(Form)
        self.middle_frame.setObjectName(u"middle_frame")
        self.middle_frame.setMinimumSize(QSize(881, 300))
        self.middle_frame.setFrameShape(QFrame.StyledPanel)
        self.middle_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.middle_frame, 2, 0, 1, 1)

        self.lower_frame = QFrame(Form)
        self.lower_frame.setObjectName(u"lower_frame")
        self.lower_frame.setMinimumSize(QSize(881, 50))
        self.lower_frame.setMaximumSize(QSize(16777215, 16777215))
        self.lower_frame.setStyleSheet(u"#lower_frame QPushButton {\n"
"	color:#fff;\n"
"	background-color: #29323c;\n"
"	padding: 5px 0px 5px 0px;\n"
"	text-align: center;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"#lower_frame QPushButton:hover {\n"
"	background-color: #485563;\n"
"}\n"
"\n"
"#lower_frame QPushButton:checked {\n"
"	background-color: #4398d8;\n"
"}")
        self.lower_frame.setFrameShape(QFrame.StyledPanel)
        self.lower_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.lower_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.getRecipeButton = QPushButton(self.lower_frame)
        self.getRecipeButton.setObjectName(u"getRecipeButton")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/arrow-right-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.getRecipeButton.setIcon(icon1)
        self.getRecipeButton.setAutoRepeatDelay(300)

        self.horizontalLayout_3.addWidget(self.getRecipeButton)


        self.gridLayout.addWidget(self.lower_frame, 4, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.input_imageUrl.setPlaceholderText(QCoreApplication.translate("Form", u"Image Url", None))
        self.imagga_searchButton.setText("")
        self.getRecipeButton.setText(QCoreApplication.translate("Form", u"get recipe", None))
    # retranslateUi

