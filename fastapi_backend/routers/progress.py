from fastapi import APIRouter

router = APIRouter()

@router.get("/progress/view/")
def view_progress():
    return {"message": "Progress view endpoint"}