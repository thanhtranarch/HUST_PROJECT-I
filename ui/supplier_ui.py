# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'supplier.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(949, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_7 = QSpacerItem(18, 536, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.horizontalSpacer_7, 0, 0, 1, 1)

        self.invoice_daily = QGroupBox(self.centralwidget)
        self.invoice_daily.setObjectName(u"invoice_daily")
        self.gridLayout_2 = QGridLayout(self.invoice_daily)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.back_button = QPushButton(self.invoice_daily)
        self.back_button.setObjectName(u"back_button")

        self.gridLayout_2.addWidget(self.back_button, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.invoice_daily)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(38)

        self.gridLayout_2.addWidget(self.tableWidget, 4, 0, 1, 4)

        self.horizontalSpacer = QSpacerItem(407, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.invoice_detail = QPushButton(self.invoice_daily)
        self.invoice_detail.setObjectName(u"invoice_detail")
        self.invoice_detail.setEnabled(False)
        self.invoice_detail.setMaximumSize(QSize(85, 16777215))
        self.invoice_detail.setMouseTracking(True)
        self.invoice_detail.setAutoDefault(False)

        self.gridLayout_2.addWidget(self.invoice_detail, 5, 0, 1, 1)

        self.label = QLabel(self.invoice_daily)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)

        self.gridLayout_2.addWidget(self.label, 1, 2, 1, 1)

        self.search_input = QLineEdit(self.invoice_daily)
        self.search_input.setObjectName(u"search_input")
        self.search_input.setEnabled(True)

        self.gridLayout_2.addWidget(self.search_input, 1, 3, 1, 1)


        self.gridLayout.addWidget(self.invoice_daily, 0, 2, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(28, 536, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.horizontalSpacer_6, 0, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 949, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.invoice_detail.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.invoice_daily.setTitle(QCoreApplication.translate("MainWindow", u"DANH S\u00c1CH SUPPLIER", None))
        self.back_button.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Created Time", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Updated Time", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Details", None));
        self.invoice_detail.setText(QCoreApplication.translate("MainWindow", u"PRINT", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udd0d", None))
        self.search_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search", None))
    # retranslateUi

