# HUST_PROJECT-I

# MediManager – Quản lý thuốc và bán hàng

## Tổng quan

**MediManager** là ứng dụng desktop quản lý nhà thuốc được phát triển bằng Python (PyQt6) kết nối với cơ sở dữ liệu MySQL. Hệ thống cho phép:
- Quản lý thông tin thuốc, nhà cung cấp, khách hàng, nhân viên.
- Lập hóa đơn, theo dõi tồn kho.
- Báo cáo thuốc sắp hết hạn, nhật ký hoạt động.
- Phân quyền người dùng, đăng nhập và đăng ký tài khoản.

## Công nghệ sử dụng

| Thành phần        | Công nghệ             |
|-------------------|------------------------|
| Giao diện người dùng | PyQt6 (UI dạng `.ui`) |
| Cơ sở dữ liệu     | MySQL (MariaDB)       |
| ORM đơn giản      | Tự viết với MySQLdb   |
| Bảo mật mật khẩu  | bcrypt (hash)         |
| Báo cáo & UI nâng cao | PyQt + QTableWidget + QLabel + QTimer |

## Cơ sở dữ liệu

CSDL `medimanager` bao gồm các bảng chính:
- `medicine`, `category`, `supplier`, `stock`, `stock_transaction`
- `invoice`, `invoice_detail`, `customer`
- `staff` (có phân quyền admin, manager, staff), `activity_log`

SQL schema được lưu trong `medimanager.sql`.

## Sơ đồ quan hệ các thực thể
https://dbdiagram.io/d/PROJECT-I-MEDICINE-MANAGEMENT-67ef9cc94f7afba184576060?utm_source=dbdiagram_embed&utm_medium=bottom_open

## Cấu trúc thư mục

```
MediManager/
├── main.py              # Điểm khởi chạy chính
├── main_ui.py           # Generated UI từ main.ui (PySide)
├── DBManager.py         # Kết nối và thao tác cơ sở dữ liệu
├── ui/                  # Thư mục chứa các file giao diện .ui
├── icon/                # Icon dùng cho giao diện (app_icon_dark/light)
└── README.md            # (File này)
```

## Đăng nhập & Đăng ký

- Tài khoản mặc định:  
  `Username: admin`  
  `Password: admin`  
  Hệ thống sẽ tự tạo tài khoản admin nếu chưa có.

- Người dùng có thể đăng ký thêm tài khoản mới từ cửa sổ `Login`.

## Các chức năng chính

- **Đăng nhập / Đăng ký** người dùng
- **Quản lý thuốc:** thêm, sửa, xóa, chi tiết thuốc, lọc theo danh mục
- **Quản lý kho:** theo dõi tồn kho, thuốc sắp hết hạn
- **Hóa đơn:** tạo hóa đơn, xem danh sách hóa đơn trong ngày
- **Khách hàng / Nhà cung cấp / Nhân viên:** thêm, sửa, tìm kiếm
- **Lịch sử hoạt động:** ghi nhận mọi thao tác người dùng
- **Báo cáo xuất file (dự kiến):** tổng kho, hóa đơn trong ngày, thuốc sắp hết hạn

## 🛠️ Cách cài đặt và chạy

### 1. Cài thư viện cần thiết

```bash
pip install PyQt6 mysqlclient bcrypt darkdetect
```

### 2. Khởi chạy ứng dụng

```bash
python main.py
```

> ⚠️ Lưu ý: bạn cần bật MySQL thông qua XAMPP Control Panel (port mặc định 3306), sử dụng `localhost`, user `root`, và password như đã đặt trong `DBManager.py`.

### 3. Cấu hình kết nối database (nếu cần)

- Mặc định:
  ```python
  host='localhost'
  user='root'
  passwd='@Thanh070891'
  ```
- Có thể sửa trong `DBManager.py`

## 📊 Mở rộng trong tương lai

- Thêm chức năng **xuất báo cáo PDF**
- Lọc báo cáo theo ngày, tháng, năm
- Giao diện hiện đại hơn
- API kết nối bên ngoài hoặc bản Mobile

## Tác giả

**Trần Tiến Thạnh**  
MSSV: 20239253  
Đại học Bách khoa Hà Nội – Môn: Nhập môn Công nghệ phần mềm
  


