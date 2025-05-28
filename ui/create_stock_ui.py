# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_stock.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QGroupBox, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(763, 564)
        self.invoice_information = QGroupBox(Dialog)
        self.invoice_information.setObjectName(u"invoice_information")
        self.invoice_information.setGeometry(QRect(10, 30, 341, 141))
        self.label_stock_id = QLabel(self.invoice_information)
        self.label_stock_id.setObjectName(u"label_stock_id")
        self.label_stock_id.setGeometry(QRect(10, 20, 81, 21))
        self.label_date = QLabel(self.invoice_information)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setGeometry(QRect(10, 50, 71, 21))
        self.label_staff = QLabel(self.invoice_information)
        self.label_staff.setObjectName(u"label_staff")
        self.label_staff.setGeometry(QRect(10, 80, 81, 21))
        self.label_supplier = QLabel(self.invoice_information)
        self.label_supplier.setObjectName(u"label_supplier")
        self.label_supplier.setGeometry(QRect(10, 110, 81, 21))
        self.stock_id = QLineEdit(self.invoice_information)
        self.stock_id.setObjectName(u"stock_id")
        self.stock_id.setGeometry(QRect(90, 20, 241, 20))
        self.stock_date = QDateEdit(self.invoice_information)
        self.stock_date.setObjectName(u"stock_date")
        self.stock_date.setGeometry(QRect(90, 50, 241, 22))
        self.staff_name = QLineEdit(self.invoice_information)
        self.staff_name.setObjectName(u"staff_name")
        self.staff_name.setGeometry(QRect(90, 80, 241, 20))
        self.supplier = QComboBox(self.invoice_information)
        self.supplier.setObjectName(u"supplier")
        self.supplier.setGeometry(QRect(90, 110, 241, 22))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 731, 20))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.list_medicine = QGroupBox(Dialog)
        self.list_medicine.setObjectName(u"list_medicine")
        self.list_medicine.setGeometry(QRect(10, 191, 741, 251))
        self.buy_list = QTableWidget(self.list_medicine)
        if (self.buy_list.columnCount() < 7):
            self.buy_list.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.buy_list.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.buy_list.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.buy_list.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.buy_list.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.buy_list.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.buy_list.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.buy_list.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.buy_list.rowCount() < 7):
            self.buy_list.setRowCount(7)
        self.buy_list.setObjectName(u"buy_list")
        self.buy_list.setGeometry(QRect(10, 20, 731, 192))
        self.buy_list.setRowCount(7)
        self.add_medicine = QPushButton(self.list_medicine)
        self.add_medicine.setObjectName(u"add_medicine")
        self.add_medicine.setGeometry(QRect(10, 220, 75, 23))
        self.add_new_medicine = QPushButton(self.list_medicine)
        self.add_new_medicine.setObjectName(u"add_new_medicine")
        self.add_new_medicine.setEnabled(True)
        self.add_new_medicine.setGeometry(QRect(90, 220, 111, 23))
        self.add_medicine_2 = QPushButton(Dialog)
        self.add_medicine_2.setObjectName(u"add_medicine_2")
        self.add_medicine_2.setEnabled(False)
        self.add_medicine_2.setGeometry(QRect(360, 140, 101, 23))
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 450, 741, 41))
        self.sum = QLabel(self.groupBox)
        self.sum.setObjectName(u"sum")
        self.sum.setGeometry(QRect(10, 10, 61, 21))
        self.payment = QLabel(self.groupBox)
        self.payment.setObjectName(u"payment")
        self.payment.setGeometry(QRect(570, 10, 61, 21))
        self.sum_money = QLineEdit(self.groupBox)
        self.sum_money.setObjectName(u"sum_money")
        self.sum_money.setGeometry(QRect(70, 10, 113, 20))
        self.payment_term = QComboBox(self.groupBox)
        self.payment_term.setObjectName(u"payment_term")
        self.payment_term.setGeometry(QRect(650, 10, 60, 22))
        self.save_button = QPushButton(Dialog)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(300, 510, 75, 23))
        self.cancel_button = QPushButton(Dialog)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(390, 510, 75, 23))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.invoice_information.setTitle(QCoreApplication.translate("Dialog", u"TH\u00d4NG TIN PHI\u1ebeU NH\u1eacP", None))
        self.label_stock_id.setText(QCoreApplication.translate("Dialog", u"M\u00e3 phi\u1ebfu nh\u1eadp", None))
        self.label_date.setText(QCoreApplication.translate("Dialog", u"Ng\u00e0y l\u1eadp", None))
        self.label_staff.setText(QCoreApplication.translate("Dialog", u"Nh\u00e2n vi\u00ean", None))
        self.label_supplier.setText(QCoreApplication.translate("Dialog", u"Supplier", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"PHI\u1ebeU NH\u1eacP", None))
        self.list_medicine.setTitle(QCoreApplication.translate("Dialog", u"DANH S\u00c1CH THU\u1ed0C MUA", None))
        ___qtablewidgetitem = self.buy_list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"T\u00ean thu\u1ed1c", None));
        ___qtablewidgetitem1 = self.buy_list.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"\u0110\u01a1n v\u1ecb", None));
        ___qtablewidgetitem2 = self.buy_list.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Gi\u00e1 b\u00e1n", None));
        ___qtablewidgetitem3 = self.buy_list.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"S\u1ed1 l\u01b0\u1ee3ng", None));
        ___qtablewidgetitem4 = self.buy_list.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Th\u00e0nh ti\u1ec1n", None));
        ___qtablewidgetitem5 = self.buy_list.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"ID", None));
        ___qtablewidgetitem6 = self.buy_list.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"X\u00f3a", None));
        self.add_medicine.setText(QCoreApplication.translate("Dialog", u"Th\u00eam thu\u1ed1c", None))
        self.add_new_medicine.setText(QCoreApplication.translate("Dialog", u"Th\u00eam thu\u1ed1c m\u1edbi", None))
        self.add_medicine_2.setText(QCoreApplication.translate("Dialog", u"Th\u00eam Supplier", None))
        self.groupBox.setTitle("")
        self.sum.setText(QCoreApplication.translate("Dialog", u"T\u1ed5ng ti\u1ec1n:", None))
        self.payment.setText(QCoreApplication.translate("Dialog", u"Thanh to\u00e1n:", None))
        self.save_button.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.cancel_button.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

