from fastapi import HTTPException,Depends,status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt,JWTError,ExpiredSignatureError


Secrete_key="mysecretekey"
AlGORITHM="HS256"

outh2_pass=OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token:str =Depends(outh2_pass)):

    try:
        payload=jwt.decode(
            token,
            Secrete_key,
            algorithms=[AlGORITHM]
        )

        return payload
    
    except ExpiredSignatureError :

        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Token Expired",headers={"WWW-Authenticated":"bearer"})
    
    except JWTError :

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid Token",headers={"WWW-Authenticated":"bearer"})
    