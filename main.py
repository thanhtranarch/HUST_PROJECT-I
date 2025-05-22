from PyQt6 import QtCore, QtWidgets, QtGui, uic
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
from PyQt6.QtGui import QIcon, QFont, QBrush, QColor
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

def load_data_into_table(table_widget, sql_query, column_names, cursor):
    cursor.execute(sql_query)
    rows = cursor.fetchall()

    table_widget.setRowCount(len(rows))
    table_widget.setColumnCount(len(column_names))
    table_widget.setHorizontalHeaderLabels(column_names)

    for row_idx, row_data in enumerate(rows):
        for col_idx, value in enumerate(row_data):
            item = QTableWidgetItem(str(value))
            table_widget.setItem(row_idx, col_idx, item)

# Connect to DataBase
class AppContext:
    def __init__(self):
        self.db_manager = DBManager()
        self.connection = self.db_manager.connect()
    def __del__(self):
        self.db_manager.close()

# Main Window
class Main_w(QMainWindow):  
    def __init__(self, context, staff_id=None):
        super(Main_w, self).__init__()
        self.context = context
        ui_path = os.path.join(current_dir, 'ui', 'main.ui')
        print(">>> main.ui path:", ui_path)
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"Không tìm thấy UI file: {ui_path}")
        uic.loadUi(ui_path, self)
        self.setWindowTitle("MediManager")
        self.setWindowIcon(QtGui.QIcon(icon_path))
        self.staff_id = staff_id
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        # Connect action for each menu
        self.actionSupplier.triggered.connect(self.goto_supplier)
        self.actionMedicine.triggered.connect(self.goto_medicine)
        self.actionStock.triggered.connect(self.goto_stock)
        self.actionCustomer.triggered.connect(self.goto_customer)
        self.actionStaff.triggered.connect(self.goto_staff)
        self.actionLog_out.triggered.connect(self.goto_login)

    def closeEvent(self, event):
        QApplication.quit()

    def goto_login(self):
        self.login_window = Login_w(self.context)
        self.login_window.show()
        self.hide()

    def goto_supplier(self):
        self.supplier_window = Supplier_w(self.context)
        self.supplier_window.show()
        self.hide()

    def goto_medicine(self):
        self.medicine_window = Medicine_w(self.context)
        self.medicine_window.show()
        self.hide()

    def goto_customer(self):
        self.customer_window = Customer_w(self.context)
        self.customer_window.show()
        self.hide()

    def goto_stock(self):
        self.stock_window = Stock_w(self.context)
        self.stock_window.show()
        self.hide()

    def goto_staff(self):
        self.staff_window = Staff_w(self.context)
        self.staff_window.show()
        self.hide()

    def goto_invoice(self):
        self.invoice_window = Invoice_w(self.context)
        self.invoice_window.show()
        self.hide()

# Supplier Window
class Supplier_w(QMainWindow):
    def __init__(self, context):
        super(Supplier_w, self).__init__()
        self.context = context
        ui_path = os.path.join(current_dir, 'ui', 'supplier.ui')
        print(">>> supplier.ui path:", ui_path)
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"Không tìm thấy UI file: {ui_path}")
        uic.loadUi(ui_path, self)
        self.setWindowTitle("Supplier Management")
        self.setWindowIcon(QtGui.QIcon(icon_path))
        self.load_supplier_data()

    def load_supplier_data(self):
        try:
            db = self.context.db_manager
            sql= """SELECT supplier_id, supplier_name, created_at, updated_at FROM supplier"""
            db.execute(sql)
            results = db.fetchall()

            # Cập nhật TableWidget
            self.tableWidget.setRowCount(len(results))
            self.tableWidget.setColumnCount(len(db.execute(sql).description)+1)
            # self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
            self.tableWidget.setColumnHidden(0, True)
            self.tableWidget.setColumnWidth(1, 300)  
            self.tableWidget.setColumnWidth(2, 150) 
            self.tableWidget.setColumnWidth(3, 150) 
            self.tableWidget.setColumnWidth(4, 200) 
            self.tableWidget.cellClicked.connect(self.handle_cell_click)

            column_count = self.tableWidget.columnCount()

            for row_idx, row_data in enumerate(results):
                supplier_id = row_data[0]  # Giữ lại để dùng UserRole

                for col_idx in range(column_count):
                    if col_idx < len(row_data):
                        value = row_data[col_idx]
                        item = QTableWidgetItem(str(value))

                        # Supplier Name (hiển thị với underline)
                        if col_idx == 1:
                            font = QFont()
                            font.setBold(True)
                            font.setUnderline(True)
                            item.setFont(font)
                            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                            item.setToolTip("Click để xem chi tiết nhà cung cấp")
                            item.setData(Qt.ItemDataRole.UserRole, supplier_id)

                        elif col_idx == 0:
                            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                        self.tableWidget.setItem(row_idx, col_idx, item)

                    else:
                        # Cột "View Details"
                        detail_item = QTableWidgetItem("View Details")
                        font = QFont()
                        font.setUnderline(True)
                        detail_item.setFont(font)
                        detail_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                        detail_item.setData(Qt.ItemDataRole.UserRole, supplier_id)
                        detail_item.setToolTip("Click để xem chi tiết nhà cung cấp")
                        self.tableWidget.setItem(row_idx, col_idx, detail_item)
        except Exception as e:
            print("Lỗi khi tải dữ liệu:", e)
    
    def show_supplier_detail(self, supplier_id):
        detail_dialog = SupplierInformation_w(self.context, supplier_id)
        detail_dialog.exec()
    
    def handle_cell_click(self, row, column):
        if column == 1 or column == 4:
            item = self.tableWidget.item(row, column)
            if item is None:
                print("Item not found")
                return
            supplier_id = item.data(Qt.ItemDataRole.UserRole)
            if supplier_id:
                print(f"Opening details for supplier ID: {supplier_id}")
                self.show_supplier_detail(supplier_id)

    def goto_staff(self):
        self.staff_window = Staff_w(self.context)
        self.staff_window.show()
        self.hide()

    def goto_customer(self):
        self.customer_window = Customer_w(self.context)
        self.customer_window.show()
        self.hide()
class SupplierInformation_w(QDialog):
    def __init__(self, context, supplier_id):
        super(SupplierInformation_w, self).__init__()
        self.context = context
        self.supplier_id_value = supplier_id
        ui_path = os.path.join(current_dir, 'ui', 'supplier_information.ui')
        print(">>> supplier_information.ui' path:", ui_path)
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"Không tìm thấy UI file: {ui_path}")
        uic.loadUi(ui_path, self)
        self.setWindowTitle("Supplier Management")
        self.setWindowIcon(QtGui.QIcon(icon_path))
        self.load_supplier_data(self.supplier_id_value)
        

    def load_supplier_data(self, supplier_id_value):
        try:
            db = self.context.db_manager
            sql = """SELECT supplier_id, supplier_name, supplier_address,
                            contact_name, contact_phone, contact_email, payment_terms 
                        FROM supplier WHERE supplier_id = %s"""
            db.execute(sql, (supplier_id_value,))
            result = db.fetchone()
            print(f"Query result: {result}")

            if result:
                self.supplier_id.setText(str(result[0]))
                self.supplier_id.setReadOnly(True)
                self.supplier_name.setText(result[1] if result[1] else "")
                self.supplier_name.setReadOnly(True)
                self.supplier_address.setPlainText(result[2] if result[2] else "")
                self.supplier_address.setReadOnly(True)
                self.contact_name.setText(result[3] if result[3] else "")
                self.contact_name.setReadOnly(True)
                self.contact_phone.setText(result[4] if result[4] else "")
                self.contact_phone.setReadOnly(True)
                self.contact_email.setText(result[5] if result[5] else "")
                self.contact_email.setReadOnly(True)
                if result[6]:
                    self.comboBox_payment_terms.setCurrentText(result[6])
                    self.comboBox_payment_terms.setEnabled(False)
            else:
                QMessageBox.warning(self, "Thông báo", "Không tìm thấy thông tin nhà cung cấp.")
        except Exception as e:
            print("Lỗi khi tải dữ liệu chi tiết:", e)

# Customer Window
class Customer_w(QMainWindow):
    def __init__(self, context):
        super(Customer_w, self).__init__()
        self.context = context
        ui_path = os.path.join(current_dir, 'ui', 'customer.ui')
        print(">>> customer.ui path:", ui_path)
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"Không tìm thấy UI file: {ui_path}")
        uic.loadUi(ui_path, self)
        self.setWindowTitle("Customer Management")
        self.setWindowIcon(QtGui.QIcon(icon_path))
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.actionSave.triggered.connect(self.save_customer_data)

    def save_customer_data(self):
        customer_name = self.lineEdit_Customer_Name.text()
        contact_person = self.lineEdit_Contact_Person.text()
        phone_number = self.lineEdit_Phone_Number.text()
        address = self.textEdit_Address.toPlainText()

        sql_query = f"INSERT INTO customers (name, contact_person, phone_number, address) VALUES ('{customer_name}', '{contact_person}', '{phone_number}', '{address}')"
        self.context.cursor.execute(sql_query)
        self.context.connection.commit()

    def goto_staff(self):
        self.staff_window = Staff_w(self.context)
        self.staff_window.show()
        self.hide()


# Staff Window
class Staff_w(QMainWindow):
    def __init__(self, context, staff_id=None):
        super(Staff_w, self).__init__()
        self.context = context
        ui_path = os.path.join(current_dir, 'ui', 'staff.ui')
        print(">>> staff.ui path:", ui_path)
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"Không tìm thấy UI file: {ui_path}")
        uic.loadUi(ui_path, self)
        self.setWindowTitle("Staff Management")
        self.setWindowIcon(QtGui.QIcon(icon_path))
        self.staff_id = staff_id
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.actionSave.triggered.connect(self.save_staff_data)

    def save_staff_data(self):
        name = self.lineEdit_Name.text()
        username = self.lineEdit_Username.text()
        password = self.lineEdit_Password.text()

        sql_query = f"INSERT INTO staff (name, username, password) VALUES ('{name}', '{username}', '{password}')"
        self.context.cursor.execute(sql_query)
        self.context.connection.commit()

    def goto_customer(self):
        self.customer_window = Customer_w(self.context)
        self.customer_window.show()
        self.hide()


# Medicine Window
class Medicine_w(QMainWindow):
    def __init__(self, context):
        super(Medicine_w, self).__init__()
        self.context = context
        ui_path = os.path.join(current_dir, 'ui', 'medicine.ui')
        print(">>> medicine.ui path:", ui_path)
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"Không tìm thấy UI file: {ui_path}")
        uic.loadUi(ui_path, self)
        self.setWindowTitle("Medicine Management")
        self.setWindowIcon(QtGui.QIcon(icon_path))
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.actionSave.triggered.connect(self.save_medicine_data)

    def save_medicine_data(self):
        medicine_name = self.lineEdit_Medicine_Name.text()
        supplier_id = int(self.comboBox_Supplier_ID.currentText())
        quantity = int(self.spinBox_Quantity.value())

        sql_query = f"INSERT INTO medicines (name, supplier_id, quantity) VALUES ('{medicine_name}', {supplier_id}, {quantity})"
        self.context.cursor.execute(sql_query)
        self.context.connection.commit()

    def goto_staff(self):
        self.staff_window = Staff_w(self.context)
        self.staff_window.show()
        self.hide()


# Stock Window
class Stock_w(QMainWindow):
    def __init__(self, context):
        super(Stock_w, self).__init__()
        self.context = context
        ui_path = os.path.join(current_dir, 'ui', 'stock.ui')
        print(">>> stock.ui path:", ui_path)
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"Không tìm thấy UI file: {ui_path}")
        uic.loadUi(ui_path, self)
        self.setWindowTitle("Stock Management")
        self.setWindowIcon(QtGui.QIcon(icon_path))
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.actionSave.triggered.connect(self.save_stock_data)

    def save_stock_data(self):
        medicine_id = int(self.comboBox_Medicine_ID.currentText())
        supplier_id = int(self.comboBox_Supplier_ID.currentText())
        quantity = int(self.spinBox_Quantity.value())

        sql_query = f"INSERT INTO stock (medicine_id, supplier_id, quantity) VALUES ({medicine_id}, {supplier_id}, {quantity})"
        self.context.cursor.execute(sql_query)
        self.context.connection.commit()

    def goto_medicine(self):
        self.medicine_window = Medicine_w(self.context)
        self.medicine_window.show()
        self.hide()


# Invoice Window
class Invoice_w(QMainWindow):
    def __init__(self, context):
        super(Invoice_w, self).__init__()
        self.context = context
        ui_path = os.path.join(current_dir, 'ui', 'invoice.ui')
        print(">>> invoice.ui path:", ui_path)
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"Không tìm thấy UI file: {ui_path}")
        uic.loadUi(ui_path, self)
        self.setWindowTitle("Invoice Management")
        self.setWindowIcon(QtGui.QIcon(icon_path))
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.actionSave.triggered.connect(self.save_invoice_data)

    def save_invoice_data(self):
        customer_id = int(self.comboBox_Customer_ID.currentText())
        medicine_id = int(self.comboBox_Medicine_ID.currentText())
        quantity = int(self.spinBox_Quantity.value())
        total_cost = float(self.lineEdit_Total_Cost.text())

        sql_query = f"INSERT INTO invoices (customer_id, medicine_id, quantity, total_cost) VALUES ({customer_id}, {medicine_id}, {quantity}, {total_cost})"
        self.context.cursor.execute(sql_query)
        self.context.connection.commit()

    def goto_customer(self):
        self.customer_window = Customer_w(self.context)
        self.customer_window.show()
        self.hide()


# Login Window
class Login_w(QDialog):
    def __init__(self, context):
        super(Login_w, self).__init__()
        self.context = context
        ui_path = os.path.join(current_dir, 'ui', 'login.ui')
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"Không tìm thấy file UI: {ui_path}")
        uic.loadUi(ui_path, self)

        self.setFixedSize(250, 110)
        self.setWindowTitle("MediManager")
        self.setWindowIcon(QtGui.QIcon(icon_path))

        self.register_label.linkActivated.connect(self.goto_register)
        self.login_button.clicked.connect(self.login)
        self.login_button.setDefault(True)

    def login(self):
        un = self.login_user.text()
        psw = self.login_password.text()
        try:
            db = self.context.db_manager
            sql = 'SELECT staff_id, staff_psw FROM staff WHERE staff_id = %s AND staff_psw = %s'
            db.execute(sql, (un, psw))
            result = db.fetchone()

            if result:
                QMessageBox.information(self, "Login Success", "Đăng nhập thành công!")
                self.main_window = Main_w(self.context, un)
                self.main_window.show()
                self.close()
            else:
                QMessageBox.warning(self, "Login Failed", "Sai tài khoản hoặc mật khẩu.")
        except mysql_db.Error as e:
            QMessageBox.critical(self, "Database Error", f"Lỗi kết nối CSDL: {str(e)}")

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            self.login()

    def goto_register(self):
        self.register_window = Register_w(self.context)
        self.register_window.show()
        self.close()

# Register Window
class Register_w(QDialog):
    def __init__(self, context):
        super(Register_w, self).__init__()   
        self.context = context
        ui_path = os.path.join(current_dir, 'ui', 'register.ui')
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"Không tìm thấy file UI: {ui_path}")
        uic.loadUi(ui_path, self)
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
            db = self.context.db_manager
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
            db.execute(create_sql)
            db.execute("SELECT staff_id FROM staff WHERE staff_id = %s", (un,))
            if db.fetchone():
                QMessageBox.warning(self, "Lỗi", "Mã nhân viên đã tồn tại. Vui lòng chọn mã khác.")
                return

            insert_sql = """INSERT INTO staff (staff_id, staff_psw, staff_name, staff_phone, staff_email)
                           VALUES (%s, %s, %s, %s, %s)"""
            db.execute(insert_sql, (un, psw, name, phone, email))
            db.commit()

            QMessageBox.information(self, "Register Success", "Đăng ký thành công!")

            self.staff_id.clear()
            self.staff_psw.clear()
            self.staff_name.clear()
            self.staff_phone.clear()
            self.staff_email.clear()
        except mysql_db.Error as e:
            QMessageBox.critical(self, "Database Error", f"Lỗi đăng ký: {str(e)}")

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            self.register()

    def goto_login(self):
        self.login_window = Login_w(self.context)
        self.login_window.show()
        self.close()

# Program starts here
if __name__ == '__main__':
    context = AppContext()
    app = QApplication(sys.argv)
    login_window = Login_w(context)
    login_window.show()
    sys.exit(app.exec())
