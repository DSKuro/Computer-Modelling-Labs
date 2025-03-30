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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(922, 634)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 871, 591))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(240, 17, 141, 31))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 67, 191, 21))
        self.label_2.setFont(font)
        self.txtl = QTextEdit(self.tab)
        self.txtl.setObjectName(u"txtl")
        self.txtl.setGeometry(QRect(400, 10, 441, 41))
        self.txtl.setFont(font)
        self.btnRun = QPushButton(self.tab)
        self.btnRun.setObjectName(u"btnRun")
        self.btnRun.setGeometry(QRect(310, 230, 171, 51))
        self.btnRun.setFont(font)
        self.tableWidget = QTableWidget(self.tab)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(50, 290, 751, 261))
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(210, 127, 181, 21))
        self.label_3.setFont(font)
        self.txtTO = QTextEdit(self.tab)
        self.txtTO.setObjectName(u"txtTO")
        self.txtTO.setGeometry(QRect(400, 117, 441, 51))
        self.txtTO.setFont(font)
        self.txtt = QTextEdit(self.tab)
        self.txtt.setObjectName(u"txtt")
        self.txtt.setGeometry(QRect(400, 57, 441, 51))
        self.txtt.setFont(font)
        self.txtO = QTextEdit(self.tab)
        self.txtO.setObjectName(u"txtO")
        self.txtO.setGeometry(QRect(400, 190, 441, 31))
        self.txtO.setFont(font)
        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(160, 190, 201, 21))
        self.label_9.setFont(font)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(130, 20, 141, 31))
        self.label_4.setFont(font)
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(140, 120, 181, 21))
        self.label_5.setFont(font)
        self.txtt_2 = QTextEdit(self.tab_2)
        self.txtt_2.setObjectName(u"txtt_2")
        self.txtt_2.setGeometry(QRect(370, 60, 441, 41))
        self.txtt_2.setFont(font)
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(130, 70, 191, 21))
        self.label_6.setFont(font)
        self.btnRun_2 = QPushButton(self.tab_2)
        self.btnRun_2.setObjectName(u"btnRun_2")
        self.btnRun_2.setGeometry(QRect(340, 270, 171, 51))
        self.btnRun_2.setFont(font)
        self.txtl_2 = QTextEdit(self.tab_2)
        self.txtl_2.setObjectName(u"txtl_2")
        self.txtl_2.setGeometry(QRect(370, 10, 441, 41))
        self.txtl_2.setFont(font)
        self.txtTO_2 = QTextEdit(self.tab_2)
        self.txtTO_2.setObjectName(u"txtTO_2")
        self.txtTO_2.setGeometry(QRect(370, 110, 441, 41))
        self.txtTO_2.setFont(font)
        self.tableWidget_2 = QTableWidget(self.tab_2)
        if (self.tableWidget_2.columnCount() < 4):
            self.tableWidget_2.setColumnCount(4)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(60, 330, 751, 261))
        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(130, 170, 181, 21))
        self.label_7.setFont(font)
        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(130, 230, 201, 21))
        self.label_8.setFont(font)
        self.txtC = QTextEdit(self.tab_2)
        self.txtC.setObjectName(u"txtC")
        self.txtC.setGeometry(QRect(370, 170, 441, 41))
        self.txtC.setFont(font)
        self.txtO2 = QTextEdit(self.tab_2)
        self.txtO2.setObjectName(u"txtO2")
        self.txtO2.setGeometry(QRect(370, 230, 441, 31))
        self.txtO2.setFont(font)
        self.pushButton = QPushButton(self.tab_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(600, 273, 181, 41))
        self.pushButton.setFont(font)
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0418\u043d\u0442\u0435\u043d\u0441\u0438\u0432\u043d\u043e\u0441\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0412\u0440\u0435\u043c\u044f \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u044f", None))
        self.btnRun.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u0422\u0438\u043f", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u0412\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u044c \u043e\u0442\u043a\u0430\u0437\u0430", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u0412\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u044c \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u044f", None));
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0412\u0440\u0435\u043c\u044f \u0440\u0430\u0431\u043e\u0442\u044b", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u043e\u0447\u0435\u0440\u0435\u0434\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u041e\u0434\u043d\u043e\u043a\u0430\u043d\u0430\u043b\u044c\u043d\u0430\u044f", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0418\u043d\u0442\u0435\u043d\u0441\u0438\u0432\u043d\u043e\u0441\u0442\u044c", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0412\u0440\u0435\u043c\u044f \u0440\u0430\u0431\u043e\u0442\u044b", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u0412\u0440\u0435\u043c\u044f \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u044f", None))
        self.btnRun_2.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u0422\u0438\u043f", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"\u0412\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u044c \u043e\u0442\u043a\u0430\u0437\u0430", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"\u0412\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u044c \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u044f", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"\u0414\u043b\u0438\u043d\u0430 \u041e\u0447\u0435\u0440\u0435\u0434\u0438", None));
        self.label_7.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u0430\u043d\u0430\u043b\u043e\u0432", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u043e\u0447\u0435\u0440\u0435\u0434\u0438", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0432\u043e\u0434 \u043f\u043e \u043a\u0430\u043d\u0430\u043b\u0430\u043c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u041c\u043d\u043e\u0433\u043e\u043a\u0430\u043d\u0430\u043b\u044c\u043d\u0430\u044f", None))
    # retranslateUi

