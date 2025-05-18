from PyQt6 import QtCore, QtWidgets, QtGui, uic
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
import sys
import MySQLdb as mysql_db

# Login Window
class Login_w(QMainWindow):
    def __init__(self):
        super(Login_w,self).__init__()
        uic.loadUi("login.ui", self)
        self.setWindowFlags(
            QtCore.Qt.WindowType.Window |
            QtCore.Qt.WindowType.CustomizeWindowHint |
            QtCore.Qt.WindowType.WindowTitleHint |
            QtCore.Qt.WindowType.WindowCloseButtonHint
        )

        # (Optional) Cố định kích thước cửa sổ để tránh resize
        self.setFixedSize(250,150)
# Register Window
class Register_w(QMainWindow):
    def __init__(self):
        super(Register_w,self).__init__()   
        uic.loadUi("register.ui", self)
        self.setWindowFlags(
            QtCore.Qt.WindowType.Window |
            QtCore.Qt.WindowType.CustomizeWindowHint |
            QtCore.Qt.WindowType.WindowTitleHint |
            QtCore.Qt.WindowType.WindowCloseButtonHint
        )

        # (Optional) Cố định kích thước cửa
        self.setFixedSize(250,150)
# Main Window
class Main_w(QMainWindow):  
    def __init__(self):
        super(Main_w,self).__init__()
        uic.loadUi('maindashboard.ui')
        
        
# Program starts here
app=QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
Login_f=Login_w()
Register_f=Register_w()
Main_f=Main_w()
widget.addWidget(Login_f)
widget.addWidget(Register_f)
widget.addWidget(Main_f)
widget.setCurrentIndex(0)
widget.show()
app.exec()






