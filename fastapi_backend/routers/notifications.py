from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Notification
from schemas import NotificationResponse, MarkReadSchema
from auth_utils import get_current_user

router = APIRouter(prefix="/notifications", tags=["Notifications"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ✅ GET USER NOTIFICATIONS
@router.get("/", response_model=list[NotificationResponse])
def get_notifications(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    notifications = db.query(Notification).filter(
        Notification.user_id == current_user.id
    ).order_by(Notification.created_at.desc()).all()

    return notifications


# ✅ MARK AS READ
@router.post("/mark-read/")
def mark_notification_read(
    data: MarkReadSchema,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    notification = db.query(Notification).filter(
        Notification.id == data.notification_id,
        Notification.user_id == current_user.id
    ).first()

    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")

    notification.is_read = True
    db.commit()

    return {"message": "Notification marked as read"}