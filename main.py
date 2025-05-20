from PyQt6 import QtCore, QtWidgets, QtGui, uic
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import sys
import MySQLdb as mysql_db
from DBManager import DBManager
import os
import darkdetect
# Path management
current_dir = os.path.dirname(os.path.abspath(__file__))  


def iconset():
    icon_dir = os.path.join(current_dir, "icon")
    if darkdetect.isDark():
        icon_path = os.path.join(icon_dir, "app_icon_dark.png")
    else:
        icon_path = os.path.join(icon_dir, "app_icon_light.png")
    return icon_path

icon_path = iconset()

def load_data_into_table(table_widget, sql_query, column_names):
    cursor.execute(sql_query)
    rows = cursor.fetchall()

    table_widget.setRowCount(len(rows))
    table_widget.setColumnCount(len(column_names))
    table_widget.setHorizontalHeaderLabels(column_names)

    for row_idx, row_data in enumerate(rows):
        for col_idx, value in enumerate(row_data):
            item = QTableWidgetItem(str(value))
            table_widget.setItem(row_idx, col_idx, item)
# # Connect DataBase
# class DBManager:
#     def __int__(self):
#         self.connection = None
#         self.cursor = None
        
#     def connect(self):
#         self.connection = mysql_db.connector.connect('localhost','root','@Thanh070891','medimanager')          
#         self.cursor = self.connection.cursor()
#         return self.cursor
    
#     def execute (self,query, params = None):
#         self.cursor.excute(query, params or ())
#         return self.cursor
    
#     def commit(self):
#         self.connection.commit()
        
#     def close(self):
#         if self.cursor:
#             self.cursor.close()
#         if self.connection:
#             self.connection.close()
# Main Window
class Main_w(QMainWindow):  
    def __init__(self,staff_id=None):
        super(Main_w,self).__init__()
        ui_path = os.path.join(current_dir, 'ui', 'main.ui')
        print(">>> main.ui path:", ui_path)
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"Không tìm thấy UI file: {ui_path}")
        uic.loadUi(ui_path, self)
        self.setWindowTitle("MediManager")
        self.setWindowIcon(QtGui.QIcon(icon_path))
        self.staff_id=staff_id
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.actionLog_out.triggered.connect(self.goto_login)
        # # Bảng hóa đơn trong ngày
        
        

        # # Bảng thông tin thuốc
        # load_data_into_table(self.stock_medicine,
        #     "SELECT medicine_id, medicine_name, generic_name, stock_quantity, batch_number FROM medicine",
        #     ["ID", "Name", "Unit", "Quantity", "Batch No.", "Price"]
        # )
        # #Bảng thuốc quá hạn

    def closeEvent(self, event):
        QApplication.quit()
    def goto_login(self):
        self.login_window = Login_w()
        self.login_window.show()
        self.hide()

# Login Window
class Login_w(QMainWindow):
    def __init__(self):
        super(Login_w,self).__init__()
        current_dir = os.path.dirname(os.path.abspath(__file__))  
        ui_path = os.path.join(current_dir, 'ui', 'login.ui')
        uic.loadUi(ui_path, self)
        
        self.setFixedSize(250, 140)
        self.setWindowTitle("MediManager")
        self.setWindowIcon(QtGui.QIcon(icon_path))
        
        self.register_label.linkActivated.connect(self.goto_register)
        self.login_button.clicked.connect(self.login)
        self.login_button.setDefault(True)


    def login(self):
        un = self.login_user.text()
        psw = self.login_password.text()
        try:
            
            # Connect to MySQL
            db = DBManager()
            cursor = db.connect()
            sql = 'SELECT staff_id, staff_psw FROM staff WHERE staff_id = %s AND staff_psw = %s'
            cursor.execute(sql, (un, psw))
            result = cursor.fetchone()
            cursor.close()
            connect.close()
            if result:
                QMessageBox.information(self, "Login Success", "Đăng nhập thành công!")
                
                self.main_window = Main_w(un)
                self.main_window.show()
                self.close()
                
            else:
                QMessageBox.warning(self, "Login Failed", "Sai tài khoản hoặc mật khẩu.")
        except mysql_db.Error as e:
            QMessageBox.critical(self,"Database Error", f"Lỗi kết nối CSDL: {str(e)}")
        
        
    
    def keyPressEvent(self, event):
        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            self.login()
            
    def goto_register(self):
        # widget.setCurrentIndex(1) 
        # widget.setFixedSize(250,220)
        self.register_window = Register_w()
        self.register_window.show()
        self.close()
        
# Register Window
class Register_w(QMainWindow):
    def __init__(self):
        super(Register_w,self).__init__()   
        ui_path = os.path.join(current_dir, 'ui', 'register.ui')
        uic.loadUi(ui_path, self)
        # widget.setFixedSize(250,220)
        self.setFixedSize(250, 220)
        self.setWindowTitle("MediManager")
        self.setWindowIcon(QtGui.QIcon(icon_path))
        
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
        self.login_window = Login_w()
        self.login_window.show()
        self.close()


# Program starts here
if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = Login_w()
    login_window.show()
    sys.exit(app.exec())







