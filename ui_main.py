# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QMainWindow, QScrollArea, QSizePolicy, QStackedWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(939, 682)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush1 = QBrush(QColor(186, 191, 200, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        MainWindow.setPalette(palette)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.drop_shadow_layout = QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        sizePolicy1.setHeightForWidth(self.drop_shadow_frame.sizePolicy().hasHeightForWidth())
        self.drop_shadow_frame.setSizePolicy(sizePolicy1)
        self.drop_shadow_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(42, 44, 111, 255), stop:0.521825 rgba(28, 29, 73, 255));\n"
"border-radius: 10px;")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.drop_shadow_frame)
        self.title_bar.setObjectName(u"title_bar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.title_bar.sizePolicy().hasHeightForWidth())
        self.title_bar.setSizePolicy(sizePolicy2)
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        self.title_bar.setStyleSheet(u"background-color: none")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(14)
        self.frame_title.setFont(font)
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_title)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Light"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.label_title.setFont(font1)
        self.label_title.setLayoutDirection(Qt.LeftToRight)
        self.label_title.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_title)


        self.horizontalLayout.addWidget(self.frame_title)


        self.verticalLayout.addWidget(self.title_bar)

        self.content_bar = QFrame(self.drop_shadow_frame)
        self.content_bar.setObjectName(u"content_bar")
        self.content_bar.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.content_bar.sizePolicy().hasHeightForWidth())
        self.content_bar.setSizePolicy(sizePolicy1)
        self.content_bar.setLayoutDirection(Qt.RightToLeft)
        self.content_bar.setStyleSheet(u"background-color: none")
        self.content_bar.setFrameShape(QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.content_bar)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 9, 0)
        self.stackedWidget = QStackedWidget(self.content_bar)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(20)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setPointSize(10)
        self.stackedWidget.setFont(font2)
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.horizontalLayout_9 = QHBoxLayout(self.page_home)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.label = QLabel(self.page_home)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(9)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.label)

        self.line_4 = QFrame(self.page_home)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setAutoFillBackground(False)
        self.line_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_4.setLineWidth(0)
        self.line_4.setMidLineWidth(1)
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.scrollArea = QScrollArea(self.page_home)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 419, 363))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.scrollAreaWidgetContents.setStyleSheet(u"background-color: rgb(42, 47, 108);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Gemini_Text = QTextEdit(self.scrollAreaWidgetContents)
        self.Gemini_Text.setObjectName(u"Gemini_Text")
        self.Gemini_Text.setMinimumSize(QSize(0, 0))
        font4 = QFont()
        font4.setFamilies([u"MS Shell Dlg 2"])
        font4.setPointSize(8)
        font4.setBold(False)
        font4.setItalic(False)
        self.Gemini_Text.setFont(font4)
        self.Gemini_Text.setStyleSheet(u"background-color: rgb(42, 47, 108);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.Gemini_Text.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.Gemini_Text.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.Gemini_Text.setLineWrapMode(QTextEdit.WidgetWidth)
        self.Gemini_Text.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout_4.addWidget(self.Gemini_Text)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.verticalLayout_5.setStretch(0, 2)
        self.verticalLayout_5.setStretch(3, 4)

        self.horizontalLayout_9.addLayout(self.verticalLayout_5)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_7 = QLabel(self.page_home)
        self.label_7.setObjectName(u"label_7")
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(False)
        font5.setUnderline(False)
        self.label_7.setFont(font5)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_12.addWidget(self.label_7)

        self.line_2 = QFrame(self.page_home)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setAutoFillBackground(False)
        self.line_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_2.setLineWidth(0)
        self.line_2.setMidLineWidth(1)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.line_2)

        self.tableWidget_4 = QTableWidget(self.page_home)
        if (self.tableWidget_4.columnCount() < 6):
            self.tableWidget_4.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget_4.rowCount() < 4):
            self.tableWidget_4.setRowCount(4)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(0, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(0, 1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(0, 2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(1, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(1, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(1, 2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(2, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(2, 1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(2, 2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(3, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(3, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(3, 2, __qtablewidgetitem18)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        font6 = QFont()
        font6.setFamilies([u"MS Shell Dlg 2"])
        font6.setPointSize(10)
        font6.setBold(False)
        font6.setItalic(False)
        self.tableWidget_4.setFont(font6)
        self.tableWidget_4.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget_4.setStyleSheet(u"background-color: rgb(42, 47, 108);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.tableWidget_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_4.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_4.setTabKeyNavigation(False)
        self.tableWidget_4.setProperty("showDropIndicator", False)
        self.tableWidget_4.setDragDropOverwriteMode(False)
        self.tableWidget_4.setShowGrid(False)
        self.tableWidget_4.setGridStyle(Qt.SolidLine)
        self.tableWidget_4.setWordWrap(False)
        self.tableWidget_4.setColumnCount(6)
        self.tableWidget_4.horizontalHeader().setVisible(True)
        self.tableWidget_4.horizontalHeader().setHighlightSections(False)
        self.tableWidget_4.verticalHeader().setVisible(True)
        self.tableWidget_4.verticalHeader().setHighlightSections(False)

        self.verticalLayout_12.addWidget(self.tableWidget_4)


        self.verticalLayout_13.addLayout(self.verticalLayout_12)

        self.label_8 = QLabel(self.page_home)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font5)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_13.addWidget(self.label_8)

        self.line_3 = QFrame(self.page_home)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setAutoFillBackground(False)
        self.line_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_3.setLineWidth(0)
        self.line_3.setMidLineWidth(1)
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_13.addWidget(self.line_3)

        self.tableWidget_5 = QTableWidget(self.page_home)
        if (self.tableWidget_5.columnCount() < 6):
            self.tableWidget_5.setColumnCount(6)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt. AlignCenter);
        self.tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_5.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        if (self.tableWidget_5.rowCount() < 7):
            self.tableWidget_5.setRowCount(7)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(3, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(4, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(5, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(6, __qtablewidgetitem28)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        self.tableWidget_5.setFont(font6)
        self.tableWidget_5.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget_5.setStyleSheet(u"background-color: rgb(42, 47, 108);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.tableWidget_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_5.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_5.setTabKeyNavigation(False)
        self.tableWidget_5.setProperty("showDropIndicator", False)
        self.tableWidget_5.setDragDropOverwriteMode(False)
        self.tableWidget_5.setShowGrid(False)
        self.tableWidget_5.setGridStyle(Qt.SolidLine)
        self.tableWidget_5.setWordWrap(False)
        self.tableWidget_5.setColumnCount(6)
        self.tableWidget_5.horizontalHeader().setVisible(True)
        self.tableWidget_5.horizontalHeader().setHighlightSections(False)
        self.tableWidget_5.verticalHeader().setVisible(True)
        self.tableWidget_5.verticalHeader().setHighlightSections(False)

        self.verticalLayout_13.addWidget(self.tableWidget_5)


        self.horizontalLayout_9.addLayout(self.verticalLayout_13)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_3 = QLabel(self.page_home)
        self.label_3.setObjectName(u"label_3")
        font7 = QFont()
        font7.setPointSize(11)
        self.label_3.setFont(font7)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_3)

        self.tableWidget_2 = QTableWidget(self.page_home)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem30)
        if (self.tableWidget_2.rowCount() < 10):
            self.tableWidget_2.setRowCount(10)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, __qtablewidgetitem40)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setFont(font6)
        self.tableWidget_2.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget_2.setStyleSheet(u"background-color: rgb(42, 47, 108);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.tableWidget_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setTabKeyNavigation(False)
        self.tableWidget_2.setProperty("showDropIndicator", False)
        self.tableWidget_2.setDragDropOverwriteMode(False)
        self.tableWidget_2.setShowGrid(False)
        self.tableWidget_2.setWordWrap(False)
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setHighlightSections(False)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setHighlightSections(False)

        self.verticalLayout_10.addWidget(self.tableWidget_2)


        self.horizontalLayout_8.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_4 = QLabel(self.page_home)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font7)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_4)

        self.tableWidget_3 = QTableWidget(self.page_home)
        if (self.tableWidget_3.columnCount() < 2):
            self.tableWidget_3.setColumnCount(2)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem42)
        if (self.tableWidget_3.rowCount() < 10):
            self.tableWidget_3.setRowCount(10)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(4, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(5, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(6, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(7, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(8, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(9, __qtablewidgetitem52)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setFont(font6)
        self.tableWidget_3.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget_3.setStyleSheet(u"background-color: rgb(42, 47, 108);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.tableWidget_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_3.setTabKeyNavigation(False)
        self.tableWidget_3.setProperty("showDropIndicator", False)
        self.tableWidget_3.setDragDropOverwriteMode(False)
        self.tableWidget_3.setShowGrid(False)
        self.tableWidget_3.setWordWrap(False)
        self.tableWidget_3.horizontalHeader().setVisible(False)
        self.tableWidget_3.horizontalHeader().setHighlightSections(False)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_3.verticalHeader().setHighlightSections(False)

        self.verticalLayout_11.addWidget(self.tableWidget_3)


        self.horizontalLayout_8.addLayout(self.verticalLayout_11)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_2 = QLabel(self.page_home)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font7)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.label_2)

        self.tableWidget = QTableWidget(self.page_home)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem54)
        if (self.tableWidget.rowCount() < 10):
            self.tableWidget.setRowCount(10)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem64)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFont(font6)
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setStyleSheet(u"background-color: rgb(42, 47, 108);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setAutoScroll(False)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)

        self.verticalLayout_8.addWidget(self.tableWidget)


        self.horizontalLayout_8.addLayout(self.verticalLayout_8)


        self.verticalLayout_9.addLayout(self.horizontalLayout_8)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_5 = QLabel(self.page_home)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_16.addWidget(self.label_5)

        self.line = QFrame(self.page_home)
        self.line.setObjectName(u"line")
        self.line.setAutoFillBackground(False)
        self.line.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line.setLineWidth(0)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_16.addWidget(self.line)

        self.label_6 = QLabel(self.page_home)
        self.label_6.setObjectName(u"label_6")
        font8 = QFont()
        font8.setPointSize(8)
        font8.setBold(True)
        font8.setUnderline(False)
        self.label_6.setFont(font8)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_16.addWidget(self.label_6)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.widget_m_time = QWidget(self.page_home)
        self.widget_m_time.setObjectName(u"widget_m_time")
        self.widget_m_time.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.widget_m_time.sizePolicy().hasHeightForWidth())
        self.widget_m_time.setSizePolicy(sizePolicy1)
        self.widget_m_time.setLayoutDirection(Qt.RightToLeft)
        self.widget_m_time.setStyleSheet(u"background-color: rgb(42, 47, 108)")

        self.verticalLayout_15.addWidget(self.widget_m_time)


        self.verticalLayout_16.addLayout(self.verticalLayout_15)


        self.verticalLayout_9.addLayout(self.verticalLayout_16)

        self.verticalLayout_9.setStretch(0, 14)
        self.verticalLayout_9.setStretch(1, 11)

        self.horizontalLayout_9.addLayout(self.verticalLayout_9)

        self.horizontalLayout_9.setStretch(0, 9)
        self.horizontalLayout_9.setStretch(1, 4)
        self.horizontalLayout_9.setStretch(2, 4)
        self.stackedWidget.addWidget(self.page_home)
        self.page_credits = QWidget()
        self.page_credits.setObjectName(u"page_credits")
        self.stackedWidget.addWidget(self.page_credits)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.content_bar)


        self.drop_shadow_layout.addWidget(self.drop_shadow_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"Whatsapp Analytics", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"LLM Insights (Gemini)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Message Analysis", None))
        ___qtablewidgetitem = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem1 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem2 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem3 = self.tableWidget_4.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Messages:", None));
        ___qtablewidgetitem4 = self.tableWidget_4.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Words", None));
        ___qtablewidgetitem5 = self.tableWidget_4.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Unique Words:", None));
        ___qtablewidgetitem6 = self.tableWidget_4.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Characters:", None));

        __sortingEnabled = self.tableWidget_4.isSortingEnabled()
        self.tableWidget_4.setSortingEnabled(False)
        self.tableWidget_4.setSortingEnabled(__sortingEnabled)

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Conversation Analysis", None))
        ___qtablewidgetitem7 = self.tableWidget_5.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem8 = self.tableWidget_5.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem9 = self.tableWidget_5.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem10 = self.tableWidget_5.verticalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Started:", None));
        ___qtablewidgetitem11 = self.tableWidget_5.verticalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Ended:", None));
        ___qtablewidgetitem12 = self.tableWidget_5.verticalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Double Reach:", None));
        ___qtablewidgetitem13 = self.tableWidget_5.verticalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Resp <1min (%):", None));
        ___qtablewidgetitem14 = self.tableWidget_5.verticalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Questions:", None));
        ___qtablewidgetitem15 = self.tableWidget_5.verticalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Apologies:", None));
        ___qtablewidgetitem16 = self.tableWidget_5.verticalHeaderItem(6)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Encouregement", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"XXX", None))
        ___qtablewidgetitem17 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Emoji", None));
        ___qtablewidgetitem18 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Count", None));
        ___qtablewidgetitem19 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem20 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem21 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem22 = self.tableWidget_2.verticalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem23 = self.tableWidget_2.verticalHeaderItem(4)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem24 = self.tableWidget_2.verticalHeaderItem(5)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem25 = self.tableWidget_2.verticalHeaderItem(6)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem26 = self.tableWidget_2.verticalHeaderItem(7)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem27 = self.tableWidget_2.verticalHeaderItem(8)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem28 = self.tableWidget_2.verticalHeaderItem(9)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"XXX", None))
        ___qtablewidgetitem29 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Emoji", None));
        ___qtablewidgetitem30 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Count", None));
        ___qtablewidgetitem31 = self.tableWidget_3.verticalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem32 = self.tableWidget_3.verticalHeaderItem(1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem33 = self.tableWidget_3.verticalHeaderItem(2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem34 = self.tableWidget_3.verticalHeaderItem(3)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem35 = self.tableWidget_3.verticalHeaderItem(4)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem36 = self.tableWidget_3.verticalHeaderItem(5)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem37 = self.tableWidget_3.verticalHeaderItem(6)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem38 = self.tableWidget_3.verticalHeaderItem(7)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem39 = self.tableWidget_3.verticalHeaderItem(8)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem40 = self.tableWidget_3.verticalHeaderItem(9)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Top 10 Emojis:", None))
        ___qtablewidgetitem41 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Emoji", None));
        ___qtablewidgetitem42 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Count", None));
        ___qtablewidgetitem43 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem44 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem45 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem46 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem47 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem48 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem49 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem50 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem51 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem52 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Messaging Times", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"The majority of conversations was hapening:", None))
    # retranslateUi

