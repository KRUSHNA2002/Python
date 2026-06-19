

from fastapi import(
    APIRouter,
    Depends,
    HTTPException
)
from sqlalchemy.orm import Session
from models.user import usermodel
from schemas.auth_schema import RegisterSchema
from database.config import get_db

# for REGISTER ROUTE
from security.hashing import hash_password

# for LOGIN ROUTE
from security.jwt import create_token
from schemas.auth_schema import LoginSchema
from security.hashing import verify_password


router=APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    data:RegisterSchema,
    db:Session=Depends(get_db)
):
    
    user=db.query(usermodel).filter(usermodel.email==data.email).first()

    if user:
        raise HTTPException(status_code=404,detail="User Not found")
    
    new_user=usermodel(
        email=data.email,
        name=data.name,
        password=hash_password(data.password)
    )

    db.add(new_user)
    db.commit()


    return {
        "msg":"user Register Succesfully",
        "data":new_user
    }


@router.post("/login")
def login(
    data:LoginSchema,
    db:Session=Depends(get_db)
):
    
    user=db.query(usermodel).filter(usermodel.email==data.email).first()

    if not user:
        raise HTTPException(status_code=404,detail="User Not Found")
    
    if not verify_password(
        data.password,
        user.password
    ):
         
        raise HTTPException(status_code=401,detail="Wrong Password")
    
    token=create_token(
        {
            "sub":user.email
        }
    )

    return {
        "access_token":token,
        "type":"bearer",
        "data":user
    }

