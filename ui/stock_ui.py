# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stock.ui'
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
        MainWindow.resize(942, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_6 = QSpacerItem(28, 536, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.horizontalSpacer_6, 0, 2, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(18, 536, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.horizontalSpacer_7, 0, 0, 1, 1)

        self.invoice_daily = QGroupBox(self.centralwidget)
        self.invoice_daily.setObjectName(u"invoice_daily")
        self.gridLayout_2 = QGridLayout(self.invoice_daily)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.back_button = QPushButton(self.invoice_daily)
        self.back_button.setObjectName(u"back_button")

        self.gridLayout_2.addWidget(self.back_button, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(407, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.label = QLabel(self.invoice_daily)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)

        self.gridLayout_2.addWidget(self.label, 1, 5, 1, 1)

        self.invoice_detail = QPushButton(self.invoice_daily)
        self.invoice_detail.setObjectName(u"invoice_detail")
        self.invoice_detail.setEnabled(False)
        self.invoice_detail.setMaximumSize(QSize(85, 16777215))
        self.invoice_detail.setMouseTracking(True)
        self.invoice_detail.setAutoDefault(False)

        self.gridLayout_2.addWidget(self.invoice_detail, 3, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 3, 1, 1, 2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 3, 4, 1, 1)

        self.tableWidget = QTableWidget(self.invoice_daily)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(38)

        self.gridLayout_2.addWidget(self.tableWidget, 2, 0, 1, 7)

        self.search_input = QLineEdit(self.invoice_daily)
        self.search_input.setObjectName(u"search_input")
        self.search_input.setEnabled(True)

        self.gridLayout_2.addWidget(self.search_input, 1, 6, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 3, 3, 1, 1)

        self.add_stock = QPushButton(self.invoice_daily)
        self.add_stock.setObjectName(u"add_stock")
        self.add_stock.setMaximumSize(QSize(120, 16777215))

        self.gridLayout_2.addWidget(self.add_stock, 3, 6, 1, 1)


        self.gridLayout.addWidget(self.invoice_daily, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 942, 22))
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
        self.invoice_daily.setTitle(QCoreApplication.translate("MainWindow", u"TH\u1ed0NG K\u00ca NH\u1eacP KHO", None))
        self.back_button.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udd0d", None))
        self.invoice_detail.setText(QCoreApplication.translate("MainWindow", u"PRINT", None))
        self.search_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search", None))
        self.add_stock.setText(QCoreApplication.translate("MainWindow", u"T\u1ea0O PHI\u1ebeU NH\u1eacP", None))
    # retranslateUi

