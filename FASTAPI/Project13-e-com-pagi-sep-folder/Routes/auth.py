from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from Database.config import get_db
from Security.hashing import hash_password
from Security.hashing import verify_password
from Security.create_token import create_token
from Models.Register import RegisterModel
from Schemas.Register import RegisterSchema
from Services.auth_services import authdata,logindata

router=APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    data:RegisterSchema,
    db:Session=Depends(get_db)
):

  return authdata(data,db)

@router.post("/login")
def login(
    data:RegisterSchema,
    db:Session=Depends(get_db)
):


  return logindata(data,db)