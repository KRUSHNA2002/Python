from pydantic import BaseModel

class OrderSchema(BaseModel):
    id:int
    name:str
    user_id:int


    