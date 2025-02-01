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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

from Lab1.task2 import create_graphics
from task1 import calculate_goal_function

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(657, 380)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 0, 441, 71))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 280, 161, 61))
        font1 = QFont()
        font1.setPointSize(14)
        self.pushButton.setFont(font1)
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(400, 280, 181, 61))
        self.pushButton_2.setFont(font1)
        self.lblVariable = QLabel(Form)
        self.lblVariable.setObjectName(u"lblVariable")
        self.lblVariable.setGeometry(QRect(40, 110, 431, 41))
        self.lblVariable.setFont(font1)
        self.lblResult = QLabel(Form)
        self.lblResult.setObjectName(u"lblResult")
        self.lblResult.setGeometry(QRect(40, 220, 431, 41))
        self.lblResult.setFont(font1)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 60, 431, 41))
        self.label_4.setFont(font1)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 170, 431, 41))
        self.label_5.setFont(font1)

        self.pushButton.clicked.connect(self.click_goal_function)
        self.pushButton_2.clicked.connect(self.click_graphics)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0420\u0430\u0441\u0441\u0447\u0451\u0442 \u043f\u0440\u0438\u0431\u044b\u043b\u0438 \u0438 \u043f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435 \u0433\u0440\u0430\u0444\u0438\u043a\u043e\u0432", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u0413\u0440\u0430\u0444\u0438\u043a\u0438", None))
        self.lblVariable.setText("")
        self.lblResult.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0446\u0435\u043b\u0435\u0432\u043e\u0439 \u0444\u0443\u043d\u043a\u0446\u0438\u0438", None))
    # retranslateUi


    def click_goal_function(self):
        v, res = calculate_goal_function()
        print(v)
        self.lblVariable.setText(str(v))
        self.lblResult.setText(str(res))

    def click_graphics(self):
        create_graphics()