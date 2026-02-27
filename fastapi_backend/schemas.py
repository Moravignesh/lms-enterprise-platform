# schemas.py
# Pydantic request & response models

from pydantic import BaseModel, EmailStr
from typing import Optional

class RegisterSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str


class LoginSchema(BaseModel):
    username: str
    password: str


class CourseResponse(BaseModel):
    id: int
    title: str
    description: str
    is_premium: bool

    class Config:
        from_attributes = True


class SubscribeSchema(BaseModel):
    plan_id: int


class ProgressUpdateSchema(BaseModel):
    enrollment_id: int
    completed_lessons: int
    progress_percent: float


from pydantic import BaseModel
from datetime import datetime


class NotificationResponse(BaseModel):
    id: int
    message: str
    is_read: bool
    created_at: datetime

    class Config:
        from_attributes = True


class MarkReadSchema(BaseModel):
    notification_id: int