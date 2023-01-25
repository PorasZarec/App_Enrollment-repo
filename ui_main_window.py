# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1313, 776)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidgetfront = QStackedWidget(self.centralwidget)
        self.stackedWidgetfront.setObjectName(u"stackedWidgetfront")
        self.register_page = QWidget()
        self.register_page.setObjectName(u"register_page")
        self.verticalLayout_14 = QVBoxLayout(self.register_page)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.top_frame_reg_pg = QFrame(self.register_page)
        self.top_frame_reg_pg.setObjectName(u"top_frame_reg_pg")
        self.top_frame_reg_pg.setFrameShape(QFrame.StyledPanel)
        self.top_frame_reg_pg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.top_frame_reg_pg)
        self.horizontalLayout_10.setSpacing(25)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(25, 15, 25, 15)
        self.center_header_frame = QFrame(self.top_frame_reg_pg)
        self.center_header_frame.setObjectName(u"center_header_frame")
        font = QFont()
        font.setFamilies([u"Segoe UI Black"])
        font.setPointSize(15)
        font.setBold(True)
        self.center_header_frame.setFont(font)
        self.center_header_frame.setFrameShape(QFrame.StyledPanel)
        self.center_header_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.center_header_frame)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.lbl_registration = QLabel(self.center_header_frame)
        self.lbl_registration.setObjectName(u"lbl_registration")

        self.verticalLayout_16.addWidget(self.lbl_registration, 0, Qt.AlignHCenter)


        self.horizontalLayout_10.addWidget(self.center_header_frame, 0, Qt.AlignLeft)

        self.right_header_frame = QFrame(self.top_frame_reg_pg)
        self.right_header_frame.setObjectName(u"right_header_frame")
        self.right_header_frame.setFrameShape(QFrame.StyledPanel)
        self.right_header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.right_header_frame)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.button_back_reg_pg = QPushButton(self.right_header_frame)
        self.button_back_reg_pg.setObjectName(u"button_back_reg_pg")
        self.button_back_reg_pg.setFont(font)

        self.horizontalLayout_18.addWidget(self.button_back_reg_pg, 0, Qt.AlignRight)


        self.horizontalLayout_10.addWidget(self.right_header_frame)


        self.verticalLayout_14.addWidget(self.top_frame_reg_pg, 0, Qt.AlignTop)

        self.body_middle_frame = QFrame(self.register_page)
        self.body_middle_frame.setObjectName(u"body_middle_frame")
        self.body_middle_frame.setFrameShape(QFrame.StyledPanel)
        self.body_middle_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.body_middle_frame)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.body_middle_frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1310, 664))
        self.horizontalLayout_12 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.middle_frame = QFrame(self.scrollAreaWidgetContents)
        self.middle_frame.setObjectName(u"middle_frame")
        self.middle_frame.setFrameShape(QFrame.StyledPanel)
        self.middle_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.middle_frame)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.middle_frame)
        self.frame_21.setObjectName(u"frame_21")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(False)
        self.frame_21.setFont(font1)
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_21)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(50)
        self.formLayout.setVerticalSpacing(30)
        self.formLayout.setContentsMargins(300, 20, 300, 20)
        self.label_12 = QLabel(self.frame_21)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_12)

        self.lineEdit_firstname = QLineEdit(self.frame_21)
        self.lineEdit_firstname.setObjectName(u"lineEdit_firstname")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_firstname)

        self.label_13 = QLabel(self.frame_21)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_13)

        self.line_Edit_lastname = QLineEdit(self.frame_21)
        self.line_Edit_lastname.setObjectName(u"line_Edit_lastname")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.line_Edit_lastname)

        self.label_14 = QLabel(self.frame_21)
        self.label_14.setObjectName(u"label_14")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_14)

        self.cmbbox_title = QComboBox(self.frame_21)
        self.cmbbox_title.addItem("")
        self.cmbbox_title.addItem("")
        self.cmbbox_title.setObjectName(u"cmbbox_title")
        self.cmbbox_title.setEditable(True)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.cmbbox_title)

        self.label_15 = QLabel(self.frame_21)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_15)

        self.spinBox_age = QSpinBox(self.frame_21)
        self.spinBox_age.setObjectName(u"spinBox_age")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.spinBox_age)

        self.label_16 = QLabel(self.frame_21)
        self.label_16.setObjectName(u"label_16")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_16)

        self.cmbbox_nationality = QComboBox(self.frame_21)
        self.cmbbox_nationality.addItem("")
        self.cmbbox_nationality.addItem("")
        self.cmbbox_nationality.setObjectName(u"cmbbox_nationality")
        self.cmbbox_nationality.setEditable(True)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.cmbbox_nationality)

        self.label_18 = QLabel(self.frame_21)
        self.label_18.setObjectName(u"label_18")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_18)

        self.spinBox_course = QSpinBox(self.frame_21)
        self.spinBox_course.setObjectName(u"spinBox_course")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.spinBox_course)

        self.label_19 = QLabel(self.frame_21)
        self.label_19.setObjectName(u"label_19")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_19)

        self.spinBox_semester = QSpinBox(self.frame_21)
        self.spinBox_semester.setObjectName(u"spinBox_semester")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.spinBox_semester)

        self.label_17 = QLabel(self.frame_21)
        self.label_17.setObjectName(u"label_17")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_17)

        self.checkBox_registered = QCheckBox(self.frame_21)
        self.checkBox_registered.setObjectName(u"checkBox_registered")
        font2 = QFont()
        font2.setBold(True)
        self.checkBox_registered.setFont(font2)
        self.checkBox_registered.setTristate(False)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.checkBox_registered)

        self.label_20 = QLabel(self.frame_21)
        self.label_20.setObjectName(u"label_20")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_20)

        self.checkBox_terms = QCheckBox(self.frame_21)
        self.checkBox_terms.setObjectName(u"checkBox_terms")
        self.checkBox_terms.setFont(font2)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.checkBox_terms)


        self.horizontalLayout_20.addWidget(self.frame_21)


        self.horizontalLayout_12.addWidget(self.middle_frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_17.addWidget(self.scrollArea)

        self.bottom_frame_reg_pg = QFrame(self.body_middle_frame)
        self.bottom_frame_reg_pg.setObjectName(u"bottom_frame_reg_pg")
        self.bottom_frame_reg_pg.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame_reg_pg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.bottom_frame_reg_pg)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(600, 30, 600, 30)
        self.button_submit_data = QPushButton(self.bottom_frame_reg_pg)
        self.button_submit_data.setObjectName(u"button_submit_data")
        self.button_submit_data.setFont(font)

        self.horizontalLayout_21.addWidget(self.button_submit_data)


        self.verticalLayout_17.addWidget(self.bottom_frame_reg_pg)


        self.verticalLayout_14.addWidget(self.body_middle_frame)

        self.bottom_version_frame_reg_pg = QFrame(self.register_page)
        self.bottom_version_frame_reg_pg.setObjectName(u"bottom_version_frame_reg_pg")
        self.bottom_version_frame_reg_pg.setFrameShape(QFrame.StyledPanel)
        self.bottom_version_frame_reg_pg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.bottom_version_frame_reg_pg)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_version_number = QLabel(self.bottom_version_frame_reg_pg)
        self.label_version_number.setObjectName(u"label_version_number")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Black"])
        font3.setBold(True)
        self.label_version_number.setFont(font3)

        self.verticalLayout_15.addWidget(self.label_version_number, 0, Qt.AlignHCenter)


        self.verticalLayout_14.addWidget(self.bottom_version_frame_reg_pg, 0, Qt.AlignBottom)

        self.stackedWidgetfront.addWidget(self.register_page)
        self.front_page = QWidget()
        self.front_page.setObjectName(u"front_page")
        self.verticalLayout_2 = QVBoxLayout(self.front_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.front_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.front_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.register_button = QPushButton(self.frame_5)
        self.register_button.setObjectName(u"register_button")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI Black"])
        font4.setPointSize(20)
        font4.setBold(True)
        self.register_button.setFont(font4)

        self.verticalLayout_3.addWidget(self.register_button, 0, Qt.AlignVCenter)


        self.horizontalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.view_button = QPushButton(self.frame_6)
        self.view_button.setObjectName(u"view_button")
        font5 = QFont()
        font5.setFamilies([u"Segoe UI Black"])
        font5.setPointSize(20)
        font5.setBold(True)
        font5.setItalic(False)
        self.view_button.setFont(font5)

        self.verticalLayout_4.addWidget(self.view_button, 0, Qt.AlignVCenter)


        self.horizontalLayout.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_7)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.front_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_3)

        self.stackedWidgetfront.addWidget(self.front_page)
        self.second_page = QWidget()
        self.second_page.setObjectName(u"second_page")
        self.verticalLayout_13 = QVBoxLayout(self.second_page)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.header_frame = QFrame(self.second_page)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header_frame_left = QFrame(self.header_frame)
        self.header_frame_left.setObjectName(u"header_frame_left")
        self.header_frame_left.setFrameShape(QFrame.StyledPanel)
        self.header_frame_left.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_frame_left)
        self.horizontalLayout_4.setSpacing(7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.header_frame_left)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.open_close_side_bar_button = QPushButton(self.frame_20)
        self.open_close_side_bar_button.setObjectName(u"open_close_side_bar_button")

        self.horizontalLayout_7.addWidget(self.open_close_side_bar_button, 0, Qt.AlignLeft|Qt.AlignTop)

        self.label_2 = QLabel(self.frame_20)
        self.label_2.setObjectName(u"label_2")
        font6 = QFont()
        font6.setFamilies([u"Segoe UI Black"])
        font6.setPointSize(10)
        font6.setBold(True)
        self.label_2.setFont(font6)

        self.horizontalLayout_7.addWidget(self.label_2)


        self.horizontalLayout_4.addWidget(self.frame_20, 0, Qt.AlignLeft)


        self.horizontalLayout_2.addWidget(self.header_frame_left)

        self.header_frame_center = QFrame(self.header_frame)
        self.header_frame_center.setObjectName(u"header_frame_center")
        self.header_frame_center.setFrameShape(QFrame.StyledPanel)
        self.header_frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_frame_center)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.header_frame_center)
        self.label.setObjectName(u"label")
        font7 = QFont()
        font7.setFamilies([u"Goma Octagon"])
        font7.setPointSize(14)
        self.label.setFont(font7)

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.header_frame_center)

        self.header_right_frame = QFrame(self.header_frame)
        self.header_right_frame.setObjectName(u"header_right_frame")
        self.header_right_frame.setFrameShape(QFrame.StyledPanel)
        self.header_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.header_right_frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.back_button_ = QPushButton(self.header_right_frame)
        self.back_button_.setObjectName(u"back_button_")
        self.back_button_.setFont(font6)

        self.horizontalLayout_11.addWidget(self.back_button_, 0, Qt.AlignRight)


        self.horizontalLayout_2.addWidget(self.header_right_frame)


        self.verticalLayout_13.addWidget(self.header_frame)

        self.main_body_frame = QFrame(self.second_page)
        self.main_body_frame.setObjectName(u"main_body_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_frame.sizePolicy().hasHeightForWidth())
        self.main_body_frame.setSizePolicy(sizePolicy)
        self.main_body_frame.setFrameShape(QFrame.NoFrame)
        self.main_body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.main_body_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.left_menu_cont_frame = QFrame(self.main_body_frame)
        self.left_menu_cont_frame.setObjectName(u"left_menu_cont_frame")
        self.left_menu_cont_frame.setMinimumSize(QSize(220, 0))
        self.left_menu_cont_frame.setMaximumSize(QSize(20, 16777215))
        self.left_menu_cont_frame.setStyleSheet(u"")
        self.left_menu_cont_frame.setFrameShape(QFrame.StyledPanel)
        self.left_menu_cont_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.left_menu_cont_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.menu_frame = QFrame(self.left_menu_cont_frame)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMinimumSize(QSize(160, 0))
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.menu_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(15, 15, 15, 15)
        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_10, 15, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 5, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 10, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 0, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_7, 11, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 1, 1, 1, 1)

        self.lbl_college_db = QLabel(self.menu_frame)
        self.lbl_college_db.setObjectName(u"lbl_college_db")
        self.lbl_college_db.setFont(font3)
        self.lbl_college_db.setMargin(5)

        self.gridLayout.addWidget(self.lbl_college_db, 9, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_8, 12, 1, 1, 1)

        self.college_page_button = QPushButton(self.menu_frame)
        self.college_page_button.setObjectName(u"college_page_button")
        self.college_page_button.setStyleSheet(u"")

        self.gridLayout.addWidget(self.college_page_button, 9, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_9, 13, 1, 1, 1)

        self.label_6 = QLabel(self.menu_frame)
        self.label_6.setObjectName(u"label_6")
        font8 = QFont()
        font8.setFamilies([u"Segoe UI Black"])
        font8.setPointSize(9)
        font8.setBold(True)
        font8.setItalic(True)
        font8.setUnderline(True)
        self.label_6.setFont(font8)
        self.label_6.setMargin(5)

        self.gridLayout.addWidget(self.label_6, 6, 1, 1, 1)

        self.elementary_page_button = QPushButton(self.menu_frame)
        self.elementary_page_button.setObjectName(u"elementary_page_button")
        self.elementary_page_button.setStyleSheet(u"")

        self.gridLayout.addWidget(self.elementary_page_button, 8, 0, 1, 1)

        self.lbl_elem_db = QLabel(self.menu_frame)
        self.lbl_elem_db.setObjectName(u"lbl_elem_db")
        self.lbl_elem_db.setFont(font3)
        self.lbl_elem_db.setMargin(5)

        self.gridLayout.addWidget(self.lbl_elem_db, 8, 1, 1, 1)

        self.lbl_reg_queue_db = QLabel(self.menu_frame)
        self.lbl_reg_queue_db.setObjectName(u"lbl_reg_queue_db")
        self.lbl_reg_queue_db.setFont(font3)
        self.lbl_reg_queue_db.setMargin(5)

        self.gridLayout.addWidget(self.lbl_reg_queue_db, 7, 1, 1, 1)

        self.queue_data = QPushButton(self.menu_frame)
        self.queue_data.setObjectName(u"queue_data")
        self.queue_data.setStyleSheet(u"")

        self.gridLayout.addWidget(self.queue_data, 7, 0, 1, 1)


        self.horizontalLayout_6.addWidget(self.menu_frame)


        self.horizontalLayout_5.addWidget(self.left_menu_cont_frame)

        self.main__body_contents = QFrame(self.main_body_frame)
        self.main__body_contents.setObjectName(u"main__body_contents")
        self.main__body_contents.setFrameShape(QFrame.StyledPanel)
        self.main__body_contents.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.main__body_contents)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.main_body_stackedWidget = QStackedWidget(self.main__body_contents)
        self.main_body_stackedWidget.setObjectName(u"main_body_stackedWidget")
        self.mixData = QWidget()
        self.mixData.setObjectName(u"mixData")
        self.verticalLayout_6 = QVBoxLayout(self.mixData)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_8 = QFrame(self.mixData)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font6)

        self.horizontalLayout_8.addWidget(self.label_7)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFont(font6)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.frame_9)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.searchLineEdit = QLineEdit(self.frame_9)
        self.searchLineEdit.setObjectName(u"searchLineEdit")

        self.horizontalLayout_9.addWidget(self.searchLineEdit)


        self.horizontalLayout_8.addWidget(self.frame_9, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_8)

        self.frame_10 = QFrame(self.mixData)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.frame_10)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(527, 0))

        self.horizontalLayout_15.addWidget(self.tableWidget)


        self.verticalLayout_6.addWidget(self.frame_10)

        self.main_body_stackedWidget.addWidget(self.mixData)
        self.elementary_data = QWidget()
        self.elementary_data.setObjectName(u"elementary_data")
        self.verticalLayout_8 = QVBoxLayout(self.elementary_data)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.header_elementary_tbl = QFrame(self.elementary_data)
        self.header_elementary_tbl.setObjectName(u"header_elementary_tbl")
        self.header_elementary_tbl.setFrameShape(QFrame.StyledPanel)
        self.header_elementary_tbl.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.header_elementary_tbl)
        self.horizontalLayout_13.setSpacing(7)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(11, 11, 11, 11)
        self.label_9 = QLabel(self.header_elementary_tbl)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font6)

        self.horizontalLayout_13.addWidget(self.label_9)

        self.frame_13 = QFrame(self.header_elementary_tbl)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFont(font6)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_4 = QLabel(self.frame_13)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font6)

        self.horizontalLayout_14.addWidget(self.label_4)

        self.searchLineEdit_elem = QLineEdit(self.frame_13)
        self.searchLineEdit_elem.setObjectName(u"searchLineEdit_elem")
        self.searchLineEdit_elem.setFont(font6)

        self.horizontalLayout_14.addWidget(self.searchLineEdit_elem)


        self.horizontalLayout_13.addWidget(self.frame_13, 0, Qt.AlignRight)


        self.verticalLayout_8.addWidget(self.header_elementary_tbl)

        self.frame_14 = QFrame(self.elementary_data)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_14)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_elem = QTableWidget(self.frame_14)
        if (self.tableWidget_elem.columnCount() < 8):
            self.tableWidget_elem.setColumnCount(8)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_elem.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_elem.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_elem.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_elem.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_elem.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_elem.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_elem.setHorizontalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_elem.setHorizontalHeaderItem(7, __qtablewidgetitem15)
        self.tableWidget_elem.setObjectName(u"tableWidget_elem")
        self.tableWidget_elem.setMinimumSize(QSize(527, 0))

        self.verticalLayout_9.addWidget(self.tableWidget_elem)


        self.verticalLayout_8.addWidget(self.frame_14)

        self.main_body_stackedWidget.addWidget(self.elementary_data)
        self.college_data = QWidget()
        self.college_data.setObjectName(u"college_data")
        self.verticalLayout_10 = QVBoxLayout(self.college_data)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.header_college_table = QFrame(self.college_data)
        self.header_college_table.setObjectName(u"header_college_table")
        self.header_college_table.setFrameShape(QFrame.StyledPanel)
        self.header_college_table.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.header_college_table)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_10 = QLabel(self.header_college_table)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font6)

        self.horizontalLayout_16.addWidget(self.label_10)

        self.frame_17 = QFrame(self.header_college_table)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFont(font6)
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_5 = QLabel(self.frame_17)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font6)

        self.horizontalLayout_17.addWidget(self.label_5)

        self.searchLineEdit_college = QLineEdit(self.frame_17)
        self.searchLineEdit_college.setObjectName(u"searchLineEdit_college")
        self.searchLineEdit_college.setFont(font6)

        self.horizontalLayout_17.addWidget(self.searchLineEdit_college)


        self.horizontalLayout_16.addWidget(self.frame_17, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.header_college_table)

        self.frame_18 = QFrame(self.college_data)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_18)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_college = QTableWidget(self.frame_18)
        if (self.tableWidget_college.columnCount() < 8):
            self.tableWidget_college.setColumnCount(8)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_college.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_college.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_college.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_college.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_college.setHorizontalHeaderItem(4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_college.setHorizontalHeaderItem(5, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_college.setHorizontalHeaderItem(6, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_college.setHorizontalHeaderItem(7, __qtablewidgetitem23)
        self.tableWidget_college.setObjectName(u"tableWidget_college")
        self.tableWidget_college.setMinimumSize(QSize(527, 0))

        self.verticalLayout_11.addWidget(self.tableWidget_college)


        self.verticalLayout_10.addWidget(self.frame_18)

        self.main_body_stackedWidget.addWidget(self.college_data)

        self.verticalLayout_5.addWidget(self.main_body_stackedWidget)


        self.horizontalLayout_5.addWidget(self.main__body_contents)


        self.verticalLayout_13.addWidget(self.main_body_frame)

        self.footer_frame = QFrame(self.second_page)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frm_apply_changes = QFrame(self.footer_frame)
        self.frm_apply_changes.setObjectName(u"frm_apply_changes")
        self.frm_apply_changes.setFrameShape(QFrame.StyledPanel)
        self.frm_apply_changes.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frm_apply_changes)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(240, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer)

        self.lbl_apply = QLabel(self.frm_apply_changes)
        self.lbl_apply.setObjectName(u"lbl_apply")
        font9 = QFont()
        font9.setFamilies([u"Segoe UI Black"])
        font9.setPointSize(12)
        font9.setBold(True)
        font9.setItalic(True)
        self.lbl_apply.setFont(font9)
        self.lbl_apply.setMargin(5)

        self.horizontalLayout_22.addWidget(self.lbl_apply)

        self.btn_save_all_data = QPushButton(self.frm_apply_changes)
        self.btn_save_all_data.setObjectName(u"btn_save_all_data")
        font10 = QFont()
        font10.setFamilies([u"Segoe UI Black"])
        font10.setPointSize(12)
        font10.setBold(True)
        font10.setItalic(False)
        font10.setUnderline(False)
        self.btn_save_all_data.setFont(font10)

        self.horizontalLayout_22.addWidget(self.btn_save_all_data)

        self.horizontalSpacer_2 = QSpacerItem(90, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_19.addWidget(self.frm_apply_changes, 0, Qt.AlignLeft)

        self.frm_delete_select = QFrame(self.footer_frame)
        self.frm_delete_select.setObjectName(u"frm_delete_select")
        self.frm_delete_select.setFrameShape(QFrame.StyledPanel)
        self.frm_delete_select.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frm_delete_select)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frm_delete_select)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font9)

        self.horizontalLayout_23.addWidget(self.label_3)

        self.btn_delete_selected = QPushButton(self.frm_delete_select)
        self.btn_delete_selected.setObjectName(u"btn_delete_selected")
        font11 = QFont()
        font11.setFamilies([u"Segoe UI Black"])
        font11.setPointSize(12)
        font11.setBold(True)
        self.btn_delete_selected.setFont(font11)

        self.horizontalLayout_23.addWidget(self.btn_delete_selected)

        self.horizontalSpacer_3 = QSpacerItem(90, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_3)


        self.horizontalLayout_19.addWidget(self.frm_delete_select, 0, Qt.AlignLeft)

        self.frm_refresh = QFrame(self.footer_frame)
        self.frm_refresh.setObjectName(u"frm_refresh")
        self.frm_refresh.setFrameShape(QFrame.StyledPanel)
        self.frm_refresh.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frm_refresh)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.lbl_refresh = QLabel(self.frm_refresh)
        self.lbl_refresh.setObjectName(u"lbl_refresh")
        self.lbl_refresh.setFont(font9)

        self.horizontalLayout_24.addWidget(self.lbl_refresh, 0, Qt.AlignRight)

        self.btn_refresh_page = QPushButton(self.frm_refresh)
        self.btn_refresh_page.setObjectName(u"btn_refresh_page")
        self.btn_refresh_page.setFont(font11)

        self.horizontalLayout_24.addWidget(self.btn_refresh_page, 0, Qt.AlignLeft)


        self.horizontalLayout_19.addWidget(self.frm_refresh)


        self.verticalLayout_13.addWidget(self.footer_frame)

        self.footer_version_frame = QFrame(self.second_page)
        self.footer_version_frame.setObjectName(u"footer_version_frame")
        self.footer_version_frame.setFrameShape(QFrame.NoFrame)
        self.footer_version_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.footer_version_frame)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.version_ = QLabel(self.footer_version_frame)
        self.version_.setObjectName(u"version_")
        self.version_.setFont(font3)

        self.verticalLayout_12.addWidget(self.version_, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_13.addWidget(self.footer_version_frame)

        self.stackedWidgetfront.addWidget(self.second_page)

        self.verticalLayout.addWidget(self.stackedWidgetfront)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1313, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidgetfront.setCurrentIndex(1)
        self.cmbbox_title.setCurrentIndex(0)
        self.main_body_stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_registration.setText(QCoreApplication.translate("MainWindow", u"REGISTRATION", None))
        self.button_back_reg_pg.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Firstname", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Lastname", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.cmbbox_title.setItemText(0, QCoreApplication.translate("MainWindow", u"Male", None))
        self.cmbbox_title.setItemText(1, QCoreApplication.translate("MainWindow", u"Female", None))

        self.cmbbox_title.setCurrentText(QCoreApplication.translate("MainWindow", u"Male", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Nationality", None))
        self.cmbbox_nationality.setItemText(0, "")
        self.cmbbox_nationality.setItemText(1, QCoreApplication.translate("MainWindow", u"Filipino", None))

        self.label_18.setText(QCoreApplication.translate("MainWindow", u"#Completed Course", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"#Completed Semester", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Registration status", None))
        self.checkBox_registered.setText(QCoreApplication.translate("MainWindow", u"Currently Registered", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Terms And Condition", None))
        self.checkBox_terms.setText(QCoreApplication.translate("MainWindow", u"I Accept Terms and Conditions", None))
        self.button_submit_data.setText(QCoreApplication.translate("MainWindow", u"SUBMIT", None))
        self.label_version_number.setText(QCoreApplication.translate("MainWindow", u"Version 1.0.0", None))
        self.register_button.setText(QCoreApplication.translate("MainWindow", u"REGISTER", None))
        self.view_button.setText(QCoreApplication.translate("MainWindow", u"VIEW", None))
        self.open_close_side_bar_button.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Database Manager", None))
        self.back_button_.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.lbl_college_db.setText(QCoreApplication.translate("MainWindow", u"COLLEGE", None))
        self.college_page_button.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"NAVIGATE TABLES:", None))
        self.elementary_page_button.setText("")
        self.lbl_elem_db.setText(QCoreApplication.translate("MainWindow", u"ELEMENTARY", None))
        self.lbl_reg_queue_db.setText(QCoreApplication.translate("MainWindow", u"REGISTRATION QUEUE", None))
        self.queue_data.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Registration Queue Database", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"FILTER DATA:", None))
        self.searchLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Data", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Firstname", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Lastname", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Nationality", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Registration", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Semester", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Course", None));
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"ELEMENTARY DATA", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"FILTER DATA:", None))
        self.searchLineEdit_elem.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Data", None))
        ___qtablewidgetitem8 = self.tableWidget_elem.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Firstname", None));
        ___qtablewidgetitem9 = self.tableWidget_elem.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Lastname", None));
        ___qtablewidgetitem10 = self.tableWidget_elem.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem11 = self.tableWidget_elem.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem12 = self.tableWidget_elem.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Nationality", None));
        ___qtablewidgetitem13 = self.tableWidget_elem.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Registration", None));
        ___qtablewidgetitem14 = self.tableWidget_elem.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Semester", None));
        ___qtablewidgetitem15 = self.tableWidget_elem.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Course", None));
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"COLLEGE DATA", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"FILTER DATA:", None))
        self.searchLineEdit_college.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Data", None))
        ___qtablewidgetitem16 = self.tableWidget_college.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Firstname", None));
        ___qtablewidgetitem17 = self.tableWidget_college.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Lastname", None));
        ___qtablewidgetitem18 = self.tableWidget_college.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem19 = self.tableWidget_college.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem20 = self.tableWidget_college.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Nationality", None));
        ___qtablewidgetitem21 = self.tableWidget_college.horizontalHeaderItem(5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Registration", None));
        ___qtablewidgetitem22 = self.tableWidget_college.horizontalHeaderItem(6)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Semester", None));
        ___qtablewidgetitem23 = self.tableWidget_college.horizontalHeaderItem(7)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Course", None));
        self.lbl_apply.setText(QCoreApplication.translate("MainWindow", u"APPLY CHANGES :", None))
        self.btn_save_all_data.setText(QCoreApplication.translate("MainWindow", u"SAVE", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"DELETE SELECTED :", None))
        self.btn_delete_selected.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.lbl_refresh.setText(QCoreApplication.translate("MainWindow", u"REFRESH TABLE :", None))
        self.btn_refresh_page.setText(QCoreApplication.translate("MainWindow", u"REFRESH", None))
        self.version_.setText(QCoreApplication.translate("MainWindow", u"Version 1.0.0.00", None))
    # retranslateUi

