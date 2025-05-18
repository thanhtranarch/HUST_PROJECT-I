from PyQt6 import QtCore, QtWidgets, QtGui, uic
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import sys
import MySQLdb as mysql_db
import os
import darkdetect
# Path management
def iconset():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    icon_dir = os.path.join(base_dir, "icon")
    
    if darkdetect.isDark():
        icon_path = os.path.join(icon_dir, "app_icon_dark.png")
    else:
        icon_path = os.path.join(icon_dir, "app_icon_light.png")
    return icon_path
icon_path = iconset()

current_dir = os.path.dirname(os.path.abspath(__file__))  

# Login Window
class Login_w(QMainWindow):
    def __init__(self):
        super(Login_w,self).__init__()
        current_dir = os.path.dirname(os.path.abspath(__file__))  
        ui_path = os.path.join(current_dir, 'ui', 'login.ui')
        uic.loadUi(ui_path, self)
        self.register_label.linkActivated.connect(self.goto_register)
        self.login_button.clicked.connect(self.login)
        self.login_button.setDefault(True)

    def login(self):
        un = self.login_user.text()
        psw = self.login_password.text()
        
        try:
            # Connect to MySQL
            connect = mysql_db.connect('localhost','root','@Thanh070891','medimanager')
            cursor = connect.cursor()
            sql = 'SELECT staff_id, staff_psw FROM staff WHERE staff_id = %s AND staff_psw = %s'
            cursor.execute(sql, (un, psw))
            result = cursor.fetchone()
            cursor.close()
            connect.close()
            if result:
                QMessageBox.information(self, "Login Success", "Đăng nhập thành công!")
                widget.setCurrentIndex(2)
                widget.showMaximized()
            else:
                QMessageBox.warning(self, "Login Failed", "Sai tài khoản hoặc mật khẩu.")
        except mysql_db.Error as e:
            QMessageBox.critical(self,"Database Error", f"Lỗi kết nối CSDL: {str(e)}")
        
        
    
    def keyPressEvent(self, event):
        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            self.login()
            
    def goto_register(self):
        widget.setCurrentIndex(1) 
        widget.resize(250,220)
# Register Window
class Register_w(QMainWindow):
    def __init__(self):
        super(Register_w,self).__init__()   
        ui_path = os.path.join(current_dir, 'ui', 'register.ui')
        uic.loadUi(ui_path, self)
        self.login_label.linkActivated.connect(self.goto_login)
        self.register_button.clicked.connect(self.register)
        self.register_button.setDefault(True)
        
    def register(self):
        un = self.staff_id.text()
        psw = self.staff_psw.text()
        name = self.staff_name.text()
        phone = self.staff_phone.text()
        email = self.staff_email.text()

        try:
            connect = mysql_db.connect('localhost','root','@Thanh070891','medimanager')
            cursor = connect.cursor()

            # Create table if not exists
            create_sql = """CREATE TABLE IF NOT EXISTS staff (
                        staff_id INT PRIMARY KEY,
                        staff_psw VARCHAR(255),
                        staff_name VARCHAR(255),
                        staff_phone VARCHAR(20),
                        staff_email VARCHAR(50),
                        staff_position VARCHAR(100),
                        staff_salary DECIMAL(10, 0),
                        hire_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
                    )"""
            cursor.execute(create_sql)
            # Check if staff_id already exists
            cursor.execute("SELECT staff_id FROM staff WHERE staff_id = %s", (un,))
            if cursor.fetchone():
                QMessageBox.warning(self, "Lỗi", "Mã nhân viên đã tồn tại. Vui lòng chọn mã khác.")
                return

            # Insert data into table
            insert_sql = """INSERT INTO staff (staff_id, staff_psw, staff_name, staff_phone, staff_email) VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(insert_sql, (un, psw, name, phone, email))
            connect.commit()
            QMessageBox.information(self, "Register Success", "Đăng ký thành công!")

            self.staff_id.clear()
            self.staff_psw.clear()
            self.staff_name.clear()
            self.staff_phone.clear()
            self.staff_email.clear()
        except mysql_db.Error as e:
            QMessageBox.critical(self,"Database Error", f"Lỗi đăng ký: {str(e)}")
        finally:
            try:
                cursor.close()
                connect.close()
            except:
                pass
    def keyPressEvent(self, event):
        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            self.register()
            
    def goto_login(self):
        widget.setCurrentIndex(0)
        widget.resize(250,140)
        
# Main Window
class Main_w(QMainWindow):  
    def __init__(self):
        super(Main_w,self).__init__()
        ui_path = os.path.join(current_dir, 'ui', 'main.ui')
        uic.loadUi(ui_path, self)
        self.showFullScreen()


# Program starts here
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
Login_f = Login_w()
Register_f = Register_w()
Main_f = Main_w()
widget.setWindowTitle("MediManager")
widget.setWindowIcon(QtGui.QIcon(icon_path))
widget.addWidget(Login_f)
widget.addWidget(Register_f)
widget.addWidget(Main_f)
widget.setCurrentIndex(0)
widget.show()
app.exec()







