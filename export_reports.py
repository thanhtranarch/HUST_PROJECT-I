from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import os

def export_stock_report(context):
    filename = f"report_stock_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    filepath = os.path.join("exports", filename)
    os.makedirs("exports", exist_ok=True)

    db = context.db_manager
    sql = """SELECT medicine_name, unit, stock_quantity, batch_number, sale_price FROM medicine"""
    db.execute(sql)
    results = db.fetchall()

    c = canvas.Canvas(filepath, pagesize=A4)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, 800, "📦 BÁO CÁO TỒN KHO")

    c.setFont("Helvetica", 10)
    y = 780
    headers = ["Tên thuốc", "Đơn vị", "Tồn kho", "Lô", "Giá bán"]
    for i, header in enumerate(headers):
        c.drawString(50 + i * 100, y, header)

    y -= 20
    for row in results:
        if y < 50:
            c.showPage()
            y = 800
        for i, value in enumerate(row):
            c.drawString(50 + i * 100, y, str(value))
        y -= 20

    c.save()
    return filepath

def export_invoice_report(context, date):
    filename = f"report_invoice_{date}.pdf"
    filepath = os.path.join("exports", filename)
    os.makedirs("exports", exist_ok=True)

    db = context.db_manager
    sql = """SELECT invoice_id, invoice_date, customer_id, total_amount, staff_id, payment_status 
             FROM invoice WHERE DATE(invoice_date) = %s"""
    db.execute(sql, (date,))
    results = db.fetchall()

    c = canvas.Canvas(filepath, pagesize=A4)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, 800, f"🧾 BÁO CÁO HÓA ĐƠN NGÀY {date}")

    c.setFont("Helvetica", 10)
    y = 780
    headers = ["ID", "Thời gian", "Khách", "Tổng", "Nhân viên", "Trạng thái"]
    for i, header in enumerate(headers):
        c.drawString(50 + i * 80, y, header)

    y -= 20
    for row in results:
        if y < 50:
            c.showPage()
            y = 800
        for i, value in enumerate(row):
            c.drawString(50 + i * 80, y, str(value))
        y -= 20

    c.save()
    return filepath

def export_expiry_warning_report(context):
    filename = f"report_expiring_meds_{datetime.now().strftime('%Y%m%d')}.pdf"
    filepath = os.path.join("exports", filename)
    os.makedirs("exports", exist_ok=True)

    db = context.db_manager
    sql = """
        SELECT medicine_name, stock_quantity, unit, batch_number, expiration_date,
               DATEDIFF(expiration_date, NOW()) AS days_left
        FROM medicine
        WHERE DATEDIFF(expiration_date, NOW()) <= 60
        ORDER BY expiration_date ASC
    """
    db.execute(sql)
    results = db.fetchall()

    c = canvas.Canvas(filepath, pagesize=A4)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, 800, "⏰ BÁO CÁO THUỐC SẮP HẾT HẠN")

    c.setFont("Helvetica", 10)
    y = 780
    headers = ["Tên thuốc", "SL", "Đơn vị", "Lô", "Hạn dùng", "Còn lại"]
    for i, header in enumerate(headers):
        c.drawString(50 + i * 80, y, header)

    y -= 20
    for row in results:
        if y < 50:
            c.showPage()
            y = 800
        for i, value in enumerate(row):
            c.drawString(50 + i * 80, y, str(value))
        y -= 20

    c.save()
    return filepath
