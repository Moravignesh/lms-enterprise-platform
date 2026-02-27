LMS Enterprise Platform

Django Admin + FastAPI Backend + MySQL + Docker
Project Overview

This project is a full-stack Learning Management System (LMS) built using Django for the Admin Panel and FastAPI for the User API backend. Both services share a single MySQL database and are containerized using Docker.

The platform includes authentication, course management, subscription plans, payments, analytics dashboard, notifications system, and activity logging.

This system demonstrates enterprise-level backend architecture combining Django and FastAPI in one project.

Tech Stack

Django 4.x

FastAPI

SQLAlchemy

Pydantic

JWT Authentication

MySQL 8

Docker & Docker Compose

Chart.js (Analytics Dashboard)

Core Features

JWT Authentication (Register, Login, Token)

Role-Based Access (Student / Instructor)

Course Management

Subscription Plans

Payment Tracking

Activity Logging

In-App Notifications

Analytics Dashboard

Monthly Revenue Reports

Popular Course Tracking

Shared MySQL Database

Dockerized Multi-Service Architecture

Project Structure

The project contains two main services:

django_admin → Handles Admin Panel, Analytics, Reports, and Data Management

fastapi_backend → Handles API endpoints, authentication, subscriptions, notifications, and activity logs

Both connect to the same MySQL database defined in docker-compose.yml.

Running the Project (Docker – Recommended)

Make sure Docker Desktop is running.

From project root:

docker compose up --build

This will start:

MySQL database

Django server on port 8000

FastAPI server on port 8001

Access URLs:

Django Admin
http://localhost:8000/admin/

FastAPI Swagger
http://localhost:8001/docs

Creating Django Superuser

Run:

docker compose exec django_admin python manage.py createsuperuser

Then login at:

http://localhost:8000/admin/

Running Without Docker (Manual Setup)

Step 1 – Create Virtual Environment

python -m venv venv
venv\Scripts\activate

Step 2 – Install Dependencies

For Django:

cd django_admin
pip install -r requirements.txt

For FastAPI:

cd fastapi_backend
pip install -r requirements.txt

Step 3 – Run Django

cd django_admin
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 8000

Step 4 – Run FastAPI

cd fastapi_backend
uvicorn main:app --reload --port 8001

Authentication Endpoints (FastAPI)

POST /auth/register

POST /auth/login

POST /token

After login, use the JWT token in Swagger Authorize section:

Bearer <your_token>

Plans & Subscription

GET /plans

POST /subscribe

Features:

Activates subscription

Creates payment record

Updates revenue

Generates notification

Logs activity

Courses

GET /courses

GET /courses/{id}

POST /courses/create (Instructor)

Premium courses require active subscription.

Enrollment

POST /enroll

GET /my-courses

Triggers:

Notification creation

Activity logging

Progress

POST /progress/update

GET /progress/view

Tracks lesson completion and progress percentage.

Notifications

GET /notifications

POST /notifications/mark-read

Generated when:

User subscribes

User enrolls

Course updates

Plan nearing expiry

Activity Logging

POST /activity

Tracks:

Enrollment

Subscription purchase

Course views

Lesson completion

Analytics

GET /analytics/overview

GET /analytics/monthly

Analytics dashboard displays:

Total Users

Active Subscriptions

Monthly Revenue

Most Popular Course

Activity Trends

Database Models

User

Course

Plan

Subscription

Payment

Enrollment

Progress

Notification

ActivityLog

AnalyticsRecord

Postman Testing

Import postman.json file.

Testing Flow:

Register user

Login

Copy JWT token

Authorize in Swagger or Postman

Subscribe to a plan

Enroll in course

Check notifications

Verify analytics endpoints

Key Learning Outcomes

Django and FastAPI integration

JWT authentication implementation

Subscription-based content access

Revenue aggregation queries

Analytics dashboard integration

Activity tracking system

Notification system implementation

Docker multi-container setup

Enterprise LMS architecture design

Final Notes

Django manages the Admin Panel and Analytics Dashboard.

FastAPI handles high-performance API services.

MySQL is shared between both services.

Docker ensures consistent development and deployment environment.

The system is designed to simulate a production-ready LMS backend architecture.
