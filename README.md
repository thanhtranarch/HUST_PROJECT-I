# HUST_PROJECT-I

# Pharmacy Management App

Ứng dụng quản lý thuốc cơ bản viết bằng Python và PyQt6, hỗ trợ các chức năng:

- Quản lý tồn kho thuốc
- Theo dõi hóa đơn bán hàng trong ngày
- Quản lý thuốc sắp hết hạn
- In báo cáo cuối ngày
- Giao diện đồ họa đơn giản, dễ sử dụng

## Giao diện

Xem ảnh giao diện trong thư mục `screenshot/`.

## Công nghệ sử dụng

- Python 3.x
- PyQt6
- MySQL

## Cách chạy ứng dụng

### 1. Cài đặt thư viện

```
pip install PyQt6
```
### 2. Thiết kế UI trên Qt Designer

### 3. Load UI
```
class Login_w(QMainWindow):
    def __init__(self):
        super(Login_w,self).__init__()
        uic.loadUi(ui_path, self)
```

## Cấu trúc thư mục

```
MediManager/
├── main.py              # Tập tin khởi động ứng dụng
├── main.ui              # Giao diện thiết kế bằng Qt Designer
├── main_ui.py           # Giao diện chuyển từ .ui (nếu dùng)
├── assets/              # Hình ảnh, icon
├── screenshot/          # Ảnh chụp giao diện
└── README.md
```

## Các chức năng chính

- [x] Xem danh sách thuốc tồn kho
- [x] Hiển thị danh sách hóa đơn trong ngày
- [x] Thêm/Xem chi tiết hóa đơn
- [x] Thống kê thuốc sắp hết hạn
- [x] In báo cáo ngày

## Gợi ý phát triển tiếp

- Thêm chức năng tìm kiếm thuốc
- Lưu dữ liệu vào SQLite hoặc MySQL
- Tạo form đăng nhập phân quyền (admin/nhân viên)
- Xuất báo cáo sang Excel/PDF
  
## Sơ đồ quan hệ các thực thể
https://dbdiagram.io/d/PROJECT-I-MEDICINE-MANAGEMENT-67ef9cc94f7afba184576060?utm_source=dbdiagram_embed&utm_medium=bottom_open

## Tác giả

TRẦN TIẾN THẠNH – HUST - PROJECT I

