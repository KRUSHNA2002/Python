from pydantic import BaseModel
from schemas.orderschema import OrderSchema

class userCreate(BaseModel):

    id:int
    name:str
    email:str
    password:str
    orders: list[OrderSchema] = []

    class Config:
        from_attributes = True