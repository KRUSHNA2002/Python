from jose import jwt 
from datetime import (
    datetime,timedelta
)
import os

Mysecretekey=os.getenv(
    "Mysecretekey"
)

Algorithm=os.getenv(
    "ALGORITHM"
)

def create_token(data:dict):

    user_data=data.copy()


    expired=datetime.utcnow()+timedelta(
        minutes=30
    )

    user_data.update(
        {"exp":expired}
    )

    token=jwt.encode(
        user_data,
        Mysecretekey,
        algorithm=Algorithm
        
    )

    return token