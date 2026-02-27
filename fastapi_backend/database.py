# fastapi_backend/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:vignesh@mysql:3306/lms_db"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()
# ✅ THIS MUST EXIST
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()