from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import ActivityLog
from auth_utils import get_current_user

router = APIRouter(prefix="/activity", tags=["Activity"])


@router.post("/")
def log_activity(
    action_type: str,
    action_detail: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    new_activity = ActivityLog(
        user_id=current_user.id,
        action_type=action_type,
        action_detail=action_detail
    )

    db.add(new_activity)
    db.commit()

    return {"message": "Activity logged successfully"}