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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QFormLayout, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import icons_rc_rc

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
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.left_header_frame = QFrame(self.top_frame_reg_pg)
        self.left_header_frame.setObjectName(u"left_header_frame")
        self.left_header_frame.setFrameShape(QFrame.StyledPanel)
        self.left_header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.left_header_frame)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_10.addWidget(self.left_header_frame)

        self.center_header_frame = QFrame(self.top_frame_reg_pg)
        self.center_header_frame.setObjectName(u"center_header_frame")
        font = QFont()
        font.setFamilies([u"Segoe UI Black"])
        font.setPointSize(15)
        font.setBold(True)
        self.center_header_frame.setFont(font)
        self.center_header_frame.setFrameShape(QFrame.StyledPanel)
        self.center_header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.center_header_frame)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.lbl_registration = QLabel(self.center_header_frame)
        self.lbl_registration.setObjectName(u"lbl_registration")

        self.horizontalLayout_26.addWidget(self.lbl_registration, 0, Qt.AlignHCenter)


        self.horizontalLayout_10.addWidget(self.center_header_frame)

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
        self.button_back_reg_pg.setCursor(QCursor(Qt.PointingHandCursor))

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
        self.scrollAreaWidgetContents.setGeometry(QRect(-14, 0, 1826, 545))
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
        self.frame_21.setLayoutDirection(Qt.LeftToRight)
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_21)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(70)
        self.gridLayout.setVerticalSpacing(30)
        self.gridLayout.setContentsMargins(100, 10, 100, 10)
        self.label_12 = QLabel(self.frame_21)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 0, 0, 1, 1)

        self.lineEdit_firstname = QLineEdit(self.frame_21)
        self.lineEdit_firstname.setObjectName(u"lineEdit_firstname")

        self.gridLayout.addWidget(self.lineEdit_firstname, 0, 1, 1, 1)

        self.label_20 = QLabel(self.frame_21)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout.addWidget(self.label_20, 11, 2, 1, 1)

        self.checkBox_terms = QCheckBox(self.frame_21)
        self.checkBox_terms.setObjectName(u"checkBox_terms")
        font2 = QFont()
        font2.setBold(True)
        self.checkBox_terms.setFont(font2)

        self.gridLayout.addWidget(self.checkBox_terms, 11, 3, 1, 1)

        self.lineEdit_grade_year_lvl = QLineEdit(self.frame_21)
        self.lineEdit_grade_year_lvl.setObjectName(u"lineEdit_grade_year_lvl")

        self.gridLayout.addWidget(self.lineEdit_grade_year_lvl, 1, 3, 1, 1)

        self.cmbbox_title = QComboBox(self.frame_21)
        self.cmbbox_title.addItem("")
        self.cmbbox_title.addItem("")
        self.cmbbox_title.setObjectName(u"cmbbox_title")
        self.cmbbox_title.setCursor(QCursor(Qt.CrossCursor))
        self.cmbbox_title.setLayoutDirection(Qt.RightToLeft)
        self.cmbbox_title.setEditable(True)

        self.gridLayout.addWidget(self.cmbbox_title, 5, 3, 1, 1)

        self.label_24 = QLabel(self.frame_21)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout.addWidget(self.label_24, 1, 2, 1, 1)

        self.spinBox_semester = QSpinBox(self.frame_21)
        self.spinBox_semester.setObjectName(u"spinBox_semester")
        self.spinBox_semester.setCursor(QCursor(Qt.CrossCursor))
        self.spinBox_semester.setLayoutDirection(Qt.LeftToRight)
        self.spinBox_semester.setMinimum(0)
        self.spinBox_semester.setMaximum(2)
        self.spinBox_semester.setValue(0)

        self.gridLayout.addWidget(self.spinBox_semester, 6, 3, 1, 1)

        self.cmbbox_course = QComboBox(self.frame_21)
        self.cmbbox_course.addItem("")
        self.cmbbox_course.addItem("")
        self.cmbbox_course.setObjectName(u"cmbbox_course")
        self.cmbbox_course.setCursor(QCursor(Qt.CrossCursor))
        self.cmbbox_course.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.cmbbox_course, 6, 1, 1, 1)

        self.line_Edit_lastname = QLineEdit(self.frame_21)
        self.line_Edit_lastname.setObjectName(u"line_Edit_lastname")

        self.gridLayout.addWidget(self.line_Edit_lastname, 1, 1, 1, 1)

        self.label_13 = QLabel(self.frame_21)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 1, 0, 1, 1)

        self.birth_dateEdit = QDateEdit(self.frame_21)
        self.birth_dateEdit.setObjectName(u"birth_dateEdit")
        self.birth_dateEdit.setCursor(QCursor(Qt.CrossCursor))
        self.birth_dateEdit.setLayoutDirection(Qt.LeftToRight)
        self.birth_dateEdit.setCalendarPopup(True)

        self.gridLayout.addWidget(self.birth_dateEdit, 5, 1, 1, 1)

        self.label_7 = QLabel(self.frame_21)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)

        self.lineEdit_address = QLineEdit(self.frame_21)
        self.lineEdit_address.setObjectName(u"lineEdit_address")

        self.gridLayout.addWidget(self.lineEdit_address, 2, 1, 1, 1)

        self.label_22 = QLabel(self.frame_21)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout.addWidget(self.label_22, 5, 0, 1, 1)

        self.label_19 = QLabel(self.frame_21)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 6, 2, 1, 1)

        self.label_17 = QLabel(self.frame_21)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 11, 0, 1, 1)

        self.label_18 = QLabel(self.frame_21)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 6, 0, 1, 1)

        self.checkBox_registered = QCheckBox(self.frame_21)
        self.checkBox_registered.setObjectName(u"checkBox_registered")
        self.checkBox_registered.setFont(font2)
        self.checkBox_registered.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_registered, 11, 1, 1, 1)

        self.label_14 = QLabel(self.frame_21)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 5, 2, 1, 1)

        self.label_23 = QLabel(self.frame_21)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout.addWidget(self.label_23, 0, 2, 1, 1)

        self.lineEdit_middleName = QLineEdit(self.frame_21)
        self.lineEdit_middleName.setObjectName(u"lineEdit_middleName")

        self.gridLayout.addWidget(self.lineEdit_middleName, 0, 3, 1, 1)

        self.label_16 = QLabel(self.frame_21)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 4, 0, 1, 1)

        self.cmbbox_nationality = QComboBox(self.frame_21)
        self.cmbbox_nationality.addItem("")
        self.cmbbox_nationality.addItem("")
        self.cmbbox_nationality.setObjectName(u"cmbbox_nationality")
        self.cmbbox_nationality.setCursor(QCursor(Qt.IBeamCursor))
        self.cmbbox_nationality.setLayoutDirection(Qt.LeftToRight)
        self.cmbbox_nationality.setEditable(True)

        self.gridLayout.addWidget(self.cmbbox_nationality, 4, 1, 1, 1)

        self.lineEdit_telephone = QLineEdit(self.frame_21)
        self.lineEdit_telephone.setObjectName(u"lineEdit_telephone")

        self.gridLayout.addWidget(self.lineEdit_telephone, 2, 3, 1, 1)

        self.label_25 = QLabel(self.frame_21)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout.addWidget(self.label_25, 2, 2, 1, 1)

        self.label_15 = QLabel(self.frame_21)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 4, 2, 1, 1)

        self.spinBox_age = QSpinBox(self.frame_21)
        self.spinBox_age.setObjectName(u"spinBox_age")
        self.spinBox_age.setCursor(QCursor(Qt.CrossCursor))
        self.spinBox_age.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.spinBox_age, 4, 3, 1, 1)


        self.horizontalLayout_20.addWidget(self.frame_21)


        self.horizontalLayout_12.addWidget(self.middle_frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_17.addWidget(self.scrollArea)

        self.bottom_frame_reg_pg = QFrame(self.body_middle_frame)
        self.bottom_frame_reg_pg.setObjectName(u"bottom_frame_reg_pg")
        self.bottom_frame_reg_pg.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame_reg_pg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.bottom_frame_reg_pg)
        self.horizontalLayout_21.setSpacing(8)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(600, 10, 600, 10)
        self.button_submit_data = QPushButton(self.bottom_frame_reg_pg)
        self.button_submit_data.setObjectName(u"button_submit_data")
        self.button_submit_data.setFont(font)
        self.button_submit_data.setCursor(QCursor(Qt.PointingHandCursor))

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
        self.register_button.setCursor(QCursor(Qt.PointingHandCursor))

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
        self.view_button.setCursor(QCursor(Qt.PointingHandCursor))

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
        self.open_close_side_bar_button.setMinimumSize(QSize(0, 0))
        self.open_close_side_bar_button.setBaseSize(QSize(0, 0))
        font6 = QFont()
        font6.setPointSize(8)
        font6.setBold(False)
        self.open_close_side_bar_button.setFont(font6)
        self.open_close_side_bar_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.open_close_side_bar_button.setIcon(icon)

        self.horizontalLayout_7.addWidget(self.open_close_side_bar_button, 0, Qt.AlignLeft|Qt.AlignTop)

        self.label_2 = QLabel(self.frame_20)
        self.label_2.setObjectName(u"label_2")
        font7 = QFont()
        font7.setFamilies([u"Segoe UI Black"])
        font7.setPointSize(10)
        font7.setBold(True)
        self.label_2.setFont(font7)

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
        font8 = QFont()
        font8.setFamilies([u"Goma Octagon"])
        font8.setPointSize(14)
        self.label.setFont(font8)

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.header_frame_center)

        self.header_right_frame = QFrame(self.header_frame)
        self.header_right_frame.setObjectName(u"header_right_frame")
        self.header_right_frame.setFrameShape(QFrame.StyledPanel)
        self.header_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.header_right_frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btn_back_second_page = QPushButton(self.header_right_frame)
        self.btn_back_second_page.setObjectName(u"btn_back_second_page")
        self.btn_back_second_page.setFont(font7)
        self.btn_back_second_page.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.btn_back_second_page, 0, Qt.AlignRight)


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
        self.left_menu_cont_frame.setMinimumSize(QSize(224, 0))
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
        self.formLayout_2 = QFormLayout(self.menu_frame)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(15, 15, 15, 15)
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(0, QFormLayout.FieldRole, self.verticalSpacer_5)

        self.label_6 = QLabel(self.menu_frame)
        self.label_6.setObjectName(u"label_6")
        font9 = QFont()
        font9.setFamilies([u"Segoe UI Black"])
        font9.setPointSize(9)
        font9.setBold(True)
        font9.setItalic(True)
        font9.setUnderline(True)
        self.label_6.setFont(font9)
        self.label_6.setMargin(5)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.label_6)

        self.queue_data = QPushButton(self.menu_frame)
        self.queue_data.setObjectName(u"queue_data")
        self.queue_data.setCursor(QCursor(Qt.PointingHandCursor))
        self.queue_data.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"icons/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.queue_data.setIcon(icon1)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.queue_data)

        self.lbl_reg_queue_db = QLabel(self.menu_frame)
        self.lbl_reg_queue_db.setObjectName(u"lbl_reg_queue_db")
        self.lbl_reg_queue_db.setMinimumSize(QSize(0, 0))
        self.lbl_reg_queue_db.setFont(font3)
        self.lbl_reg_queue_db.setMargin(5)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lbl_reg_queue_db)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(3, QFormLayout.FieldRole, self.verticalSpacer)

        self.BSIT_page_button = QPushButton(self.menu_frame)
        self.BSIT_page_button.setObjectName(u"BSIT_page_button")
        self.BSIT_page_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.BSIT_page_button.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"icons/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.BSIT_page_button.setIcon(icon2)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.BSIT_page_button)

        self.lbl_BSIT_db = QLabel(self.menu_frame)
        self.lbl_BSIT_db.setObjectName(u"lbl_BSIT_db")
        self.lbl_BSIT_db.setFont(font3)
        self.lbl_BSIT_db.setMargin(5)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.lbl_BSIT_db)

        self.COMSCI_page_button = QPushButton(self.menu_frame)
        self.COMSCI_page_button.setObjectName(u"COMSCI_page_button")
        self.COMSCI_page_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.COMSCI_page_button.setStyleSheet(u"")
        self.COMSCI_page_button.setIcon(icon2)

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.COMSCI_page_button)

        self.lbl_COMSCI_db = QLabel(self.menu_frame)
        self.lbl_COMSCI_db.setObjectName(u"lbl_COMSCI_db")
        self.lbl_COMSCI_db.setFont(font3)
        self.lbl_COMSCI_db.setMargin(5)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.lbl_COMSCI_db)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(6, QFormLayout.FieldRole, self.verticalSpacer_6)

        self.lbl_approve = QLabel(self.menu_frame)
        self.lbl_approve.setObjectName(u"lbl_approve")
        font10 = QFont()
        font10.setFamilies([u"Segoe UI Black"])
        font10.setPointSize(8)
        font10.setBold(True)
        font10.setItalic(True)
        font10.setUnderline(True)
        self.lbl_approve.setFont(font10)

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.lbl_approve)

        self.btn_approve_BSIT = QPushButton(self.menu_frame)
        self.btn_approve_BSIT.setObjectName(u"btn_approve_BSIT")
        icon3 = QIcon()
        icon3.addFile(u"icons/chevrons-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_approve_BSIT.setIcon(icon3)

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.btn_approve_BSIT)

        self.label_11 = QLabel(self.menu_frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.label_11)

        self.btn_approve_COMSCI = QPushButton(self.menu_frame)
        self.btn_approve_COMSCI.setObjectName(u"btn_approve_COMSCI")
        self.btn_approve_COMSCI.setIcon(icon3)

        self.formLayout_2.setWidget(10, QFormLayout.LabelRole, self.btn_approve_COMSCI)

        self.label_21 = QLabel(self.menu_frame)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font3)

        self.formLayout_2.setWidget(10, QFormLayout.FieldRole, self.label_21)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(11, QFormLayout.FieldRole, self.verticalSpacer_9)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(12, QFormLayout.FieldRole, self.verticalSpacer_10)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(7, QFormLayout.FieldRole, self.verticalSpacer_2)


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
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_8)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.dis_btn = QPushButton(self.frame_11)
        self.dis_btn.setObjectName(u"dis_btn")
        font11 = QFont()
        font11.setPointSize(15)
        self.dis_btn.setFont(font11)
        self.dis_btn.setIcon(icon1)

        self.horizontalLayout_27.addWidget(self.dis_btn)

        self.lbl_reg_que = QLabel(self.frame_11)
        self.lbl_reg_que.setObjectName(u"lbl_reg_que")
        font12 = QFont()
        font12.setFamilies([u"Segoe UI Black"])
        font12.setPointSize(10)
        font12.setBold(True)
        font12.setUnderline(True)
        self.lbl_reg_que.setFont(font12)

        self.horizontalLayout_27.addWidget(self.lbl_reg_que)


        self.horizontalLayout_8.addWidget(self.frame_11, 0, Qt.AlignLeft)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFont(font7)
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
        if (self.tableWidget.columnCount() < 9):
            self.tableWidget.setColumnCount(9)
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
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(527, 0))

        self.horizontalLayout_15.addWidget(self.tableWidget)


        self.verticalLayout_6.addWidget(self.frame_10)

        self.main_body_stackedWidget.addWidget(self.mixData)
        self.BSIT_table_data = QWidget()
        self.BSIT_table_data.setObjectName(u"BSIT_table_data")
        self.verticalLayout_8 = QVBoxLayout(self.BSIT_table_data)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.header_elementary_tbl = QFrame(self.BSIT_table_data)
        self.header_elementary_tbl.setObjectName(u"header_elementary_tbl")
        self.header_elementary_tbl.setFrameShape(QFrame.StyledPanel)
        self.header_elementary_tbl.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.header_elementary_tbl)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.header_elementary_tbl)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.pushButton = QPushButton(self.frame_15)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setIcon(icon2)

        self.horizontalLayout_28.addWidget(self.pushButton)

        self.label_9 = QLabel(self.frame_15)
        self.label_9.setObjectName(u"label_9")
        font13 = QFont()
        font13.setFamilies([u"Segoe UI Black"])
        font13.setPointSize(10)
        font13.setBold(True)
        font13.setItalic(False)
        font13.setUnderline(True)
        self.label_9.setFont(font13)

        self.horizontalLayout_28.addWidget(self.label_9)


        self.horizontalLayout_13.addWidget(self.frame_15, 0, Qt.AlignLeft)

        self.frame_13 = QFrame(self.header_elementary_tbl)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFont(font7)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_4 = QLabel(self.frame_13)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font7)

        self.horizontalLayout_14.addWidget(self.label_4)

        self.searchLineEdit_BSIT = QLineEdit(self.frame_13)
        self.searchLineEdit_BSIT.setObjectName(u"searchLineEdit_BSIT")
        self.searchLineEdit_BSIT.setFont(font7)

        self.horizontalLayout_14.addWidget(self.searchLineEdit_BSIT)


        self.horizontalLayout_13.addWidget(self.frame_13, 0, Qt.AlignRight)


        self.verticalLayout_8.addWidget(self.header_elementary_tbl)

        self.frame_14 = QFrame(self.BSIT_table_data)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_BSIT = QTableWidget(self.frame_14)
        if (self.tableWidget_BSIT.columnCount() < 9):
            self.tableWidget_BSIT.setColumnCount(9)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_BSIT.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_BSIT.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_BSIT.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_BSIT.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_BSIT.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_BSIT.setHorizontalHeaderItem(5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_BSIT.setHorizontalHeaderItem(6, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_BSIT.setHorizontalHeaderItem(7, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_BSIT.setHorizontalHeaderItem(8, __qtablewidgetitem17)
        self.tableWidget_BSIT.setObjectName(u"tableWidget_BSIT")
        self.tableWidget_BSIT.setMinimumSize(QSize(527, 0))

        self.horizontalLayout_30.addWidget(self.tableWidget_BSIT)


        self.verticalLayout_8.addWidget(self.frame_14)

        self.main_body_stackedWidget.addWidget(self.BSIT_table_data)
        self.COMSCI_table_data = QWidget()
        self.COMSCI_table_data.setObjectName(u"COMSCI_table_data")
        self.verticalLayout_10 = QVBoxLayout(self.COMSCI_table_data)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, -1, -1, 11)
        self.header_college_table = QFrame(self.COMSCI_table_data)
        self.header_college_table.setObjectName(u"header_college_table")
        self.header_college_table.setFrameShape(QFrame.StyledPanel)
        self.header_college_table.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.header_college_table)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.header_college_table)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_29.setSpacing(7)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(11, 11, 11, 11)
        self.pushButton_2 = QPushButton(self.frame_12)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setIcon(icon2)

        self.horizontalLayout_29.addWidget(self.pushButton_2)

        self.label_10 = QLabel(self.frame_12)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font12)

        self.horizontalLayout_29.addWidget(self.label_10)


        self.horizontalLayout_16.addWidget(self.frame_12, 0, Qt.AlignLeft)

        self.frame_17 = QFrame(self.header_college_table)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFont(font7)
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_5 = QLabel(self.frame_17)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font7)

        self.horizontalLayout_17.addWidget(self.label_5)

        self.searchLineEdit_COMSCI = QLineEdit(self.frame_17)
        self.searchLineEdit_COMSCI.setObjectName(u"searchLineEdit_COMSCI")
        self.searchLineEdit_COMSCI.setFont(font7)

        self.horizontalLayout_17.addWidget(self.searchLineEdit_COMSCI)


        self.horizontalLayout_16.addWidget(self.frame_17, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.header_college_table)

        self.frame_18 = QFrame(self.COMSCI_table_data)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_COMSCI = QTableWidget(self.frame_18)
        if (self.tableWidget_COMSCI.columnCount() < 9):
            self.tableWidget_COMSCI.setColumnCount(9)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_COMSCI.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_COMSCI.setHorizontalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_COMSCI.setHorizontalHeaderItem(2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_COMSCI.setHorizontalHeaderItem(3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_COMSCI.setHorizontalHeaderItem(4, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_COMSCI.setHorizontalHeaderItem(5, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_COMSCI.setHorizontalHeaderItem(6, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_COMSCI.setHorizontalHeaderItem(7, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_COMSCI.setHorizontalHeaderItem(8, __qtablewidgetitem26)
        self.tableWidget_COMSCI.setObjectName(u"tableWidget_COMSCI")
        self.tableWidget_COMSCI.setMinimumSize(QSize(527, 0))

        self.horizontalLayout_31.addWidget(self.tableWidget_COMSCI)


        self.verticalLayout_10.addWidget(self.frame_18)

        self.main_body_stackedWidget.addWidget(self.COMSCI_table_data)

        self.verticalLayout_5.addWidget(self.main_body_stackedWidget)


        self.horizontalLayout_5.addWidget(self.main__body_contents)


        self.verticalLayout_13.addWidget(self.main_body_frame)

        self.footer_frame = QFrame(self.second_page)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setMinimumSize(QSize(0, 40))
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
        self.lbl_apply = QLabel(self.frm_apply_changes)
        self.lbl_apply.setObjectName(u"lbl_apply")
        font14 = QFont()
        font14.setFamilies([u"Segoe UI Black"])
        font14.setPointSize(12)
        font14.setBold(True)
        font14.setItalic(True)
        self.lbl_apply.setFont(font14)
        self.lbl_apply.setMargin(5)

        self.horizontalLayout_22.addWidget(self.lbl_apply)

        self.btn_save_all_data = QPushButton(self.frm_apply_changes)
        self.btn_save_all_data.setObjectName(u"btn_save_all_data")
        font15 = QFont()
        font15.setFamilies([u"Segoe UI Black"])
        font15.setPointSize(12)
        font15.setBold(True)
        font15.setItalic(False)
        font15.setUnderline(False)
        self.btn_save_all_data.setFont(font15)
        self.btn_save_all_data.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_22.addWidget(self.btn_save_all_data)


        self.horizontalLayout_19.addWidget(self.frm_apply_changes, 0, Qt.AlignRight)

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
        font16 = QFont()
        font16.setFamilies([u"Segoe UI Black"])
        font16.setPointSize(12)
        font16.setBold(True)
        font16.setItalic(True)
        font16.setKerning(True)
        self.label_3.setFont(font16)
        self.label_3.setStyleSheet(u"")

        self.horizontalLayout_23.addWidget(self.label_3)

        self.btn_delete_selected = QPushButton(self.frm_delete_select)
        self.btn_delete_selected.setObjectName(u"btn_delete_selected")
        font17 = QFont()
        font17.setFamilies([u"Segoe UI Black"])
        font17.setPointSize(12)
        font17.setBold(True)
        font17.setItalic(False)
        font17.setStrikeOut(True)
        self.btn_delete_selected.setFont(font17)
        self.btn_delete_selected.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delete_selected.setStyleSheet(u"color:rgb(255, 0, 0)")

        self.horizontalLayout_23.addWidget(self.btn_delete_selected)


        self.horizontalLayout_19.addWidget(self.frm_delete_select, 0, Qt.AlignRight)

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
        self.lbl_refresh.setFont(font14)

        self.horizontalLayout_24.addWidget(self.lbl_refresh, 0, Qt.AlignRight)

        self.btn_refresh_page = QPushButton(self.frm_refresh)
        self.btn_refresh_page.setObjectName(u"btn_refresh_page")
        font18 = QFont()
        font18.setFamilies([u"Segoe UI Black"])
        font18.setPointSize(12)
        font18.setBold(True)
        self.btn_refresh_page.setFont(font18)
        self.btn_refresh_page.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_24.addWidget(self.btn_refresh_page, 0, Qt.AlignLeft)


        self.horizontalLayout_19.addWidget(self.frm_refresh, 0, Qt.AlignRight)


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

        self.stackedWidgetfront.setCurrentIndex(0)
        self.cmbbox_title.setCurrentIndex(0)
        self.cmbbox_nationality.setCurrentIndex(0)
        self.main_body_stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_registration.setText(QCoreApplication.translate("MainWindow", u"COLLEGE REGISTRATION", None))
        self.button_back_reg_pg.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
#if QT_CONFIG(accessibility)
        self.frame_21.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"First name", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Terms And Condition", None))
        self.checkBox_terms.setText(QCoreApplication.translate("MainWindow", u"I Accept Terms and Conditions", None))
        self.cmbbox_title.setItemText(0, QCoreApplication.translate("MainWindow", u"Male", None))
        self.cmbbox_title.setItemText(1, QCoreApplication.translate("MainWindow", u"Female", None))

        self.cmbbox_title.setCurrentText(QCoreApplication.translate("MainWindow", u"Male", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Grade / Year Level", None))
        self.cmbbox_course.setItemText(0, QCoreApplication.translate("MainWindow", u"Bachelor of Science in Information Technology", None))
        self.cmbbox_course.setItemText(1, QCoreApplication.translate("MainWindow", u"Bachelor of Science in Computer Science", None))

        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Last name", None))
#if QT_CONFIG(accessibility)
        self.birth_dateEdit.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Date of Birth", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"#Completed Semester", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Registration status", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Course", None))
        self.checkBox_registered.setText(QCoreApplication.translate("MainWindow", u"Currently Registered", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Middle name", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Nationality", None))
        self.cmbbox_nationality.setItemText(0, QCoreApplication.translate("MainWindow", u"Filipino", None))
        self.cmbbox_nationality.setItemText(1, QCoreApplication.translate("MainWindow", u"American", None))

        self.cmbbox_nationality.setCurrentText(QCoreApplication.translate("MainWindow", u"Filipino", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Telephone Number", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.button_submit_data.setText(QCoreApplication.translate("MainWindow", u"SUBMIT", None))
        self.label_version_number.setText(QCoreApplication.translate("MainWindow", u"Version 1.0.0.00", None))
        self.register_button.setText(QCoreApplication.translate("MainWindow", u"REGISTER", None))
        self.view_button.setText(QCoreApplication.translate("MainWindow", u"VIEW", None))
        self.open_close_side_bar_button.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Database Manager", None))
        self.btn_back_second_page.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"NAVIGATE TABLES:", None))
        self.queue_data.setText("")
        self.lbl_reg_queue_db.setText(QCoreApplication.translate("MainWindow", u"REGISTRATION QUEUE", None))
        self.BSIT_page_button.setText("")
        self.lbl_BSIT_db.setText(QCoreApplication.translate("MainWindow", u"BSIT TABLE", None))
        self.COMSCI_page_button.setText("")
        self.lbl_COMSCI_db.setText(QCoreApplication.translate("MainWindow", u"COMSCI TABLE", None))
        self.lbl_approve.setText(QCoreApplication.translate("MainWindow", u"APPROVE SELECTED TO:", None))
        self.btn_approve_BSIT.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"BS Information Tech", None))
        self.btn_approve_COMSCI.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"BS Ccomputer Science", None))
        self.dis_btn.setText("")
        self.lbl_reg_que.setText(QCoreApplication.translate("MainWindow", u"Registration Queue Database", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"FILTER DATA:", None))
        self.searchLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Data", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"IDnumber", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Firstname", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Lastname", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Nationality", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Registration", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Semester", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Course", None));
        self.pushButton.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"BACHELOR OF SCIENCE IN INFORMATION TECHNOLOGY ( BSIT )", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"FILTER DATA:", None))
        self.searchLineEdit_BSIT.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Data", None))
        ___qtablewidgetitem9 = self.tableWidget_BSIT.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"IDnumber", None));
        ___qtablewidgetitem10 = self.tableWidget_BSIT.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Firstname", None));
        ___qtablewidgetitem11 = self.tableWidget_BSIT.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Lastname", None));
        ___qtablewidgetitem12 = self.tableWidget_BSIT.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem13 = self.tableWidget_BSIT.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem14 = self.tableWidget_BSIT.horizontalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Nationality", None));
        ___qtablewidgetitem15 = self.tableWidget_BSIT.horizontalHeaderItem(6)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Registration", None));
        ___qtablewidgetitem16 = self.tableWidget_BSIT.horizontalHeaderItem(7)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Semester", None));
        ___qtablewidgetitem17 = self.tableWidget_BSIT.horizontalHeaderItem(8)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Course", None));
        self.pushButton_2.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"BACHELOR OF SCIENCE IN COMPUTER SCIENCE ( COMSCI )", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"FILTER DATA:", None))
        self.searchLineEdit_COMSCI.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Data", None))
        ___qtablewidgetitem18 = self.tableWidget_COMSCI.horizontalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"IDnumber", None));
        ___qtablewidgetitem19 = self.tableWidget_COMSCI.horizontalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Firstname", None));
        ___qtablewidgetitem20 = self.tableWidget_COMSCI.horizontalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Lastname", None));
        ___qtablewidgetitem21 = self.tableWidget_COMSCI.horizontalHeaderItem(3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem22 = self.tableWidget_COMSCI.horizontalHeaderItem(4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem23 = self.tableWidget_COMSCI.horizontalHeaderItem(5)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Nationality", None));
        ___qtablewidgetitem24 = self.tableWidget_COMSCI.horizontalHeaderItem(6)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Registration", None));
        ___qtablewidgetitem25 = self.tableWidget_COMSCI.horizontalHeaderItem(7)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Semester", None));
        ___qtablewidgetitem26 = self.tableWidget_COMSCI.horizontalHeaderItem(8)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Course", None));
        self.lbl_apply.setText(QCoreApplication.translate("MainWindow", u"APPLY TABLE CHANGES :", None))
        self.btn_save_all_data.setText(QCoreApplication.translate("MainWindow", u"SAVE", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"DELETE SELECTED :", None))
        self.btn_delete_selected.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.lbl_refresh.setText(QCoreApplication.translate("MainWindow", u"REFRESH TABLE :", None))
        self.btn_refresh_page.setText(QCoreApplication.translate("MainWindow", u"REFRESH", None))
        self.version_.setText(QCoreApplication.translate("MainWindow", u"Version 1.0.0.00", None))
    # retranslateUi

