# Django Email Authentication System

A simple **Email Authentication System** built with Python and Django. This project allows users to register and log in using their username or email address and password. It also provides secure session management through Django's built-in authentication system.

## 🚀 Features

- User Registration
- User Login
- Login using Username or Email Address
- Password Authentication
- Django Authentication System
- User Logout
- Dashboard after Successful Login
- Session Management
- Form Validation

## 🛠️ Technologies Used

- Python
- Django
- HTML5
- CSS3
- Bootstrap
- SQLite3

## 📂 Project Structure

```text
Email_Authentication/
│
├── myApp/
│   ├── migrations/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── admin.py
│   └── apps.py
│
├── templates/
│   ├── register.html
│   ├── login.html
│   └── dashboard.html
│
├── manage.py
├── db.sqlite3
└── README.md
```

## ⚙️ Installation and Setup

**Step 1: Clone the Repository**

```bash
git clone https://github.com/your-username/Email_Authentication.git
```

**Step 2: Navigate to the Project Folder**

```bash
cd Email_Authentication
```

**Step 3: Create a Virtual Environment**

```bash
python -m venv newEnv
```

**Step 4: Activate Virtual Environment**

Windows:

```bash
newEnv\Scripts\activate
```

**Step 5: Install Django**

```bash
pip install django
```

**Step 6: Apply Migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

**Step 7: Run the Development Server**

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## 🔐 Authentication Process

### 1. Registration
- Users can create an account using the registration form.
- Registration information is stored in the database.
- Django validates the submitted information.

### 2. Login
- Users can log in using their username or email address.
- The system checks the user's credentials.
- Django's `authenticate()` function verifies the password.
- After successful authentication, users are redirected to the dashboard.

### 3. Dashboard
- Users can access the dashboard after successful login.

### 4. Logout
- Users can securely log out of their accounts.
- After logout, users are redirected to the login page.

## 💻 Main Django Functions

| Function | Description |
|---|---|
| `register_view()` | Handles user registration |
| `login_view()` | Handles username/email login |
| `authenticate()` | Verifies user credentials |
| `login()` | Creates an authenticated session |
| `logout_view()` | Logs out the user |
| `dashboard()` | Displays the user dashboard |

## 🎯 Project Purpose

The main purpose of this project is to understand Django's authentication system and learn how to implement user registration, username/email-based login, password verification, and session management.

## 👨‍💻 Author

**Oren Michael Dessai**

BBA Student | Django Developer | Python Learner

---
