# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'medicine_information_add.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(335, 455)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(-20, 410, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)
        self.Name = QLabel(Dialog)
        self.Name.setObjectName(u"Name")
        self.Name.setGeometry(QRect(20, 320, 61, 21))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 321, 20))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.Image = QLabel(Dialog)
        self.Image.setObjectName(u"Image")
        self.Image.setGeometry(QRect(30, 50, 251, 211))
        self.Image.setPixmap(QPixmap(u"../icon/medicine_icon.png"))
        self.Image.setScaledContents(True)
        self.Image.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 30, 311, 261))
        self.label_5.setAutoFillBackground(True)
        self.Category = QLabel(Dialog)
        self.Category.setObjectName(u"Category")
        self.Category.setGeometry(QRect(20, 380, 61, 21))
        self.GenName = QLabel(Dialog)
        self.GenName.setObjectName(u"GenName")
        self.GenName.setGeometry(QRect(20, 350, 61, 21))
        self.medicine_name = QLineEdit(Dialog)
        self.medicine_name.setObjectName(u"medicine_name")
        self.medicine_name.setGeometry(QRect(100, 320, 221, 20))
        self.generic_name = QLineEdit(Dialog)
        self.generic_name.setObjectName(u"generic_name")
        self.generic_name.setGeometry(QRect(100, 350, 221, 20))
        self.Image_2 = QLabel(Dialog)
        self.Image_2.setObjectName(u"Image_2")
        self.Image_2.setGeometry(QRect(40, 50, 251, 211))
        self.Image_2.setPixmap(QPixmap(u"../icon/medicine_icon.png"))
        self.Image_2.setScaledContents(True)
        self.Image_2.setAlignment(Qt.AlignCenter)
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(100, 380, 221, 22))
        self.label_5.raise_()
        self.buttonBox.raise_()
        self.Name.raise_()
        self.label_3.raise_()
        self.Image.raise_()
        self.Category.raise_()
        self.GenName.raise_()
        self.medicine_name.raise_()
        self.generic_name.raise_()
        self.Image_2.raise_()
        self.comboBox.raise_()

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Name.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"ADD NEW MEDICINE", None))
        self.Image.setText("")
        self.label_5.setText("")
        self.Category.setText(QCoreApplication.translate("Dialog", u"Category", None))
        self.GenName.setText(QCoreApplication.translate("Dialog", u"Gen. Name", None))
        self.Image_2.setText("")
    # retranslateUi

