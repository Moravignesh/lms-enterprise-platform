from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models import User
from schemas import RegisterSchema, LoginSchema
from dependencies import get_db
from auth_utils import hash_password, verify_password, create_access_token
from datetime import datetime

router = APIRouter()


# ============================
# REGISTER USER
# ============================
@router.post("/register/")
def register(data: RegisterSchema, db: Session = Depends(get_db)):
    # Check if username already exists
    existing_user = db.query(User).filter(User.username == data.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    # Hash password
    hashed_password = hash_password(data.password)

    # Create user
    user = User(
    username=data.username,
    email=data.email,
    password=hashed_password,
    role=data.role,
    created_at=datetime.utcnow()
)
    

    db.add(user)
    db.commit()
    db.refresh(user)

    return {"message": "User created successfully"}


# ============================
# LOGIN USER
# ============================
@router.post("/login/")
def login(data: LoginSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == data.username).first()

    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.username})

    return {
        "access_token": token,
        "token_type": "bearer"
    }