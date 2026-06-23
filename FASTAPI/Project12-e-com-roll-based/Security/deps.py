from fastapi import HTTPException,status,Depends
from jose import JWTError,ExpiredSignatureError,jwt
from fastapi.security import OAuth2PasswordBearer
import os


mysecuritykey=os.getenv("Mysecretekey")
algorithm=os.getenv("ALGORITHM")


outh2pass=OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_cur_user(token: str = Depends(outh2pass)):
    try:
        payload = jwt.decode(
            token,
            mysecuritykey,
            algorithms=[algorithm]
        )

        if "role" not in payload:
            raise HTTPException(
                status_code=401,
                detail="Invalid token structure: role missing"
            )

        return payload

    except ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Expired Token",
            headers={"WWW-Authenticate": "Bearer"}
        )

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Token Invalid",
            headers={"WWW-Authenticate": "Bearer"}
        )