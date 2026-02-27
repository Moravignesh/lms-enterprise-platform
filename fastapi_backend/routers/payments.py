from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Payment

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/payments/")
def payment_history(user_id: int, db: Session = Depends(get_db)):
    return db.query(Payment).filter(Payment.user_id == user_id).all()