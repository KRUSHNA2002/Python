from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from Database.config import get_db
from Security.hashing import hash_password
from Security.hashing import verify_password
from Security.create_token import create_token
from Models.Register import RegisterModel
from Schemas.Register import RegisterSchema

router=APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    data:RegisterSchema,
    db:Session=Depends(get_db)
):
    user = RegisterModel(
        name=data.name,
        email=data.email,
        password=hash_password(data.password),
        role=data.role
    )

    db.add(user)
    db.commit()

    return {
        "msg":"User Added Succesfully",
        "data":user
    }


@router.post("/login")
def login(
    data:RegisterSchema,
    db:Session=Depends(get_db)
):
    user=db.query(RegisterModel).filter(RegisterModel.email==data.email).first()

    if not user:
        raise HTTPException(status_code=404,detail="User Not Found")
    
    if not verify_password(
        data.password,
        user.password
    ):
         raise HTTPException(status_code=401,detail="Invalid Password")       
    
    token=create_token(
         {
            "sub":user.email,
            "role":user.role
        }
    )
    
    return {
        "access_token":token,
        "type":"bearer",
        "data":user
    }