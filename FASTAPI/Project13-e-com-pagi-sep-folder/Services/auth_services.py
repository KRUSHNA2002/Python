from Reposetories.auth_repo import auth_data,login_data
from Models.Register import RegisterModel
from fastapi import HTTPException
from Security.hashing import verify_password


def authdata(data,db):

    exits=db.query(RegisterModel).filter(RegisterModel.email==data.email).first()

    if exits:

        raise HTTPException(status_code=400,detail="Email already exits")

    return auth_data(data,db)

def logindata(data,db):


    user=db.query(RegisterModel).filter(RegisterModel.email==data.email).first()

    if not user:
        raise HTTPException(status_code=404,detail="User Not Found")
    
    if not verify_password(
        data.password,
        user.password
    ):
         raise HTTPException(status_code=401,detail="Invalid Password") 
    

    return login_data(user)