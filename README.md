# Gas Utility Service Management API

## 📌 Features
- Customers can **create service requests** with details and file attachments.
- Customers can **track request status** (Pending, In Progress, Resolved).
- Support representatives can **update and manage service requests**.
- RESTful API with **GET, POST, PUT, DELETE** endpoints.
- Uses `.env` for environment variables & security.
- Docker support for easy deployment.

---


## 📦 Installation & Setup

### 1️⃣ Clone the Repository

git clone <url>


### 2️⃣ Set Up a Virtual Environment
python -m venv venv source venv/bin/activate # On macOS/Linux venv\Scripts\activate # On Windows


### 3️⃣ Install Dependencies
pip install -r requirements.txt


### 4️⃣ Create .env File
touch .env # macOS/Linux echo > .env # Windows

Add the following inside `.env`:
SECRET_KEY="your-django-secret-key" DEBUG=True


### 5️⃣ Apply Migrations
python manage.py migrate

### 6️⃣ Run the Development Server
python manage.py runserver

- **API Base URL:** `http://127.0.0.1:8000/`
- **Django Admin Panel:** `http://127.0.0.1:8000/admin/`

---

## 🚀 API Endpoints

### Customer Management
| Method | Endpoint                 | Description           |
|--------|--------------------------|-----------------------|
| GET    | `/api/customers/`         | List all customers   |
| POST   | `/api/customers/`         | Create a new customer |
| GET    | `/api/customers/{id}/`    | Retrieve a customer  |
| PUT    | `/api/customers/{id}/`    | Update customer details |
| DELETE | `/api/customers/{id}/`    | Delete a customer    |

### Service Requests
| Method | Endpoint                          | Description             |
|--------|-----------------------------------|-------------------------|
| GET    | `/api/service-requests/`         | List all service requests |
| POST   | `/api/service-requests/`         | Create a new request    |
| GET    | `/api/service-requests/{id}/`    | Retrieve a request      |
| PUT    | `/api/service-requests/{id}/`    | Update request status   |
| DELETE | `/api/service-requests/{id}/`    | Delete a request        |

Test API in the browser: `http://127.0.0.1:8000/api/`

---




