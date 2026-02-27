from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from database import SessionLocal
from models import User, Subscription, Course
from auth_utils import get_current_user

router = APIRouter(prefix="/analytics", tags=["Analytics"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/dashboard")
def admin_dashboard(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    # Optional: allow only admin
    if current_user.role != "ADMIN":
        return {"error": "Not authorized"}

    total_users = db.query(func.count(User.id)).scalar()
    total_courses = db.query(func.count(Course.id)).scalar()
    total_subscriptions = db.query(func.count(Subscription.id)).scalar()

    return {
        "total_users": total_users,
        "total_courses": total_courses,
        "total_subscriptions": total_subscriptions,
    }