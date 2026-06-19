from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from models.user import UserModel
from schemas.userschema import userCreate
from security.createtoken import create_token
from security.hashing import verify_password,hash_password
from database.config import get_db



router = APIRouter(
    prefix="/auth",
    tags=["Authenticated"]
)


@router.post("/register")
def register(
    data:userCreate,
    db:Session=Depends(get_db)
):

    user = UserModel(
        name=data.name,
        email=data.email,
        password=hash_password(data.password)

    )

    db.add(user)
    db.commit()

    return {
        "msg":"USER ADDED succesfully",
        "data":user
    }




@router.post("/login")
def login(
    data:userCreate,
    db:Session=Depends(get_db)
):
    
    user=db.query(UserModel).filter(UserModel.email==data.email).first()

    if not user:
        raise HTTPException(status_code=404,detail="User Not FOUND")
    
    if not verify_password(
        data.password,
        user.password
    ):
        raise HTTPException(status_code=401,detail="Invalid Password")
    

    token=create_token(
        {
            "sub":user.email
        }
    )

    return {
        "token":token,
        "type":"bearer",
        "data":data
    }