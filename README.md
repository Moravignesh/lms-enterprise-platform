# 📚 Learning Management & Subscription-Based Video Platform

---

## Project Overview

This project is a Multi-Panel Learning Platform built using:

- Django → Admin Panel  
- FastAPI → User Panel (REST APIs)  
- MySQL → Shared Database  

The system combines:

1. Learning Management System (LMS)
2. Subscription-Based Video Learning Platform

Both Django and FastAPI share the same MySQL database to ensure seamless integration between admin and user panels.

---

#  Architecture Overview

| Component       | Technology | Description |
|-----------------|------------|------------|
| Admin Panel     | Django     | Manage users, instructors, courses, plans, payments |
| User Panel      | FastAPI    | REST APIs for learners & instructors |
| Database        | MySQL      | Shared database |
| Authentication  | Django Auth + JWT | Admin login & API authentication |

---

# Project Structure

learning-platform/
│
├── django_admin/
│   ├── core/
│   ├── subscriptions/
│   ├── manage.py
│   ├── settings.py
│   └── requirements.txt
│
├── fastapi_user/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── auth.py
│   └── requirements.txt
│
├── learning_db.sql
├── learning_platform.postman_collection.json
├── docker-compose.yml
└── README.md

---

#  MODULE 1: Learning Management Platform

##  Goal

Build a system where:
- Admin manages users, instructors, courses & lessons
- Users browse & enroll in courses
- Track learning progress

---

##  LMS Database Models

- User (id, name, email, role, password_hash)
- Course (id, title, description, instructor_id, status)
- Lesson (id, course_id, title, content, video_url)
- Enrollment (id, user_id, course_id, enrolled_on)
- Progress (id, enrollment_id, completed_lessons, progress_percent)

---

## LMS FastAPI Endpoints

POST   /register/  
POST   /login/  
GET    /courses/  
GET    /courses/{id}  
POST   /enroll/  
POST   /progress/update/  
GET    /progress/view/  

---

# MODULE 2: Subscription-Based Video Learning Platform

# Goal

Extend LMS with:
- Paid subscription plans
- Premium course access
- Payment tracking
- Plan expiry logic

---

##  Subscription Database Models

- Plan (id, name, price, duration_days)
- Subscription (user_id, plan_id, start_date, end_date, status)
- Payment (user_id, plan_id, amount, payment_date)
- Course (is_premium field added)

---

##  Django Admin Panel Features

✔ Manage subscription plans (Basic, Pro, Enterprise)  
✔ Manage users (activate/deactivate)  
✔ View subscriptions  
✔ View payments  
✔ Manage premium courses  





##  FastAPI Subscription Endpoints

POST   /auth/register/  
POST   /auth/login/  
GET    /plans/  
POST   /subscribe/  
GET    /premium-courses/  
GET    /payments/  



---

#  JWT Authentication

1. Register user  
2. Login via /login/  
3. Copy access_token  
4. Authorize using:

Authorization: Bearer <your_token>

Protected APIs require valid JWT token.

---

#  Plan Expiry Logic

When subscribing:

end_date = start_date + duration_days

Premium course access allowed only if:

subscription.end_date >= current_date

Otherwise → 403 Forbidden

---

#  Shared MySQL Database

Database name:

learning_db

Example connection string:

mysql+pymysql://root:password@localhost:3306/learning_db

Important:
- Django manages migrations
- FastAPI does NOT create tables
- Both share same schema

---

#  Local Setup (Without Docker)

## 1️⃣ Clone Repository

git clone <your-github-link>  
cd learning-platform  

---

## 2️⃣ Create Virtual Environment

python -m venv venv  
venv\Scripts\activate  

---

## 3️⃣ Install Dependencies

### Django

cd django_admin  
pip install -r requirements.txt  

### FastAPI

cd ../fastapi_user  
pip install -r requirements.txt  

---

## 4️⃣ Setup MySQL

mysql -u root -p  

CREATE DATABASE learning_db;  

---

## 5️⃣ Run Django

cd django_admin  
python manage.py makemigrations  
python manage.py migrate  
python manage.py createsuperuser  
python manage.py runserver  


---

## 6️⃣ Run FastAPI

cd fastapi_user  
uvicorn main:app --reload --port 9000  






#  Docker Setup 

docker-compose up --build  

Run migrations:

docker exec -it django_admin python manage.py migrate  



#  Postman Collection

learning_platform.postman_collection.json  

Import into Postman to test APIs.

---

# Database Schema

learning_db.sql  

Import manually:

mysql -u root -p learning_db < learning_db.sql  

---

# Key Learning Outcomes

✔ Django + FastAPI Integration  
✔ Shared MySQL Architecture  
✔ JWT Authentication  
✔ Subscription Expiry Handling  
✔ Payment Tracking  
✔ RESTful API Design  

---

#  Deliverables Included

✔ Source Code (Django + FastAPI)  
✔ README.md  
✔ Database Schema  
✔ Postman Collection  
✔ Screenshots  
✔ Docker Setup  



#  Final Result

This platform successfully combines:

- Full Learning Management System  
- Subscription-Based Premium Learning  
- Admin Control Panel  
- JWT-Secured API Backend  
- Shared MySQL Architecture  
