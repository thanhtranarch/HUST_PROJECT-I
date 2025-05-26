# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1003, 672)
        self.actionCustomer = QAction(MainWindow)
        self.actionCustomer.setObjectName(u"actionCustomer")
        self.actionStaff = QAction(MainWindow)
        self.actionStaff.setObjectName(u"actionStaff")
        self.actionMedicine = QAction(MainWindow)
        self.actionMedicine.setObjectName(u"actionMedicine")
        self.actionInvoice = QAction(MainWindow)
        self.actionInvoice.setObjectName(u"actionInvoice")
        self.actionSupplier = QAction(MainWindow)
        self.actionSupplier.setObjectName(u"actionSupplier")
        self.actionStock = QAction(MainWindow)
        self.actionStock.setObjectName(u"actionStock")
        self.actionLog_out = QAction(MainWindow)
        self.actionLog_out.setObjectName(u"actionLog_out")
        self.actionLog = QAction(MainWindow)
        self.actionLog.setObjectName(u"actionLog")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.list_outdate = QGroupBox(self.groupBox)
        self.list_outdate.setObjectName(u"list_outdate")
        self.gridLayout = QGridLayout(self.list_outdate)
        self.gridLayout.setObjectName(u"gridLayout")
        self.warning_detail = QPushButton(self.list_outdate)
        self.warning_detail.setObjectName(u"warning_detail")

        self.gridLayout.addWidget(self.warning_detail, 1, 3, 2, 1)

        self.label = QLabel(self.list_outdate)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 1, 0, 2, 2)

        self.outdate_medicine = QTableWidget(self.list_outdate)
        if (self.outdate_medicine.columnCount() < 8):
            self.outdate_medicine.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.outdate_medicine.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.outdate_medicine.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.outdate_medicine.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.outdate_medicine.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.outdate_medicine.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.outdate_medicine.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.outdate_medicine.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.outdate_medicine.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.outdate_medicine.setObjectName(u"outdate_medicine")
        self.outdate_medicine.horizontalHeader().setCascadingSectionResizes(True)

        self.gridLayout.addWidget(self.outdate_medicine, 0, 0, 1, 4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 2, 1)

        self.label_2 = QLabel(self.list_outdate)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 1)

        self.label_3 = QLabel(self.list_outdate)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)


        self.gridLayout_4.addWidget(self.list_outdate, 2, 0, 1, 1)

        self.stock_medicine = QTableWidget(self.groupBox)
        if (self.stock_medicine.columnCount() < 6):
            self.stock_medicine.setColumnCount(6)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.stock_medicine.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.stock_medicine.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.stock_medicine.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.stock_medicine.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.stock_medicine.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.stock_medicine.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        self.stock_medicine.setObjectName(u"stock_medicine")
        self.stock_medicine.setColumnCount(6)
        self.stock_medicine.horizontalHeader().setCascadingSectionResizes(True)
        self.stock_medicine.verticalHeader().setCascadingSectionResizes(False)

        self.gridLayout_4.addWidget(self.stock_medicine, 0, 0, 1, 1)

        self.stock_detail = QPushButton(self.groupBox)
        self.stock_detail.setObjectName(u"stock_detail")

        self.gridLayout_4.addWidget(self.stock_detail, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 1, 1, 2, 4)

        self.invoice_create = QPushButton(self.centralwidget)
        self.invoice_create.setObjectName(u"invoice_create")
        self.invoice_create.setEnabled(True)
        self.invoice_create.setMouseTracking(True)
        self.invoice_create.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_3.addWidget(self.invoice_create, 3, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(685, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 3, 3, 1, 1)

        self.invoice_daily = QGroupBox(self.centralwidget)
        self.invoice_daily.setObjectName(u"invoice_daily")
        self.gridLayout_2 = QGridLayout(self.invoice_daily)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.invoice_detail = QPushButton(self.invoice_daily)
        self.invoice_detail.setObjectName(u"invoice_detail")

        self.gridLayout_2.addWidget(self.invoice_detail, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.invoice_daily)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem20)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)

        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.invoice_daily, 0, 1, 1, 4)

        self.horizontalSpacer_6 = QSpacerItem(20, 582, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.horizontalSpacer_6, 0, 5, 4, 1)

        self.horizontalSpacer_7 = QSpacerItem(20, 582, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.horizontalSpacer_7, 0, 0, 4, 1)

        self.export_report = QPushButton(self.centralwidget)
        self.export_report.setObjectName(u"export_report")

        self.gridLayout_3.addWidget(self.export_report, 3, 1, 1, 2)

        self.horizontalSpacer_3 = QSpacerItem(679, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 4, 1, 1, 4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1003, 22))
        self.menuMaindashboard = QMenu(self.menubar)
        self.menuMaindashboard.setObjectName(u"menuMaindashboard")
        self.menuGeneral_Management = QMenu(self.menubar)
        self.menuGeneral_Management.setObjectName(u"menuGeneral_Management")
        MainWindow.setMenuBar(self.menubar)
        QWidget.setTabOrder(self.stock_detail, self.invoice_detail)

        self.menubar.addAction(self.menuGeneral_Management.menuAction())
        self.menubar.addAction(self.menuMaindashboard.menuAction())
        self.menuGeneral_Management.addSeparator()
        self.menuGeneral_Management.addAction(self.actionCustomer)
        self.menuGeneral_Management.addAction(self.actionMedicine)
        self.menuGeneral_Management.addAction(self.actionInvoice)
        self.menuGeneral_Management.addAction(self.actionStaff)
        self.menuGeneral_Management.addAction(self.actionStock)
        self.menuGeneral_Management.addAction(self.actionSupplier)
        self.menuGeneral_Management.addAction(self.actionLog)
        self.menuGeneral_Management.addAction(self.actionLog_out)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.actionCustomer.setText(QCoreApplication.translate("MainWindow", u"Customer", None))
        self.actionStaff.setText(QCoreApplication.translate("MainWindow", u"Staff", None))
        self.actionMedicine.setText(QCoreApplication.translate("MainWindow", u"Medicine", None))
        self.actionInvoice.setText(QCoreApplication.translate("MainWindow", u"Invoice", None))
        self.actionSupplier.setText(QCoreApplication.translate("MainWindow", u"Supplier", None))
        self.actionStock.setText(QCoreApplication.translate("MainWindow", u"Stock", None))
        self.actionLog_out.setText(QCoreApplication.translate("MainWindow", u"\u2b8c Log out", None))
        self.actionLog.setText(QCoreApplication.translate("MainWindow", u"Log", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"DANH S\u00c1CH THU\u1ed0C T\u1ed2N KHO", None))
        self.list_outdate.setTitle(QCoreApplication.translate("MainWindow", u"THU\u1ed0C S\u1eaeP H\u1ebeT H\u1ea0N", None))
        self.warning_detail.setText(QCoreApplication.translate("MainWindow", u"CHI TI\u1ebeT", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"*C\u1ea3nh b\u00e1o s\u1edbm nh\u1eefng thu\u1ed1c s\u1eafp h\u1ebft h\u1ea1n", None))
        ___qtablewidgetitem = self.outdate_medicine.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.outdate_medicine.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.outdate_medicine.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem3 = self.outdate_medicine.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Unit", None));
        ___qtablewidgetitem4 = self.outdate_medicine.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Batch No.", None));
        ___qtablewidgetitem5 = self.outdate_medicine.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None));
        ___qtablewidgetitem6 = self.outdate_medicine.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Days Left", None));
        ___qtablewidgetitem7 = self.outdate_medicine.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u26a0\ufe0f: 60 ng\u00e0y ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u2757:30 ng\u00e0y ", None))
        ___qtablewidgetitem8 = self.stock_medicine.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem9 = self.stock_medicine.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem10 = self.stock_medicine.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Unit", None));
        ___qtablewidgetitem11 = self.stock_medicine.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem12 = self.stock_medicine.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Batch No.", None));
        ___qtablewidgetitem13 = self.stock_medicine.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        self.stock_detail.setText(QCoreApplication.translate("MainWindow", u"CHI TI\u1ebeT", None))
        self.invoice_create.setText(QCoreApplication.translate("MainWindow", u"T\u1ea0O H\u00d3A \u0110\u01a0N", None))
        self.invoice_daily.setTitle(QCoreApplication.translate("MainWindow", u"DANH S\u00c1CH H\u00d3A \u0110\u01a0N TRONG NG\u00c0Y", None))
        self.invoice_detail.setText(QCoreApplication.translate("MainWindow", u"CHI TI\u1ebeT", None))
        ___qtablewidgetitem14 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Invoice ID", None));
        ___qtablewidgetitem15 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Time", None));
        ___qtablewidgetitem16 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Customer", None));
        ___qtablewidgetitem17 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Total Amount", None));
        ___qtablewidgetitem18 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Staff", None));
        ___qtablewidgetitem19 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Notes", None));
        ___qtablewidgetitem20 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Details", None));
        self.export_report.setText(QCoreApplication.translate("MainWindow", u"IN B\u00c1O C\u00c1O NG\u00c0Y", None))
        self.menuMaindashboard.setTitle(QCoreApplication.translate("MainWindow", u"Maindashboard", None))
        self.menuGeneral_Management.setTitle(QCoreApplication.translate("MainWindow", u"General Management", None))
        pass
    # retranslateUi

