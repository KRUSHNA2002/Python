from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError,jwt,ExpiredSignatureError

Secrete_key="mysecretekey"
ALGORITHM="HS256"

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(token: str =Depends(oauth2_scheme)):
    try:
        payload=jwt.decode(
            token,
            Secrete_key,
            algorithms=[ALGORITHM]
        )

        return payload
    
    except ExpiredSignatureError:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token Expired",
            headers={"WWW-Authenticate":"bearer"}
        )
    
    except JWTError:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=" Inavalid Token",
            headers={"WWW-Authenticate":"bearer"}
        )