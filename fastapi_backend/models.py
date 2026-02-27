# models.py
# SQLAlchemy models mapped to Django-created tables

from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from database import Base
from sqlalchemy.sql import func
from datetime import datetime
# Django table name: core_user
class User(Base):
    __tablename__ = "core_user"
    id = Column(Integer, primary_key=True)
    username = Column(String(150))
    email = Column(String(255))
    password = Column(String(255))
    role = Column(String(20))
    created_at = Column(DateTime)


class Course(Base):
    __tablename__ = "core_course"
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    description = Column(String(500))
    instructor_id = Column(Integer)
    is_premium = Column(Boolean)


class Enrollment(Base):
    __tablename__ = "core_enrollment"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    course_id = Column(Integer)


class Progress(Base):
    __tablename__ = "core_progress"
    id = Column(Integer, primary_key=True)
    enrollment_id = Column(Integer)
    completed_lessons = Column(Integer)
    progress_percent = Column(Float)


class Plan(Base):
    __tablename__ = "core_plan"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Float)
    duration_days = Column(Integer)


class Subscription(Base):
    __tablename__ = "core_subscription"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    plan_id = Column(Integer)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    status = Column(String(20))


class Payment(Base):
    __tablename__ = "core_payment"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    plan_id = Column(Integer)
    amount = Column(Float)
    payment_date = Column(DateTime)


class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    message = Column(String(500))
    is_read = Column(Boolean)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class ActivityLog(Base):
    __tablename__ = "analytics_activitylog"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    action_type = Column(String(100))
    action_detail = Column(String(500))
    created_at = Column(DateTime, default=datetime.utcnow)