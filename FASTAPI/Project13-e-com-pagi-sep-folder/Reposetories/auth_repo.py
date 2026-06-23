from Models.Register import RegisterModel
from fastapi import HTTPException
from Security.hashing import hash_password,verify_password
from Security.create_token import create_token
def auth_data(data,db):

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

def login_data(user):
      
    
    token=create_token(
         {
            "id":user.id,
            "sub":user.email,
            "role":user.role
        }
    )
    
    return {
        "access_token":token,
        "type":"bearer",
        "data":user
    }