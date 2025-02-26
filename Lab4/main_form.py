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
                           QPalette, QPixmap, QRadialGradient, QTransform, QStandardItemModel, QStandardItem)
from PySide6.QtWidgets import (QApplication, QLabel, QListView, QPushButton,
                               QSizePolicy, QTabWidget, QTextEdit, QVBoxLayout,
                               QWidget, QDialog, QDialogButtonBox)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from numgen import GammaGenerator
from generator import TrigonomicOperations, Generator
from test import GammaGenerator, NumpyTest, GeneratorTest


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
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(906, 464)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(-10, 0, 921, 501))
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.txtN = QTextEdit(self.tab_3)
        self.txtN.setObjectName(u"txtN")
        self.txtN.setGeometry(QRect(30, 50, 221, 41))
        font = QFont()
        font.setPointSize(16)
        self.txtN.setFont(font)
        self.txtInit = QTextEdit(self.tab_3)
        self.txtInit.setObjectName(u"txtInit")
        self.txtInit.setGeometry(QRect(30, 100, 221, 41))
        self.txtInit.setFont(font)
        self.txtSize = QTextEdit(self.tab_3)
        self.txtSize.setObjectName(u"txtSize")
        self.txtSize.setGeometry(QRect(30, 150, 221, 41))
        self.txtSize.setFont(font)
        self.lblTrig = QLabel(self.tab_3)
        self.lblTrig.setObjectName(u"lblTrig")
        self.lblTrig.setGeometry(QRect(250, -10, 241, 51))
        self.lblTrig.setFont(font)
        self.listView = QListView(self.tab_3)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(260, 50, 191, 151))
        self.verticalLayoutWidget = QWidget(self.tab_3)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(470, 40, 431, 381))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.txtM = QTextEdit(self.tab_3)
        self.txtM.setObjectName(u"txtM")
        self.txtM.setGeometry(QRect(30, 200, 221, 41))
        self.txtM.setFont(font)
        self.txtD = QTextEdit(self.tab_3)
        self.txtD.setObjectName(u"txtD")
        self.txtD.setGeometry(QRect(30, 250, 221, 41))
        self.txtD.setFont(font)
        self.txtD.setReadOnly(True)
        self.txtB = QTextEdit(self.tab_3)
        self.txtB.setObjectName(u"txtB")
        self.txtB.setGeometry(QRect(30, 300, 221, 41))
        self.txtB.setFont(font)
        self.txtB.setReadOnly(True)
        self.btnRunTrig = QPushButton(self.tab_3)
        self.btnRunTrig.setObjectName(u"btnRunTrig")
        self.btnRunTrig.setGeometry(QRect(290, 260, 131, 41))
        self.btnRunTrig.setFont(font)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.lblGamma = QLabel(self.tab_4)
        self.lblGamma.setObjectName(u"lblGamma")
        self.lblGamma.setGeometry(QRect(350, 10, 241, 51))
        self.lblGamma.setFont(font)
        self.verticalLayoutWidget_2 = QWidget(self.tab_4)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(470, 50, 431, 381))
        self.verticalLayoutGamma = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayoutGamma.setObjectName(u"verticalLayoutGamma")
        self.verticalLayoutGamma.setContentsMargins(0, 0, 0, 0)
        self.txtM_2 = QTextEdit(self.tab_4)
        self.txtM_2.setObjectName(u"txtM_2")
        self.txtM_2.setGeometry(QRect(30, 210, 221, 41))
        self.txtM_2.setFont(font)
        self.txtSize2 = QTextEdit(self.tab_4)
        self.txtSize2.setObjectName(u"txtSize2")
        self.txtSize2.setGeometry(QRect(30, 160, 221, 41))
        self.txtSize2.setFont(font)
        self.txtD_2 = QTextEdit(self.tab_4)
        self.txtD_2.setObjectName(u"txtD_2")
        self.txtD_2.setGeometry(QRect(30, 260, 221, 41))
        self.txtD_2.setFont(font)
        self.txtD_2.setReadOnly(True)
        self.txtScale = QTextEdit(self.tab_4)
        self.txtScale.setObjectName(u"txtScale")
        self.txtScale.setGeometry(QRect(30, 110, 221, 41))
        self.txtScale.setFont(font)
        self.txtShape = QTextEdit(self.tab_4)
        self.txtShape.setObjectName(u"txtShape")
        self.txtShape.setGeometry(QRect(30, 60, 221, 41))
        self.txtShape.setFont(font)
        self.txtB_2 = QTextEdit(self.tab_4)
        self.txtB_2.setObjectName(u"txtB_2")
        self.txtB_2.setGeometry(QRect(30, 310, 221, 41))
        self.txtB_2.setFont(font)
        self.txtB_2.setReadOnly(True)
        self.listViewGamma = QListView(self.tab_4)
        self.listViewGamma.setObjectName(u"listViewGamma")
        self.listViewGamma.setGeometry(QRect(260, 60, 191, 151))
        self.btnRun = QPushButton(self.tab_4)
        self.btnRun.setObjectName(u"btnRun")
        self.btnRun.setGeometry(QRect(300, 260, 131, 41))
        self.btnRun.setFont(font)
        self.tabWidget.addTab(self.tab_4, "")

        self.btnRun.clicked.connect(self.btn_gamma_clicked)
        self.btnRunTrig.clicked.connect(self.btn_trig_clicked)

        self.pl1 = Figure()
        self.cs1 = FigureCanvas(self.pl1)
        self.verticalLayoutGamma.addWidget(self.cs1)

        self.pl2 = Figure()
        self.cs2 = FigureCanvas(self.pl2)
        self.verticalLayout.addWidget(self.cs2)

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.txtN.setPlaceholderText(QCoreApplication.translate("Form", u"n", None))
        self.txtInit.setPlaceholderText(QCoreApplication.translate("Form", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u044b\u0439", None))
        self.txtSize.setPlaceholderText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.lblTrig.setText(QCoreApplication.translate("Form", u"\u0422\u0440\u0438\u0433\u043e\u043d\u043e\u043c\u0435\u0442\u0440\u0438\u0447\u0435\u0441\u043a\u0438\u0439", None))
        self.txtM.setPlaceholderText(QCoreApplication.translate("Form", u"M", None))
        self.txtD.setPlaceholderText(QCoreApplication.translate("Form", u"D", None))
        self.txtB.setPlaceholderText(QCoreApplication.translate("Form", u"B", None))
        self.btnRunTrig.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\u0422\u0440\u0438\u0433\u043e\u043d\u043e\u043c\u0435\u0442\u0440\u0438\u0447\u0435\u0441\u043a\u0438\u0439", None))
        self.lblGamma.setText(QCoreApplication.translate("Form", u"\u0413\u0430\u043c\u043c\u0430", None))
        self.txtM_2.setPlaceholderText(QCoreApplication.translate("Form", u"M", None))
        self.txtSize2.setPlaceholderText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.txtD_2.setPlaceholderText(QCoreApplication.translate("Form", u"D", None))
        self.txtScale.setPlaceholderText(QCoreApplication.translate("Form", u"Scale", None))
        self.txtShape.setPlaceholderText(QCoreApplication.translate("Form", u"Shape", None))
        self.txtB_2.setPlaceholderText(QCoreApplication.translate("Form", u"B", None))
        self.btnRun.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"\u0413\u0430\u043c\u043c\u0430", None))
    # retranslateUi

    def btn_trig_clicked(self):
        try:
            trig = TrigonomicOperations(int(self.txtN.toPlainText()), float(self.txtInit.toPlainText()))
            gen = Generator(trig)
            values = gen.generate(int(self.txtSize.toPlainText()))

            gt = GeneratorTest(values, int(self.txtSize.toPlainText()))
            m, b, d = gt.calc_char()
            print(m, b, d)
            self.txtM.setText(str(m))
            self.txtB.setText(str(b))
            self.txtD.setText(str(d))
            self.update_list(self.listView, values)
            self.refresh_plots(self.pl2, self.cs2, values)
        except ValueError:
            dlg = AlertBox("Неправильный формат данных")
            dlg.exec()
            return

    def btn_gamma_clicked(self):
        try:
            ng = GammaGenerator(int(self.txtShape.toPlainText()), int(self.txtScale.toPlainText()))
            values = ng.generate(int(self.txtSize2.toPlainText()))

            nt = NumpyTest(values, int(self.txtSize2.toPlainText()))
            m, b, d = nt.calc_char()
            self.txtM_2.setText(str(m))
            self.txtB_2.setText(str(b))
            self.txtD_2.setText(str(d))
            self.update_list(self.listViewGamma, values)
            self.refresh_plots(self.pl1, self.cs1, values)
        except ValueError:
            dlg = AlertBox("Неправильный формат данных")
            dlg.exec()
            return

    def update_list(self, list_view, data):
        model = QStandardItemModel()
        for i in data:
            s_item = QStandardItem(str(i))
            model.appendRow(s_item)
        list_view.setModel(model)

    def refresh_plots(self, pl, cs, x):
        pl.clear()
        v_g = pl.add_subplot(1, 1, 1)
        v_g.hist(x, label="Распределение")
        v_g.set_xlabel("x")
        v_g.set_ylabel("y")
        v_g.legend()
        v_g.grid()

        cs.draw()


