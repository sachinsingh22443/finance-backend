#  Finance Data Processing Backend

##  Overview

This project is a backend system for managing financial data with role-based access control.

It allows different users (Admin, Analyst, Viewer) to interact with financial records based on their roles.

---

##  Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic

---

##  Project Structure

```
app/
 ├── models/
 ├── schemas/
 ├── routes/
 ├── utils/
 ├── main.py
 ├── database.py
```

---

##  Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-link>
cd finance-backend
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Setup PostgreSQL

Create database:

```
CREATE DATABASE finance_db;
```

Update database URL in `database.py`:

```
postgresql://username:password@localhost:5432/finance_db
```

### 5. Run server

```
uvicorn app.main:app --reload
```

Open Swagger:

```
http://127.0.0.1:8000/docs
```

---

##  Role-Based Access Control

| Role    | Permissions             |
| ------- | ----------------------- |
| Viewer  | Read-only access        |
| Analyst | Read + Dashboard access |
| Admin   | Full CRUD access        |

---

##  Features

### 👤 User Management

* Create users
* Assign roles
* Activate / deactivate users

---

###  Transaction Management

* Create transaction
* View transactions
* Update transaction
* Delete transaction
* Filter transactions

---

###  Dashboard APIs

* Total Income
* Total Expense
* Net Balance
* Category-wise summary
* Recent transactions
* Monthly trends

---

##  Assumptions

* Authentication is simulated using request headers (`x-role`)
* Roles are predefined: admin, analyst, viewer
* Categories are predefined using Enum

---

##  Improvements (Future Scope)

* JWT Authentication
* Pagination
* Search functionality
* Unit testing
* Frontend integration

---

##  Conclusion

This project demonstrates:

* Clean backend architecture
* Role-based access control
* Data aggregation and analytics
* Scalable API design
