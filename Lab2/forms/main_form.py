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
    QSizePolicy, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(790, 530)
        self.txtCopper = QTextEdit(Form)
        self.txtCopper.setObjectName(u"txtCopper")
        self.txtCopper.setGeometry(QRect(130, 20, 104, 31))
        self.txtRadius = QTextEdit(Form)
        self.txtRadius.setObjectName(u"txtRadius")
        self.txtRadius.setGeometry(QRect(130, 100, 104, 31))
        self.txtPetrol = QTextEdit(Form)
        self.txtPetrol.setObjectName(u"txtPetrol")
        self.txtPetrol.setGeometry(QRect(130, 60, 104, 31))
        self.txtM = QTextEdit(Form)
        self.txtM.setObjectName(u"txtM")
        self.txtM.setGeometry(QRect(130, 140, 104, 31))
        self.txtCount = QTextEdit(Form)
        self.txtCount.setObjectName(u"txtCount")
        self.txtCount.setGeometry(QRect(130, 180, 104, 31))
        self.txtStep = QTextEdit(Form)
        self.txtStep.setObjectName(u"txtStep")
        self.txtStep.setGeometry(QRect(130, 220, 104, 31))
        self.txtG = QTextEdit(Form)
        self.txtG.setObjectName(u"txtG")
        self.txtG.setGeometry(QRect(130, 260, 104, 31))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 111, 21))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 70, 111, 16))
        self.label_2.setFont(font)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 100, 91, 16))
        self.label_3.setFont(font)
        self.table = QTableWidget(Form)
        if (self.table.columnCount() < 3):
            self.table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(0, 330, 231, 192))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 150, 91, 16))
        self.label_4.setFont(font)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 190, 91, 16))
        self.label_5.setFont(font)
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 220, 91, 16))
        self.label_6.setFont(font)
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 260, 91, 21))
        self.label_7.setFont(font)
        self.btnRun = QPushButton(Form)
        self.btnRun.setObjectName(u"btnRun")
        self.btnRun.setGeometry(QRect(60, 290, 101, 31))
        self.btnRun.setFont(font)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(270, 20, 511, 491))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Copper Density", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Copper Petrol", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Radius", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"t", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"v", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"h", None));
        self.label_4.setText(QCoreApplication.translate("Form", u"m", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Max Count", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Step", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"g", None))
        self.btnRun.setText(QCoreApplication.translate("Form", u"Run", None))
    # retranslateUi

