-- CREATE database pharmacy;
USE medimanager;

-- Table: supplier
-- CREATE TABLE supplier (
--     supplier_id INTEGER PRIMARY KEY,
--     suppier_name TEXT,
--     contact_name TEXT,
--     contact_phone TEXT,
--     contact_email TEXT,
--     suppier_address TEXT,
--     payment_terms TEXT,
--     created_at TIMESTAMP,
--     updated_at TIMESTAMP
-- );

-- Table: category
--  CREATE TABLE category (
-- 	category_id INTEGER PRIMARY KEY,
-- 	category_name TEXT,
-- 	category_description TEXT,
-- 	created_at TIMESTAMP,
-- 	update_at TIMESTAMP
-- );

-- Table: medicine
-- DROP TABLE 	medicine;
-- CREATE TABLE medicine (
--     medicine_id INTEGER PRIMARY KEY,
--     medicine_name TEXT,
--     generic_name TEXT,
--     brand_name TEXT,
--     supplier_id INTEGER,
--     category_id INTEGER,
--     unit_price DECIMAL,
--     sale_price DECIMAL,
--     stock_quantity INTEGER,
--     expiration_date TIMESTAMP,
--     batch_number TEXT,
--     created_at TIMESTAMP,
--     updated_at TIMESTAMP,
--     FOREIGN KEY (supplier_id) REFERENCES supplier(supplier_id),
--     FOREIGN KEY (category_id) REFERENCES category(category_id)
-- );

-- Table: staff
-- CREATE TABLE staff (
--     staff_id INTEGER PRIMARY KEY,
--     staff_psw TEXT,
--     first_name TEXT,
--     last_name TEXT,
--     position TEXT,
--     phone TEXT,
--     email TEXT,
--     salary DECIMAL,
--     hire_date TIMESTAMP,
--     created_at TIMESTAMP,
--     updated_at TIMESTAMP
-- );
-- ALTER TABLE staff
-- MODIFY staff_id VARCHAR(10);
-- INSERT INTO staff (
--     staff_id, staff_psw, first_name, last_name, position, phone, email, salary, hire_date, created_at, updated_at
-- ) VALUES
-- ('staff1', 'staff1', 'Nguyen', 'Van A', 'Quản lý', '0909123456', 'a@example.com', 15000000, '2022-01-01 08:00:00', NOW(), NOW()),
-- ('staff2', 'staff2', 'Tran', 'Thi B', 'Dược sĩ', '0909234567', 'b@example.com', 12000000, '2022-02-01 08:00:00', NOW(), NOW()),
-- ('staff3', 'staff3', 'Le', 'Van C', 'Dược sĩ', '0909345678', 'c@example.com', 11000000, '2022-03-01 08:00:00', NOW(), NOW()),
-- ('staff4', 'staff4', 'Pham', 'Thi D', 'Nhân viên bán thuốc', '0909456789', 'd@example.com', 10000000, '2022-04-01 08:00:00', NOW(), NOW()),
-- ('staff5', 'staff5', 'Hoang', 'Van E', 'Kế toán', '0909567890', 'e@example.com', 13000000, '2022-05-01 08:00:00', NOW(), NOW());

-- Table: customer
-- CREATE TABLE customer (
--     customer_id INTEGER PRIMARY KEY,
--     customer_name TEXT,
--     customer_phone VARCHAR(11),
--     customer_email TEXT,
--     created_at TIMESTAMP,
--     updated_at TIMESTAMP
-- );
-- Table: invoice
-- CREATE TABLE invoice (
--     invoice_id INTEGER PRIMARY KEY,
--     invoice_date TIMESTAMP,
--     customer_id INTEGER,
--     staff_id VARCHAR(10),
--     total_amount DECIMAL,
--     payment_status TEXT,
--     due_date TIMESTAMP,
--     created_at TIMESTAMP,
--     updated_at TIMESTAMP,
--     FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
--     FOREIGN KEY (staff_id) REFERENCES staff(staff_id)
-- );
-- Table: invoice_detail
CREATE TABLE invoice_detail (
    invoice_detail_id INTEGER PRIMARY KEY,
    invoice_id INTEGER,
    medicine_id INTEGER,
    quantity INTEGER,
    sale_price DECIMAL,
    total_price DECIMAL,
    FOREIGN KEY (invoice_id) REFERENCES invoice(invoice_id),
    FOREIGN KEY (medicine_id) REFERENCES medicine(medicine_id)
);
-- Table: stock_transaction
CREATE TABLE stock_transaction (
    transaction_id INTEGER PRIMARY KEY,
    medicine_id INTEGER,
    transaction_type TEXT,
    quantity INTEGER,
    transaction_date TIMESTAMP,
    staff_id VARCHAR(10),
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    FOREIGN KEY (medicine_id) REFERENCES medicine(medicine_id),
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id)
);
-- Table: stock_transaction_detail
-- CREATE TABLE stock_transaction_detail (
--     transaction_detail_id INTEGER PRIMARY KEY,
--     transaction_id INTEGER,
--     medicine_id INTEGER,
--     quantity INTEGER,
--     unit_price DECIMAL,
--     FOREIGN KEY (transaction_id) REFERENCES stock_transaction(transaction_id),
--     FOREIGN KEY (medicine_id) REFERENCES medicine(medicine_id)
-- );
-- Table: payment_method
-- CREATE TABLE payment_method (
--     payment_method_id INTEGER PRIMARY KEY,
--     name TEXT,
--     description TEXT,
--     created_at TIMESTAMP,
--     updated_at TIMESTAMP
-- );
-- INSERT INTO supplier (supplier_id, name, contact_name, contact_phone, contact_email, address, payment_terms, created_at, updated_at)
-- VALUES
-- (1, 'PharmaCo', 'John Doe', '0987654321', 'john.doe@pharmaco.com', '123 Pharma Street, District 1, HCMC', 'Net 30', '2023-01-01 10:00:00', '2023-01-01 10:00:00'),
-- (2, 'MediSupply', 'Alice Smith', '0912345678', 'alice.smith@medisupply.com', '456 Medical Avenue, District 3, HCMC', 'Net 45', '2023-02-15 09:00:00', '2023-02-15 09:00:00'),
-- (3, 'HealthCorp', 'Robert Johnson', '0976543210', 'robert.johnson@healthcorp.com', '789 Health Road, District 5, HCMC', 'Net 60', '2023-03-01 08:30:00', '2023-03-01 08:30:00'),
-- (4, 'WellMed', 'Linda Lee', '0923456789', 'linda.lee@wellmed.com', '101 Wellness Blvd, District 7, HCMC', 'Net 30', '2023-04-10 11:45:00', '2023-04-10 11:45:00');

-- INSERT INTO category (category_id, name, description, created_at, update_at)
-- VALUES
-- (1, 'Pain Relievers', 'Medications used to relieve pain', '2023-01-01 10:00:00', '2023-01-01 10:00:00'),
-- (2, 'Antibiotics', 'Medications used to treat bacterial infections', '2023-02-01 09:00:00', '2023-02-01 09:00:00'),
-- (3, 'Antihistamines', 'Medications used to relieve allergy symptoms', '2023-03-01 08:30:00', '2023-03-01 08:30:00'),
-- (4, 'Diabetes Medications', 'Medications for managing diabetes', '2023-04-01 11:30:00', '2023-04-01 11:30:00'),
-- (5, 'Cardiovascular Medications', 'Medications for treating heart and blood vessel conditions', '2023-05-01 10:45:00', '2023-05-01 10:45:00');
-- INSERT INTO medicine (medicine_id, name, generic_name, brand_name, supplier_id, category_id, unit_price, stock_quantity, expiration_date, batch_number, created_at, updated_at)
-- VALUES
-- (1, 'Paracetamol 500mg', 'Paracetamol', 'Panadol', 1, 1, 12000.00, 100, '2026-12-31 00:00:00', 'BATCH001', '2023-01-01 10:00:00', '2023-01-01 10:00:00'),
-- (2, 'Amoxicillin 500mg', 'Amoxicillin', 'Amoxil', 2, 2, 25000.00, 50, '2025-11-15 00:00:00', 'BATCH002', '2023-02-15 09:00:00', '2023-02-15 09:00:00'),
-- (3, 'Ibuprofen 200mg', 'Ibuprofen', 'Brufen', 1, 1, 15000.00, 200, '2026-08-20 00:00:00', 'BATCH003', '2023-03-01 08:30:00', '2023-03-01 08:30:00'),
-- (4, 'Cetirizine 10mg', 'Cetirizine', 'Zyrtec', 3, 3, 18000.00, 150, '2025-10-10 00:00:00', 'BATCH004', '2023-04-01 11:00:00', '2023-04-01 11:00:00'),
-- (5, 'Metformin 500mg', 'Metformin', 'Glucophage', 2, 4, 22000.00, 80, '2027-01-05 00:00:00', 'BATCH005', '2023-05-01 08:00:00', '2023-05-01 08:00:00'),
-- (6, 'Lisinopril 10mg', 'Lisinopril', 'Zestril', 4, 5, 30000.00, 40, '2026-07-01 00:00:00', 'BATCH006', '2023-05-10 10:30:00', '2023-05-10 10:30:00'),
-- (7, 'Simvastatin 20mg', 'Simvastatin', 'Zocor', 4, 5, 27000.00, 120, '2026-09-30 00:00:00', 'BATCH007', '2023-06-01 09:00:00', '2023-06-01 09:00:00'),
-- (8, 'Omeprazole 20mg', 'Omeprazole', 'Losec', 2, 3, 25000.00, 75, '2025-12-12 00:00:00', 'BATCH008', '2023-06-15 10:00:00', '2023-06-15 10:00:00'),
-- (9, 'Aspirin 81mg', 'Aspirin', 'Ecotrin', 1, 1, 10000.00, 200, '2026-03-15 00:00:00', 'BATCH009', '2023-07-01 11:30:00', '2023-07-01 11:30:00'),
-- (10, 'Azithromycin 250mg', 'Azithromycin', 'Zithromax', 3, 2, 35000.00, 30, '2025-08-01 00:00:00', 'BATCH010', '2023-07-10 14:00:00', '2023-07-10 14:00:00');

-- Tìm kiếm thuốc
-- SELECT * FROM Medicine WHERE name LIKE 'Aspirin 81mg';

-- Thuốc sắp hết hạn
-- SELECT * FROM medicine WHERE expiration_date <= CURDATE() + INTERVAL 100 DAY;
