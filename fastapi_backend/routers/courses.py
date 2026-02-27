from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Course

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/courses/")
def list_courses(db: Session = Depends(get_db)):
    return db.query(Course).all()

@router.get("/courses/{course_id}")
def course_detail(course_id: int, db: Session = Depends(get_db)):
    return db.query(Course).filter(Course.id == course_id).first()