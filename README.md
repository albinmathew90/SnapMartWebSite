# SnapMartWebSite

![Python](https://img.shields.io/badge/-Python-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/-Django-green?logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-blue?logo=postgresql&logoColor=white)
![Razorpay](https://img.shields.io/badge/-Razorpay-purple)

---

## 📝 Description

SnapMartWebSite is a secure Django-powered e-commerce platform built as part of a 48-hour technical assignment.  

The application demonstrates complete payment flow integration using Razorpay (Test Mode) with secure backend verification and PostgreSQL database management.

The system allows users to:

- Browse fixed products
- Add products to cart
- Select quantity
- Complete payment via Razorpay
- View paid orders instantly
- Download invoices

The project focuses on secure payment handling, prevention of double charges, and robust server-side validation before marking any order as paid.

---

## 🎯 Assignment Objectives Covered

- ✅ Django + PostgreSQL backend
- ✅ Razorpay Test Mode integration
- ✅ Secure signature verification
- ✅ Server-side payment validation
- ✅ Double charge / refresh protection
- ✅ Paid order visibility on same page
- ✅ Order status system (Processing / Shipped / Delivered)

---

## 🛠️ Tech Stack

- 🐍 Python 3.14
- 🌐 Django 6
- 🐘 PostgreSQL
- 💳 Razorpay (Test Mode)
- 🎨 HTML, CSS, JavaScript
- 🔐 Server-side Payment Verification

---

## 💳 Payment Architecture

### Secure Payment Flow

1. User selects products and quantity
2. Django creates Razorpay Order (Orders API)
3. Razorpay Checkout popup opens
4. After payment:
   - Signature verification is performed
   - Payment details are fetched from Razorpay server
   - Payment status is validated (`captured`)
   - Amount is verified against database
   - Order is marked as paid
5. Paid order appears in "My Orders" section

---

## 🔐 Security Implementation

✔ Razorpay Signature Verification  
✔ Server-side Payment Fetch Validation  
✔ Amount Matching Validation  
✔ Unique Razorpay Order ID  
✔ Double Charge Protection  
✔ Order marked paid only after validation  
✔ Cart cleared only after successful verification  

---

## 📦 Key Dependencies


1. Django: latest
2. razorpay: latest
3. psycopg2-binary: latest
4. python-dotenv: latest


---

📁 Project Structure
.
├── SnapMart_Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── orders
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_order_products_order_status.py
│   │   ├── 0003_alter_order_products.py
│   │   ├── 0004_wishlist.py
│   │   ├── 0005_alter_wishlist_user.py
│   │   ├── 0006_delete_wishlist.py
│   │   ├── 0007_alter_order_razorpay_payment_id.py
│   │   └── __init__.py
│   ├── models.py
│   ├── services.py
│   ├── static
│   │   └── orders
│   │       └── images
│   │           ├── 16pro.jpg
│   │           ├── Asus.jpg
│   │           ├── Lenovotab.jpg
│   │           ├── M4Ipad.jpg
│   │           ├── MacProM4.jpg
│   │           ├── Oneplus13.jpg
│   │           ├── TabS10.jpg
│   │           ├── Xps15.jpg
│   │           └── s25.jpg
│   ├── templates
│   │   └── orders
│   │       └── index.html
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
└── requirements.txt

---

## 🗃 Database Models

### Order Model

- razorpay_order_id (unique)
- razorpay_payment_id
- razorpay_signature
- amount
- products
- status
- is_paid
- created_at

---

## 🛠️ Development Setup

### 1️⃣ Python Setup

1. Install Python (v3.8+ recommended)
2. Create virtual environment:

python -m venv venv

3. Activate environment:
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`
4. Install dependencies:

pip install -r requirements.txt


---

### 2️⃣ Environment Variables Setup

Create a `.env` file in project root:


RAZORPAY_KEY_ID=your_test_key
RAZORPAY_KEY_SECRET=your_test_secret
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432


⚠️ `.env` is excluded from GitHub for security.

---

### 3️⃣ Database Setup


python manage.py makemigrations
python manage.py migrate


---

### 4️⃣ Run Server


python manage.py runserver


Open:


http://127.0.0.1:8000/


---

## 🔁 Double Charge Protection

Implemented using:

- Unique Razorpay order ID
- Payment status check before marking as paid
- Server-side validation before DB update
- Amount verification against Razorpay API

Prevents:
- Refresh-based duplicate charges
- Manual manipulation
- Re-submission attacks

---

## 📦 Features

- 🛒 Dynamic Cart System
- ❤️ Wishlist System
- 📦 My Orders Drawer
- 📄 Invoice Download
- 🏷 Order Status Badges
- 💳 Secure Payment Flow
- 🎨 Modern Responsive UI

---

## 👨‍💻 Author

**Albin Mathew**  
BCA Student   

---

## 👥 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Clone** your fork: `git clone https://github.com/albinmathew90/SnapMartWebSite.git`
3. **Create** a new branch: `git checkout -b feature/your-feature`
4. **Commit** your changes: `git commit -am 'Add some feature'`
5. **Push** to your branch: `git push origin feature/your-feature`
6. **Open** a pull request

---

## 📜 License

This project was built for academic/assignment purposes.




