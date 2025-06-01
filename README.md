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
│
├── MediManager.py          # Điểm bắt đầu chương trình
├── app_context.py          # Kết nối CSDL
├── constants.py            # Đường dẫn icon, query mẫu, v.v.
├── utils/
│   └── helpers.py          # Các hàm dùng chung (load_ui, logging)
├── services/
│   ├── db_service.py       # Đóng gói thao tác DB
│   └── report_service.py   # Xuất báo cáo
├── screens/
│   ├── main_window.py
│   ├── login.py
│   ├── register.py
│   ├── supplier.py
│   ├── customer.py
│   ├── staff.py
│   ├── medicine.py
│   ├── invoice.py
│   └── stock.py
├── ui/                     # Các file .ui
└── icons/                  # Các file icon


```
## 🧾 Các chức năng chính

- **Đăng nhập / Đăng ký** (Phân quyền: admin, manager, staff)
- **Quản lý thuốc**: thêm, sửa, xóa, chi tiết, lọc theo danh mục
- **Quản lý nhà cung cấp**
- **Quản lý khách hàng**
- **Quản lý nhân viên**
- **Hóa đơn**: tạo và theo dõi hóa đơn trong ngày
- **Tồn kho**: theo dõi tồn kho, thuốc sắp hết hạn
- **Lịch sử hoạt động**: log hành động người dùng
- **Báo cáo xuất file (đang phát triển)**: tổng tồn kho, hóa đơn, thuốc sắp hết hạn

---

## 🛠Cài đặt và chạy

### 1. Cài đặt thư viện cần thiết

```bash
pip install PyQt6 mysqlclient bcrypt darkdetect
```

### 2. Thiết lập MySQL qua XAMPP

> ⚠️ Bật MySQL từ XAMPP Control Panel (port mặc định 3306)  
> Sử dụng `localhost`, user `root`, và password như khai báo trong `DBManager.py`

### 3. Khởi chạy ứng dụng

```bash
python main.py
```

---

## Tài khoản mặc định

- `Username: admin`  
- `Password: admin`  
> Hệ thống sẽ tự động tạo tài khoản admin nếu chưa có.

---

## Đóng gói thành file .exe

Bạn có thể đóng gói ứng dụng thành `.exe` bằng `PyInstaller`.

### Bước 1: Cài đặt PyInstaller

```bash
pip install pyinstaller
```

### Bước 2: Đóng gói ứng dụng

```bash
pyinstaller --noconfirm --windowed --icon=icon/app_icon_dark.ico --add-data "ui;ui" --add-data "icon;icon" main.py
```

### Bước 3: Chạy ứng dụng

File `main.exe` nằm trong thư mục `dist/`. Chạy file này để sử dụng mà không cần Python.

> ⚠️ Đảm bảo đường dẫn `ui/` và `icon/` chính xác. Nếu dùng PySide6 có thể cần bổ sung `--hidden-import`.

---

## Cơ sở dữ liệu

Dữ liệu nằm trong schema `medimanager` với các bảng chính:
- `medicine`, `category`, `supplier`, `stock`, `stock_transaction`
- `invoice`, `invoice_detail`, `customer`
- `staff`, `activity_log`

SQL script mẫu: `medimanager.sql`

---

## Hướng phát triển tương lai

- Xuất báo cáo định dạng PDF
- Lọc báo cáo theo ngày/tháng/năm
- Tích hợp API / phiên bản mobile
- Giao diện hiện đại hơn

---

## Tác giả

**Trần Tiến Thạnh**  
MSSV: 20239253  
Đại học Bách khoa Hà Nội – Môn: PROJECT I
  


