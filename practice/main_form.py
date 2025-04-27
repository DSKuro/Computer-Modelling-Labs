# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
                               QPushButton, QSizePolicy, QStatusBar, QTabWidget,
                               QTextEdit, QVBoxLayout, QWidget, QDialog, QDialogButtonBox)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

from classes.task1 import process_first_func, refresh_plots
from practice.classes.Function import Function
from practice.classes.task1 import process_second_func
from practice.classes.task2 import process_all, refresh_plots2

from classes.task3 import process_first_func as task3_first, refresh_plots3
from classes.task3 import process_second_func as task3_second

import classes.task4


class AlertBox(QDialog):
    def __init__(self, error):
        super().__init__()
        self.setWindowTitle("Ошибка!")

        q_btn = QDialogButtonBox.StandardButton.Ok
        self.button_box = QDialogButtonBox(q_btn)
        self.button_box.accepted.connect(self.accept)

        layout = QVBoxLayout()
        message = QLabel(error)
        layout.addWidget(message)
        layout.addWidget(self.button_box)
        self.setLayout(layout)

class Ui_Form(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(953, 667)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 951, 611))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(300, 10, 161, 41))
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 311, 41))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 320, 301, 41))
        self.label_3.setFont(font)
        self.txtStart1 = QTextEdit(self.tab)
        self.txtStart1.setObjectName(u"txtStart1")
        self.txtStart1.setGeometry(QRect(20, 120, 281, 31))
        self.txtEnd1 = QTextEdit(self.tab)
        self.txtEnd1.setObjectName(u"txtEnd1")
        self.txtEnd1.setGeometry(QRect(20, 160, 281, 31))
        self.txtH = QTextEdit(self.tab)
        self.txtH.setObjectName(u"txtH")
        self.txtH.setGeometry(QRect(20, 200, 281, 31))
        self.txtInit = QTextEdit(self.tab)
        self.txtInit.setObjectName(u"txtInit")
        self.txtInit.setGeometry(QRect(20, 240, 281, 31))
        self.txtH2 = QTextEdit(self.tab)
        self.txtH2.setObjectName(u"txtH2")
        self.txtH2.setGeometry(QRect(20, 450, 281, 31))
        self.txtStart2 = QTextEdit(self.tab)
        self.txtStart2.setObjectName(u"txtStart2")
        self.txtStart2.setGeometry(QRect(20, 370, 281, 31))
        self.txtInit2 = QTextEdit(self.tab)
        self.txtInit2.setObjectName(u"txtInit2")
        self.txtInit2.setGeometry(QRect(20, 490, 281, 31))
        self.txtEnd2 = QTextEdit(self.tab)
        self.txtEnd2.setObjectName(u"txtEnd2")
        self.txtEnd2.setGeometry(QRect(20, 410, 281, 31))
        self.verticalLayoutWidget = QWidget(self.tab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(340, 60, 571, 511))
        self.vl1 = QVBoxLayout(self.verticalLayoutWidget)
        self.vl1.setObjectName(u"vl1")
        self.vl1.setContentsMargins(0, 0, 0, 0)
        self.btnRun1 = QPushButton(self.tab)
        self.btnRun1.setObjectName(u"btnRun1")
        self.btnRun1.setGeometry(QRect(70, 283, 161, 31))
        self.btnRun2 = QPushButton(self.tab)
        self.btnRun2.setObjectName(u"btnRun2")
        self.btnRun2.setGeometry(QRect(80, 540, 161, 31))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 60, 311, 41))
        self.label_4.setFont(font)
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(340, 10, 231, 41))
        self.label_5.setFont(font)
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 100, 311, 41))
        self.label_6.setFont(font)
        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 140, 311, 41))
        self.label_7.setFont(font)
        self.txtH_3 = QTextEdit(self.tab_2)
        self.txtH_3.setObjectName(u"txtH_3")
        self.txtH_3.setGeometry(QRect(30, 260, 281, 31))
        self.txtStart3 = QTextEdit(self.tab_2)
        self.txtStart3.setObjectName(u"txtStart3")
        self.txtStart3.setGeometry(QRect(30, 180, 281, 31))
        self.txtA = QTextEdit(self.tab_2)
        self.txtA.setObjectName(u"txtA")
        self.txtA.setGeometry(QRect(30, 340, 281, 31))
        self.txtC = QTextEdit(self.tab_2)
        self.txtC.setObjectName(u"txtC")
        self.txtC.setGeometry(QRect(30, 420, 281, 31))
        self.txtInit_3 = QTextEdit(self.tab_2)
        self.txtInit_3.setObjectName(u"txtInit_3")
        self.txtInit_3.setGeometry(QRect(30, 300, 281, 31))
        self.txtEnd3 = QTextEdit(self.tab_2)
        self.txtEnd3.setObjectName(u"txtEnd3")
        self.txtEnd3.setGeometry(QRect(30, 220, 281, 31))
        self.txtB = QTextEdit(self.tab_2)
        self.txtB.setObjectName(u"txtB")
        self.txtB.setGeometry(QRect(30, 380, 281, 31))
        self.btnRun3 = QPushButton(self.tab_2)
        self.btnRun3.setObjectName(u"btnRun3")
        self.btnRun3.setGeometry(QRect(80, 470, 161, 31))
        self.verticalLayoutWidget_2 = QWidget(self.tab_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(330, 60, 581, 511))
        self.vl1_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.vl1_2.setObjectName(u"vl1_2")
        self.vl1_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.btnRun1_2 = QPushButton(self.tab_3)
        self.btnRun1_2.setObjectName(u"btnRun1_2")
        self.btnRun1_2.setGeometry(QRect(60, 273, 161, 31))
        self.txtH_4 = QTextEdit(self.tab_3)
        self.txtH_4.setObjectName(u"txtH_4")
        self.txtH_4.setGeometry(QRect(10, 190, 281, 31))
        self.txtStart1_4 = QTextEdit(self.tab_3)
        self.txtStart1_4.setObjectName(u"txtStart1_4")
        self.txtStart1_4.setGeometry(QRect(10, 110, 281, 31))
        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 50, 321, 41))
        self.label_8.setFont(font)
        self.txtStart2_4 = QTextEdit(self.tab_3)
        self.txtStart2_4.setObjectName(u"txtStart2_4")
        self.txtStart2_4.setGeometry(QRect(10, 360, 281, 31))
        self.txtInit2_4 = QTextEdit(self.tab_3)
        self.txtInit2_4.setObjectName(u"txtInit2_4")
        self.txtInit2_4.setGeometry(QRect(10, 480, 281, 31))
        self.txtH2_4 = QTextEdit(self.tab_3)
        self.txtH2_4.setObjectName(u"txtH2_4")
        self.txtH2_4.setGeometry(QRect(10, 440, 281, 31))
        self.txtInit_4 = QTextEdit(self.tab_3)
        self.txtInit_4.setObjectName(u"txtInit_4")
        self.txtInit_4.setGeometry(QRect(10, 230, 281, 31))
        self.verticalLayoutWidget_3 = QWidget(self.tab_3)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(310, 50, 601, 511))
        self.vl1_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.vl1_3.setObjectName(u"vl1_3")
        self.vl1_3.setContentsMargins(0, 0, 0, 0)
        self.btnRun2_2 = QPushButton(self.tab_3)
        self.btnRun2_2.setObjectName(u"btnRun2_2")
        self.btnRun2_2.setGeometry(QRect(70, 530, 161, 31))
        self.label_9 = QLabel(self.tab_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(290, 0, 161, 41))
        self.label_9.setFont(font)
        self.txtEnd1_4 = QTextEdit(self.tab_3)
        self.txtEnd1_4.setObjectName(u"txtEnd1_4")
        self.txtEnd1_4.setGeometry(QRect(10, 150, 281, 31))
        self.txtEnd2_4 = QTextEdit(self.tab_3)
        self.txtEnd2_4.setObjectName(u"txtEnd2_4")
        self.txtEnd2_4.setGeometry(QRect(10, 400, 281, 31))
        self.label_10 = QLabel(self.tab_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 310, 271, 41))
        self.label_10.setFont(font)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.label_11 = QLabel(self.tab_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(310, 10, 231, 41))
        self.label_11.setFont(font)
        self.txtEnd1_5 = QTextEdit(self.tab_4)
        self.txtEnd1_5.setObjectName(u"txtEnd1_5")
        self.txtEnd1_5.setGeometry(QRect(10, 200, 211, 31))
        self.txtStart1_5 = QTextEdit(self.tab_4)
        self.txtStart1_5.setObjectName(u"txtStart1_5")
        self.txtStart1_5.setGeometry(QRect(10, 160, 211, 31))
        self.txtb2 = QTextEdit(self.tab_4)
        self.txtb2.setObjectName(u"txtb2")
        self.txtb2.setGeometry(QRect(10, 440, 211, 31))
        self.txtH_5 = QTextEdit(self.tab_4)
        self.txtH_5.setObjectName(u"txtH_5")
        self.txtH_5.setGeometry(QRect(10, 240, 211, 31))
        self.txtl2 = QTextEdit(self.tab_4)
        self.txtl2.setObjectName(u"txtl2")
        self.txtl2.setGeometry(QRect(10, 400, 211, 31))
        self.txtInit_5 = QTextEdit(self.tab_4)
        self.txtInit_5.setObjectName(u"txtInit_5")
        self.txtInit_5.setGeometry(QRect(10, 280, 211, 31))
        self.txtl1 = QTextEdit(self.tab_4)
        self.txtl1.setObjectName(u"txtl1")
        self.txtl1.setGeometry(QRect(10, 360, 211, 31))
        self.txtr1 = QTextEdit(self.tab_4)
        self.txtr1.setObjectName(u"txtr1")
        self.txtr1.setGeometry(QRect(10, 320, 211, 31))
        self.txtg1 = QTextEdit(self.tab_4)
        self.txtg1.setObjectName(u"txtg1")
        self.txtg1.setGeometry(QRect(10, 480, 211, 31))
        self.btnRun1_3 = QPushButton(self.tab_4)
        self.btnRun1_3.setObjectName(u"btnRun1_3")
        self.btnRun1_3.setGeometry(QRect(50, 530, 161, 31))
        self.label_14 = QLabel(self.tab_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 70, 151, 21))
        self.btnOpen = QPushButton(self.tab_4)
        self.btnOpen.setObjectName(u"btnOpen")
        self.btnOpen.setGeometry(QRect(40, 30, 121, 24))
        font1 = QFont()
        font1.setPointSize(14)
        self.label_14.setFont(font1)
        self.label_13 = QLabel(self.tab_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 90, 211, 31))
        self.label_13.setFont(font1)
        self.label_12 = QLabel(self.tab_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 120, 231, 31))
        self.label_12.setFont(font1)
        self.verticalLayoutWidget_4 = QWidget(self.tab_4)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(240, 60, 691, 511))
        self.vl1_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.vl1_4.setObjectName(u"vl1_4")
        self.vl1_4.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 953, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.btnRun1.clicked.connect(self.btnRun1_click)
        self.btnRun2.clicked.connect(self.btnRun2_click)
        self.btnRun3.clicked.connect(self.btnRun3_click)
        self.btnRun1_2.clicked.connect(self.btnRun4_click)
        self.btnRun2_2.clicked.connect(self.btnRun5_click)
        self.btnRun1_3.clicked.connect(self.btnRun6_click)
        self.btnOpen.clicked.connect(self.btnOpen_click)

        self.retranslateUi(MainWindow)

        self.pl1 = plt.figure()
        self.cs1 = FigureCanvas(self.pl1)
        self.vl1.addWidget(self.cs1)

        self.i = 0
        self.pl2 = plt.figure()
        self.cs2 = FigureCanvas(self.pl2)
        self.vl1_2.addWidget(self.cs2)

        self.pl3 = plt.figure()
        self.cs3 = FigureCanvas(self.pl3)
        self.vl1_3.addWidget(self.cs3)

        self.pl4 = plt.figure()
        self.cs4 = FigureCanvas(self.pl4)
        self.vl1_4.addWidget(self.cs4)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0438 \u041a\u043e\u0448\u0438", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"y' = y^2 - yt, y(0) = 0, [0,1]", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"y' = y ^ 2 + 1, y(0) = 0, [0, 1]", None))
        self.txtStart1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.txtEnd1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0435\u0447\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.txtH.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0433", None))
        self.txtInit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0445\u043e\u0434\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.txtH2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0433", None))
        self.txtStart2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.txtInit2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0445\u043e\u0434\u043d\u044b\u0435\u0414\u0430\u043d\u043d\u044b\u0435", None))
        self.txtEnd2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0435\u0447\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.btnRun1.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
        self.btnRun2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0430 1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"y'1 = -y2 - y3", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u0441\u0442\u0435\u043c\u0430 \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0439", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"y'2 = y1 + ay2", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"y'3 = b + y3(y1 - c)", None))
        self.txtH_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0433", None))
        self.txtStart3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.txtA.setPlaceholderText(QCoreApplication.translate("MainWindow", u"a", None))
        self.txtC.setPlaceholderText(QCoreApplication.translate("MainWindow", u"c", None))
        self.txtInit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0445\u043e\u0434\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.txtEnd3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0435\u0447\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.txtB.setPlaceholderText(QCoreApplication.translate("MainWindow", u"b", None))
        self.btnRun3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0430 2", None))
        self.btnRun1_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
        self.txtH_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0433", None))
        self.txtStart1_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"y'' + 2y' + 3y = cos(t)", None))
        self.txtStart2_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.txtInit2_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0445\u043e\u0434\u043d\u044b\u0435\u0414\u0430\u043d\u043d\u044b\u0435", None))
        self.txtH2_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0433", None))
        self.txtInit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0445\u043e\u0434\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.btnRun2_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0442\u043e\u0440\u043e\u0433\u043e \u043f\u043e\u0440\u044f\u0434\u043a\u0430", None))
        self.txtEnd1_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0435\u0447\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.txtEnd2_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0435\u0447\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"z'' - a(1-z^2)z' + z = 0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0430 3", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u0441\u0442\u0435\u043c\u0430 \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0439", None))
        self.txtEnd1_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0435\u0447\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.txtStart1_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.txtb2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"b2", None))
        self.txtH_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0433", None))
        self.txtl2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"l2", None))
        self.txtInit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0445\u043e\u0434\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.txtl1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"l1", None))
        self.txtr1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"r1", None))
        self.txtg1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"g1", None))
        self.btnRun1_3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"dx/dt = r1x - l1xy", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"dy/dt = l2xy - b2y", None))
        self.run = False
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"dx/dt = r1x - l1xy - g1x^2", None))
        self.btnOpen.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u0439", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0430 4", None))
    # retranslateUi

    def btnRun1_click(self):
        self.pl1.clear()
        try:
            start = float(self.txtStart1.toPlainText())
            end = float(self.txtEnd1.toPlainText())
            h = float(self.txtH.toPlainText())
            params = float(self.txtInit.toPlainText())
            if end <= start or h < 0:
                raise ValueError("Неправильный формат данных")
        except ValueError:
            dlg = AlertBox("Неправильный формат данных")
            dlg.exec()
            return
        ti, yi = process_first_func(start, end, h, params)

        refresh_plots(self.pl1, ti, yi)
        self.cs1.draw()

    def btnRun2_click(self):
        self.pl1.clear()
        try:
            start = float(self.txtStart2.toPlainText())
            end = float(self.txtEnd2.toPlainText())
            h = float(self.txtH2.toPlainText())
            params = float(self.txtInit2.toPlainText())
            if end <= start or h < 0:
                raise ValueError("Неправильный формат данных")
        except ValueError:
            dlg = AlertBox("Неправильный формат данных")
            dlg.exec()
            return
        ti, yi = process_second_func(start, end, h, params)

        v_g = refresh_plots(self.pl1, ti, yi)
        self.cs1.draw()


    def btnRun3_click(self):
        self.pl2.clear()
        try:
            start = float(self.txtStart3.toPlainText())
            end = float(self.txtEnd3.toPlainText())
            h = float(self.txtH_3.toPlainText())
            str = self.txtInit_3.toPlainText().split(",")
            params = []
            for i in str:
                params.append(i.strip())

            if len(params) != 3:
                raise ValueError("")
            a = float(self.txtA.toPlainText())
            b = float(self.txtB.toPlainText())
            c = float(self.txtC.toPlainText())
            if end <= start or h < 0:
                raise ValueError("Неправильный формат данных")
        except ValueError:
            dlg = AlertBox("Неправильный формат данных")
            dlg.exec()
            return

        print(params)
        func1 = Function(lambda x, y, z: -y - z)
        func2 = Function(lambda x, y, z: x + a * y)
        func3 = Function(lambda x, y, z: b + z * (x - c))

        x, y, z, ti = process_all([func1, func2, func3], a, b, c, params, start, end, h)

        refresh_plots2(self.pl2, ti, z, x, y)
        self.cs2.draw()

    def btnRun4_click(self):
        self.pl3.clear()
        try:
            start = float(self.txtStart1_4.toPlainText())
            end = float(self.txtEnd1_4.toPlainText())
            h = float(self.txtH_4.toPlainText())
            str = self.txtInit_4.toPlainText().split(",")
            params = []
            for i in str:
                params.append(i.strip())

            if len(params) != 2:
                print(params)
                raise ValueError("")
            if end <= start or h < 0:
                raise ValueError("Неправильный формат данных")
        except ValueError:
            dlg = AlertBox("Неправильный формат данных")
            dlg.exec()
            return

        ti, x, y = task3_first(start, end, h, params)
        refresh_plots3(self.pl3, ti, x, y)
        self.cs3.draw()

    def btnRun5_click(self):
        self.pl3.clear()
        try:
            start = float(self.txtStart2_4.toPlainText())
            end = float(self.txtEnd2_4.toPlainText())
            h = float(self.txtH2_4.toPlainText())
            str = self.txtInit2_4.toPlainText().split(",")
            params = []
            for i in str:
                params.append(i.strip())

            if len(params) != 2:
                print(params)
                raise ValueError("")
            if end <= start or h < 0:
                raise ValueError("Неправильный формат данных")
        except ValueError:
            dlg = AlertBox("Неправильный формат данных")
            dlg.exec()
            return

        ti, x, y = task3_second(start, end, h, params)
        refresh_plots3(self.pl3, ti, x, y)
        self.cs3.draw()

    def btnRun6_click(self):
        self.pl4.clear()
        self.i = 0
        try:
            start = float(self.txtStart1_5.toPlainText())
            end = float(self.txtEnd1_5.toPlainText())
            h = float(self.txtH_5.toPlainText())
            str = self.txtInit_5.toPlainText().split(",")
            params = []
            for i in str:
                params.append(i.strip())

            if len(params) != 2:
                print(params)
                raise ValueError("")
            r1 = float(self.txtr1.toPlainText())
            l1 = float(self.txtl1.toPlainText())
            l2 = float(self.txtl2.toPlainText())
            b2 = float(self.txtb2.toPlainText())
            g1 = float(self.txtg1.toPlainText())
            if end <= start or h < 0:
                raise ValueError("Неправильный формат данных")
        except ValueError:
            dlg = AlertBox("Неправильный формат данных")
            dlg.exec()
            return

        classes.task4.r1 = r1
        classes.task4.l1 = l1
        classes.task4.l2 = l2
        classes.task4.b2 = b2
        classes.task4.g1 = g1

        self.params = classes.task4.graphics(self.pl4, start, end, h, params)
        self.cs4.draw()
        self.run = True
        self.i = self.i + 1

    def btnOpen_click(self):
        if self.run:
            self.pl4.clear()
            classes.task4.refresh_plots4(self.pl4, *self.params, self.i)
            self.cs4.draw()
            if self.i == 3:
                self.i = 0
            else:
                self.i = self.i + 1