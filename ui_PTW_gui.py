# -*- coding: utf-8 -*-
# ptw.py - 'Put to Wall concept' only gui part
# Author: Tomasz Zgrys AiR, 2021/2022, WWSIS Horyzont
# Copyright: Tomasz Zgrys & WWSIS Horyzont
################################################################################
## Form generated from reading UI file 'PTW_guiyvgiVW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import ptw_ui_resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1900, 1000)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1360, 760))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        MainWindow.setToolButtonStyle(Qt.ToolButtonTextOnly)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.mw_centralwidget = QWidget(MainWindow)
        self.mw_centralwidget.setObjectName(u"mw_centralwidget")
        sizePolicy.setHeightForWidth(self.mw_centralwidget.sizePolicy().hasHeightForWidth())
        self.mw_centralwidget.setSizePolicy(sizePolicy)
        self.mw_centralwidget.setStyleSheet(u"")
        self.verticalLayout_32 = QVBoxLayout(self.mw_centralwidget)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_32.setContentsMargins(6, 6, 6, 6)
        self.splitter = QSplitter(self.mw_centralwidget)
        self.splitter.setObjectName(u"splitter")
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_24 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.batch_br_tabWidget = QTabWidget(self.layoutWidget)
        self.batch_br_tabWidget.setObjectName(u"batch_br_tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.batch_br_tabWidget.sizePolicy().hasHeightForWidth())
        self.batch_br_tabWidget.setSizePolicy(sizePolicy1)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(95, 95, 95, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(170, 85, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush2)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush4 = QBrush(QColor(0, 0, 0, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        brush5 = QBrush(QColor(177, 177, 177, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        brush6 = QBrush(QColor(113, 113, 113, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        brush7 = QBrush(QColor(161, 161, 161, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush8 = QBrush(QColor(0, 0, 0, 128))
        brush8.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush9 = QBrush(QColor(0, 0, 0, 128))
        brush9.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.batch_br_tabWidget.setPalette(palette)
        self.batch_br_tabWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.batch_br_tabWidget.setFocusPolicy(Qt.NoFocus)
        self.batch_br_tabWidget.setAutoFillBackground(False)
        self.batch_br_tabWidget.setStyleSheet(u"")
        self.batch_br_tabWidget.setTabPosition(QTabWidget.North)
        self.batch_br_tabWidget.setTabShape(QTabWidget.Rounded)
        self.batch_br_tabWidget.setElideMode(Qt.ElideNone)
        self.batch_br_tabWidget.setTabBarAutoHide(True)
        self.register_batch = QWidget()
        self.register_batch.setObjectName(u"register_batch")
        self.register_batch.setEnabled(True)
        self.gridLayout_4 = QGridLayout(self.register_batch)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.batch_register_frame = QFrame(self.register_batch)
        self.batch_register_frame.setObjectName(u"batch_register_frame")
        self.batch_register_frame.setMinimumSize(QSize(0, 0))
        self.batch_register_frame.setMaximumSize(QSize(450, 16777215))
        font1 = QFont()
        font1.setFamily(u"FreeSans")
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(7)
        self.batch_register_frame.setFont(font1)
        self.batch_register_frame.setStyleSheet(u"font: 63 16pt \"FreeSans\";\n"
"color: rgb(255, 255, 255);\n"
"border-bottom-style: outline;\n"
"border-bottom-color: rgb(66, 66, 66);")
        self.batch_register_frame.setFrameShape(QFrame.StyledPanel)
        self.batch_register_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.batch_register_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.info_br_label = QLabel(self.batch_register_frame)
        self.info_br_label.setObjectName(u"info_br_label")
        sizePolicy.setHeightForWidth(self.info_br_label.sizePolicy().hasHeightForWidth())
        self.info_br_label.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamily(u"FreeSans")
        font2.setPointSize(16)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setWeight(7)
        self.info_br_label.setFont(font2)

        self.verticalLayout_3.addWidget(self.info_br_label)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.batch_no_br_descr_label = QLabel(self.batch_register_frame)
        self.batch_no_br_descr_label.setObjectName(u"batch_no_br_descr_label")
        self.batch_no_br_descr_label.setFont(font1)
        self.batch_no_br_descr_label.setScaledContents(False)

        self.horizontalLayout_21.addWidget(self.batch_no_br_descr_label)

        self.batch_no_br_label = QLabel(self.batch_register_frame)
        self.batch_no_br_label.setObjectName(u"batch_no_br_label")
        self.batch_no_br_label.setStyleSheet(u"border-bottom-color: rgb(102, 102, 102);")
        self.batch_no_br_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.batch_no_br_label)

        self.horizontalLayout_21.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.carts_quantity_descr_label = QLabel(self.batch_register_frame)
        self.carts_quantity_descr_label.setObjectName(u"carts_quantity_descr_label")
        self.carts_quantity_descr_label.setFont(font1)
        self.carts_quantity_descr_label.setScaledContents(False)

        self.horizontalLayout_22.addWidget(self.carts_quantity_descr_label)

        self.carts_qty_br_label = QLabel(self.batch_register_frame)
        self.carts_qty_br_label.setObjectName(u"carts_qty_br_label")
        self.carts_qty_br_label.setStyleSheet(u"border-bottom-color: rgb(102, 102, 102);")
        self.carts_qty_br_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.carts_qty_br_label)

        self.horizontalLayout_22.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.orders_quantity_descr_label = QLabel(self.batch_register_frame)
        self.orders_quantity_descr_label.setObjectName(u"orders_quantity_descr_label")
        self.orders_quantity_descr_label.setFont(font1)
        self.orders_quantity_descr_label.setScaledContents(False)

        self.horizontalLayout_23.addWidget(self.orders_quantity_descr_label)

        self.orders_qty_br_label = QLabel(self.batch_register_frame)
        self.orders_qty_br_label.setObjectName(u"orders_qty_br_label")
        self.orders_qty_br_label.setStyleSheet(u"border-bottom-color: rgb(102, 102, 102);")
        self.orders_qty_br_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_23.addWidget(self.orders_qty_br_label)

        self.horizontalLayout_23.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.items_qantity_descr_label = QLabel(self.batch_register_frame)
        self.items_qantity_descr_label.setObjectName(u"items_qantity_descr_label")
        self.items_qantity_descr_label.setFont(font1)
        self.items_qantity_descr_label.setScaledContents(False)

        self.horizontalLayout_24.addWidget(self.items_qantity_descr_label)

        self.items_qty_br_label = QLabel(self.batch_register_frame)
        self.items_qty_br_label.setObjectName(u"items_qty_br_label")
        self.items_qty_br_label.setStyleSheet(u"border-bottom-color: rgb(102, 102, 102);")
        self.items_qty_br_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_24.addWidget(self.items_qty_br_label)

        self.horizontalLayout_24.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_24)

        self.widget = QWidget(self.batch_register_frame)
        self.widget.setObjectName(u"widget")
        font3 = QFont()
        font3.setFamily(u"FreeSans")
        font3.setPointSize(16)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(9)
        self.widget.setFont(font3)
        self.widget.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 75 16pt \"FreeSans\";\n"
"border-radius:15px;\n"
"padding:10px;\n"
"\n"
"")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.register_br_pushButton = QPushButton(self.widget)
        self.register_br_pushButton.setObjectName(u"register_br_pushButton")
        self.register_br_pushButton.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.register_br_pushButton.sizePolicy().hasHeightForWidth())
        self.register_br_pushButton.setSizePolicy(sizePolicy2)
        self.register_br_pushButton.setMinimumSize(QSize(180, 80))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        gradient = QLinearGradient(0.517, 1, 0.49, 0)
        gradient.setSpread(QGradient.PadSpread)
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient.setColorAt(0, QColor(255, 0, 128, 255))
        gradient.setColorAt(1, QColor(128, 0, 63, 246))
        brush10 = QBrush(gradient)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        gradient1 = QLinearGradient(0.517, 1, 0.49, 0)
        gradient1.setSpread(QGradient.PadSpread)
        gradient1.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient1.setColorAt(0, QColor(255, 0, 128, 255))
        gradient1.setColorAt(1, QColor(128, 0, 63, 246))
        brush11 = QBrush(gradient1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush11)
        gradient2 = QLinearGradient(0.517, 1, 0.49, 0)
        gradient2.setSpread(QGradient.PadSpread)
        gradient2.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient2.setColorAt(0, QColor(255, 0, 128, 255))
        gradient2.setColorAt(1, QColor(128, 0, 63, 246))
        brush12 = QBrush(gradient2)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush12)
        brush13 = QBrush(QColor(170, 0, 127, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush13)
        brush14 = QBrush(QColor(255, 255, 255, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush14)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        gradient3 = QLinearGradient(0.517, 1, 0.49, 0)
        gradient3.setSpread(QGradient.PadSpread)
        gradient3.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient3.setColorAt(0, QColor(255, 0, 128, 255))
        gradient3.setColorAt(1, QColor(128, 0, 63, 246))
        brush15 = QBrush(gradient3)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        gradient4 = QLinearGradient(0.517, 1, 0.49, 0)
        gradient4.setSpread(QGradient.PadSpread)
        gradient4.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient4.setColorAt(0, QColor(255, 0, 128, 255))
        gradient4.setColorAt(1, QColor(128, 0, 63, 246))
        brush16 = QBrush(gradient4)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush16)
        gradient5 = QLinearGradient(0.517, 1, 0.49, 0)
        gradient5.setSpread(QGradient.PadSpread)
        gradient5.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient5.setColorAt(0, QColor(255, 0, 128, 255))
        gradient5.setColorAt(1, QColor(128, 0, 63, 246))
        brush17 = QBrush(gradient5)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush17)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush13)
        brush18 = QBrush(QColor(255, 255, 255, 128))
        brush18.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush18)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        brush19 = QBrush(QColor(97, 0, 49, 255))
        brush19.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush19)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush19)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush19)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush13)
        brush20 = QBrush(QColor(255, 255, 255, 128))
        brush20.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.register_br_pushButton.setPalette(palette1)
        self.register_br_pushButton.setFont(font3)
        self.register_br_pushButton.setMouseTracking(False)
        self.register_br_pushButton.setFocusPolicy(Qt.ClickFocus)
        self.register_br_pushButton.setAutoFillBackground(False)
        self.register_br_pushButton.setStyleSheet(u"QPushButton {\n"
"	background-color:qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.49, y2:0, stop:0 rgba(255, 0, 128, 255), stop:1 rgba(128, 0, 63, 246));\n"
"	border: 6px solid rgb(140, 0, 70);\n"
"}\n"
"QPushButton:checked{	\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.49, y2:0, stop:0 rgba(182, 0, 255, 255), stop:1 rgba(88, 0, 129, 255));\n"
"}\n"
"QPushButton:disabled{\n"
"	background-color:rgb(97, 0, 49);}")
        self.register_br_pushButton.setCheckable(True)
        self.register_br_pushButton.setAutoExclusive(False)
        self.register_br_pushButton.setAutoDefault(False)

        self.gridLayout_2.addWidget(self.register_br_pushButton, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.widget)


        self.gridLayout_4.addWidget(self.batch_register_frame, 0, 0, 1, 1)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.batch_list_label = QLabel(self.register_batch)
        self.batch_list_label.setObjectName(u"batch_list_label")
        self.batch_list_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.batch_list_label)

        self.batch_br_tableView = QTableView(self.register_batch)
        self.batch_br_tableView.setObjectName(u"batch_br_tableView")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.batch_br_tableView.sizePolicy().hasHeightForWidth())
        self.batch_br_tableView.setSizePolicy(sizePolicy3)
        self.batch_br_tableView.setMaximumSize(QSize(160, 16777215))
        self.batch_br_tableView.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)

        self.verticalLayout_33.addWidget(self.batch_br_tableView)


        self.gridLayout_4.addLayout(self.verticalLayout_33, 0, 1, 1, 1)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.loab_descr_label = QLabel(self.register_batch)
        self.loab_descr_label.setObjectName(u"loab_descr_label")

        self.verticalLayout_21.addWidget(self.loab_descr_label)

        self.content_br_tableView = QTableView(self.register_batch)
        self.content_br_tableView.setObjectName(u"content_br_tableView")
        sizePolicy3.setHeightForWidth(self.content_br_tableView.sizePolicy().hasHeightForWidth())
        self.content_br_tableView.setSizePolicy(sizePolicy3)
        self.content_br_tableView.setFont(font)
        self.content_br_tableView.setAlternatingRowColors(True)
        self.content_br_tableView.setSortingEnabled(True)

        self.verticalLayout_21.addWidget(self.content_br_tableView)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.clear_status_br_pushButton = QPushButton(self.register_batch)
        self.clear_status_br_pushButton.setObjectName(u"clear_status_br_pushButton")

        self.horizontalLayout_4.addWidget(self.clear_status_br_pushButton)


        self.verticalLayout_21.addLayout(self.horizontalLayout_4)


        self.gridLayout_4.addLayout(self.verticalLayout_21, 0, 2, 1, 1)

        self.gridLayout_4.setColumnStretch(2, 1)
        self.batch_br_tabWidget.addTab(self.register_batch, "")
        self.batch_stats = QWidget()
        self.batch_stats.setObjectName(u"batch_stats")
        self.gridLayout_7 = QGridLayout(self.batch_stats)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.bs_load_pushButton = QPushButton(self.batch_stats)
        self.bs_load_pushButton.setObjectName(u"bs_load_pushButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.bs_load_pushButton.sizePolicy().hasHeightForWidth())
        self.bs_load_pushButton.setSizePolicy(sizePolicy4)

        self.gridLayout_7.addWidget(self.bs_load_pushButton, 0, 1, 1, 1)

        self.bs_present_pushButton = QPushButton(self.batch_stats)
        self.bs_present_pushButton.setObjectName(u"bs_present_pushButton")
        sizePolicy4.setHeightForWidth(self.bs_present_pushButton.sizePolicy().hasHeightForWidth())
        self.bs_present_pushButton.setSizePolicy(sizePolicy4)

        self.gridLayout_7.addWidget(self.bs_present_pushButton, 7, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 242, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_7.addItem(self.verticalSpacer_4, 4, 1, 1, 1)

        self.bs_frame = QFrame(self.batch_stats)
        self.bs_frame.setObjectName(u"bs_frame")
        self.bs_frame.setMinimumSize(QSize(0, 40))
        self.bs_frame.setFrameShape(QFrame.Panel)
        self.gridLayout_6 = QGridLayout(self.bs_frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.bs_oq_avg_label = QLabel(self.bs_frame)
        self.bs_oq_avg_label.setObjectName(u"bs_oq_avg_label")
        font4 = QFont()
        font4.setPointSize(16)
        font4.setBold(True)
        font4.setItalic(True)
        font4.setWeight(75)
        self.bs_oq_avg_label.setFont(font4)
        self.bs_oq_avg_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.bs_oq_avg_label, 6, 2, 1, 1)

        self.bs_max_descr_label = QLabel(self.bs_frame)
        self.bs_max_descr_label.setObjectName(u"bs_max_descr_label")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.bs_max_descr_label.sizePolicy().hasHeightForWidth())
        self.bs_max_descr_label.setSizePolicy(sizePolicy5)
        self.bs_max_descr_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.bs_max_descr_label, 2, 3, 1, 1)

        self.bs_iq_frame = QFrame(self.bs_frame)
        self.bs_iq_frame.setObjectName(u"bs_iq_frame")
        self.bs_iq_frame.setMinimumSize(QSize(0, 60))
        self.bs_iq_frame.setStyleSheet(u"#bs_iq_frame{border: 5px solid rgb(213, 0, 0);\n"
"border-radius: 35px;}")
        self.bs_iq_frame.setFrameShape(QFrame.StyledPanel)
        self.bs_iq_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.bs_iq_frame)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.bs_iq_label = QLabel(self.bs_iq_frame)
        self.bs_iq_label.setObjectName(u"bs_iq_label")
        font5 = QFont()
        font5.setFamily(u"Open Sans Extrabold")
        font5.setPointSize(16)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setWeight(75)
        self.bs_iq_label.setFont(font5)
        self.bs_iq_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.bs_iq_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.bs_iq_label, 1, 0, 1, 1)

        self.bs_iq_descr_label = QLabel(self.bs_iq_frame)
        self.bs_iq_descr_label.setObjectName(u"bs_iq_descr_label")
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(50)
        self.bs_iq_descr_label.setFont(font6)
        self.bs_iq_descr_label.setStyleSheet(u"color: rgb(200, 200, 200);")
        self.bs_iq_descr_label.setTextFormat(Qt.AutoText)
        self.bs_iq_descr_label.setScaledContents(False)
        self.bs_iq_descr_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.bs_iq_descr_label, 2, 0, 1, 1)


        self.gridLayout_6.addWidget(self.bs_iq_frame, 4, 0, 1, 1)

        self.bs_iq_min_label = QLabel(self.bs_frame)
        self.bs_iq_min_label.setObjectName(u"bs_iq_min_label")
        self.bs_iq_min_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.bs_iq_min_label, 4, 1, 1, 1)

        self.bs_batch_frame = QFrame(self.bs_frame)
        self.bs_batch_frame.setObjectName(u"bs_batch_frame")
        self.bs_batch_frame.setAutoFillBackground(False)
        self.bs_batch_frame.setStyleSheet(u"#bs_batch_frame{border: 8px solid rgb(213, 0, 0);\n"
"border-radius: 35px;}")
        self.bs_batch_frame.setFrameShape(QFrame.StyledPanel)
        self.bs_batch_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.bs_batch_frame)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(2, 2, 2, 2)
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_38.addItem(self.verticalSpacer_7)

        self.bs_batch_progress_label = QLabel(self.bs_batch_frame)
        self.bs_batch_progress_label.setObjectName(u"bs_batch_progress_label")
        font7 = QFont()
        font7.setPointSize(16)
        font7.setBold(True)
        font7.setWeight(75)
        self.bs_batch_progress_label.setFont(font7)
        self.bs_batch_progress_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.bs_batch_progress_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_38.addWidget(self.bs_batch_progress_label)

        self.bs_batch_no_label = QLabel(self.bs_batch_frame)
        self.bs_batch_no_label.setObjectName(u"bs_batch_no_label")
        font8 = QFont()
        font8.setPointSize(18)
        font8.setBold(True)
        font8.setItalic(True)
        font8.setWeight(75)
        self.bs_batch_no_label.setFont(font8)
        self.bs_batch_no_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.bs_batch_no_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_38.addWidget(self.bs_batch_no_label)

        self.bs_batch_time_descr_label = QLabel(self.bs_batch_frame)
        self.bs_batch_time_descr_label.setObjectName(u"bs_batch_time_descr_label")
        sizePolicy.setHeightForWidth(self.bs_batch_time_descr_label.sizePolicy().hasHeightForWidth())
        self.bs_batch_time_descr_label.setSizePolicy(sizePolicy)
        self.bs_batch_time_descr_label.setMaximumSize(QSize(16777215, 16777215))
        self.bs_batch_time_descr_label.setFont(font6)
        self.bs_batch_time_descr_label.setStyleSheet(u"color: rgb(200, 200, 200);")
        self.bs_batch_time_descr_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_38.addWidget(self.bs_batch_time_descr_label)

        self.bs_batch_time_label = QLabel(self.bs_batch_frame)
        self.bs_batch_time_label.setObjectName(u"bs_batch_time_label")
        self.bs_batch_time_label.setFont(font5)
        self.bs_batch_time_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.bs_batch_time_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_38.addWidget(self.bs_batch_time_label)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_38.addItem(self.verticalSpacer_6)


        self.gridLayout_6.addWidget(self.bs_batch_frame, 0, 0, 3, 1)

        self.line_13 = QFrame(self.bs_frame)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setMaximumSize(QSize(16777215, 3))
        self.line_13.setStyleSheet(u"background-color: rgb(213, 0,0000);")
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line_13, 3, 1, 1, 3)

        self.bs_avg_descr_label = QLabel(self.bs_frame)
        self.bs_avg_descr_label.setObjectName(u"bs_avg_descr_label")
        sizePolicy5.setHeightForWidth(self.bs_avg_descr_label.sizePolicy().hasHeightForWidth())
        self.bs_avg_descr_label.setSizePolicy(sizePolicy5)
        self.bs_avg_descr_label.setFont(font4)
        self.bs_avg_descr_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.bs_avg_descr_label, 2, 2, 1, 1)

        self.bs_iq_max_label = QLabel(self.bs_frame)
        self.bs_iq_max_label.setObjectName(u"bs_iq_max_label")
        self.bs_iq_max_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.bs_iq_max_label, 4, 3, 1, 1)

        self.bs_ipo_frame = QFrame(self.bs_frame)
        self.bs_ipo_frame.setObjectName(u"bs_ipo_frame")
        self.bs_ipo_frame.setMinimumSize(QSize(0, 60))
        self.bs_ipo_frame.setStyleSheet(u"#bs_ipo_frame{border: 5px solid rgb(213, 0, 0);\n"
"border-radius: 35px;}")
        self.bs_ipo_frame.setFrameShape(QFrame.StyledPanel)
        self.bs_ipo_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.bs_ipo_frame)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.bs_ipo_label = QLabel(self.bs_ipo_frame)
        self.bs_ipo_label.setObjectName(u"bs_ipo_label")
        self.bs_ipo_label.setFont(font5)
        self.bs_ipo_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.bs_ipo_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.bs_ipo_label)

        self.bs_ipo_descr_label = QLabel(self.bs_ipo_frame)
        self.bs_ipo_descr_label.setObjectName(u"bs_ipo_descr_label")
        self.bs_ipo_descr_label.setMinimumSize(QSize(0, 35))
        self.bs_ipo_descr_label.setFont(font6)
        self.bs_ipo_descr_label.setStyleSheet(u"color: rgb(200, 200, 200);")
        self.bs_ipo_descr_label.setTextFormat(Qt.AutoText)
        self.bs_ipo_descr_label.setScaledContents(False)
        self.bs_ipo_descr_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.bs_ipo_descr_label)


        self.gridLayout_6.addWidget(self.bs_ipo_frame, 6, 4, 1, 1)

        self.bs_time_descr_label = QLabel(self.bs_frame)
        self.bs_time_descr_label.setObjectName(u"bs_time_descr_label")
        sizePolicy5.setHeightForWidth(self.bs_time_descr_label.sizePolicy().hasHeightForWidth())
        self.bs_time_descr_label.setSizePolicy(sizePolicy5)
        self.bs_time_descr_label.setMinimumSize(QSize(0, 0))
        font9 = QFont()
        font9.setPointSize(12)
        font9.setBold(True)
        font9.setItalic(False)
        font9.setWeight(75)
        self.bs_time_descr_label.setFont(font9)
        self.bs_time_descr_label.setStyleSheet(u"color: white;\n"
"border: 5px solid rgb(213, 0, 0);\n"
"border-radius: 15px;")
        self.bs_time_descr_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.bs_time_descr_label, 1, 1, 1, 3)

        self.bs_iq_avg_label = QLabel(self.bs_frame)
        self.bs_iq_avg_label.setObjectName(u"bs_iq_avg_label")
        self.bs_iq_avg_label.setFont(font4)
        self.bs_iq_avg_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.bs_iq_avg_label, 4, 2, 1, 1)

        self.bs_oq_min_label = QLabel(self.bs_frame)
        self.bs_oq_min_label.setObjectName(u"bs_oq_min_label")
        self.bs_oq_min_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.bs_oq_min_label, 6, 1, 1, 1)

        self.bs_ipc_frame = QFrame(self.bs_frame)
        self.bs_ipc_frame.setObjectName(u"bs_ipc_frame")
        self.bs_ipc_frame.setMinimumSize(QSize(0, 60))
        self.bs_ipc_frame.setStyleSheet(u"#bs_ipc_frame{border: 5px solid rgb(213, 0, 0);\n"
"border-radius: 35px;}")
        self.bs_ipc_frame.setFrameShape(QFrame.StyledPanel)
        self.bs_ipc_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.bs_ipc_frame)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.bs_ipc_label = QLabel(self.bs_ipc_frame)
        self.bs_ipc_label.setObjectName(u"bs_ipc_label")
        self.bs_ipc_label.setFont(font5)
        self.bs_ipc_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.bs_ipc_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_36.addWidget(self.bs_ipc_label)

        self.bs_ipc_descr_label = QLabel(self.bs_ipc_frame)
        self.bs_ipc_descr_label.setObjectName(u"bs_ipc_descr_label")
        self.bs_ipc_descr_label.setMinimumSize(QSize(0, 35))
        self.bs_ipc_descr_label.setFont(font6)
        self.bs_ipc_descr_label.setStyleSheet(u"color: rgb(200, 200, 200);")
        self.bs_ipc_descr_label.setTextFormat(Qt.AutoText)
        self.bs_ipc_descr_label.setScaledContents(False)
        self.bs_ipc_descr_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_36.addWidget(self.bs_ipc_descr_label)


        self.gridLayout_6.addWidget(self.bs_ipc_frame, 4, 4, 1, 1)

        self.bs_oq_max_label = QLabel(self.bs_frame)
        self.bs_oq_max_label.setObjectName(u"bs_oq_max_label")
        self.bs_oq_max_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.bs_oq_max_label, 6, 3, 1, 1)

        self.bs_oq_frame = QFrame(self.bs_frame)
        self.bs_oq_frame.setObjectName(u"bs_oq_frame")
        sizePolicy.setHeightForWidth(self.bs_oq_frame.sizePolicy().hasHeightForWidth())
        self.bs_oq_frame.setSizePolicy(sizePolicy)
        self.bs_oq_frame.setMinimumSize(QSize(0, 60))
        self.bs_oq_frame.setStyleSheet(u"#bs_oq_frame{border: 5px solid rgb(213, 0, 0);\n"
"border-radius: 35px;}")
        self.bs_oq_frame.setFrameShape(QFrame.StyledPanel)
        self.bs_oq_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.bs_oq_frame)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.bs_oq_label = QLabel(self.bs_oq_frame)
        self.bs_oq_label.setObjectName(u"bs_oq_label")
        self.bs_oq_label.setFont(font5)
        self.bs_oq_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.bs_oq_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.bs_oq_label, 0, 0, 1, 1)

        self.bs_oq_descr_label = QLabel(self.bs_oq_frame)
        self.bs_oq_descr_label.setObjectName(u"bs_oq_descr_label")
        self.bs_oq_descr_label.setFont(font6)
        self.bs_oq_descr_label.setStyleSheet(u"color: rgb(200, 200, 200);")
        self.bs_oq_descr_label.setTextFormat(Qt.AutoText)
        self.bs_oq_descr_label.setScaledContents(False)
        self.bs_oq_descr_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.bs_oq_descr_label, 2, 0, 1, 1)


        self.gridLayout_6.addWidget(self.bs_oq_frame, 6, 0, 1, 1)

        self.bs_descr_label = QLabel(self.bs_frame)
        self.bs_descr_label.setObjectName(u"bs_descr_label")
        sizePolicy5.setHeightForWidth(self.bs_descr_label.sizePolicy().hasHeightForWidth())
        self.bs_descr_label.setSizePolicy(sizePolicy5)
        self.bs_descr_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.bs_descr_label, 0, 1, 1, 1)

        self.bs_cq_frame = QFrame(self.bs_frame)
        self.bs_cq_frame.setObjectName(u"bs_cq_frame")
        self.bs_cq_frame.setMinimumSize(QSize(0, 60))
        self.bs_cq_frame.setStyleSheet(u"#bs_cq_frame{border: 5px solid rgb(213, 0, 0);border-radius: 35px;}")
        self.bs_cq_frame.setFrameShape(QFrame.StyledPanel)
        self.bs_cq_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.bs_cq_frame)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.bs_cq_label = QLabel(self.bs_cq_frame)
        self.bs_cq_label.setObjectName(u"bs_cq_label")
        self.bs_cq_label.setFont(font5)
        self.bs_cq_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.bs_cq_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_35.addWidget(self.bs_cq_label)

        self.bs_cq_descr_label = QLabel(self.bs_cq_frame)
        self.bs_cq_descr_label.setObjectName(u"bs_cq_descr_label")
        self.bs_cq_descr_label.setFont(font6)
        self.bs_cq_descr_label.setStyleSheet(u"color: rgb(200, 200, 200);")
        self.bs_cq_descr_label.setTextFormat(Qt.AutoText)
        self.bs_cq_descr_label.setScaledContents(False)
        self.bs_cq_descr_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_35.addWidget(self.bs_cq_descr_label)


        self.gridLayout_6.addWidget(self.bs_cq_frame, 2, 4, 1, 1)

        self.bs_min_descr_label = QLabel(self.bs_frame)
        self.bs_min_descr_label.setObjectName(u"bs_min_descr_label")
        sizePolicy5.setHeightForWidth(self.bs_min_descr_label.sizePolicy().hasHeightForWidth())
        self.bs_min_descr_label.setSizePolicy(sizePolicy5)
        self.bs_min_descr_label.setAlignment(Qt.AlignCenter)
        self.bs_min_descr_label.setWordWrap(True)

        self.gridLayout_6.addWidget(self.bs_min_descr_label, 2, 1, 1, 1)

        self.line_14 = QFrame(self.bs_frame)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setMaximumSize(QSize(16777215, 3))
        self.line_14.setStyleSheet(u"background-color: rgb(213, 0, 0);")
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line_14, 5, 1, 1, 3)

        self.bs_filename_label = QLabel(self.bs_frame)
        self.bs_filename_label.setObjectName(u"bs_filename_label")
        self.bs_filename_label.setMinimumSize(QSize(0, 0))
        self.bs_filename_label.setFrameShadow(QFrame.Raised)
        self.bs_filename_label.setTextFormat(Qt.RichText)

        self.gridLayout_6.addWidget(self.bs_filename_label, 0, 2, 1, 3)


        self.gridLayout_7.addWidget(self.bs_frame, 0, 0, 8, 1)

        self.line_35 = QFrame(self.batch_stats)
        self.line_35.setObjectName(u"line_35")
        sizePolicy5.setHeightForWidth(self.line_35.sizePolicy().hasHeightForWidth())
        self.line_35.setSizePolicy(sizePolicy5)
        self.line_35.setMaximumSize(QSize(16777215, 3))
        self.line_35.setStyleSheet(u"background-color: rgb(213, 0, 0);")
        self.line_35.setLineWidth(3)
        self.line_35.setFrameShape(QFrame.HLine)
        self.line_35.setFrameShadow(QFrame.Sunken)

        self.gridLayout_7.addWidget(self.line_35, 2, 1, 1, 1)

        self.bs_delete_pushButton = QPushButton(self.batch_stats)
        self.bs_delete_pushButton.setObjectName(u"bs_delete_pushButton")
        sizePolicy4.setHeightForWidth(self.bs_delete_pushButton.sizePolicy().hasHeightForWidth())
        self.bs_delete_pushButton.setSizePolicy(sizePolicy4)

        self.gridLayout_7.addWidget(self.bs_delete_pushButton, 3, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_7.addItem(self.verticalSpacer_5, 1, 1, 1, 1)

        self.bs_ll_pushButton = QPushButton(self.batch_stats)
        self.bs_ll_pushButton.setObjectName(u"bs_ll_pushButton")
        sizePolicy4.setHeightForWidth(self.bs_ll_pushButton.sizePolicy().hasHeightForWidth())
        self.bs_ll_pushButton.setSizePolicy(sizePolicy4)

        self.gridLayout_7.addWidget(self.bs_ll_pushButton, 6, 1, 1, 1)

        self.batch_br_tabWidget.addTab(self.batch_stats, "")
        self.history_bo = QWidget()
        self.history_bo.setObjectName(u"history_bo")
        self.gridLayout_5 = QGridLayout(self.history_bo)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pbo_descr_label = QLabel(self.history_bo)
        self.pbo_descr_label.setObjectName(u"pbo_descr_label")
        sizePolicy5.setHeightForWidth(self.pbo_descr_label.sizePolicy().hasHeightForWidth())
        self.pbo_descr_label.setSizePolicy(sizePolicy5)

        self.gridLayout_5.addWidget(self.pbo_descr_label, 0, 5, 1, 1)

        self.hboff_load_pushButton = QPushButton(self.history_bo)
        self.hboff_load_pushButton.setObjectName(u"hboff_load_pushButton")
        sizePolicy4.setHeightForWidth(self.hboff_load_pushButton.sizePolicy().hasHeightForWidth())
        self.hboff_load_pushButton.setSizePolicy(sizePolicy4)

        self.gridLayout_5.addWidget(self.hboff_load_pushButton, 1, 2, 1, 1)

        self.hboff_delete_pushButton = QPushButton(self.history_bo)
        self.hboff_delete_pushButton.setObjectName(u"hboff_delete_pushButton")
        sizePolicy4.setHeightForWidth(self.hboff_delete_pushButton.sizePolicy().hasHeightForWidth())
        self.hboff_delete_pushButton.setSizePolicy(sizePolicy4)

        self.gridLayout_5.addWidget(self.hboff_delete_pushButton, 4, 2, 1, 1)

        self.hboff_clear_pushButton = QPushButton(self.history_bo)
        self.hboff_clear_pushButton.setObjectName(u"hboff_clear_pushButton")
        sizePolicy4.setHeightForWidth(self.hboff_clear_pushButton.sizePolicy().hasHeightForWidth())
        self.hboff_clear_pushButton.setSizePolicy(sizePolicy4)

        self.gridLayout_5.addWidget(self.hboff_clear_pushButton, 6, 2, 1, 1)

        self.line_10 = QFrame(self.history_bo)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setMinimumSize(QSize(3, 0))
        self.line_10.setStyleSheet(u"color: rgb(213, 0, 0);")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_10, 0, 4, 7, 1)

        self.line_12 = QFrame(self.history_bo)
        self.line_12.setObjectName(u"line_12")
        sizePolicy5.setHeightForWidth(self.line_12.sizePolicy().hasHeightForWidth())
        self.line_12.setSizePolicy(sizePolicy5)
        self.line_12.setMaximumSize(QSize(16777215, 3))
        self.line_12.setStyleSheet(u"background-color: rgb(213, 0, 0);")
        self.line_12.setLineWidth(3)
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_12, 3, 2, 1, 1)

        self.hboff_filename_label = QLabel(self.history_bo)
        self.hboff_filename_label.setObjectName(u"hboff_filename_label")
        sizePolicy5.setHeightForWidth(self.hboff_filename_label.sizePolicy().hasHeightForWidth())
        self.hboff_filename_label.setSizePolicy(sizePolicy5)
        self.hboff_filename_label.setTextFormat(Qt.RichText)

        self.gridLayout_5.addWidget(self.hboff_filename_label, 0, 1, 1, 2)

        self.hboff_textBrowser = QTextBrowser(self.history_bo)
        self.hboff_textBrowser.setObjectName(u"hboff_textBrowser")
        sizePolicy.setHeightForWidth(self.hboff_textBrowser.sizePolicy().hasHeightForWidth())
        self.hboff_textBrowser.setSizePolicy(sizePolicy)
        self.hboff_textBrowser.setMinimumSize(QSize(0, 0))
        self.hboff_textBrowser.setFrameShape(QFrame.StyledPanel)

        self.gridLayout_5.addWidget(self.hboff_textBrowser, 1, 0, 6, 2)

        self.line_11 = QFrame(self.history_bo)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setMinimumSize(QSize(3, 0))
        self.line_11.setStyleSheet(u"color: rgb(213, 0, 0);")
        self.line_11.setFrameShape(QFrame.VLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_11, 0, 3, 7, 1)

        self.pbo_textBrowser = QTextBrowser(self.history_bo)
        self.pbo_textBrowser.setObjectName(u"pbo_textBrowser")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pbo_textBrowser.sizePolicy().hasHeightForWidth())
        self.pbo_textBrowser.setSizePolicy(sizePolicy6)
        self.pbo_textBrowser.setMinimumSize(QSize(0, 0))

        self.gridLayout_5.addWidget(self.pbo_textBrowser, 1, 5, 6, 2)

        self.hboff_descr_label = QLabel(self.history_bo)
        self.hboff_descr_label.setObjectName(u"hboff_descr_label")
        sizePolicy5.setHeightForWidth(self.hboff_descr_label.sizePolicy().hasHeightForWidth())
        self.hboff_descr_label.setSizePolicy(sizePolicy5)

        self.gridLayout_5.addWidget(self.hboff_descr_label, 0, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_5.addItem(self.verticalSpacer_8, 5, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 2, 2, 1, 1)

        self.batch_br_tabWidget.addTab(self.history_bo, "")
        self.create_batch = QWidget()
        self.create_batch.setObjectName(u"create_batch")
        self.create_batch.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.create_batch)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.splitter_3 = QSplitter(self.create_batch)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Vertical)
        self.layoutWidget1 = QWidget(self.splitter_3)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout_23 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.batch_no_descr_label_2 = QLabel(self.layoutWidget1)
        self.batch_no_descr_label_2.setObjectName(u"batch_no_descr_label_2")
        font10 = QFont()
        font10.setFamily(u"FreeSans")
        font10.setPointSize(14)
        font10.setBold(True)
        font10.setItalic(False)
        font10.setWeight(75)
        self.batch_no_descr_label_2.setFont(font10)

        self.verticalLayout_23.addWidget(self.batch_no_descr_label_2)

        self.batch_no_comboBox = QComboBox(self.layoutWidget1)
        self.batch_no_comboBox.setObjectName(u"batch_no_comboBox")
        self.batch_no_comboBox.setEditable(False)
        self.batch_no_comboBox.setInsertPolicy(QComboBox.InsertAlphabetically)
        self.batch_no_comboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.verticalLayout_23.addWidget(self.batch_no_comboBox)

        self.line_7 = QFrame(self.layoutWidget1)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShadow(QFrame.Raised)
        self.line_7.setLineWidth(3)
        self.line_7.setFrameShape(QFrame.HLine)

        self.verticalLayout_23.addWidget(self.line_7)

        self.order_no_descr_label = QLabel(self.layoutWidget1)
        self.order_no_descr_label.setObjectName(u"order_no_descr_label")
        self.order_no_descr_label.setFont(font10)

        self.verticalLayout_23.addWidget(self.order_no_descr_label)

        self.order_no_comboBox = QComboBox(self.layoutWidget1)
        self.order_no_comboBox.setObjectName(u"order_no_comboBox")
        self.order_no_comboBox.setEditable(False)
        self.order_no_comboBox.setInsertPolicy(QComboBox.InsertAlphabetically)
        self.order_no_comboBox.setModelColumn(1)

        self.verticalLayout_23.addWidget(self.order_no_comboBox)

        self.line_6 = QFrame(self.layoutWidget1)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShadow(QFrame.Raised)
        self.line_6.setLineWidth(3)
        self.line_6.setFrameShape(QFrame.HLine)

        self.verticalLayout_23.addWidget(self.line_6)

        self.item_barcode_descr_label = QLabel(self.layoutWidget1)
        self.item_barcode_descr_label.setObjectName(u"item_barcode_descr_label")
        self.item_barcode_descr_label.setFont(font10)

        self.verticalLayout_23.addWidget(self.item_barcode_descr_label)

        self.item_no_comboBox = QComboBox(self.layoutWidget1)
        self.item_no_comboBox.setObjectName(u"item_no_comboBox")
        self.item_no_comboBox.setEditable(False)
        self.item_no_comboBox.setInsertPolicy(QComboBox.InsertAlphabetically)
        self.item_no_comboBox.setModelColumn(2)

        self.verticalLayout_23.addWidget(self.item_no_comboBox)

        self.line_4 = QFrame(self.layoutWidget1)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShadow(QFrame.Raised)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QFrame.HLine)

        self.verticalLayout_23.addWidget(self.line_4)

        self.cart_barcode_descr_label = QLabel(self.layoutWidget1)
        self.cart_barcode_descr_label.setObjectName(u"cart_barcode_descr_label")
        self.cart_barcode_descr_label.setFont(font10)

        self.verticalLayout_23.addWidget(self.cart_barcode_descr_label)

        self.cart_barcode_comboBox = QComboBox(self.layoutWidget1)
        self.cart_barcode_comboBox.setObjectName(u"cart_barcode_comboBox")
        self.cart_barcode_comboBox.setEditable(False)
        self.cart_barcode_comboBox.setInsertPolicy(QComboBox.InsertAlphabetically)
        self.cart_barcode_comboBox.setMinimumContentsLength(3)

        self.verticalLayout_23.addWidget(self.cart_barcode_comboBox)

        self.line_8 = QFrame(self.layoutWidget1)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShadow(QFrame.Raised)
        self.line_8.setLineWidth(3)
        self.line_8.setFrameShape(QFrame.HLine)

        self.verticalLayout_23.addWidget(self.line_8)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer)

        self.add_item_cb_pushButton = QPushButton(self.layoutWidget1)
        self.add_item_cb_pushButton.setObjectName(u"add_item_cb_pushButton")
        self.add_item_cb_pushButton.setMinimumSize(QSize(0, 0))
        self.add_item_cb_pushButton.setAutoFillBackground(False)

        self.verticalLayout_23.addWidget(self.add_item_cb_pushButton)

        self.splitter_3.addWidget(self.layoutWidget1)

        self.gridLayout_3.addWidget(self.splitter_3, 0, 0, 2, 1)

        self.line = QFrame(self.create_batch)
        self.line.setObjectName(u"line")
        self.line.setLineWidth(3)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 0, 1, 2, 2)

        self.line_2 = QFrame(self.create_batch)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_2, 0, 3, 2, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.clear_batch_status_cb_pushButton = QPushButton(self.create_batch)
        self.clear_batch_status_cb_pushButton.setObjectName(u"clear_batch_status_cb_pushButton")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.clear_batch_status_cb_pushButton.sizePolicy().hasHeightForWidth())
        self.clear_batch_status_cb_pushButton.setSizePolicy(sizePolicy7)

        self.verticalLayout_4.addWidget(self.clear_batch_status_cb_pushButton)

        self.clear_order_status_cb_pushButton = QPushButton(self.create_batch)
        self.clear_order_status_cb_pushButton.setObjectName(u"clear_order_status_cb_pushButton")
        sizePolicy7.setHeightForWidth(self.clear_order_status_cb_pushButton.sizePolicy().hasHeightForWidth())
        self.clear_order_status_cb_pushButton.setSizePolicy(sizePolicy7)

        self.verticalLayout_4.addWidget(self.clear_order_status_cb_pushButton)

        self.clear_item_status_cb_pushButton = QPushButton(self.create_batch)
        self.clear_item_status_cb_pushButton.setObjectName(u"clear_item_status_cb_pushButton")
        sizePolicy7.setHeightForWidth(self.clear_item_status_cb_pushButton.sizePolicy().hasHeightForWidth())
        self.clear_item_status_cb_pushButton.setSizePolicy(sizePolicy7)

        self.verticalLayout_4.addWidget(self.clear_item_status_cb_pushButton)

        self.line_9 = QFrame(self.create_batch)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShadow(QFrame.Sunken)
        self.line_9.setLineWidth(4)
        self.line_9.setMidLineWidth(2)
        self.line_9.setFrameShape(QFrame.HLine)

        self.verticalLayout_4.addWidget(self.line_9)

        self.remove_batch_cb_pushButton = QPushButton(self.create_batch)
        self.remove_batch_cb_pushButton.setObjectName(u"remove_batch_cb_pushButton")
        self.remove_batch_cb_pushButton.setEnabled(True)
        sizePolicy7.setHeightForWidth(self.remove_batch_cb_pushButton.sizePolicy().hasHeightForWidth())
        self.remove_batch_cb_pushButton.setSizePolicy(sizePolicy7)
        self.remove_batch_cb_pushButton.setMinimumSize(QSize(90, 60))
        self.remove_batch_cb_pushButton.setBaseSize(QSize(0, 0))
        self.remove_batch_cb_pushButton.setFont(font)
        self.remove_batch_cb_pushButton.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.remove_batch_cb_pushButton)

        self.remove_order_cb_pushButton = QPushButton(self.create_batch)
        self.remove_order_cb_pushButton.setObjectName(u"remove_order_cb_pushButton")
        self.remove_order_cb_pushButton.setEnabled(True)
        sizePolicy7.setHeightForWidth(self.remove_order_cb_pushButton.sizePolicy().hasHeightForWidth())
        self.remove_order_cb_pushButton.setSizePolicy(sizePolicy7)
        self.remove_order_cb_pushButton.setMinimumSize(QSize(90, 60))
        self.remove_order_cb_pushButton.setBaseSize(QSize(0, 0))

        self.verticalLayout_4.addWidget(self.remove_order_cb_pushButton)

        self.remove_cart_cb_pushButton = QPushButton(self.create_batch)
        self.remove_cart_cb_pushButton.setObjectName(u"remove_cart_cb_pushButton")
        self.remove_cart_cb_pushButton.setEnabled(True)
        sizePolicy7.setHeightForWidth(self.remove_cart_cb_pushButton.sizePolicy().hasHeightForWidth())
        self.remove_cart_cb_pushButton.setSizePolicy(sizePolicy7)
        self.remove_cart_cb_pushButton.setMinimumSize(QSize(90, 60))
        self.remove_cart_cb_pushButton.setBaseSize(QSize(0, 0))
        self.remove_cart_cb_pushButton.setAutoFillBackground(False)

        self.verticalLayout_4.addWidget(self.remove_cart_cb_pushButton)

        self.remove_row_cb_pushButton = QPushButton(self.create_batch)
        self.remove_row_cb_pushButton.setObjectName(u"remove_row_cb_pushButton")
        sizePolicy7.setHeightForWidth(self.remove_row_cb_pushButton.sizePolicy().hasHeightForWidth())
        self.remove_row_cb_pushButton.setSizePolicy(sizePolicy7)

        self.verticalLayout_4.addWidget(self.remove_row_cb_pushButton)


        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 4, 2, 1)

        self.line_3 = QFrame(self.create_batch)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_3, 0, 5, 2, 1)

        self.cb_verticalLayout_22 = QVBoxLayout()
        self.cb_verticalLayout_22.setObjectName(u"cb_verticalLayout_22")
        self.locb_descr_label_2 = QLabel(self.create_batch)
        self.locb_descr_label_2.setObjectName(u"locb_descr_label_2")
        self.locb_descr_label_2.setAlignment(Qt.AlignCenter)

        self.cb_verticalLayout_22.addWidget(self.locb_descr_label_2)

        self.locb_cb_tableView = QTableView(self.create_batch)
        self.locb_cb_tableView.setObjectName(u"locb_cb_tableView")
        sizePolicy3.setHeightForWidth(self.locb_cb_tableView.sizePolicy().hasHeightForWidth())
        self.locb_cb_tableView.setSizePolicy(sizePolicy3)
        self.locb_cb_tableView.setMaximumSize(QSize(190, 16777215))
        self.locb_cb_tableView.setFrameShadow(QFrame.Raised)
        self.locb_cb_tableView.setEditTriggers(QAbstractItemView.CurrentChanged|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.locb_cb_tableView.setSortingEnabled(True)

        self.cb_verticalLayout_22.addWidget(self.locb_cb_tableView)


        self.gridLayout_3.addLayout(self.cb_verticalLayout_22, 0, 6, 2, 1)

        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.dv_descr_label = QLabel(self.create_batch)
        self.dv_descr_label.setObjectName(u"dv_descr_label")

        self.horizontalLayout_25.addWidget(self.dv_descr_label)

        self.items_qty_pushButton = QPushButton(self.create_batch)
        self.items_qty_pushButton.setObjectName(u"items_qty_pushButton")

        self.horizontalLayout_25.addWidget(self.items_qty_pushButton)

        self.cbfs_cb_pushButton = QPushButton(self.create_batch)
        self.cbfs_cb_pushButton.setObjectName(u"cbfs_cb_pushButton")

        self.horizontalLayout_25.addWidget(self.cbfs_cb_pushButton)

        self.horizontalLayout_25.setStretch(0, 1)

        self.verticalLayout_34.addLayout(self.horizontalLayout_25)

        self.dv_cb_tableView = QTableView(self.create_batch)
        self.dv_cb_tableView.setObjectName(u"dv_cb_tableView")
        sizePolicy3.setHeightForWidth(self.dv_cb_tableView.sizePolicy().hasHeightForWidth())
        self.dv_cb_tableView.setSizePolicy(sizePolicy3)
        font11 = QFont()
        font11.setPointSize(11)
        font11.setBold(True)
        font11.setItalic(False)
        font11.setWeight(75)
        self.dv_cb_tableView.setFont(font11)
        self.dv_cb_tableView.setSortingEnabled(False)
        self.dv_cb_tableView.setCornerButtonEnabled(False)

        self.verticalLayout_34.addWidget(self.dv_cb_tableView)


        self.gridLayout_3.addLayout(self.verticalLayout_34, 1, 2, 1, 1)

        self.gridLayout_3.setColumnStretch(2, 1)
        self.batch_br_tabWidget.addTab(self.create_batch, "")

        self.verticalLayout_24.addWidget(self.batch_br_tabWidget)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_2)

        self.info_panel_groupBox = QGroupBox(self.layoutWidget)
        self.info_panel_groupBox.setObjectName(u"info_panel_groupBox")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.info_panel_groupBox.sizePolicy().hasHeightForWidth())
        self.info_panel_groupBox.setSizePolicy(sizePolicy8)
        self.info_panel_groupBox.setMinimumSize(QSize(0, 0))
        self.info_panel_groupBox.setAutoFillBackground(False)
        self.horizontalLayout_26 = QHBoxLayout(self.info_panel_groupBox)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.lopi_descr_label = QLabel(self.info_panel_groupBox)
        self.lopi_descr_label.setObjectName(u"lopi_descr_label")
        sizePolicy5.setHeightForWidth(self.lopi_descr_label.sizePolicy().hasHeightForWidth())
        self.lopi_descr_label.setSizePolicy(sizePolicy5)

        self.verticalLayout_22.addWidget(self.lopi_descr_label)

        self.lopi_tableView = QTableView(self.info_panel_groupBox)
        self.lopi_tableView.setObjectName(u"lopi_tableView")
        sizePolicy1.setHeightForWidth(self.lopi_tableView.sizePolicy().hasHeightForWidth())
        self.lopi_tableView.setSizePolicy(sizePolicy1)
        self.lopi_tableView.setMinimumSize(QSize(0, 260))
        self.lopi_tableView.setSortingEnabled(False)

        self.verticalLayout_22.addWidget(self.lopi_tableView)

        self.verticalLayout_22.setStretch(1, 1)

        self.horizontalLayout_26.addLayout(self.verticalLayout_22)


        self.verticalLayout_24.addWidget(self.info_panel_groupBox)

        self.scanning_groupBox = QGroupBox(self.layoutWidget)
        self.scanning_groupBox.setObjectName(u"scanning_groupBox")
        self.scanning_groupBox.setEnabled(False)
        self.scanning_groupBox.setMaximumSize(QSize(16777215, 140))
        self.scanning_groupBox.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_28 = QHBoxLayout(self.scanning_groupBox)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.start_pushButton = QPushButton(self.scanning_groupBox)
        self.start_pushButton.setObjectName(u"start_pushButton")
        self.start_pushButton.setEnabled(False)
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.start_pushButton.sizePolicy().hasHeightForWidth())
        self.start_pushButton.setSizePolicy(sizePolicy9)
        self.start_pushButton.setMinimumSize(QSize(120, 120))
        self.start_pushButton.setMaximumSize(QSize(120, 120))
        font12 = QFont()
        font12.setFamily(u"FreeSans")
        font12.setPointSize(16)
        font12.setBold(True)
        font12.setItalic(False)
        font12.setWeight(75)
        self.start_pushButton.setFont(font12)
        self.start_pushButton.setAutoFillBackground(False)
        self.start_pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0.503, y1:0, x2:0.513, y2:1, stop:0.120192 rgba(36, 126, 0, 255), stop:1 rgba(0, 229, 33, 246));\n"
"border-radius: 15px;\n"
"color: white}\n"
"QPushButton:disabled{	\n"
"	background-image:url(:/glossy_buttons/glossy_button.png);\n"
"	background-position: center center;\n"
"}\n"
"")
        self.start_pushButton.setInputMethodHints(Qt.ImhNone)
        self.start_pushButton.setCheckable(True)
        self.start_pushButton.setChecked(False)
        self.start_pushButton.setAutoRepeat(False)

        self.horizontalLayout_28.addWidget(self.start_pushButton)

        self.barcode_scan_lineEdit = QLineEdit(self.scanning_groupBox)
        self.barcode_scan_lineEdit.setObjectName(u"barcode_scan_lineEdit")
        self.barcode_scan_lineEdit.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.barcode_scan_lineEdit.sizePolicy().hasHeightForWidth())
        self.barcode_scan_lineEdit.setSizePolicy(sizePolicy5)
        font13 = QFont()
        font13.setFamily(u"FreeSans")
        font13.setPointSize(36)
        font13.setBold(True)
        font13.setItalic(False)
        font13.setWeight(75)
        self.barcode_scan_lineEdit.setFont(font13)
        self.barcode_scan_lineEdit.setCursor(QCursor(Qt.WaitCursor))
        self.barcode_scan_lineEdit.setStyleSheet(u"QLineEdit:disabled{\n"
"	background-color: qlineargradient(spread:pad, x1:0.508338, y1:0, x2:0.527, y2:1, stop:0.391304 rgba(255, 0, 0, 0), stop:1 rgba(179, 0, 0, 173));\n"
"	color:white\n"
"}\n"
"QLineEdit:enabled{\n"
"background-color: qlineargradient(spread:pad, x1:0.508338, y1:0, x2:0.517, y2:1, stop:0.391304 rgba(255, 0, 0, 0), stop:1 rgba(20, 80, 0, 255));\n"
"}")
        self.barcode_scan_lineEdit.setAlignment(Qt.AlignCenter)
        self.barcode_scan_lineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_28.addWidget(self.barcode_scan_lineEdit, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.barcode_label = QLabel(self.scanning_groupBox)
        self.barcode_label.setObjectName(u"barcode_label")
        sizePolicy2.setHeightForWidth(self.barcode_label.sizePolicy().hasHeightForWidth())
        self.barcode_label.setSizePolicy(sizePolicy2)
        self.barcode_label.setMaximumSize(QSize(500, 120))
        self.barcode_label.setFrameShape(QFrame.StyledPanel)
        self.barcode_label.setFrameShadow(QFrame.Raised)
        self.barcode_label.setLineWidth(2)
        self.barcode_label.setScaledContents(True)
        self.barcode_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_28.addWidget(self.barcode_label)

        self.counters_gridLayout = QGridLayout()
        self.counters_gridLayout.setObjectName(u"counters_gridLayout")
        self.orders_left_descr_label = QLabel(self.scanning_groupBox)
        self.orders_left_descr_label.setObjectName(u"orders_left_descr_label")
        font14 = QFont()
        font14.setPointSize(14)
        font14.setBold(False)
        font14.setItalic(False)
        font14.setWeight(50)
        self.orders_left_descr_label.setFont(font14)
        self.orders_left_descr_label.setAlignment(Qt.AlignCenter)

        self.counters_gridLayout.addWidget(self.orders_left_descr_label, 0, 1, 1, 1)

        self.items_left_descr_label = QLabel(self.scanning_groupBox)
        self.items_left_descr_label.setObjectName(u"items_left_descr_label")
        self.items_left_descr_label.setFont(font14)
        self.items_left_descr_label.setStyleSheet(u"")
        self.items_left_descr_label.setAlignment(Qt.AlignCenter)

        self.counters_gridLayout.addWidget(self.items_left_descr_label, 0, 0, 1, 1)

        self.orders_left_label = QLabel(self.scanning_groupBox)
        self.orders_left_label.setObjectName(u"orders_left_label")
        self.orders_left_label.setMinimumSize(QSize(100, 0))
        self.orders_left_label.setFont(font4)
        self.orders_left_label.setStyleSheet(u"border: 4px solid rgb(213, 0, 0);\n"
"border-radius: 10px;\n"
"")
        self.orders_left_label.setAlignment(Qt.AlignCenter)

        self.counters_gridLayout.addWidget(self.orders_left_label, 1, 1, 1, 1)

        self.items_left_label = QLabel(self.scanning_groupBox)
        self.items_left_label.setObjectName(u"items_left_label")
        self.items_left_label.setMinimumSize(QSize(100, 0))
        self.items_left_label.setFont(font4)
        self.items_left_label.setStyleSheet(u"border: 4px solid rgb(213, 0, 0);\n"
"border-radius: 10px;\n"
"")
        self.items_left_label.setAlignment(Qt.AlignCenter)

        self.counters_gridLayout.addWidget(self.items_left_label, 1, 0, 1, 1)


        self.horizontalLayout_28.addLayout(self.counters_gridLayout)


        self.verticalLayout_24.addWidget(self.scanning_groupBox)

        self.verticalLayout_24.setStretch(2, 1)
        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget2 = QWidget(self.splitter)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.verticalLayout_31 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.batch_frame = QFrame(self.layoutWidget2)
        self.batch_frame.setObjectName(u"batch_frame")
        self.batch_frame.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.batch_frame.sizePolicy().hasHeightForWidth())
        self.batch_frame.setSizePolicy(sizePolicy5)
        self.batch_frame.setMinimumSize(QSize(0, 140))
        self.batch_frame.setMaximumSize(QSize(16777215, 16777215))
        self.batch_frame.setStyleSheet(u"#batch_frame{border-radius:10px; border: 4px solid rgb(213, 0, 0)}")
        self.verticalLayout_30 = QVBoxLayout(self.batch_frame)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(10, -1, 10, 0)
        self.title_batch_label = QLabel(self.batch_frame)
        self.title_batch_label.setObjectName(u"title_batch_label")
        sizePolicy.setHeightForWidth(self.title_batch_label.sizePolicy().hasHeightForWidth())
        self.title_batch_label.setSizePolicy(sizePolicy)
        self.title_batch_label.setMinimumSize(QSize(0, 30))
        font15 = QFont()
        font15.setPointSize(36)
        font15.setBold(True)
        font15.setItalic(False)
        font15.setWeight(75)
        self.title_batch_label.setFont(font15)
        self.title_batch_label.setStyleSheet(u"QLabel{\n"
"border-radius: 25px}\n"
"\n"
"QLabel:enabled{	\n"
"	\n"
"	background-color: qlineargradient(spread:reflect, x1:0.192324, y1:0.506, x2:0.199, y2:1, stop:0.352657 rgba(18, 255, 0, 88), stop:0.942029 rgba(0, 0, 0, 0));\n"
"}\n"
"QLabel:disabled{	\n"
"	\n"
"	\n"
"	background-color: qlineargradient(spread:reflect, x1:0.192324, y1:0.506, x2:0.199, y2:1, stop:0.338164 rgba(144, 0, 0, 87), stop:0.942029 rgba(0, 0, 0, 0));\n"
"}")
        self.title_batch_label.setFrameShape(QFrame.StyledPanel)
        self.title_batch_label.setTextFormat(Qt.AutoText)
        self.title_batch_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.title_batch_label)

        self.wall_progress_descr_label = QLabel(self.batch_frame)
        self.wall_progress_descr_label.setObjectName(u"wall_progress_descr_label")
        self.wall_progress_descr_label.setMinimumSize(QSize(0, 0))
        self.wall_progress_descr_label.setMaximumSize(QSize(16777215, 20))
        self.wall_progress_descr_label.setFont(font)
        self.wall_progress_descr_label.setStyleSheet(u"color: white;")
        self.wall_progress_descr_label.setAlignment(Qt.AlignCenter)
        self.wall_progress_descr_label.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_25.addWidget(self.wall_progress_descr_label)

        self.progressBar_batch = QProgressBar(self.batch_frame)
        self.progressBar_batch.setObjectName(u"progressBar_batch")
        self.progressBar_batch.setMinimumSize(QSize(0, 0))
        font16 = QFont()
        font16.setPointSize(14)
        font16.setBold(True)
        font16.setWeight(75)
        self.progressBar_batch.setFont(font16)
        self.progressBar_batch.setAutoFillBackground(False)
        self.progressBar_batch.setStyleSheet(u"\n"
"color:white;\n"
"")
        self.progressBar_batch.setValue(0)
        self.progressBar_batch.setAlignment(Qt.AlignCenter)
        self.progressBar_batch.setInvertedAppearance(False)
        self.progressBar_batch.setTextDirection(QProgressBar.BottomToTop)

        self.verticalLayout_25.addWidget(self.progressBar_batch)


        self.verticalLayout_29.addLayout(self.verticalLayout_25)

        self.line_5 = QFrame(self.batch_frame)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"background-color:rgb(213, 0, 0)")
        self.line_5.setFrameShadow(QFrame.Raised)
        self.line_5.setFrameShape(QFrame.HLine)

        self.verticalLayout_29.addWidget(self.line_5)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.batch_no_descr_label = QLabel(self.batch_frame)
        self.batch_no_descr_label.setObjectName(u"batch_no_descr_label")
        self.batch_no_descr_label.setFont(font16)
        self.batch_no_descr_label.setStyleSheet(u"")
        self.batch_no_descr_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.batch_no_descr_label)

        self.batch_no_label = QLabel(self.batch_frame)
        self.batch_no_label.setObjectName(u"batch_no_label")
        font17 = QFont()
        font17.setPointSize(24)
        font17.setBold(True)
        font17.setItalic(True)
        font17.setWeight(75)
        self.batch_no_label.setFont(font17)
        self.batch_no_label.setStyleSheet(u"border: 2px outline ;\n"
"border-radius: 15px;\n"
"border-bottom-style: solid;\n"
"border-bottom-color: rgb(66, 66, 66);")
        self.batch_no_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.batch_no_label)


        self.horizontalLayout_27.addLayout(self.verticalLayout_28)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.orders_qty_descr_label = QLabel(self.batch_frame)
        self.orders_qty_descr_label.setObjectName(u"orders_qty_descr_label")
        self.orders_qty_descr_label.setFont(font16)
        self.orders_qty_descr_label.setStyleSheet(u"")
        self.orders_qty_descr_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.orders_qty_descr_label)

        self.orders_qty_label = QLabel(self.batch_frame)
        self.orders_qty_label.setObjectName(u"orders_qty_label")
        self.orders_qty_label.setFont(font17)
        self.orders_qty_label.setStyleSheet(u"border: 2px outline ;\n"
"border-radius: 15px;\n"
"border-bottom-style: solid;\n"
"border-bottom-color: rgb(66, 66, 66);\n"
"")
        self.orders_qty_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.orders_qty_label)


        self.horizontalLayout_27.addLayout(self.verticalLayout_27)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.carts_qty_descr_label = QLabel(self.batch_frame)
        self.carts_qty_descr_label.setObjectName(u"carts_qty_descr_label")
        self.carts_qty_descr_label.setFont(font16)
        self.carts_qty_descr_label.setStyleSheet(u"")
        self.carts_qty_descr_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.carts_qty_descr_label)

        self.carts_qty_label = QLabel(self.batch_frame)
        self.carts_qty_label.setObjectName(u"carts_qty_label")
        self.carts_qty_label.setFont(font17)
        self.carts_qty_label.setStyleSheet(u"border: 2px outline ;\n"
"border-radius: 15px;\n"
"border-bottom-style: solid;\n"
"border-bottom-color: rgb(66, 66, 66);\n"
"")
        self.carts_qty_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.carts_qty_label)


        self.horizontalLayout_27.addLayout(self.verticalLayout_26)


        self.verticalLayout_29.addLayout(self.horizontalLayout_27)


        self.verticalLayout_30.addLayout(self.verticalLayout_29)


        self.verticalLayout_31.addWidget(self.batch_frame)

        self.message_frame = QFrame(self.layoutWidget2)
        self.message_frame.setObjectName(u"message_frame")
        sizePolicy6.setHeightForWidth(self.message_frame.sizePolicy().hasHeightForWidth())
        self.message_frame.setSizePolicy(sizePolicy6)
        self.message_frame.setMinimumSize(QSize(0, 0))
        self.message_frame.setMaximumSize(QSize(16777215, 200))
        self.message_frame.setStyleSheet(u"#message_frame{border-radius:10px;border: 4px solid rgb(213, 0, 0)}")
        self.message_frame.setFrameShape(QFrame.StyledPanel)
        self.message_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.message_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.message_descr_label = QLabel(self.message_frame)
        self.message_descr_label.setObjectName(u"message_descr_label")
        sizePolicy8.setHeightForWidth(self.message_descr_label.sizePolicy().hasHeightForWidth())
        self.message_descr_label.setSizePolicy(sizePolicy8)
        self.message_descr_label.setFont(font16)
        self.message_descr_label.setStyleSheet(u"color:white")
        self.message_descr_label.setLineWidth(1)
        self.message_descr_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.message_descr_label)

        self.shelf_textBrowser = QTextBrowser(self.message_frame)
        self.shelf_textBrowser.setObjectName(u"shelf_textBrowser")
        sizePolicy1.setHeightForWidth(self.shelf_textBrowser.sizePolicy().hasHeightForWidth())
        self.shelf_textBrowser.setSizePolicy(sizePolicy1)
        self.shelf_textBrowser.setMinimumSize(QSize(0, 0))
        self.shelf_textBrowser.setStyleSheet(u"QTextBrowser:{border-radius:15px;color:white}")
        self.shelf_textBrowser.setAutoFormatting(QTextEdit.AutoAll)
        self.shelf_textBrowser.setTabChangesFocus(False)
        self.shelf_textBrowser.setOverwriteMode(True)
        self.shelf_textBrowser.setOpenLinks(False)

        self.horizontalLayout_3.addWidget(self.shelf_textBrowser)


        self.verticalLayout_31.addWidget(self.message_frame)

        self.groupBox_shelf = QGroupBox(self.layoutWidget2)
        self.groupBox_shelf.setObjectName(u"groupBox_shelf")
        sizePolicy6.setHeightForWidth(self.groupBox_shelf.sizePolicy().hasHeightForWidth())
        self.groupBox_shelf.setSizePolicy(sizePolicy6)
        self.groupBox_shelf.setMinimumSize(QSize(0, 400))
        font18 = QFont()
        font18.setPointSize(14)
        font18.setBold(True)
        font18.setItalic(False)
        font18.setWeight(75)
        self.groupBox_shelf.setFont(font18)
        self.groupBox_shelf.setAutoFillBackground(False)
        self.groupBox_shelf.setStyleSheet(u"border-radius:10px;\n"
"border: 4px solid rgb(213, 0, 0);\n"
"")
        self.groupBox_shelf.setAlignment(Qt.AlignCenter)
        self.groupBox_shelf.setFlat(False)
        self.groupBox_shelf.setCheckable(False)
        self.gridLayout = QGridLayout(self.groupBox_shelf)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_sh_8 = QGroupBox(self.groupBox_shelf)
        self.groupBox_sh_8.setObjectName(u"groupBox_sh_8")
        self.groupBox_sh_8.setStyleSheet(u"border: 2px oultine rgb(95,95,95);")
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_sh_8)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.shelf_no_label_sh_8 = QLabel(self.groupBox_sh_8)
        self.shelf_no_label_sh_8.setObjectName(u"shelf_no_label_sh_8")
        font19 = QFont()
        font19.setFamily(u"FreeSans")
        font19.setPointSize(26)
        font19.setBold(True)
        font19.setWeight(75)
        self.shelf_no_label_sh_8.setFont(font19)
        self.shelf_no_label_sh_8.setStyleSheet(u"border-color: rgb(83, 83, 83);\n"
"background-color: rgb(70, 70, 70);\n"
"color: rgb(255, 255, 255);")
        self.shelf_no_label_sh_8.setFrameShape(QFrame.Panel)
        self.shelf_no_label_sh_8.setFrameShadow(QFrame.Raised)
        self.shelf_no_label_sh_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.shelf_no_label_sh_8)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.qty_descr_label_sh_8 = QLabel(self.groupBox_sh_8)
        self.qty_descr_label_sh_8.setObjectName(u"qty_descr_label_sh_8")
        font20 = QFont()
        font20.setFamily(u"FreeSans")
        font20.setPointSize(14)
        font20.setBold(True)
        font20.setWeight(75)
        self.qty_descr_label_sh_8.setFont(font20)
        self.qty_descr_label_sh_8.setStyleSheet(u"border-color: rgb(130, 130, 130);\n"
"color: rgb(255, 255, 255);\n"
"padding: 5px;\n"
"")
        self.qty_descr_label_sh_8.setFrameShadow(QFrame.Sunken)
        self.qty_descr_label_sh_8.setLineWidth(0)

        self.horizontalLayout_17.addWidget(self.qty_descr_label_sh_8)

        self.qty_label_sh_8 = QLabel(self.groupBox_sh_8)
        self.qty_label_sh_8.setObjectName(u"qty_label_sh_8")
        self.qty_label_sh_8.setMinimumSize(QSize(0, 0))
        font21 = QFont()
        font21.setFamily(u"FreeSans")
        font21.setPointSize(15)
        font21.setBold(True)
        font21.setWeight(75)
        self.qty_label_sh_8.setFont(font21)
        self.qty_label_sh_8.setStyleSheet(u"border-bottom-style: solid;\n"
"border-bottom-color: rgb(66, 66, 66);\n"
"")
        self.qty_label_sh_8.setFrameShape(QFrame.Box)
        self.qty_label_sh_8.setFrameShadow(QFrame.Plain)
        self.qty_label_sh_8.setLineWidth(3)
        self.qty_label_sh_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.qty_label_sh_8.setIndent(-1)

        self.horizontalLayout_17.addWidget(self.qty_label_sh_8)


        self.verticalLayout_18.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.order_descr_label_sh_8 = QLabel(self.groupBox_sh_8)
        self.order_descr_label_sh_8.setObjectName(u"order_descr_label_sh_8")
        self.order_descr_label_sh_8.setFont(font20)
        self.order_descr_label_sh_8.setStyleSheet(u"border-color: rgb(130, 130, 130);\n"
"color: rgb(255, 255, 255);\n"
"padding: 5px;\n"
"")
        self.order_descr_label_sh_8.setFrameShadow(QFrame.Plain)
        self.order_descr_label_sh_8.setLineWidth(0)

        self.horizontalLayout_18.addWidget(self.order_descr_label_sh_8)

        self.order_label_sh_8 = QLabel(self.groupBox_sh_8)
        self.order_label_sh_8.setObjectName(u"order_label_sh_8")
        self.order_label_sh_8.setMinimumSize(QSize(0, 0))
        self.order_label_sh_8.setFont(font21)
        self.order_label_sh_8.setStyleSheet(u"border-bottom-style: solid;\n"
"border-bottom-color: rgb(66, 66, 66);\n"
"")
        self.order_label_sh_8.setFrameShadow(QFrame.Sunken)
        self.order_label_sh_8.setLineWidth(4)
        self.order_label_sh_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.order_label_sh_8.setIndent(2)

        self.horizontalLayout_18.addWidget(self.order_label_sh_8)

        self.horizontalLayout_18.setStretch(1, 1)

        self.verticalLayout_18.addLayout(self.horizontalLayout_18)

        self.progressBar_sh_8 = QProgressBar(self.groupBox_sh_8)
        self.progressBar_sh_8.setObjectName(u"progressBar_sh_8")
        self.progressBar_sh_8.setFont(font7)
        self.progressBar_sh_8.setAcceptDrops(False)
        self.progressBar_sh_8.setStyleSheet(u"border-color: rgb(130, 130, 130);\n"
"background-color: rgb(79, 79, 79);\n"
"color: rgb(255, 255, 255);")
        self.progressBar_sh_8.setValue(0)
        self.progressBar_sh_8.setAlignment(Qt.AlignCenter)
        self.progressBar_sh_8.setOrientation(Qt.Horizontal)
        self.progressBar_sh_8.setInvertedAppearance(False)
        self.progressBar_sh_8.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_18.addWidget(self.progressBar_sh_8)


        self.verticalLayout_17.addLayout(self.verticalLayout_18)


        self.gridLayout.addWidget(self.groupBox_sh_8, 0, 2, 1, 1)

        self.groupBox_sh_3 = QGroupBox(self.groupBox_shelf)
        self.groupBox_sh_3.setObjectName(u"groupBox_sh_3")
        self.groupBox_sh_3.setStyleSheet(u"border: 2px oultine rgb(95,95,95);")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_sh_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.shelf_no_label_sh_3 = QLabel(self.groupBox_sh_3)
        self.shelf_no_label_sh_3.setObjectName(u"shelf_no_label_sh_3")
        self.shelf_no_label_sh_3.setFont(font19)
        self.shelf_no_label_sh_3.setStyleSheet(u"border-color: rgb(83, 83, 83);\n"
"background-color: rgb(70, 70, 70);\n"
"color: rgb(255, 255, 255);")
        self.shelf_no_label_sh_3.setFrameShape(QFrame.Panel)
        self.shelf_no_label_sh_3.setFrameShadow(QFrame.Raised)
        self.shelf_no_label_sh_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.shelf_no_label_sh_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.qty_descr_label_sh_3 = QLabel(self.groupBox_sh_3)
        self.qty_descr_label_sh_3.setObjectName(u"qty_descr_label_sh_3")
        self.qty_descr_label_sh_3.setFont(font20)
        self.qty_descr_label_sh_3.setStyleSheet(u"border-color: rgb(130, 130, 130);\n"
"color: rgb(255, 255, 255);\n"
"padding: 5px;\n"
"")
        self.qty_descr_label_sh_3.setFrameShadow(QFrame.Sunken)
        self.qty_descr_label_sh_3.setLineWidth(0)

        self.horizontalLayout_7.addWidget(self.qty_descr_label_sh_3)

        self.qty_label_sh_3 = QLabel(self.groupBox_sh_3)
        self.qty_label_sh_3.setObjectName(u"qty_label_sh_3")
        self.qty_label_sh_3.setMinimumSize(QSize(0, 0))
        self.qty_label_sh_3.setFont(font21)
        self.qty_label_sh_3.setStyleSheet(u"border-bottom-style: solid;\n"
"border-bottom-color: rgb(66, 66, 66);\n"
"")
        self.qty_label_sh_3.setFrameShape(QFrame.Box)
        self.qty_label_sh_3.setFrameShadow(QFrame.Plain)
        self.qty_label_sh_3.setLineWidth(3)
        self.qty_label_sh_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.qty_label_sh_3.setIndent(-1)

        self.horizontalLayout_7.addWidget(self.qty_label_sh_3)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.order_descr_label_sh_3 = QLabel(self.groupBox_sh_3)
        self.order_descr_label_sh_3.setObjectName(u"order_descr_label_sh_3")
        self.order_descr_label_sh_3.setFont(font20)
        self.order_descr_label_sh_3.setStyleSheet(u"border-color: rgb(130, 130, 130);\n"
"color: rgb(255, 255, 255);\n"
"padding: 5px;\n"
"")
        self.order_descr_label_sh_3.setFrameShadow(QFrame.Plain)
        self.order_descr_label_sh_3.setLineWidth(0)

        self.horizontalLayout_8.addWidget(self.order_descr_label_sh_3)

        self.order_label_sh_3 = QLabel(self.groupBox_sh_3)
        self.order_label_sh_3.setObjectName(u"order_label_sh_3")
        self.order_label_sh_3.setMinimumSize(QSize(0, 0))
        self.order_label_sh_3.setFont(font21)
        self.order_label_sh_3.setStyleSheet(u"border-bottom-style: solid;\n"
"border-bottom-color: rgb(66, 66, 66);\n"
"")
        self.order_label_sh_3.setFrameShadow(QFrame.Sunken)
        self.order_label_sh_3.setLineWidth(4)
        self.order_label_sh_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.order_label_sh_3.setIndent(2)

        self.horizontalLayout_8.addWidget(self.order_label_sh_3)

        self.horizontalLayout_8.setStretch(1, 1)

        self.verticalLayout_8.addLayout(self.horizontalLayout_8)

        self.progressBar_sh_3 = QProgressBar(self.groupBox_sh_3)
        self.progressBar_sh_3.setObjectName(u"progressBar_sh_3")
        self.progressBar_sh_3.setFont(font7)
        self.progressBar_sh_3.setAcceptDrops(False)
        self.progressBar_sh_3.setStyleSheet(u"border-color: rgb(130, 130, 130);\n"
"background-color: rgb(79, 79, 79);\n"
"color: rgb(255, 255, 255);")
        self.progressBar_sh_3.setValue(0)
        self.progressBar_sh_3.setAlignment(Qt.AlignCenter)
        self.progressBar_sh_3.setOrientation(Qt.Horizontal)
        self.progressBar_sh_3.setInvertedAppearance(False)
        self.progressBar_sh_3.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_8.addWidget(self.progressBar_sh_3)


        self.verticalLayout_7.addLayout(self.verticalLayout_8)


        self.gridLayout.addWidget(self.groupBox_sh_3, 4, 4, 1, 1)

        self.groupBox_sh_7 = QGroupBox(self.groupBox_shelf)
        self.groupBox_sh_7.setObjectName(u"groupBox_sh_7")
        self.groupBox_sh_7.setStyleSheet(u"border: 2px oultine rgb(95,95,95);")
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_sh_7)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.shelf_no_label_sh_7 = QLabel(self.groupBox_sh_7)
        self.shelf_no_label_sh_7.setObjectName(u"shelf_no_label_sh_7")
        self.shelf_no_label_sh_7.setFont(font19)
        self.shelf_no_label_sh_7.setStyleSheet(u"border-color: rgb(83, 83, 83);\n"
"background-color: rgb(70, 70, 70);\n"
"color: rgb(255, 255, 255);")
        self.shelf_no_label_sh_7.setFrameShape(QFrame.Panel)
        self.shelf_no_label_sh_7.setFrameShadow(QFrame.Raised)
        self.shelf_no_label_sh_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.shelf_no_label_sh_7)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.qty_descr_label_sh_7 = QLabel(self.groupBox_sh_7)
        self.qty_descr_label_sh_7.setObjectName(u"qty_descr_label_sh_7")
        self.qty_descr_label_sh_7.setFont(font20)
        self.qty_descr_label_sh_7.setStyleSheet(u"border-color: rgb(130, 130, 130);\n"
"color: rgb(255, 255, 255);\n"
"padding: 5px;\n"
"")
        self.qty_descr_label_sh_7.setFrameShadow(QFrame.Sunken)
        self.qty_descr_label_sh_7.setLineWidth(0)

        self.horizontalLayout_15.addWidget(self.qty_descr_label_sh_7)

        self.qty_label_sh_7 = QLabel(self.groupBox_sh_7)
        self.qty_label_sh_7.setObjectName(u"qty_label_sh_7")
        self.qty_label_sh_7.setMinimumSize(QSize(0, 0))
        self.qty_label_sh_7.setFont(font21)
        self.qty_label_sh_7.setStyleSheet(u"border-bottom-style: solid;\n"
"border-bottom-color: rgb(66, 66, 66);\n"
"")
        self.qty_label_sh_7.setFrameShape(QFrame.Box)
        self.qty_label_sh_7.setFrameShadow(QFrame.Plain)
        self.qty_label_sh_7.setLineWidth(3)
        self.qty_label_sh_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.qty_label_sh_7.setIndent(-1)

        self.horizontalLayout_15.addWidget(self.qty_label_sh_7)


        self.verticalLayout_16.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.order_descr_label_sh_7 = QLabel(self.groupBox_sh_7)
        self.order_descr_label_sh_7.setObjectName(u"order_descr_label_sh_7")
        self.order_descr_label_sh_7.setFont(font20)
        self.order_descr_label_sh_7.setStyleSheet(u"border-color: rgb(130, 130, 130);\n"
"color: rgb(255, 255, 255);\n"
"padding: 5px;\n"
"")
        self.order_descr_label_sh_7.setFrameShadow(QFrame.Plain)
        self.order_descr_label_sh_7.setLineWidth(0)

        self.horizontalLayout_16.addWidget(self.order_descr_label_sh_7)

        self.order_label_sh_7 = QLabel(self.groupBox_sh_7)
        self.order_label_sh_7.setObjectName(u"order_label_sh_7")
        self.order_label_sh_7.setMinimumSize(QSize(0, 0))
        self.order_label_sh_7.setFont(font21)
        self.order_label_sh_7.setStyleSheet(u"border-bottom-style: solid;\n"
"border-bottom-color: rgb(66, 66, 66);\n"
"")
        self.order_label_sh_7.setFrameShadow(QFrame.Sunken)
        self.order_label_sh_7.setLineWidth(4)
        self.order_label_sh_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.order_label_sh_7.setIndent(2)

        self.horizontalLayout_16.addWidget(self.order_label_sh_7)


        self.verticalLayout_16.addLayout(self.horizontalLayout_16)

        self.progressBar_sh_7 = QProgressBar(self.groupBox_sh_7)
        self.progressBar_sh_7.setObjectName(u"progressBar_sh_7")
        self.progressBar_sh_7.setFont(font7)
        self.progressBar_sh_7.setAcceptDrops(False)
        self.progressBar_sh_7.setStyleSheet(u"border-color: rgb(130, 130, 130);\n"
"background-color: rgb(79, 79, 79);\n"
"color: rgb(255, 255, 255);")
        self.progressBar_sh_7.setValue(0)
        self.progressBar_sh_7.setAlignment(Qt.AlignCenter)
        self.progressBar_sh_7.setOrientation(Qt.Horizontal)
        self.progressBar_sh_7.setInvertedAppearance(False)
        self.progressBar_sh_7.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_16.addWidget(self.progressBar_sh_7)


        self.verticalLayout_15.addLayout(self.verticalLayout_16)


        self.gridLayout.addWidget(self.groupBox_sh_7, 0, 0, 1, 1)

        self.v_line_sh_1 = QFrame(self.groupBox_shelf)
        self.v_line_sh_1.setObjectName(u"v_line_sh_1")
        sizePolicy7.setHeightForWidth(self.v_line_sh_1.sizePolicy().hasHeightForWidth())
        self.v_line_sh_1.setSizePolicy(sizePolicy7)
        self.v_line_sh_1.setMinimumSize(QSize(0, 150))
        self.v_line_sh_1.setMaximumSize(QSize(3, 16777215))
        self.v_line_sh_1.setMouseTracking(True)
        self.v_line_sh_1.setLayoutDirection(Qt.LeftToRight)
        self.v_line_sh_1.setAutoFillBackground(False)
        self.v_line_sh_1.setStyleSheet(u"background-color: rgb(255, 0, 127);")
        self.v_line_sh_1.setFrameShadow(QFrame.Plain)
        self.v_line_sh_1.setLineWidth(3)
        self.v_line_sh_1.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.v_line_sh_1, 0, 1, 1, 1)

        self.h_line_sh2 = QFrame(self.groupBox_shelf)
        self.h_line_sh2.setObjectName(u"h_line_sh2")
        self.h_line_sh2.setMaximumSize(QSize(16777215, 3))
        self.h_line_sh2.setStyleSheet(u"background-color: rgb(255, 0, 127);")
        self.h_line_sh2.setFrameShadow(QFrame.Plain)
        self.h_line_sh2.setLineWidth(1)
        self.h_line_sh2.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.h_line_sh2, 3, 0, 1, 5)

        self.v_line_sh_4 = QFrame(self.groupBox_shelf)
        self.v_line_sh_4.setObjectName(u"v_line_sh_4")
        sizePolicy7.setHeightForWidth(self.v_line_sh_4.sizePolicy().hasHeightForWidth())
        self.v_line_sh_4.setSizePolicy(sizePolicy7)
        self.v_line_sh_4.setMinimumSize(QSize(0, 150))
        self.v_line_sh_4.setMaximumSize(QSize(3, 16777215))
        self.v_line_sh_4.setMouseTracking(True)
        self.v_line_sh_4.setLayoutDirection(Qt.LeftToRight)
        self.v_line_sh_4.setAutoFillBackground(False)
        self.v_line_sh_4.setStyleSheet(u"background-color: rgb(255, 0, 127);")
        self.v_line_sh_4.setFrameShadow(QFrame.Plain)
        self.v_line_sh_4.setLineWidth(3)
        self.v_line_sh_4.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.v_line_sh_4, 4, 3, 1, 1)

        self.groupBox_sh_9 = QGroupBox(self.groupBox_shelf)
        self.groupBox_sh_9.setObjectName(u"groupBox_sh_9")
        self.groupBox_sh_9.setStyleSheet(u"border: 2px oultine rgb(95,95,95);")
        self.verticalLayout_19 = QVBoxLayout(self.groupBox_sh_9)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.shelf_no_label_sh_9 = QLabel(self.groupBox_sh_9)
        self.shelf_no_label_sh_9.setObjectName(u"shelf_no_label_sh_9")
        self.shelf_no_label_sh_9.setFont(font19)
        self.shelf_no_label_sh_9.setStyleSheet(u"border-color: rgb(83, 83, 83);\n"
"background-color: rgb(70, 70, 70);\n"
"color: rgb(255, 255, 255);")
        self.shelf_no_label_sh_9.setFrameShape(QFrame.Panel)
        self.shelf_no_label_sh_9.setFrameShadow(QFrame.Raised)
        self.shelf_no_label_sh_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.shelf_no_label_sh_9)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.qty_descr_label_sh_9 = QLabel(self.groupBox_sh_9)
        self.qty_descr_label_sh_9.setObjectName(u"qty_descr_label_sh_9")
        self.qty_descr_label_sh_9.setFont(font20)
        self.qty_descr_label_sh_9.setStyleSheet(u"border-color: rgb(130, 130, 130);\n"
"color: rgb(255, 255, 255);\n"
"padding: 5px;\n"
"")
        self.qty_descr_label_sh_9.setFrameShadow(QFrame.Sunken)
        self.qty_descr_label_sh_9.setLineWidth(0)

        self.horizontalLayout_19.addWidget(self.qty_descr_label_sh_9)

        self.qty_label_sh_9 = QLabel(self.groupBox_sh_9)
        self.qty_label_sh_9.setObjectName(u"qty_label_sh_9")
        self.qty_label_sh_9.setMinimumSize(QSize(0, 0))
        self.qty_label_sh_9.setFont(font21)
        self.qty_label_sh_9.setStyleSheet(u"border-bottom-style: solid;\n"
"border-bottom-color: rgb(66, 66, 66);\n"
"")
        self.qty_label_sh_9.setFrameShape(QFrame.Box)
        self.qty_label_sh_9.setFrameShadow(QFrame.Plain)
        self.qty_label_sh_9.setLineWidth(3)
        self.qty_label_sh_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.qty_label_sh_9.setIndent(-1)

        self.horizontalLayout_19.addWidget(self.qty_label_sh_9)


        self.verticalLayout_20.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.order_descr_label_sh_9 = QLabel(self.groupBox_sh_9)
        self.order_descr_label_sh_9.setObjectName(u"order_descr_label_sh_9")
        self.order_descr_label_sh_9.setFont(font20)
        self.order_descr_label_sh_9.setStyleSheet(u"border-color: rgb(130, 130, 130);\n"
"color: rgb(255, 255, 255);\n"
"padding: 5px;\n"
"")
        self.order_descr_label_sh_9.setFrameShadow(QFrame.Plain)
        self.order_descr_label_sh_9.setLineWidth(0)

        self.horizontalLayout_20.addWidget(self.order_descr_label_sh_9)

        self.order_label_sh_9 = QLabel(self.groupBox_sh_9)
        self.order_label_sh_9.setObjectName(u"order_label_sh_9")
        self.order_label_sh_9.setMinimumSize(QSize(0, 0))
        self.order_label_sh_9.setFont(font21)
        self.order_label_sh_9.setStyleSheet(u"border-bottom-style: solid;\n"
"border-bottom-color: rgb(66, 66, 66);\n"
"")
        self.order_label_sh_9.setFrameShadow(QFrame.Sunken)
        self.order_label_sh_9.setLineWidth(4)
        self.order_label_sh_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.order_label_sh_9.setIndent(2)

        self.horizontalLayout_20.addWidget(self.order_label_sh_9)

        self.horizontalLayout_20.setStretch(1, 1)

        self.verticalLayout_20.addLayout(self.horizontalLayout_20)

        self.progressBar_sh_9 = QProgressBar(self.groupBox_sh_9)
        self.progressBar_sh_9.setObjectName(u"progressBar_sh_9")
        self.progressBar_sh_9.setFont(font7)
        self.progressBar_sh_9.setAcceptDrops(False)
        self.progressBar_sh_9.setStyleSheet(u"border-color: rgb(130, 130, 130);\n"
"background-color: rgb(79, 79, 79);\n"
"color: rgb(255, 255, 255);")
        self.progressBar_sh_9.setValue(0)
        self.progressBar_sh_9.setAlignment(Qt.AlignCenter)
        self.progressBar_sh_9.setOrientation(Qt.Horizontal)
        self.progressBar_sh_9.setInvertedAppearance(False)
        self.progressBar_sh_9.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_20.addWidget(self.progressBar_sh_9)


        self.verticalLayout_19.addLayout(self.verticalLayout_20)


        self.gridLayout.addWidget(self.groupBox_sh_9, 0, 4, 1, 1)

        self.groupBox_sh_2 = QGroupBox(self.groupBox_shelf)
        self.groupBox_sh_2.setObjectName(u"groupBox_sh_2")
        self.groupBox_sh_2.setStyleSheet(u"border: 2px oultine rgb(95,95,95);")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_sh_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.shelf_no_label_sh_2 = QLabel(self.groupBox_sh_2)
        self.shelf_no_label_sh_2.setObjectName(u"shelf_no_label_sh_2")
        self.shelf_no_label_sh_2.setFont(font19)
        self.shelf_no_label_sh_2.setStyleSheet(u"border-color: rgb(83, 83, 83);\n"
"background-color: rgb(70, 70, 70);\n"
"color: rgb(255, 255, 255);")
        self.shelf_no_label_sh_2.setFrameShape(QFrame.Panel)
        self.shelf_no_label_sh_2.setFrameShadow(QFrame.Raised)
        self.shelf_no_label_sh_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.shelf_no_label_sh_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.qty_descr_label_sh_2 = QLabel(self.groupBox_sh_2)
        self.qty_descr_label_sh_2.setObjectName(u"qty_descr_label_sh_2")
        self.qty_descr_label_sh_2.setFont(font20)
        self.qty_descr_label_sh_2.setStyleSheet(u"border-color: rgb(130, 130, 130);\n"
"color: rgb(255, 255, 255);\n"
"padding: 5px;\n"
"")
        self.qty_descr_label_sh_2.setFrameShadow(QFrame.Sunken)
        self.qty_descr_label_sh_2.setLineWidth(0)

        self.horizontalLayout_5.addWidget(self.qty_descr_label_sh_2)

        self.qty_label_sh_2 = QLabel(self.groupBox_sh_2)
        self.qty_label_sh_2.setObjectName(u"qty_label_sh_2")
        self.qty_label_sh_2.setMinimumSize(QSize(0, 0))
        self.qty_label_sh_2.setFont(font21)
        self.qty_label_sh_2.setStyleSheet(u"border-bottom-style: solid;\n"
"border-bottom-color: rgb(66, 66, 66);\n"
"")
        self.qty_label_sh_2.setFrameShape(QFrame.Box)
        self.qty_label_sh_2.setFrameShadow(QFrame.Plain)
        self.qty_label_sh_2.setLineWidth(3)
        self.qty_label_sh_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.qty_label_sh_2.setIndent(-1)

        self.horizontalLayout_5.addWidget(self.qty_label_sh_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.order_descr_label_sh_2 = QLabel(self.groupBox_sh_2)
        self.order_descr_label_sh_2.setObjectName(u"order_descr_label_sh_2")
        self.order_descr_label_sh_2.setFont(font20)
        self.order_descr_label_sh_2.setStyleSheet(u"border-color: rgb(130, 130, 130);\n"
"color: rgb(255, 255, 255);\n"
"padding: 5px;\n"
"")
        self.order_descr_label_sh_2.setFrameShadow(QFrame.Plain)
        self.order_descr_label_sh_2.setLineWidth(0)

        self.horizontalLayout_6.addWidget(self.order_descr_label_sh_2)

        self.order_label_sh_2 = QLabel(self.groupBox_sh_2)
        self.order_label_sh_2.setObjectName(u"order_label_sh_2")
        self.order_label_sh_2.setMinimumSize(QSize(0, 0))
        self.order_label_sh_2.setFont(font21)
        self.order_label_sh_2.setStyleSheet(u"border-bottom-style: solid;\n"
"border-bottom-color: rgb(66, 66, 66);\n"
"")
        self.order_label_sh_2.setFrameShadow(QFrame.Sunken)
        self.order_label_sh_2.setLineWidth(4)
        self.order_label_sh_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.order_label_sh_2.setIndent(2)

        self.horizontalLayout_6.addWidget(self.order_label_sh_2)

        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.progressBar_sh_2 = QProgressBar(self.groupBox_sh_2)
        self.progressBar_sh_2.setObjectName(u"progressBar_sh_2")
        self.progressBar_sh_2.setFont(font7)
        self.progressBar_sh_2.setAcceptDrops(False)
        self.progressBar_sh_2.setStyleSheet(u"border-color: rgb(130, 130, 130);\n"
"background-color: rgb(79, 79, 79);\n"
"color: rgb(255, 255, 255);")
        self.progressBar_sh_2.setValue(0)
        self.progressBar_sh_2.setAlignment(Qt.AlignCenter)
        self.progressBar_sh_2.setOrientation(Qt.Horizontal)
        self.progressBar_sh_2.setInvertedAppearance(False)
        self.progressBar_sh_2.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_6.addWidget(self.progressBar_sh_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)


        self.gridLayout.addWidget(self.groupBox_sh_2, 4, 2, 1, 1)

        self.groupBox_sh_5 = QGroupBox(self.groupBox_shelf)
        self.groupBox_sh_5.setObjectName(u"groupBox_sh_5")
        self.groupBox_sh_5.setStyleSheet(u"border: 2px oultine rgb(95,95,95);")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_sh_5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.shelf_no_label_sh_5 = QLabel(self.groupBox_sh_5)
        self.shelf_no_label_sh_5.setObjectName(u"shelf_no_label_sh_5")
        self.shelf_no_label_sh_5.setFont(font19)
        self.shelf_no_label_sh_5.setStyleSheet(u"border-color: rgb(83, 83, 83);\n"
"background-color: rgb(70, 70, 70);\n"
"color: rgb(255, 255, 255);")
        self.shelf_no_label_sh_5.setFrameShape(QFrame.Panel)
        self.shelf_no_label_sh_5.setFrameShadow(QFrame.Raised)
        self.shelf_no_label_sh_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.shelf_no_label_sh_5)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.qty_descr_label_sh_5 = QLabel(self.groupBox_sh_5)
        self.qty_descr_label_sh_5.setObjectName(u"qty_descr_label_sh_5")
        self.qty_descr_label_sh_5.setFont(font20)
        self.qty_descr_label_sh_5.setStyleSheet(u"border-color: rgb(130, 130, 130);\n"
"color: rgb(255, 255, 255);\n"
"padding: 5px;\n"
"")
        self.qty_descr_label_sh_5.setFrameShadow(QFrame.Sunken)
        self.qty_descr_label_sh_5.setLineWidth(0)

        self.horizontalLayout_11.addWidget(self.qty_descr_label_sh_5)

        self.qty_label_sh_5 = QLabel(self.groupBox_sh_5)
        self.qty_label_sh_5.setObjectName(u"qty_label_sh_5")
        self.qty_label_sh_5.setMinimumSize(QSize(0, 0))
        self.qty_label_sh_5.setFont(font21)
        self.qty_label_sh_5.setStyleSheet(u"border-bottom-style: solid;\n"
"border-bottom-color: rgb(66, 66, 66);\n"
"")
        self.qty_label_sh_5.setFrameShape(QFrame.Box)
        self.qty_label_sh_5.setFrameShadow(QFrame.Plain)
        self.qty_label_sh_5.setLineWidth(3)
        self.qty_label_sh_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.qty_label_sh_5.setIndent(-1)

        self.horizontalLayout_11.addWidget(self.qty_label_sh_5)


        self.verticalLayout_12.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.order_descr_label_sh_5 = QLabel(self.groupBox_sh_5)
        self.order_descr_label_sh_5.setObjectName(u"order_descr_label_sh_5")
        self.order_descr_label_sh_5.setFont(font20)
        self.order_descr_label_sh_5.setStyleSheet(u"border-color: rgb(130, 130, 130);\n"
"color: rgb(255, 255, 255);\n"
"padding: 5px;\n"
"")
        self.order_descr_label_sh_5.setFrameShadow(QFrame.Plain)
        self.order_descr_label_sh_5.setLineWidth(0)

        self.horizontalLayout_12.addWidget(self.order_descr_label_sh_5)

        self.order_label_sh_5 = QLabel(self.groupBox_sh_5)
        self.order_label_sh_5.setObjectName(u"order_label_sh_5")
        self.order_label_sh_5.setMinimumSize(QSize(0, 0))
        self.order_label_sh_5.setFont(font21)
        self.order_label_sh_5.setStyleSheet(u"border-bottom-style: solid;\n"
"border-bottom-color: rgb(66, 66, 66);\n"
"")
        self.order_label_sh_5.setFrameShadow(QFrame.Sunken)
        self.order_label_sh_5.setLineWidth(4)
        self.order_label_sh_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.order_label_sh_5.setIndent(2)

        self.horizontalLayout_12.addWidget(self.order_label_sh_5)

        self.horizontalLayout_12.setStretch(1, 1)

        self.verticalLayout_12.addLayout(self.horizontalLayout_12)

        self.progressBar_sh_5 = QProgressBar(self.groupBox_sh_5)
        self.progressBar_sh_5.setObjectName(u"progressBar_sh_5")
        self.progressBar_sh_5.setFont(font7)
        self.progressBar_sh_5.setAcceptDrops(False)
        self.progressBar_sh_5.setStyleSheet(u"border-color: rgb(130, 130, 130);\n"
"background-color: rgb(79, 79, 79);\n"
"color: rgb(255, 255, 255);")
        self.progressBar_sh_5.setValue(0)
        self.progressBar_sh_5.setAlignment(Qt.AlignCenter)
        self.progressBar_sh_5.setOrientation(Qt.Horizontal)
        self.progressBar_sh_5.setInvertedAppearance(False)
        self.progressBar_sh_5.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_12.addWidget(self.progressBar_sh_5)


        self.verticalLayout_11.addLayout(self.verticalLayout_12)


        self.gridLayout.addWidget(self.groupBox_sh_5, 2, 2, 1, 1)

        self.groupBox_sh_1 = QGroupBox(self.groupBox_shelf)
        self.groupBox_sh_1.setObjectName(u"groupBox_sh_1")
        self.groupBox_sh_1.setStyleSheet(u"border:2px oultine rgb(95,95,95)")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_sh_1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.shelf_no_label_sh_1 = QLabel(self.groupBox_sh_1)
        self.shelf_no_label_sh_1.setObjectName(u"shelf_no_label_sh_1")
        self.shelf_no_label_sh_1.setFont(font19)
        self.shelf_no_label_sh_1.setStyleSheet(u"border-color: rgb(83, 83, 83);\n"
"background-color: rgb(70, 70, 70);\n"
"color: rgb(255, 255, 255);")
        self.shelf_no_label_sh_1.setFrameShape(QFrame.Panel)
        self.shelf_no_label_sh_1.setFrameShadow(QFrame.Raised)
        self.shelf_no_label_sh_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.shelf_no_label_sh_1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.qty_descr_label_sh_1 = QLabel(self.groupBox_sh_1)
        self.qty_descr_label_sh_1.setObjectName(u"qty_descr_label_sh_1")
        self.qty_descr_label_sh_1.setFont(font20)
        self.qty_descr_label_sh_1.setStyleSheet(u"border-color: rgb(130, 130, 130);\n"
"color: rgb(255, 255, 255);\n"
"padding: 5px;\n"
"")
        self.qty_descr_label_sh_1.setFrameShadow(QFrame.Sunken)
        self.qty_descr_label_sh_1.setLineWidth(0)

        self.horizontalLayout.addWidget(self.qty_descr_label_sh_1)

        self.qty_label_sh_1 = QLabel(self.groupBox_sh_1)
        self.qty_label_sh_1.setObjectName(u"qty_label_sh_1")
        self.qty_label_sh_1.setMinimumSize(QSize(0, 0))
        self.qty_label_sh_1.setFont(font21)
        self.qty_label_sh_1.setStyleSheet(u"border-bottom-style: solid;\n"
"border-bottom-color: rgb(66, 66, 66);\n"
"")
        self.qty_label_sh_1.setFrameShape(QFrame.Box)
        self.qty_label_sh_1.setFrameShadow(QFrame.Plain)
        self.qty_label_sh_1.setLineWidth(3)
        self.qty_label_sh_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.qty_label_sh_1.setIndent(-1)

        self.horizontalLayout.addWidget(self.qty_label_sh_1)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.order_descr_label_sh_1 = QLabel(self.groupBox_sh_1)
        self.order_descr_label_sh_1.setObjectName(u"order_descr_label_sh_1")
        self.order_descr_label_sh_1.setFont(font20)
        self.order_descr_label_sh_1.setStyleSheet(u"border-color: rgb(130, 130, 130);\n"
"color: rgb(255, 255, 255);\n"
"padding: 5px;\n"
"")
        self.order_descr_label_sh_1.setFrameShadow(QFrame.Plain)
        self.order_descr_label_sh_1.setLineWidth(0)

        self.horizontalLayout_2.addWidget(self.order_descr_label_sh_1)

        self.order_label_sh_1 = QLabel(self.groupBox_sh_1)
        self.order_label_sh_1.setObjectName(u"order_label_sh_1")
        self.order_label_sh_1.setMinimumSize(QSize(0, 0))
        self.order_label_sh_1.setFont(font21)
        self.order_label_sh_1.setStyleSheet(u"border-bottom-style: solid;\n"
"border-bottom-color: rgb(66, 66, 66);\n"
"")
        self.order_label_sh_1.setFrameShadow(QFrame.Sunken)
        self.order_label_sh_1.setLineWidth(4)
        self.order_label_sh_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.order_label_sh_1.setIndent(2)

        self.horizontalLayout_2.addWidget(self.order_label_sh_1)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.progressBar_sh_1 = QProgressBar(self.groupBox_sh_1)
        self.progressBar_sh_1.setObjectName(u"progressBar_sh_1")
        self.progressBar_sh_1.setFont(font7)
        self.progressBar_sh_1.setAcceptDrops(False)
        self.progressBar_sh_1.setStyleSheet(u"border-color: rgb(130, 130, 130);\n"
"background-color: rgb(79, 79, 79);\n"
"color: rgb(255, 255, 255);")
        self.progressBar_sh_1.setValue(0)
        self.progressBar_sh_1.setAlignment(Qt.AlignCenter)
        self.progressBar_sh_1.setOrientation(Qt.Horizontal)
        self.progressBar_sh_1.setInvertedAppearance(False)
        self.progressBar_sh_1.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout.addWidget(self.progressBar_sh_1)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout.addWidget(self.groupBox_sh_1, 4, 0, 1, 1)

        self.v_line_sh_3 = QFrame(self.groupBox_shelf)
        self.v_line_sh_3.setObjectName(u"v_line_sh_3")
        sizePolicy7.setHeightForWidth(self.v_line_sh_3.sizePolicy().hasHeightForWidth())
        self.v_line_sh_3.setSizePolicy(sizePolicy7)
        self.v_line_sh_3.setMinimumSize(QSize(0, 150))
        self.v_line_sh_3.setMaximumSize(QSize(3, 16777215))
        self.v_line_sh_3.setMouseTracking(True)
        self.v_line_sh_3.setLayoutDirection(Qt.LeftToRight)
        self.v_line_sh_3.setAutoFillBackground(False)
        self.v_line_sh_3.setStyleSheet(u"background-color: rgb(255, 0, 127);")
        self.v_line_sh_3.setFrameShadow(QFrame.Plain)
        self.v_line_sh_3.setLineWidth(3)
        self.v_line_sh_3.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.v_line_sh_3, 4, 1, 1, 1)

        self.v_line_sh_2 = QFrame(self.groupBox_shelf)
        self.v_line_sh_2.setObjectName(u"v_line_sh_2")
        sizePolicy7.setHeightForWidth(self.v_line_sh_2.sizePolicy().hasHeightForWidth())
        self.v_line_sh_2.setSizePolicy(sizePolicy7)
        self.v_line_sh_2.setMinimumSize(QSize(0, 150))
        self.v_line_sh_2.setMaximumSize(QSize(3, 16777215))
        self.v_line_sh_2.setMouseTracking(True)
        self.v_line_sh_2.setLayoutDirection(Qt.LeftToRight)
        self.v_line_sh_2.setAutoFillBackground(False)
        self.v_line_sh_2.setStyleSheet(u"background-color: rgb(255, 0, 127);")
        self.v_line_sh_2.setFrameShadow(QFrame.Plain)
        self.v_line_sh_2.setLineWidth(3)
        self.v_line_sh_2.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.v_line_sh_2, 2, 1, 1, 1)

        self.v_line_sh_5 = QFrame(self.groupBox_shelf)
        self.v_line_sh_5.setObjectName(u"v_line_sh_5")
        sizePolicy7.setHeightForWidth(self.v_line_sh_5.sizePolicy().hasHeightForWidth())
        self.v_line_sh_5.setSizePolicy(sizePolicy7)
        self.v_line_sh_5.setMinimumSize(QSize(0, 150))
        self.v_line_sh_5.setMaximumSize(QSize(3, 16777215))
        self.v_line_sh_5.setMouseTracking(True)
        self.v_line_sh_5.setLayoutDirection(Qt.LeftToRight)
        self.v_line_sh_5.setAutoFillBackground(False)
        self.v_line_sh_5.setStyleSheet(u"background-color: rgb(255, 0, 127);")
        self.v_line_sh_5.setFrameShadow(QFrame.Plain)
        self.v_line_sh_5.setLineWidth(3)
        self.v_line_sh_5.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.v_line_sh_5, 2, 3, 1, 1)

        self.v_line_sh_6 = QFrame(self.groupBox_shelf)
        self.v_line_sh_6.setObjectName(u"v_line_sh_6")
        sizePolicy7.setHeightForWidth(self.v_line_sh_6.sizePolicy().hasHeightForWidth())
        self.v_line_sh_6.setSizePolicy(sizePolicy7)
        self.v_line_sh_6.setMinimumSize(QSize(0, 150))
        self.v_line_sh_6.setMaximumSize(QSize(3, 16777215))
        self.v_line_sh_6.setMouseTracking(True)
        self.v_line_sh_6.setLayoutDirection(Qt.LeftToRight)
        self.v_line_sh_6.setAutoFillBackground(False)
        self.v_line_sh_6.setStyleSheet(u"background-color: rgb(255, 0, 127);")
        self.v_line_sh_6.setFrameShadow(QFrame.Plain)
        self.v_line_sh_6.setLineWidth(3)
        self.v_line_sh_6.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.v_line_sh_6, 0, 3, 1, 1)

        self.groupBox_sh_6 = QGroupBox(self.groupBox_shelf)
        self.groupBox_sh_6.setObjectName(u"groupBox_sh_6")
        self.groupBox_sh_6.setStyleSheet(u"border: 2px oultine rgb(95,95,95);")
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_sh_6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.shelf_no_label_sh_6 = QLabel(self.groupBox_sh_6)
        self.shelf_no_label_sh_6.setObjectName(u"shelf_no_label_sh_6")
        self.shelf_no_label_sh_6.setFont(font19)
        self.shelf_no_label_sh_6.setStyleSheet(u"border-color: rgb(83, 83, 83);\n"
"background-color: rgb(70, 70, 70);\n"
"color: rgb(255, 255, 255);")
        self.shelf_no_label_sh_6.setFrameShape(QFrame.Panel)
        self.shelf_no_label_sh_6.setFrameShadow(QFrame.Raised)
        self.shelf_no_label_sh_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.shelf_no_label_sh_6)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.qty_descr_label_sh_6 = QLabel(self.groupBox_sh_6)
        self.qty_descr_label_sh_6.setObjectName(u"qty_descr_label_sh_6")
        self.qty_descr_label_sh_6.setFont(font20)
        self.qty_descr_label_sh_6.setStyleSheet(u"border-color: rgb(130, 130, 130);\n"
"color: rgb(255, 255, 255);\n"
"padding: 5px;\n"
"")
        self.qty_descr_label_sh_6.setFrameShadow(QFrame.Sunken)
        self.qty_descr_label_sh_6.setLineWidth(0)

        self.horizontalLayout_13.addWidget(self.qty_descr_label_sh_6)

        self.qty_label_sh_6 = QLabel(self.groupBox_sh_6)
        self.qty_label_sh_6.setObjectName(u"qty_label_sh_6")
        self.qty_label_sh_6.setMinimumSize(QSize(0, 0))
        self.qty_label_sh_6.setFont(font21)
        self.qty_label_sh_6.setStyleSheet(u"border-bottom-style: solid;\n"
"border-bottom-color: rgb(66, 66, 66);\n"
"")
        self.qty_label_sh_6.setFrameShape(QFrame.Box)
        self.qty_label_sh_6.setFrameShadow(QFrame.Plain)
        self.qty_label_sh_6.setLineWidth(3)
        self.qty_label_sh_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.qty_label_sh_6.setIndent(-1)

        self.horizontalLayout_13.addWidget(self.qty_label_sh_6)


        self.verticalLayout_14.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.order_descr_label_sh_6 = QLabel(self.groupBox_sh_6)
        self.order_descr_label_sh_6.setObjectName(u"order_descr_label_sh_6")
        self.order_descr_label_sh_6.setFont(font20)
        self.order_descr_label_sh_6.setStyleSheet(u"border-color: rgb(130, 130, 130);\n"
"color: rgb(255, 255, 255);\n"
"padding: 5px;\n"
"")
        self.order_descr_label_sh_6.setFrameShadow(QFrame.Plain)
        self.order_descr_label_sh_6.setLineWidth(0)

        self.horizontalLayout_14.addWidget(self.order_descr_label_sh_6)

        self.order_label_sh_6 = QLabel(self.groupBox_sh_6)
        self.order_label_sh_6.setObjectName(u"order_label_sh_6")
        self.order_label_sh_6.setMinimumSize(QSize(0, 0))
        self.order_label_sh_6.setFont(font21)
        self.order_label_sh_6.setStyleSheet(u"border-bottom-style: solid;\n"
"border-bottom-color: rgb(66, 66, 66);\n"
"")
        self.order_label_sh_6.setFrameShadow(QFrame.Sunken)
        self.order_label_sh_6.setLineWidth(4)
        self.order_label_sh_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.order_label_sh_6.setIndent(2)

        self.horizontalLayout_14.addWidget(self.order_label_sh_6)

        self.horizontalLayout_14.setStretch(1, 1)

        self.verticalLayout_14.addLayout(self.horizontalLayout_14)

        self.progressBar_sh_6 = QProgressBar(self.groupBox_sh_6)
        self.progressBar_sh_6.setObjectName(u"progressBar_sh_6")
        self.progressBar_sh_6.setFont(font7)
        self.progressBar_sh_6.setAcceptDrops(False)
        self.progressBar_sh_6.setStyleSheet(u"border-color: rgb(130, 130, 130);\n"
"background-color: rgb(79, 79, 79);\n"
"color: rgb(255, 255, 255);")
        self.progressBar_sh_6.setValue(0)
        self.progressBar_sh_6.setAlignment(Qt.AlignCenter)
        self.progressBar_sh_6.setOrientation(Qt.Horizontal)
        self.progressBar_sh_6.setInvertedAppearance(False)
        self.progressBar_sh_6.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_14.addWidget(self.progressBar_sh_6)


        self.verticalLayout_13.addLayout(self.verticalLayout_14)


        self.gridLayout.addWidget(self.groupBox_sh_6, 2, 4, 1, 1)

        self.h_line_sh1 = QFrame(self.groupBox_shelf)
        self.h_line_sh1.setObjectName(u"h_line_sh1")
        self.h_line_sh1.setMaximumSize(QSize(16777215, 3))
        self.h_line_sh1.setStyleSheet(u"background-color: rgb(255, 0, 127);")
        self.h_line_sh1.setFrameShadow(QFrame.Plain)
        self.h_line_sh1.setLineWidth(1)
        self.h_line_sh1.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.h_line_sh1, 1, 0, 1, 5)

        self.groupBox_sh_4 = QGroupBox(self.groupBox_shelf)
        self.groupBox_sh_4.setObjectName(u"groupBox_sh_4")
        self.groupBox_sh_4.setStyleSheet(u"border: 2px oultine rgb(95,95,95);")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_sh_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.shelf_no_label_sh_4 = QLabel(self.groupBox_sh_4)
        self.shelf_no_label_sh_4.setObjectName(u"shelf_no_label_sh_4")
        self.shelf_no_label_sh_4.setFont(font19)
        self.shelf_no_label_sh_4.setStyleSheet(u"border-color: rgb(83, 83, 83);\n"
"background-color: rgb(70, 70, 70);\n"
"color: rgb(255, 255, 255);")
        self.shelf_no_label_sh_4.setFrameShape(QFrame.Panel)
        self.shelf_no_label_sh_4.setFrameShadow(QFrame.Raised)
        self.shelf_no_label_sh_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.shelf_no_label_sh_4)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.qty_descr_label_sh_4 = QLabel(self.groupBox_sh_4)
        self.qty_descr_label_sh_4.setObjectName(u"qty_descr_label_sh_4")
        self.qty_descr_label_sh_4.setFont(font20)
        self.qty_descr_label_sh_4.setStyleSheet(u"border-color: rgb(130, 130, 130);\n"
"color: rgb(255, 255, 255);\n"
"padding: 5px;\n"
"")
        self.qty_descr_label_sh_4.setFrameShadow(QFrame.Sunken)
        self.qty_descr_label_sh_4.setLineWidth(0)

        self.horizontalLayout_9.addWidget(self.qty_descr_label_sh_4)

        self.qty_label_sh_4 = QLabel(self.groupBox_sh_4)
        self.qty_label_sh_4.setObjectName(u"qty_label_sh_4")
        self.qty_label_sh_4.setMinimumSize(QSize(0, 0))
        self.qty_label_sh_4.setFont(font21)
        self.qty_label_sh_4.setStyleSheet(u"border-bottom-style: solid;\n"
"border-bottom-color: rgb(66, 66, 66);\n"
"")
        self.qty_label_sh_4.setFrameShape(QFrame.Box)
        self.qty_label_sh_4.setFrameShadow(QFrame.Plain)
        self.qty_label_sh_4.setLineWidth(3)
        self.qty_label_sh_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.qty_label_sh_4.setIndent(-1)

        self.horizontalLayout_9.addWidget(self.qty_label_sh_4)


        self.verticalLayout_10.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.order_descr_label_sh_4 = QLabel(self.groupBox_sh_4)
        self.order_descr_label_sh_4.setObjectName(u"order_descr_label_sh_4")
        self.order_descr_label_sh_4.setFont(font20)
        self.order_descr_label_sh_4.setStyleSheet(u"border-color: rgb(130, 130, 130);\n"
"color: rgb(255, 255, 255);\n"
"padding: 5px;\n"
"")
        self.order_descr_label_sh_4.setFrameShadow(QFrame.Plain)
        self.order_descr_label_sh_4.setLineWidth(0)

        self.horizontalLayout_10.addWidget(self.order_descr_label_sh_4)

        self.order_label_sh_4 = QLabel(self.groupBox_sh_4)
        self.order_label_sh_4.setObjectName(u"order_label_sh_4")
        self.order_label_sh_4.setMinimumSize(QSize(0, 0))
        self.order_label_sh_4.setFont(font21)
        self.order_label_sh_4.setStyleSheet(u"border-bottom-style: solid;\n"
"border-bottom-color: rgb(66, 66, 66);\n"
"")
        self.order_label_sh_4.setFrameShadow(QFrame.Sunken)
        self.order_label_sh_4.setLineWidth(4)
        self.order_label_sh_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.order_label_sh_4.setIndent(2)

        self.horizontalLayout_10.addWidget(self.order_label_sh_4)

        self.horizontalLayout_10.setStretch(1, 1)

        self.verticalLayout_10.addLayout(self.horizontalLayout_10)

        self.progressBar_sh_4 = QProgressBar(self.groupBox_sh_4)
        self.progressBar_sh_4.setObjectName(u"progressBar_sh_4")
        self.progressBar_sh_4.setFont(font7)
        self.progressBar_sh_4.setAcceptDrops(False)
        self.progressBar_sh_4.setStyleSheet(u"border-color: rgb(130, 130, 130);\n"
"background-color: rgb(79, 79, 79);\n"
"color: rgb(255, 255, 255);")
        self.progressBar_sh_4.setValue(0)
        self.progressBar_sh_4.setAlignment(Qt.AlignCenter)
        self.progressBar_sh_4.setOrientation(Qt.Horizontal)
        self.progressBar_sh_4.setInvertedAppearance(False)
        self.progressBar_sh_4.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_10.addWidget(self.progressBar_sh_4)


        self.verticalLayout_9.addLayout(self.verticalLayout_10)


        self.gridLayout.addWidget(self.groupBox_sh_4, 2, 0, 1, 1)


        self.verticalLayout_31.addWidget(self.groupBox_shelf)

        self.verticalLayout_31.setStretch(1, 1)
        self.splitter.addWidget(self.layoutWidget2)

        self.verticalLayout_32.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.mw_centralwidget)

        self.retranslateUi(MainWindow)
        self.barcode_scan_lineEdit.textChanged.connect(self.lopi_tableView.update)
        self.batch_br_tableView.clicked.connect(self.content_br_tableView.update)
        self.batch_br_tableView.clicked.connect(self.info_br_label.update)
        self.remove_batch_cb_pushButton.clicked.connect(self.locb_cb_tableView.update)
        self.remove_order_cb_pushButton.clicked.connect(self.dv_cb_tableView.update)
        self.cbfs_cb_pushButton.clicked.connect(self.locb_cb_tableView.clearSelection)
        self.remove_batch_cb_pushButton.clicked.connect(self.dv_cb_tableView.update)
        self.cbfs_cb_pushButton.clicked.connect(self.dv_cb_tableView.clearSelection)
        self.clear_order_status_cb_pushButton.clicked.connect(self.dv_cb_tableView.update)
        self.clear_item_status_cb_pushButton.clicked.connect(self.dv_cb_tableView.update)
        self.clear_batch_status_cb_pushButton.clicked.connect(self.dv_cb_tableView.update)
        self.remove_row_cb_pushButton.clicked.connect(self.dv_cb_tableView.update)
        self.remove_cart_cb_pushButton.clicked.connect(self.dv_cb_tableView.update)
        self.add_item_cb_pushButton.clicked.connect(self.dv_cb_tableView.update)
        self.locb_cb_tableView.clicked.connect(self.dv_cb_tableView.update)
        self.items_qty_pushButton.clicked.connect(self.dv_cb_tableView.update)
        self.add_item_cb_pushButton.clicked.connect(self.locb_cb_tableView.update)
        self.clear_status_br_pushButton.clicked.connect(self.content_br_tableView.update)

        self.batch_br_tabWidget.setCurrentIndex(0)
        self.register_br_pushButton.setDefault(False)
        self.start_pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.info_br_label.setText(QCoreApplication.translate("MainWindow", u"Choose Batch to register ", None))
        self.batch_no_br_descr_label.setText(QCoreApplication.translate("MainWindow", u"Batch no", None))
        self.batch_no_br_label.setText("")
        self.carts_quantity_descr_label.setText(QCoreApplication.translate("MainWindow", u"Carts quantity", None))
        self.carts_qty_br_label.setText("")
        self.orders_quantity_descr_label.setText(QCoreApplication.translate("MainWindow", u"Orders quantity", None))
        self.orders_qty_br_label.setText("")
        self.items_qantity_descr_label.setText(QCoreApplication.translate("MainWindow", u"Items quantity", None))
        self.items_qty_br_label.setText("")
        self.register_br_pushButton.setText(QCoreApplication.translate("MainWindow", u"REGISTER", None))
        self.batch_list_label.setText(QCoreApplication.translate("MainWindow", u"Available batches", None))
        self.loab_descr_label.setText(QCoreApplication.translate("MainWindow", u"  Content of the selected batch", None))
        self.clear_status_br_pushButton.setText(QCoreApplication.translate("MainWindow", u"Clear items status in  Batch", None))
        self.batch_br_tabWidget.setTabText(self.batch_br_tabWidget.indexOf(self.register_batch), QCoreApplication.translate("MainWindow", u"Batch register", None))
        self.bs_load_pushButton.setText(QCoreApplication.translate("MainWindow", u"Load\n"
"File", None))
        self.bs_present_pushButton.setText(QCoreApplication.translate("MainWindow", u"Present\n"
"Batch", None))
        self.bs_oq_avg_label.setText(QCoreApplication.translate("MainWindow", u"0h00m00s", None))
        self.bs_max_descr_label.setText(QCoreApplication.translate("MainWindow", u"MAXIMUM", None))
        self.bs_iq_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.bs_iq_descr_label.setText(QCoreApplication.translate("MainWindow", u"Items qty", None))
        self.bs_iq_min_label.setText(QCoreApplication.translate("MainWindow", u"0h00m00s", None))
        self.bs_batch_progress_label.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.bs_batch_no_label.setText(QCoreApplication.translate("MainWindow", u"Batch number", None))
        self.bs_batch_time_descr_label.setText(QCoreApplication.translate("MainWindow", u"Processing time", None))
        self.bs_batch_time_label.setText(QCoreApplication.translate("MainWindow", u"0h00m00s", None))
        self.bs_avg_descr_label.setText(QCoreApplication.translate("MainWindow", u"AVERAGE", None))
        self.bs_iq_max_label.setText(QCoreApplication.translate("MainWindow", u"0h00m00s", None))
        self.bs_ipo_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.bs_ipo_descr_label.setText(QCoreApplication.translate("MainWindow", u"Items pro order (average)", None))
        self.bs_time_descr_label.setText(QCoreApplication.translate("MainWindow", u"PROCESSING TIMES", None))
        self.bs_iq_avg_label.setText(QCoreApplication.translate("MainWindow", u"0h00m00s", None))
        self.bs_oq_min_label.setText(QCoreApplication.translate("MainWindow", u"0h00m00s", None))
        self.bs_ipc_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.bs_ipc_descr_label.setText(QCoreApplication.translate("MainWindow", u"Items pro cart (average)", None))
        self.bs_oq_max_label.setText(QCoreApplication.translate("MainWindow", u"0h00m00s", None))
        self.bs_oq_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.bs_oq_descr_label.setText(QCoreApplication.translate("MainWindow", u"Orders qty", None))
        self.bs_descr_label.setText(QCoreApplication.translate("MainWindow", u"Batch statistics from:", None))
        self.bs_cq_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.bs_cq_descr_label.setText(QCoreApplication.translate("MainWindow", u"Carts qty", None))
        self.bs_min_descr_label.setText(QCoreApplication.translate("MainWindow", u"MINIMUM", None))
        self.bs_filename_label.setText(QCoreApplication.translate("MainWindow", u"Present Batch", None))
        self.bs_delete_pushButton.setText(QCoreApplication.translate("MainWindow", u"Delete\n"
"File", None))
        self.bs_ll_pushButton.setText(QCoreApplication.translate("MainWindow", u"Last\n"
"loaded", None))
        self.batch_br_tabWidget.setTabText(self.batch_br_tabWidget.indexOf(self.batch_stats), QCoreApplication.translate("MainWindow", u"Batch statistics", None))
        self.pbo_descr_label.setText(QCoreApplication.translate("MainWindow", u"Present Batch operations", None))
        self.hboff_load_pushButton.setText(QCoreApplication.translate("MainWindow", u"Load\n"
"File", None))
        self.hboff_delete_pushButton.setText(QCoreApplication.translate("MainWindow", u"Delete\n"
"File", None))
        self.hboff_clear_pushButton.setText(QCoreApplication.translate("MainWindow", u"Clear\n"
"Window", None))
        self.hboff_filename_label.setText(QCoreApplication.translate("MainWindow", u"Filename...", None))
        self.hboff_descr_label.setText(QCoreApplication.translate("MainWindow", u"Historical Batch operations from:", None))
        self.batch_br_tabWidget.setTabText(self.batch_br_tabWidget.indexOf(self.history_bo), QCoreApplication.translate("MainWindow", u"History of Batch operations", None))
        self.batch_no_descr_label_2.setText(QCoreApplication.translate("MainWindow", u"Batch no.", None))
        self.batch_no_comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Batch no...", None))
        self.order_no_descr_label.setText(QCoreApplication.translate("MainWindow", u"Order no.", None))
        self.order_no_comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Order no....", None))
        self.item_barcode_descr_label.setText(QCoreApplication.translate("MainWindow", u"Item barcode", None))
        self.item_no_comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Item barcode...", None))
        self.cart_barcode_descr_label.setText(QCoreApplication.translate("MainWindow", u"Cart barcode", None))
        self.cart_barcode_comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cart barcode...", None))
        self.add_item_cb_pushButton.setText(QCoreApplication.translate("MainWindow", u"Add\n"
"Data", None))
        self.clear_batch_status_cb_pushButton.setText(QCoreApplication.translate("MainWindow", u"Clear Batch\n"
"Status", None))
        self.clear_order_status_cb_pushButton.setText(QCoreApplication.translate("MainWindow", u"Clear Order\n"
"Status", None))
        self.clear_item_status_cb_pushButton.setText(QCoreApplication.translate("MainWindow", u"Clear Item\n"
"Status", None))
        self.remove_batch_cb_pushButton.setText(QCoreApplication.translate("MainWindow", u"Remove\n"
"Batch", None))
        self.remove_order_cb_pushButton.setText(QCoreApplication.translate("MainWindow", u"Remove\n"
"Order", None))
        self.remove_cart_cb_pushButton.setText(QCoreApplication.translate("MainWindow", u"Remove\n"
"Cart", None))
        self.remove_row_cb_pushButton.setText(QCoreApplication.translate("MainWindow", u"Remove\n"
"Row", None))
        self.locb_descr_label_2.setText(QCoreApplication.translate("MainWindow", u"List of created batches", None))
        self.dv_descr_label.setText(QCoreApplication.translate("MainWindow", u"Database view", None))
        self.items_qty_pushButton.setText(QCoreApplication.translate("MainWindow", u"Items quantity", None))
        self.cbfs_cb_pushButton.setText(QCoreApplication.translate("MainWindow", u"Clear Batch selection filter", None))
        self.batch_br_tabWidget.setTabText(self.batch_br_tabWidget.indexOf(self.create_batch), QCoreApplication.translate("MainWindow", u"Create your own Batch - Batch Editor", None))
        self.info_panel_groupBox.setTitle("")
        self.lopi_descr_label.setText(QCoreApplication.translate("MainWindow", u"List of processed items", None))
        self.scanning_groupBox.setTitle("")
        self.start_pushButton.setText(QCoreApplication.translate("MainWindow", u"START\n"
"\n"
"SCANNING", None))
        self.barcode_scan_lineEdit.setText("")
        self.barcode_label.setText("")
        self.orders_left_descr_label.setText(QCoreApplication.translate("MainWindow", u"Orders left", None))
        self.items_left_descr_label.setText(QCoreApplication.translate("MainWindow", u"Items left", None))
        self.orders_left_label.setText("")
        self.items_left_label.setText("")
        self.title_batch_label.setText(QCoreApplication.translate("MainWindow", u"Put to Wall - Batch data", None))
        self.wall_progress_descr_label.setText(QCoreApplication.translate("MainWindow", u"Wall progress", None))
        self.batch_no_descr_label.setText(QCoreApplication.translate("MainWindow", u"Batch no.", None))
        self.batch_no_label.setText("")
        self.orders_qty_descr_label.setText(QCoreApplication.translate("MainWindow", u"Orders quantity", None))
        self.orders_qty_label.setText("")
        self.carts_qty_descr_label.setText(QCoreApplication.translate("MainWindow", u"Carts quantity", None))
        self.carts_qty_label.setText("")
        self.message_descr_label.setText(QCoreApplication.translate("MainWindow", u"Information\n"
"panel ", None))
        self.groupBox_shelf.setTitle("")
        self.groupBox_sh_8.setTitle("")
        self.shelf_no_label_sh_8.setText(QCoreApplication.translate("MainWindow", u"Shelf 8", None))
        self.qty_descr_label_sh_8.setText(QCoreApplication.translate("MainWindow", u"Quantity", None))
        self.qty_label_sh_8.setText("")
        self.order_descr_label_sh_8.setText(QCoreApplication.translate("MainWindow", u"Order no.", None))
        self.order_label_sh_8.setText("")
        self.groupBox_sh_3.setTitle("")
        self.shelf_no_label_sh_3.setText(QCoreApplication.translate("MainWindow", u"Shelf 3", None))
        self.qty_descr_label_sh_3.setText(QCoreApplication.translate("MainWindow", u"Quantity", None))
        self.qty_label_sh_3.setText("")
        self.order_descr_label_sh_3.setText(QCoreApplication.translate("MainWindow", u"Order no.", None))
        self.order_label_sh_3.setText("")
        self.groupBox_sh_7.setTitle("")
        self.shelf_no_label_sh_7.setText(QCoreApplication.translate("MainWindow", u"Shelf 7", None))
        self.qty_descr_label_sh_7.setText(QCoreApplication.translate("MainWindow", u"Quantity", None))
        self.qty_label_sh_7.setText("")
        self.order_descr_label_sh_7.setText(QCoreApplication.translate("MainWindow", u"Order no.", None))
        self.order_label_sh_7.setText("")
        self.groupBox_sh_9.setTitle("")
        self.shelf_no_label_sh_9.setText(QCoreApplication.translate("MainWindow", u"Shelf 9", None))
        self.qty_descr_label_sh_9.setText(QCoreApplication.translate("MainWindow", u"Quantity", None))
        self.qty_label_sh_9.setText("")
        self.order_descr_label_sh_9.setText(QCoreApplication.translate("MainWindow", u"Order no.", None))
        self.order_label_sh_9.setText("")
        self.groupBox_sh_2.setTitle("")
        self.shelf_no_label_sh_2.setText(QCoreApplication.translate("MainWindow", u"Shelf 2", None))
        self.qty_descr_label_sh_2.setText(QCoreApplication.translate("MainWindow", u"Quantity", None))
        self.qty_label_sh_2.setText("")
        self.order_descr_label_sh_2.setText(QCoreApplication.translate("MainWindow", u"Order no.", None))
        self.order_label_sh_2.setText("")
        self.groupBox_sh_5.setTitle("")
        self.shelf_no_label_sh_5.setText(QCoreApplication.translate("MainWindow", u"Shelf 5", None))
        self.qty_descr_label_sh_5.setText(QCoreApplication.translate("MainWindow", u"Quantity", None))
        self.qty_label_sh_5.setText("")
        self.order_descr_label_sh_5.setText(QCoreApplication.translate("MainWindow", u"Order no.", None))
        self.order_label_sh_5.setText("")
        self.groupBox_sh_1.setTitle("")
        self.shelf_no_label_sh_1.setText(QCoreApplication.translate("MainWindow", u"Shelf 1", None))
        self.qty_descr_label_sh_1.setText(QCoreApplication.translate("MainWindow", u"Quantity", None))
        self.qty_label_sh_1.setText("")
        self.order_descr_label_sh_1.setText(QCoreApplication.translate("MainWindow", u"Order no.", None))
        self.order_label_sh_1.setText("")
        self.groupBox_sh_6.setTitle("")
        self.shelf_no_label_sh_6.setText(QCoreApplication.translate("MainWindow", u"Shelf 6", None))
        self.qty_descr_label_sh_6.setText(QCoreApplication.translate("MainWindow", u"Quantity", None))
        self.qty_label_sh_6.setText("")
        self.order_descr_label_sh_6.setText(QCoreApplication.translate("MainWindow", u"Order no.", None))
        self.order_label_sh_6.setText("")
        self.groupBox_sh_4.setTitle("")
        self.shelf_no_label_sh_4.setText(QCoreApplication.translate("MainWindow", u"Shelf 4", None))
        self.qty_descr_label_sh_4.setText(QCoreApplication.translate("MainWindow", u"Quantity", None))
        self.qty_label_sh_4.setText("")
        self.order_descr_label_sh_4.setText(QCoreApplication.translate("MainWindow", u"Order no.", None))
        self.order_label_sh_4.setText("")
    # retranslateUi

