from jose import jwt
from datetime import (
    datetime,
    timedelta
)


Secrete_key="mysecretekey"
ALGORITHM="HS256"

def create_token(data:dict):

    user_data=data.copy()

    expired=datetime.utcnow()+ timedelta(
        minutes=2
    )


    user_data.update(
       { "exp":expired}
    )


    token=jwt.encode(
        user_data,
        Secrete_key,
        algorithm=ALGORITHM
    )


    return token