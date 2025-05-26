# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(250, 107)
        self.login_user = QLineEdit(Dialog)
        self.login_user.setObjectName(u"login_user")
        self.login_user.setGeometry(QRect(90, 10, 141, 20))
        self.login_button = QPushButton(Dialog)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(90, 70, 75, 23))
        self.login_password = QLineEdit(Dialog)
        self.login_password.setObjectName(u"login_password")
        self.login_password.setGeometry(QRect(90, 40, 141, 20))
        self.login_password.setEchoMode(QLineEdit.Password)
        self.register_label = QLabel(Dialog)
        self.register_label.setObjectName(u"register_label")
        self.register_label.setGeometry(QRect(20, 70, 61, 21))
        font = QFont()
        font.setUnderline(False)
        self.register_label.setFont(font)
        self.register_label.setMouseTracking(True)
        self.register_label.setTextFormat(Qt.RichText)
        self.user_label = QLabel(Dialog)
        self.user_label.setObjectName(u"user_label")
        self.user_label.setGeometry(QRect(20, 11, 47, 20))
        self.password_label = QLabel(Dialog)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setGeometry(QRect(20, 40, 61, 16))
        QWidget.setTabOrder(self.login_user, self.login_password)
        QWidget.setTabOrder(self.login_password, self.login_button)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.login_user.setText("")
        self.login_user.setPlaceholderText(QCoreApplication.translate("Dialog", u"enter username", None))
        self.login_button.setText(QCoreApplication.translate("Dialog", u"log in", None))
        self.login_password.setText("")
        self.login_password.setPlaceholderText(QCoreApplication.translate("Dialog", u"enter password", None))
        self.register_label.setText(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"#\"><span style=\" text-decoration: underline; color:#e1e1e1;\">Register?</span></a></p></body></html>", None))
        self.user_label.setText(QCoreApplication.translate("Dialog", u"user", None))
        self.password_label.setText(QCoreApplication.translate("Dialog", u"password", None))
    # retranslateUi

