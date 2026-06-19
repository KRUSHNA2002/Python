from jose import jwt
from datetime import (
    datetime,timedelta
)

SECRETE_KEY="mysecretekey"
ALGORITHM="HS256"

def create_token(data:dict):
    user_data=data.copy()

    expired=datetime.utcnow()+ timedelta(
        minutes=30
    )

    user_data.update(
        {"exp":expired}
    )

    token=jwt.encode(
        user_data,
        SECRETE_KEY,
        algorithm=ALGORITHM
    )

    return token