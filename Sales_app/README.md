# Django Modular REST API

A clean, modular Django REST API for managing customers and orders. Demonstrates JWT authentication, MySQL integration, signals, permissions, and query optimization.

---

## Features

- Modular apps per domain (`customers`, `orders`, `users`)
- REST API endpoints with Django REST Framework (DRF)
- JWT authentication (SimpleJWT)
- Staff-only permissions for sensitive actions
- Signals for order creation events
- Optimized queries and filtering
- Admin panel with customizations

---

## Project Structure

project_root/
├── customers/ # Customer management
├── orders/ # Order management & signals
├── users/ # Authentication & JWT
├── common/ # Shared utilities & permissions
├── config/ # Django settings & URLs
├── manage.py
├── requirements.txt
└── README.md

---

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/django-modular-rest-api.git
cd django-modular-rest-api

# Create a virtual environment
python -m venv venv
# Activate it
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Start the development server
python manage.py runserver

---

## API Endpoints

### Authentication

- **POST** `/api/token/` → Get JWT access & refresh token  
- **POST** `/api/token/refresh/` → Refresh access token  

### Customers

- **GET** `/api/customers/` → List customers  
- **POST** `/api/customers/` → Create customer  
- **DELETE** `/api/customers/{id}/` → Delete customer (staff only)  

### Orders

- **GET** `/api/orders/` → List orders (newest first)  
- **POST** `/api/orders/` → Create order  
- **GET** `/api/orders/?start_date=&end_date=` → Filter by date range  

> **Note:** Include `Authorization: Bearer <access_token>` header for all requests.

---

## Signals

- Order creation triggers a signal that logs the customer’s name in the console.

---

## Permissions

- All endpoints require authentication  
- Staff-only deletion for customers  
- Permissions are reusable via the `common` module

---

## Tech Stack

- Python  
- Django  
- Django REST Framework  
- SimpleJWT for JWT authentication  
- MySQL for database backend

---

## Author

**Faith Muronji** — Backend Engineer | Django | Junior Cybersecurity Engineer | DevSecOps

