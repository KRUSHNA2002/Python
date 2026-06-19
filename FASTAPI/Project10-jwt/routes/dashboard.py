from fastapi import APIRouter,Depends
from security.deps import get_current_user
from sqlalchemy.orm import Session
from database.config import get_db

router=APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

@router.get("/")
def get_cur_user(
    current_user:dict =Depends(get_current_user),
    db: Session = Depends(get_db)
):
    
    return {
        "message": "Dashboard Access Granted",
        "user": current_user
    }