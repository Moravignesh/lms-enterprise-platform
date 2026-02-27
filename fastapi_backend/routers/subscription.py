from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Subscription
from datetime import datetime, timedelta

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/subscribe/")
def subscribe(user_id: int, plan_id: int, duration_days: int, db: Session = Depends(get_db)):
    start = datetime.utcnow()
    end = start + timedelta(days=duration_days)

    sub = Subscription(
        user_id=user_id,
        plan_id=plan_id,
        start_date=start,
        end_date=end,
        status="active",
    )

    db.add(sub)
    db.commit()
    db.refresh(sub)

    return sub