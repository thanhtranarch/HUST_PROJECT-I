from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import datetime

def export_daily_report(self):
    filename = f"Daily_Report_{datetime.date.today()}.pdf"
    try:
        db = self.context.db_manager
        db.execute("SELECT medicine_name, stock_quantity, unit, sale_price FROM medicine")
        results = db.fetchall()

        c = canvas.Canvas(filename, pagesize=A4)
        c.setFont("Helvetica", 14)
        c.drawString(50, 800, f"📋 Báo Cáo Tồn Kho - {datetime.date.today()}")

        y = 760
        c.setFont("Helvetica", 10)
        c.drawString(50, y, "Tên thuốc")
        c.drawString(200, y, "Số lượng")
        c.drawString(300, y, "Đơn vị")
        c.drawString(400, y, "Giá bán")

        for row in results:
            y -= 20
            if y < 100:
                c.showPage()
                y = 800
            c.drawString(50, y, str(row[0]))
            c.drawString(200, y, str(row[1]))
            c.drawString(300, y, str(row[2]))
            c.drawString(400, y, str(row[3]))

        c.save()
        QMessageBox.information(self, "Thành công", f"Đã xuất báo cáo ra {filename}")
    except Exception as e:
        QMessageBox.warning(self, "Lỗi", f"Không thể xuất báo cáo: {e}")
