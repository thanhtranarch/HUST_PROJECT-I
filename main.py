from PyQt6 import QtCore, QtWidgets, QtGui, uic
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
from PyQt6.QtGui import QIcon, QFont, QBrush, QColor
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import *
from datetime import datetime
from DBManager import DBManager
import sys
import MySQLdb as mysql_db
import os
import darkdetect
import bcrypt 


# Connect to DataBase - Done
class AppContext:
    def __init__(self, staff_id = None):
        self.staff_id = staff_id
        self.db_manager = DBManager()
        self.connection = self.db_manager.connect()
    def __del__(self):
        self.db_manager.close()

# Main Window
class Main_w(QMainWindow):  
    def __init__(self, context, staff_id=None):
        super(Main_w, self).__init__()
        ui_path = os.path.join(current_dir, 'ui', 'main.ui')
        print(">>> main.ui path:", ui_path)
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"Không tìm thấy UI file: {ui_path}")
        uic.loadUi(ui_path, self)
        self.setWindowTitle("MediManager")
        self.setWindowIcon(QtGui.QIcon(icon_path))
        self.context = context
        self.staff_id = staff_id

        # Load UI file
        ui_path = os.path.join(current_dir, 'ui', 'main.ui')
        print(">>> main.ui path:", ui_path)
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"Không tìm thấy UI file: {ui_path}")
        uic.loadUi(ui_path, self)

        # Setup window properties
        self.setWindowTitle("MediManager")
        self.setWindowIcon(QtGui.QIcon(icon_path))
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        # Status bar setup
        self.status_label = QLabel()
        self.status_label.setStyleSheet("color: gray; font-size: 11px;")
        self.statusBar().addPermanentWidget(self.status_label)

        # Timer for status updates
        self.status_timer = QTimer(self)
        self.status_timer.timeout.connect(self.update_status_info)
        self.status_timer.start(1000)  # Update every second
        self.update_status_info()  # Initial update

        # Connect menu actions
        self.actionSupplier.triggered.connect(self.goto_supplier)
        self.actionMedicine.triggered.connect(self.goto_medicine)
        self.actionStock.triggered.connect(self.goto_stock)
        self.actionCustomer.triggered.connect(self.goto_customer)
        self.actionStaff.triggered.connect(self.goto_staff)
        self.actionLog_out.triggered.connect(self.goto_login)
        self.actionLogs.triggered.connect(self.goto_logs)
        self.load_stock_overview()
        self.load_outdate_warning()
        self.load_today_invoice()

    def load_stock_overview(self):
        db = self.context.db_manager
        sql = """SELECT medicine_id, medicine_name, unit, stock_quantity, batch_number, sale_price FROM medicine"""
        db.execute(sql)
        results = db.fetchall()
        self.stock_medicine.setRowCount(len(results))
        for row, data in enumerate(results):
            for col, value in enumerate(data):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.stock_medicine.setItem(row, col, item)
    def load_outdate_warning(self):
        db = self.context.db_manager
        sql = """SELECT medicine_id, medicine_name, stock_quantity, unit, batch_number, expiration_date,
                DATEDIFF(expiration_date, NOW()) AS days_left,
                CASE
                  WHEN DATEDIFF(expiration_date, NOW()) <= 30 THEN '⚠ Gấp'
                  WHEN DATEDIFF(expiration_date, NOW()) <= 60 THEN '⏳ Sắp hết hạn'
                  ELSE '✅'
                END AS status
                FROM medicine
                WHERE DATEDIFF(expiration_date, NOW()) <= 60
                ORDER BY expiration_date ASC
                """  
        db.execute(sql)
        results = db.fetchall()
        self.outdate_medicine.setRowCount(len(results))
        for row, data in enumerate(results):
            for col, value in enumerate(data):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.outdate_medicine.setItem(row, col, item)
    def load_today_invoice(self):
        db = self.context.db_manager
        sql = """SELECT invoice_id, invoice_date, customer_id, total_amount, staff_id, payment_status
                 FROM invoice WHERE DATE(invoice_date) = CURDATE()"""
        db.execute(sql)
        results = db.fetchall()
        self.tableWidget.setRowCount(len(results))
        for row, data in enumerate(results):
            for col, value in enumerate(data):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.tableWidget.setItem(row, col, item)


    
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

    def goto_logs(self):
        self.logs_window = Logs_w(self.context)
        self.logs_window.show()
        self.hide()

    def update_status_info(self):
        now = datetime.now().strftime("%H:%M:%S - %d/%m/%Y")
        status = f"👤 {self.staff_id}   | 🕒 {now}   | ✅ Database Connected"
        self.status_label.setText(status)


# Supplier Window
class Supplier_w(QMainWindow):
    def __init__(self, context):
        super(Supplier_w, self).__init__()
        self.context = context
        # Load UI file
        ui_path = os.path.join(current_dir, 'ui', 'supplier.ui')
        print(">>> supplier.ui path:", ui_path)
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"Không tìm thấy UI file: {ui_path}")
        uic.loadUi(ui_path, self)

        # Setup window properties
        self.setWindowTitle("Supplier Management")
        self.setWindowIcon(QtGui.QIcon(icon_path))

        # Initialize UI components and data
        self.load_supplier_data()
        self.back_button.clicked.connect(self.goto_main)
        self.tableWidget.setSortingEnabled(True)
        self.search_input.textChanged.connect(self.search_supplier)

    def load_supplier_data(self):
        try:
            db = self.context.db_manager
            sql = """SELECT supplier_id, supplier_name, created_at, updated_at FROM supplier"""
            db.execute(sql)
            results = db.fetchall()

            # Configure table
            self.tableWidget.setRowCount(len(results))
            self.tableWidget.setColumnCount(len(db.execute(sql).description)+1)
            self.tableWidget.setColumnHidden(0, True)
            self.tableWidget.setColumnWidth(1, 300)  
            self.tableWidget.setColumnWidth(2, 150) 
            self.tableWidget.setColumnWidth(3, 150) 
            self.tableWidget.setColumnWidth(4, 200) 
            self.tableWidget.cellClicked.connect(self.handle_cell_click)

            column_count = self.tableWidget.columnCount()

            # Populate table data
            for row_idx, row_data in enumerate(results):
                supplier_id = row_data[0]  # Store for UserRole

                for col_idx in range(column_count):
                    if col_idx < len(row_data):
                        value = row_data[col_idx]
                        item = QTableWidgetItem(str(value))

                        # Format supplier name column
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
                        # Add "View Details" column
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

    def search_supplier(self):
        keyword = self.search_input.text().strip().lower()
        for row in range(self.tableWidget.rowCount()):
            name_item = self.tableWidget.item(row, 1)  # Supplier name column
            if name_item:
                name_text = name_item.text().lower()
                match = keyword in name_text
                self.tableWidget.setRowHidden(row, not match)

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

    def goto_main(self):
        self.main_window = Main_w(self.context)
        self.main_window.show()
        self.hide()

class SupplierInformation_w(QDialog):
    def __init__(self, context, supplier_id):
        super(SupplierInformation_w, self).__init__()
        self.context = context
        self.supplier_id_value = supplier_id

        # Load UI
        ui_path = os.path.join(current_dir, 'ui', 'supplier_information.ui')
        print(">>> supplier_information.ui' path:", ui_path)
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"Không tìm thấy UI file: {ui_path}")
        uic.loadUi(ui_path, self)

        # Setup window and components
        self.setWindowTitle("Supplier Management")
        self.setWindowIcon(QtGui.QIcon(icon_path))
        self.edit_mode = False
        self.pushButton.clicked.connect(self.toggle_edit_mode)
        self.load_supplier_data(self.supplier_id_value)
        
    def load_supplier_data(self, supplier_id_value):
        try:
            db = self.context.db_manager
            sql = """SELECT supplier_id, supplier_name, supplier_address,
                            contact_name, contact_phone, contact_email, payment_terms 
                        FROM supplier WHERE supplier_id = %s"""
            db.execute(sql, (supplier_id_value,))
            result = db.fetchone()

            if result:
                # Populate form fields
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

    def toggle_edit_mode(self):
        self.edit_mode = not self.edit_mode

        # Toggle form field editability
        self.supplier_name.setReadOnly(not self.edit_mode)
        self.supplier_address.setReadOnly(not self.edit_mode)
        self.contact_name.setReadOnly(not self.edit_mode)
        self.contact_phone.setReadOnly(not self.edit_mode)
        self.contact_email.setReadOnly(not self.edit_mode)
        self.comboBox_payment_terms.setEnabled(self.edit_mode)
        self.pushButton.setText("💾 Save" if self.edit_mode else "Edit...")

        if self.edit_mode:
            self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel)
            # Store original data for cancel operation
            self.original_data = {
                "name": self.supplier_name.text(),
                "address": self.supplier_address.toPlainText(),
                "contact": self.contact_name.text(),
                "phone": self.contact_phone.text(),
                "email": self.contact_email.text(),
                "payment": self.comboBox_payment_terms.currentText()
                }
            cancel_btn = self.buttonBox.button(QDialogButtonBox.StandardButton.Cancel)
            if cancel_btn:
                try:
                    cancel_btn.clicked.disconnect()
                except:
                    pass
                cancel_btn.clicked.connect(self.cancel_edit)
        else:
            self.save_supplier_data()
            self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok)

    def set_fields_editable(self, editable):
        self.supplier_id.setReadOnly(True)
        self.supplier_name.setReadOnly(not editable)
        self.supplier_address.setReadOnly(not editable)
        self.contact_name.setReadOnly(not editable)
        self.contact_phone.setReadOnly(not editable)
        self.contact_email.setReadOnly(not editable)
        self.comboBox_payment_terms.setEnabled(editable)

    def save_supplier_data(self):
        try:
            db = self.context.db_manager
            # Default to COD if payment terms empty
            payment = self.comboBox_payment_terms.currentText().strip() or "COD"
            sql = """UPDATE supplier SET
                    supplier_name = %s,
                    supplier_address = %s,
                    contact_name = %s,
                    contact_phone = %s,
                    contact_email = %s,
                    payment_terms = %s
                     WHERE supplier_id = %s"""
            values = (
                self.supplier_name.text(),
                self.supplier_address.toPlainText(),
                self.contact_name.text(),
                self.contact_phone.text(),
                self.contact_email.text(),
                payment,
                self.supplier_id.text()
            )

            db.execute(sql, values)
            db.commit()
            QMessageBox.information(self, "Thành công", "Đã lưu thông tin nhà cung cấp.")
            self.context.db_manager.log_action(self.context.staff_id, f"Cập nhật nhà cung cấp: {self.supplier_id.text()}")

        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Không thể lưu: {e}")

    def cancel_edit(self):
        if self.edit_mode:
            # Restore original data
            self.supplier_name.setText(self.original_data["name"])
            self.supplier_address.setPlainText(self.original_data["address"])
            self.contact_name.setText(self.original_data["contact"])
            self.contact_phone.setText(self.original_data["phone"])
            self.contact_email.setText(self.original_data["email"])
           
            idx = self.comboBox_payment_terms.findText(self.original_data["payment"])
            if idx >= 0:
                self.comboBox_payment_terms.setCurrentIndex(idx)

            # Return to view mode
            self.edit_mode = False
            self.set_fields_editable(False)
            self.pushButton.setText("Edit...")
            self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok)
            QMessageBox.information(self, "Hủy chỉnh sửa", "Thay đổi đã được hủy.")
            self.context.db_manager.log_action(self.context.staff_id, f"Hủy chỉnh sửa nhà cung cấp: {self.supplier_id.text()}")


# Customer Window
class Customer_w(QMainWindow):
    def __init__(self, context):
        super(Customer_w, self).__init__()
        self.context = context
        ui_path = os.path.join(current_dir, 'ui', 'customer.ui')
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"Không tìm thấy UI file: {ui_path}")
        uic.loadUi(ui_path, self)

        self.setWindowTitle("Customer Management")
        self.setWindowIcon(QtGui.QIcon(icon_path))
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        self.actionSave.triggered.connect(self.save_customer_data)
        self.tableWidget.cellClicked.connect(self.handle_cell_click)

        self.load_customer_data()

    def load_customer_data(self):
        try:
            db = self.context.db_manager
            sql = "SELECT customer_id, customer_name, customer_phone, customer_email FROM customer"
            db.execute(sql)
            results = db.fetchall()

            self.tableWidget.setRowCount(len(results))
            self.tableWidget.setColumnCount(5)
            self.tableWidget.setHorizontalHeaderLabels(["ID", "Name", "Phone", "Email", "Details"])
            self.tableWidget.setColumnHidden(0, True)

            for row_idx, row_data in enumerate(results):
                customer_id = row_data[0]
                for col_idx in range(4):
                    item = QTableWidgetItem(str(row_data[col_idx]))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    if col_idx == 1:
                        font = QFont()
                        font.setBold(True)
                        font.setUnderline(True)
                        item.setFont(font)
                        item.setData(Qt.ItemDataRole.UserRole, customer_id)
                    self.tableWidget.setItem(row_idx, col_idx, item)

                # Cột "View Details"
                detail_item = QTableWidgetItem("View Details")
                detail_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                detail_item.setData(Qt.ItemDataRole.UserRole, customer_id)
                self.tableWidget.setItem(row_idx, 4, detail_item)
        except Exception as e:
            print("Lỗi khi tải dữ liệu khách hàng:", e)

    def save_customer_data(self):
        try:
            name = self.lineEdit_Customer_Name.text()
            phone = self.lineEdit_Phone_Number.text()
            email = self.lineEdit_Contact_Person.text()

            sql = """INSERT INTO customer (customer_name, customer_phone, customer_email) VALUES (%s, %s, %s)"""
            self.context.db_manager.execute(sql, (name, phone, email))
            self.context.db_manager.commit()

            QMessageBox.information(self, "Thành công", "Khách hàng đã được thêm!")
            self.context.db_manager.log_action(self.context.staff_id, f"Thêm khách hàng: {name}")
            self.load_customer_data()
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Không thể lưu khách hàng: {e}")

    def handle_cell_click(self, row, column):
        if column == 1 or column == 4:
            item = self.tableWidget.item(row, column)
            customer_id = item.data(Qt.ItemDataRole.UserRole)
            self.show_customer_detail(customer_id)

    def show_customer_detail(self, customer_id):
        dialog = CustomerInformation_w(self.context, customer_id)
        dialog.exec()

class CustomerInformation_w(QDialog):
    def __init__(self, context, customer_id):
        super(CustomerInformation_w, self).__init__()
        self.context = context
        self.customer_id_value = customer_id

        ui_path = os.path.join(current_dir, 'ui', 'customer_information.ui')
        uic.loadUi(ui_path, self)
        self.setWindowTitle("Customer Details")
        self.setWindowIcon(QtGui.QIcon(icon_path))
        self.edit_mode = False

        self.pushButton.clicked.connect(self.toggle_edit_mode)
        self.load_customer_data(customer_id)

    def load_customer_data(self, customer_id):
        try:
            db = self.context.db_manager
            sql = """SELECT customer_id, customer_name, customer_phone, customer_email FROM customer WHERE customer_id = %s"""
            db.execute(sql, (customer_id,))
            result = db.fetchone()

            if result:
                self.customer_id.setText(str(result[0]))
                self.customer_name.setText(result[1])
                self.customer_phone.setText(result[2])
                self.customer_email.setText(result[3])
                self.set_fields_editable(False)
            else:
                QMessageBox.warning(self, "Thông báo", "Không tìm thấy khách hàng.")
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Không thể tải dữ liệu: {e}")

    def toggle_edit_mode(self):
        self.edit_mode = not self.edit_mode
        self.set_fields_editable(self.edit_mode)
        self.pushButton.setText("💾 Save" if self.edit_mode else "Edit...")

        if self.edit_mode:
            self.original_data = {
                "name": self.customer_name.text(),
                "phone": self.customer_phone.text(),
                "email": self.customer_email.text()
            }
            self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel)
            cancel_btn = self.buttonBox.button(QDialogButtonBox.StandardButton.Cancel)
            if cancel_btn:
                try:
                    cancel_btn.clicked.disconnect()
                except:
                    pass
                cancel_btn.clicked.connect(self.cancel_edit)
        else:
            self.save_customer_data()
            self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Close)

    def save_customer_data(self):
        try:
            sql = """UPDATE customer SET customer_name = %s, customer_phone = %s, customer_email = %s WHERE customer_id = %s"""
            values = (
                self.customer_name.text(),
                self.customer_phone.text(),
                self.customer_email.text(),
                self.customer_id.text()
            )
            self.context.db_manager.execute(sql, values)
            self.context.db_manager.commit()
            QMessageBox.information(self, "Thành công", "Đã cập nhật khách hàng.")
            self.context.db_manager.log_action(self.context.staff_id, f"Cập nhật khách hàng: {self.customer_id.text()}")
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Không thể cập nhật: {e}")

    def cancel_edit(self):
        self.customer_name.setText(self.original_data["name"])
        self.customer_phone.setText(self.original_data["phone"])
        self.customer_email.setText(self.original_data["email"])
        self.set_fields_editable(False)
        self.edit_mode = False
        self.pushButton.setText("Edit...")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Close)
        QMessageBox.information(self, "Đã hủy", "Chỉnh sửa đã được hủy.")

    def set_fields_editable(self, editable):
        self.customer_id.setReadOnly(True)
        self.customer_name.setReadOnly(not editable)
        self.customer_phone.setReadOnly(not editable)
        self.customer_email.setReadOnly(not editable)

# Staff Window - Done
class Staff_w(QMainWindow):
    def __init__(self, context):
        super(Staff_w, self).__init__()
        self.context = context
        ui_path = os.path.join(current_dir, 'ui', 'staff.ui')
        print(">>> staff.ui path:", ui_path)
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"Không tìm thấy UI file: {ui_path}")
        uic.loadUi(ui_path, self)
        self.setWindowTitle("Staff Management")
        self.setWindowIcon(QtGui.QIcon(icon_path))
        self.load_staff_data()
        self.back_button.clicked.connect(self.goto_main)
        self.tableWidget.setSortingEnabled(True)
        self.search_input.textChanged.connect(self.search_staff)

    def load_staff_data(self):
        try:
            db = self.context.db_manager
            sql= """SELECT staff_id, staff_name, staff_position, created_at, updated_at FROM staff"""
            db.execute(sql)
            results = db.fetchall()

            # Cập nhật TableWidget
            self.tableWidget.setRowCount(len(results))
            self.tableWidget.setColumnCount(len(db.execute(sql).description)+1)
            # self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
            self.tableWidget.setColumnWidth(0, 50)  
            self.tableWidget.setColumnWidth(1, 200)  
            self.tableWidget.setColumnWidth(2, 100) 
            self.tableWidget.setColumnWidth(3, 150) 
            self.tableWidget.setColumnWidth(4, 150) 
            self.tableWidget.setColumnWidth(5, 200) 
            self.tableWidget.cellClicked.connect(self.handle_cell_click)

            column_count = self.tableWidget.columnCount()

            for row_idx, row_data in enumerate(results):
                staff_id = row_data[0]  # Giữ lại để dùng UserRole

                for col_idx in range(column_count):
                    if col_idx < len(row_data):
                        value = row_data[col_idx]
                        item = QTableWidgetItem(str(value))

                        # Staff Name (hiển thị với underline)
                        if col_idx == 1 or col_idx == 2:
                            font = QFont()
                            item.setFont(font)
                            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                            item.setToolTip("Click để xem chi tiết nhân viên")
                            item.setData(Qt.ItemDataRole.UserRole, staff_id)

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
                        detail_item.setData(Qt.ItemDataRole.UserRole, staff_id)
                        detail_item.setToolTip("Click để xem chi tiết nhân viên")
                        self.tableWidget.setItem(row_idx, col_idx, detail_item)
        except Exception as e:
            print("Lỗi khi tải dữ liệu:", e)
    
    def show_staff_detail(self, staff_id):
        detail_dialog = StaffInformation_w(self.context, staff_id)
        detail_dialog.exec()

    def search_staff(self):
        keyword = self.search_input.text().strip().lower()
        for row in range(self.tableWidget.rowCount()):
            name_item = self.tableWidget.item(row, 2)  # Staff name column
            if name_item:
                name_text = name_item.text().lower()
                match = keyword in name_text
                self.tableWidget.setRowHidden(row, not match)

    def handle_cell_click(self, row, column):
        if column == 1 or column == 5:
            item = self.tableWidget.item(row, column)
            if item is None:
                print("Item not found")
                return
            staff_id = item.data(Qt.ItemDataRole.UserRole)
            if staff_id:
                print(f"Opening details for staff ID: {staff_id}")
                self.show_staff_detail(staff_id)
    def goto_main(self):
        self.main_window = Main_w(self.context)
        self.main_window.show()
        self.hide()

class StaffInformation_w(QDialog):
    def __init__(self, context, staff_id):
        super(StaffInformation_w, self).__init__()
        self.context = context
        self.staff_id_value = staff_id
        ui_path = os.path.join(current_dir, 'ui', 'staff_information.ui')
        print(">>> staff_information.ui' path:", ui_path)
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"Không tìm thấy UI file: {ui_path}")
        uic.loadUi(ui_path, self)
        self.setWindowTitle("Staff Management")
        self.setWindowIcon(QtGui.QIcon(icon_path))
        self.load_staff_data(self.staff_id_value)
        

    def load_staff_data(self, staff_id_value):
        try:
            db = self.context.db_manager
            sql = """SELECT staff_name, staff_id, staff_position,
                            staff_phone, staff_email, staff_salary, hire_date FROM staff WHERE staff_id = %s"""
            db.execute(sql, (staff_id_value,))
            result = db.fetchone()
            # print(f"Query result: {result}")

            # Đổi lại các trường
            self.staff_id.setText(str(result[1]))
            self.staff_name.setText(result[0] if result[0] else "")
            self.staff_position.setText(result[2] if result[2] else "")
            self.staff_phone.setText(result[3] if result[3] else "")
            self.staff_email.setText(result[4] if result[4] else "")
            self.staff_salary.setText(str(result[5]) if result[5] else "")
            self.hire_date.setText(str(result[6]) if result[6] else "")
            self.hire_date.setReadOnly(True)
            self.staff_email.setText(result[4] if result[4] else "")
            self.staff_email.setReadOnly(True)
            self.staff_salary.setText(str(result[5]) if result[5] else "")
            self.staff_salary.setReadOnly(True)
            self.hire_date.setText(str(result[6]) if result[6] else "")
            self.hire_date.setReadOnly(True)
        except Exception as e:
            print("Lỗi khi tải dữ liệu:", e)

# Medicine Window - Done
class Medicine_w(QMainWindow):
    """Main window for medicine management."""
    def __init__(self, context):
        super(Medicine_w, self).__init__()
        self.context = context

        # Load UI
        ui_path = os.path.join(current_dir, 'ui', 'medicine.ui')
        print(f">>> medicine.ui path: {ui_path}")
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"Không tìm thấy UI file: {ui_path}")
        uic.loadUi(ui_path, self)

        # Set window properties
        self.setWindowTitle("Medicine Management")
        self.setWindowIcon(QIcon(icon_path))
        self.back_button.clicked.connect(self.goto_main)

        # Connect signals
        self.tableWidget.cellClicked.connect(self.handle_cell_click)
        self.tableWidget.setSortingEnabled(True)
        self.search_input.textChanged.connect(self.search_supplier)

        # Load initial data
        self.load_medicine_data()

    def load_medicine_data(self):
        """Load and display medicine data in the table."""
        try:
            sql = """
                SELECT m.medicine_id, m.medicine_name, c.category_name, m.created_at, m.updated_at
                FROM medicine m
                JOIN category c ON m.category_id = c.category_id
            """
            cursor = self.context.db_manager.execute(sql)
            results = cursor.fetchall()

            if not results:
                print("No medicine data found")
                return

            # Setup table
            self.tableWidget.setRowCount(len(results))
            column_count = len(cursor.description) + 1  # +1 for "View Details" column
            self.tableWidget.setColumnCount(column_count)

            self.tableWidget.setHorizontalHeaderLabels([
                "ID", "Name", "Category", "Created At", "Updated At", "Details"
            ])

            # Set column widths
            self.tableWidget.setColumnWidth(0, 50)
            self.tableWidget.setColumnWidth(1, 200)
            self.tableWidget.setColumnWidth(2, 150)
            self.tableWidget.setColumnWidth(3, 150)
            self.tableWidget.setColumnWidth(4, 150)
            self.tableWidget.setColumnWidth(5, 150)

            # Populate table
            for row_idx, row_data in enumerate(results):
                medicine_id = row_data[0]

                for col_idx in range(column_count):
                    if col_idx < len(row_data):
                        value = row_data[col_idx]
                        item = QTableWidgetItem()

                        if col_idx == 0:
                            item.setData(Qt.ItemDataRole.DisplayRole, int(value))
                            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                        else:
                            item.setText(str(value))
                            if col_idx in [1, 2]:  # Name, Category
                                font = QFont()
                                item.setFont(font)
                                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                                item.setToolTip("Click để xem chi tiết thuốc")
                                item.setData(Qt.ItemDataRole.UserRole, medicine_id)

                        self.tableWidget.setItem(row_idx, col_idx, item)
                    else:
                        # "View Details" column
                        detail_item = QTableWidgetItem("View Details")
                        font = QFont()
                        font.setUnderline(True)
                        detail_item.setFont(font)
                        detail_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                        detail_item.setData(Qt.ItemDataRole.UserRole, medicine_id)
                        detail_item.setToolTip("Click để xem chi tiết thuốc")
                        self.tableWidget.setItem(row_idx, col_idx, detail_item)

            # ✅ Enable sorting after all data is loaded
            self.tableWidget.setSortingEnabled(True)

        except Exception as e:
            print(f"Lỗi khi tải dữ liệu thuốc: {e}")
    def search_supplier(self):
        keyword = self.search_input.text().strip().lower()

        for row in range(self.tableWidget.rowCount()):
            name_item = self.tableWidget.item(row, 1)  # Cột tên nhà cung cấp
            if name_item:
                name_text = name_item.text().lower()
                match = keyword in name_text
                self.tableWidget.setRowHidden(row, not match)


    def show_medicine_detail(self, medicine_id):
        """Open medicine detail dialog."""
        detail_dialog = MedicineInformation_w(self.context, medicine_id)
        detail_dialog.data_updated.connect(self.load_medicine_data)
        detail_dialog.exec()

    def handle_cell_click(self, row, column):
        """Handle click events on table cells."""
        # Open details when clicking on name or "View Details" column
        if column == 1 or column == 5:
            item = self.tableWidget.item(row, column)
            if item is None:
                print("Item not found")
                return

            medicine_id = item.data(Qt.ItemDataRole.UserRole)
            if medicine_id:
                print(f"Opening details for medicine ID: {medicine_id}")
                self.show_medicine_detail(medicine_id)

    def goto_main(self):
        self.main_window = Main_w(self.context)
        self.main_window.show()
        self.hide()

class MedicineInformation_w(QDialog):
    """Dialog window to display detailed information about a medicine."""
    def __init__(self, context, medicine_id):
        super(MedicineInformation_w, self).__init__()
        self.context = context
        self.medicine_id_value = medicine_id

        # Load UI
        ui_path = os.path.join(current_dir, 'ui', 'medicine_information.ui')
        print(f">>> medicine_information.ui path: {ui_path}")
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"Không tìm thấy UI file: {ui_path}")
        uic.loadUi(ui_path, self)

        # Set window properties
        self.setWindowTitle("Medicine Information")
        self.setWindowIcon(QIcon(icon_path))
        self.edit_mode = False
        self.deleteButton.clicked.connect(self.confirm_delete_medicine)
        self.pushButton.clicked.connect(self.toggle_edit_mode)
        self.deleteButton.setEnabled(False)
        # Load data
        self.load_medicine_data(self.medicine_id_value)
        data_updated = pyqtSignal()

    def load_medicine_data(self, medicine_id_value):
        try:
            db = self.context.db_manager
            sql = """
                SELECT m.medicine_id, m.medicine_name, m.generic_name, c.category_name, s.supplier_name,
                    m.batch_number, m.expiration_date, m.stock_quantity, m.unit_price, m.sale_price
                FROM medicine m
                JOIN category c ON m.category_id = c.category_id
                JOIN supplier s ON m.supplier_id = s.supplier_id
                WHERE m.medicine_id = %s
            """
            db.execute(sql, (medicine_id_value,))
            result = db.fetchone()

            if result:
                self.medicine_id.setText(str(result[0]))
                self.medicine_id.setReadOnly(True)
                self.medicine_name.setText(result[1])
                self.medicine_name.setReadOnly(True)
                self.generic_name.setText(result[2])
                self.generic_name.setReadOnly(True)
                self.category_name.setText(result[3])
                self.category_name.setReadOnly(True)
                self.supplier_name.setText(result[4])
                self.supplier_name.setReadOnly(True)
                self.batch_number.setText(result[5])
                self.batch_number.setReadOnly(True)

                if result[6]:  # expiration_date
                    self.expiration_date.setDate(result[6].date())
                    # self.expiration_date.setReadOnly(True)
                    self.expiration_date.setReadOnly(True)

                self.stock_quantity.setValue(result[7])
                self.stock_quantity.setEnabled(False)
                self.unit_price.setValue(float(result[8]))
                self.unit_price.setEnabled(False)
                self.sale_price.setValue(float(result[9]))
                self.sale_price.setEnabled(False)
            else:
                QMessageBox.warning(self, "Thông báo", "Không tìm thấy thông tin thuốc.")

        except Exception as e:
            print(f"Lỗi khi tải dữ liệu thuốc: {e}")
            QMessageBox.warning(self, "Lỗi", f"Không thể tải thông tin thuốc: {e}")
    def toggle_edit_mode(self):
        self.edit_mode = not self.edit_mode

        self.set_fields_editable(self.edit_mode)
        self.pushButton.setText("💾 Save" if self.edit_mode else "Edit...")
        self.deleteButton.setEnabled(self.edit_mode)


        if self.edit_mode:
            self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel)

            # ✅ Lưu dữ liệu ban đầu
            self.original_data = {
                "name": self.medicine_name.text(),
                "generic": self.generic_name.text(),
                "category": self.category_name.text(),
                "supplier": self.supplier_name.text(),
                "batch": self.batch_number.text(),
                "exp_date": self.expiration_date.date(),
                "quantity": self.stock_quantity.value(),
                "unit_price": self.unit_price.value(),
                "sale_price": self.sale_price.value()
            }

            cancel_btn = self.buttonBox.button(QDialogButtonBox.StandardButton.Cancel)
            if cancel_btn:
                try:
                    cancel_btn.clicked.disconnect()
                except:
                    pass
                cancel_btn.clicked.connect(self.cancel_edit)
        else:
            self.save_medicine_data()
            self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Close)


    def set_fields_editable(self, editable):
        self.medicine_name.setReadOnly(not editable)
        self.generic_name.setReadOnly(not editable)
        self.category_name.setReadOnly(True)   
        self.supplier_name.setReadOnly(True)
        self.batch_number.setReadOnly(not editable)

        self.expiration_date.setEnabled(editable)
        self.stock_quantity.setEnabled(editable)
        self.unit_price.setEnabled(editable)
        self.sale_price.setEnabled(editable)


    def save_medicine_data(self):
        try:
            db = self.context.db_manager

            sql = """
                UPDATE medicine SET
                    medicine_name = %s,
                    generic_name = %s,
                    batch_number = %s,
                    expiration_date = %s,
                    stock_quantity = %s,
                    unit_price = %s,
                    sale_price = %s
                WHERE medicine_id = %s
            """
            values = (
                self.medicine_name.text(),
                self.generic_name.text(),
                self.batch_number.text(),
                self.expiration_date.date().toString("yyyy-MM-dd"),
                self.stock_quantity.value(),
                self.unit_price.value(),
                self.sale_price.value(),
                self.medicine_id.text()
            )

            db.execute(sql, values)
            db.commit()
            QMessageBox.information(self, "Thành công", "Đã lưu thông tin thuốc.")
            self.context.db_manager.log_action(self.context.staff_id, f"Cập nhật thuốc: {self.medicine_id.text()}")

        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Không thể lưu: {e}")


    def cancel_edit(self):
        if self.edit_mode:
            self.medicine_name.setText(self.original_data["name"])
            self.generic_name.setText(self.original_data["generic"])
            self.category_name.setText(self.original_data["category"])
            self.supplier_name.setText(self.original_data["supplier"])
            self.batch_number.setText(self.original_data["batch"])
            self.expiration_date.setDate(self.original_data["exp_date"])
            self.stock_quantity.setValue(self.original_data["quantity"])
            self.unit_price.setValue(self.original_data["unit_price"])
            self.sale_price.setValue(self.original_data["sale_price"])

            self.set_fields_editable(False)
            self.edit_mode = False
            self.pushButton.setText("Edit...")
            self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Close)
            QMessageBox.information(self, "Hủy chỉnh sửa", "Thay đổi đã được hủy.")

    def confirm_delete_medicine(self):
        reply = QMessageBox.question(self,"Xác nhận xóa",
        "Bạn có chắc chắn muốn xóa thuốc này?",
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.delete_medicine()
            self.context.db_manager.log_action(self.context.staff_id, f"Xóa thuốc: {medicine_id}")


    def delete_medicine(self):
        try:
            db = self.context.db_manager
            sql = "DELETE FROM medicine WHERE medicine_id = %s"
            db.execute(sql, (self.medicine_id.text(),))
            db.commit()
            QMessageBox.information(self, "Thành công", "Đã xóa thuốc khỏi hệ thống.")
            self.data_updated.emit()  # Phát tín hiệu
            self.accept()             # Đóng dialog  # Đóng dialog sau khi xóa thành công
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Không thể xóa thuốc: {e}")

class MedicineInformationAdd_w(QDialog):

    def __init__(self, context, medicine_id):
        super(MedicineInformationAdd_w, self).__init__()
        self.context = context
        self.medicine_id_value = medicine_id

        # Load UI
        ui_path = os.path.join(current_dir, 'ui', 'medicine_information_add.ui')
        print(f">>> medicine_information.ui path: {ui_path}")
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"Không tìm thấy UI file: {ui_path}")
        uic.loadUi(ui_path, self)

        # Set window properties
        self.setWindowTitle("Medicine Information")
        self.setWindowIcon(QIcon(icon_path))
    """Dialog window to display detailed information about a medicine."""
    def __init__(self, context, medicine_id):
        super(MedicineInformation_w, self).__init__()
        self.context = context
        self.medicine_id_value = medicine_id

        # Load UI
        ui_path = os.path.join(current_dir, 'ui', 'medicine_information.ui')
        print(f">>> medicine_information.ui path: {ui_path}")
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"Không tìm thấy UI file: {ui_path}")
        uic.loadUi(ui_path, self)

        # Set window properties
        self.setWindowTitle("Medicine Information")
        self.setWindowIcon(QIcon(icon_path))

        # Load data
        self.load_medicine_data(self.medicine_id_value)
        
    def load_medicine_data(self, medicine_id_value):
        """Load and display medicine data from database."""
        try:
            db = self.context.db_manager
            sql = """SELECT m.medicine_id, m.medicine_name, c.category_name, m.created_at, m.updated_at
                        FROM medicine m
                        JOIN category c ON m.category_id = c.category_id
                        """
            db.execute(sql, (medicine_id_value,))
            result = db.fetchone()

            if result:
                self.medicine_name.setText(result[0] if result[0] else "")
                self.medicine_category.setText(result[1] if result[1] else "")
                self.created_at.setText(str(result[2]) if result[2] else "")
                self.updated_at.setText(str(result[3]) if result[3] else "")
            else:
                print(f"No data found for medicine ID: {medicine_id_value}")

        except Exception as e:
            print(f"Lỗi khi tải dữ liệu thuốc: {e}")

# Invoice Window
class Invoice_w(QMainWindow):
    def __init__(self, context):
        super(Invoice_w, self).__init__()
        self.context = context
        ui_path = os.path.join(current_dir, 'ui', 'invoice.ui')
        uic.loadUi(ui_path, self)
        self.setWindowTitle("Invoice Management")
        self.setWindowIcon(QtGui.QIcon(icon_path))
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        self.load_invoice_data()
        self.tableWidget.cellClicked.connect(self.handle_cell_click)

    def load_invoice_data(self):
        try:
            db = self.context.db_manager
            sql = "SELECT invoice_id, customer_id, total_amount, created_at FROM invoice"
            db.execute(sql)
            results = db.fetchall()
            self.tableWidget.setRowCount(len(results))
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderLabels(["Invoice ID", "Customer ID", "Total", "Created At"])

            for row_idx, row_data in enumerate(results):
                for col_idx, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.tableWidget.setItem(row_idx, col_idx, item)
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Không thể tải hóa đơn: {e}")

    def handle_cell_click(self, row, column):
        invoice_id_item = self.tableWidget.item(row, 0)
        if invoice_id_item:
            invoice_id = invoice_id_item.text()
            self.detail_dialog = InvoiceInformation_w(self.context, invoice_id)
            self.detail_dialog.exec()


class InvoiceInformation_w(QDialog):
    def __init__(self, context, invoice_id):
        super(InvoiceInformation_w, self).__init__()
        self.context = context
        self.invoice_id = invoice_id
        ui_path = os.path.join(current_dir, 'ui', 'invoice_information.ui')
        uic.loadUi(ui_path, self)
        self.setWindowTitle("Invoice Detail")
        self.setWindowIcon(QtGui.QIcon(icon_path))

        self.load_data()

    def load_data(self):
        try:
            db = self.context.db_manager
            sql = "SELECT * FROM invoice WHERE invoice_id = %s"
            db.execute(sql, (self.invoice_id,))
            result = db.fetchone()

            if result:
                self.lineEdit_invoice_id.setText(str(result[0]))
                self.lineEdit_customer_id.setText(str(result[1]))
                self.doubleSpinBox_total.setValue(result[2])
                self.dateEdit_created.setDate(result[3].date())
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi tải thông tin hóa đơn: {e}")



# Stock Window
class Stock_w(QMainWindow):
    def __init__(self, context):
        super(Stock_w, self).__init__()
        self.context = context
        ui_path = os.path.join(current_dir, 'ui', 'stock.ui')
        uic.loadUi(ui_path, self)
        self.setWindowTitle("Stock Management")
        self.setWindowIcon(QtGui.QIcon(icon_path))
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        self.load_stock_data()
        self.tableWidget.cellClicked.connect(self.handle_cell_click)

    def load_stock_data(self):
        try:
            db = self.context.db_manager
            sql = "SELECT stock_id, medicine_id, quantity, last_updated FROM stock"
            db.execute(sql)
            results = db.fetchall()
            self.tableWidget.setRowCount(len(results))
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderLabels(["Stock ID", "Medicine ID", "Quantity", "Updated At"])

            for row_idx, row_data in enumerate(results):
                for col_idx, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.tableWidget.setItem(row_idx, col_idx, item)
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Không thể tải dữ liệu kho: {e}")

    def handle_cell_click(self, row, column):
        stock_id_item = self.tableWidget.item(row, 0)
        if stock_id_item:
            stock_id = stock_id_item.text()
            self.detail_dialog = StockInformation_w(self.context, stock_id)
            self.detail_dialog.exec()


class StockInformation_w(QDialog):
    def __init__(self, context, stock_id):
        super(StockInformation_w, self).__init__()
        self.context = context
        self.stock_id = stock_id
        ui_path = os.path.join(current_dir, 'ui', 'stock_information.ui')
        uic.loadUi(ui_path, self)
        self.setWindowTitle("Stock Detail")
        self.setWindowIcon(QtGui.QIcon(icon_path))

        self.load_data()

    def load_data(self):
        try:
            db = self.context.db_manager
            sql = "SELECT * FROM stock WHERE stock_id = %s"
            db.execute(sql, (self.stock_id,))
            result = db.fetchone()

            if result:
                self.lineEdit_stock_id.setText(str(result[0]))
                self.lineEdit_medicine_id.setText(str(result[1]))
                self.spinBox_quantity.setValue(result[2])
                self.dateEdit_updated.setDate(result[3].date())
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi tải thông tin kho: {e}")


# Logs Window
class Logs_w(QMainWindow):
    def __init__(self, context):    
        super(Logs_w, self).__init__()
        self.context = context
        ui_path = os.path.join(current_dir, 'ui', 'logs.ui')
        print(">>> logs.ui path:", ui_path)
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"Không tìm thấy UI file: {ui_path}")
        uic.loadUi(ui_path, self)
        self.setWindowTitle("Logs Management")
        self.setWindowIcon(QtGui.QIcon(icon_path))
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
           # Load initial data
        self.load_log_data()

        # Connect signals
        self.tableWidget.setSortingEnabled(True)
        self.search_input.textChanged.connect(self.search_logs)

    def load_log_data(self):
        try:
            db = self.context.db_manager
            sql = """
                SELECT log_id, staff_id, action, log_time
                FROM activity_log
                ORDER BY log_time DESC
            """
            db.execute(sql)
            results = db.fetchall()

            self.tableWidget.setRowCount(len(results))
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderLabels(["Log ID", "Staff ID", "Action", "Timestamp"])
            self.tableWidget.setSortingEnabled(False)
            
            for row_idx, row_data in enumerate(results):
                for col_idx, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.tableWidget.setItem(row_idx, col_idx, item)

            self.tableWidget.setSortingEnabled(True)
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.setColumnWidth(2, 500) 
            self.tableWidget.setColumnWidth(3, 150) 
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Không thể tải log: {e}")
    def search_logs(self):
        keyword = self.search_input.text().strip().lower()

        for row in range(self.tableWidget.rowCount()):
            visible = False
            if col == 3:  
                item = self.tableWidget.item(row, col)
                if item and keyword in item.text().lower():
                    visible = True
                    break
            self.tableWidget.setRowHidden(row, not visible)


# Login Window - Done
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

        # Ẩn mật khẩu mặc định
        self.login_password.setEchoMode(QLineEdit.EchoMode.Password)

        # Tạo nút 👁
        self.toggle_pw_button = QToolButton(self.login_password)
        self.toggle_pw_button.setIcon(QIcon("icon/eye_closed.png"))  # đặt icon của bạn
        self.toggle_pw_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.toggle_pw_button.setStyleSheet("border: none; padding: 0px;")
        self.toggle_pw_button.setFixedSize(20, 20)
        self.toggle_pw_button.move(self.login_password.rect().right() - 24, 0)

        # Gắn click
        self.toggle_pw_button.clicked.connect(self.show_password_temporarily)

        # Tạo QTimer để ẩn sau 1 giây
        self.hide_pw_timer = QTimer(self)
        self.hide_pw_timer.setSingleShot(True)
        self.hide_pw_timer.timeout.connect(self.hide_password)

    def login(self):
        un = self.login_user.text()
        psw = self.login_password.text()
        try:
            db = self.context.db_manager
            sql = 'SELECT staff_id, staff_psw FROM staff WHERE staff_id = %s'
            db.execute(sql, (un,))
            result = db.fetchone()

            if result:
                stored_pw = result[1]

                try:
                    # Nếu là bcrypt → kiểm tra bằng checkpw
                    if bcrypt.checkpw(psw.encode('utf-8'), stored_pw.encode('utf-8')):
                        login_success = True
                    else:
                        login_success = False
                except ValueError:
                    # Nếu không phải bcrypt → so sánh trực tiếp
                    if psw == stored_pw:
                        login_success = True

                        # Tự động mã hóa lại mật khẩu cũ
                        new_hash = bcrypt.hashpw(psw.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                        db.execute("UPDATE staff SET staff_psw = %s WHERE staff_id = %s", (new_hash, un))
                        db.commit()
                        print("Đã tự động mã hóa lại mật khẩu cũ cho user:", un)
                    else:
                        login_success = False

                if login_success:
                    QMessageBox.information(self, "Login Success", "Đăng nhập thành công!")
                    self.context.staff_id = result[0]
                    self.main_window = Main_w(self.context, un)
                    self.context.db_manager.log_action(self.context.staff_id, "Đăng nhập hệ thống")
                    self.main_window.show()
                    self.close()
                else:
                    QMessageBox.warning(self, "Login Failed", "Sai tài khoản hoặc mật khẩu.")
        except mysql_db.Error as e:
            QMessageBox.critical(self, "Database Error", f"Lỗi kết nối CSDL: {str(e)}")

    def show_password_temporarily(self):
        self.login_password.setEchoMode(QLineEdit.EchoMode.Normal)
        icon_path = os.path.join(current_dir, "icon", "eye_open.png")
        self.toggle_pw_button.setIcon(QIcon(icon_path))

        # Start timer 1 giây để ẩn lại
        self.hide_pw_timer.start(1000)

    def hide_password(self):
        self.login_password.setEchoMode(QLineEdit.EchoMode.Password)
        icon_path = os.path.join(current_dir, "icon", "eye_closed.png")
        self.toggle_pw_button.setIcon(QIcon(icon_path))





    def keyPressEvent(self, event):
        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            self.login()

    def goto_register(self):
        self.register_window = Register_w(self.context)
        self.register_window.show()
        self.close()

# Register Window - Done
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
            self.context.db_manager.log_action(self.context.staff_id, f"Thêm nhân viên: {staff_id}")
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
    current_dir = os.path.dirname(os.path.abspath(__file__))
    icon_dir = os.path.join(current_dir, "icon")
    icon_file = "app_icon_dark.png" if darkdetect.isDark() else "app_icon_light.png"
    icon_path = os.path.join(icon_dir, icon_file)
    context = AppContext()
    app = QApplication(sys.argv)
    login_window = Login_w(context)
    login_window.show()
    sys.exit(app.exec())






















































