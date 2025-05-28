# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customer_information.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(335, 482)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(-20, 440, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.ID = QLabel(Dialog)
        self.ID.setObjectName(u"ID")
        self.ID.setGeometry(QRect(20, 350, 47, 21))
        self.Name = QLabel(Dialog)
        self.Name.setObjectName(u"Name")
        self.Name.setGeometry(QRect(20, 320, 47, 21))
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
        self.Image.setPixmap(QPixmap(u"../icon/staff_icon.png"))
        self.Image.setScaledContents(True)
        self.Image.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 30, 311, 261))
        self.label_5.setAutoFillBackground(True)
        self.Phone_3 = QLabel(Dialog)
        self.Phone_3.setObjectName(u"Phone_3")
        self.Phone_3.setGeometry(QRect(20, 380, 47, 21))
        self.Email = QLabel(Dialog)
        self.Email.setObjectName(u"Email")
        self.Email.setGeometry(QRect(20, 410, 47, 21))
        self.customer_name = QLineEdit(Dialog)
        self.customer_name.setObjectName(u"customer_name")
        self.customer_name.setGeometry(QRect(80, 320, 241, 20))
        self.customer_id = QLineEdit(Dialog)
        self.customer_id.setObjectName(u"customer_id")
        self.customer_id.setGeometry(QRect(80, 350, 241, 20))
        self.customer_phone = QLineEdit(Dialog)
        self.customer_phone.setObjectName(u"customer_phone")
        self.customer_phone.setGeometry(QRect(80, 380, 241, 20))
        self.customer_email = QLineEdit(Dialog)
        self.customer_email.setObjectName(u"customer_email")
        self.customer_email.setGeometry(QRect(80, 410, 241, 20))
        self.label_5.raise_()
        self.buttonBox.raise_()
        self.ID.raise_()
        self.Name.raise_()
        self.label_3.raise_()
        self.Image.raise_()
        self.Phone_3.raise_()
        self.Email.raise_()
        self.customer_name.raise_()
        self.customer_id.raise_()
        self.customer_phone.raise_()
        self.customer_email.raise_()
        QWidget.setTabOrder(self.customer_name, self.customer_id)
        QWidget.setTabOrder(self.customer_id, self.customer_phone)
        QWidget.setTabOrder(self.customer_phone, self.customer_email)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.ID.setText(QCoreApplication.translate("Dialog", u"ID", None))
        self.Name.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"CUSTOMER INFORMATION", None))
        self.Image.setText("")
        self.label_5.setText("")
        self.Phone_3.setText(QCoreApplication.translate("Dialog", u"Phone", None))
        self.Email.setText(QCoreApplication.translate("Dialog", u"Email", None))
    # retranslateUi

