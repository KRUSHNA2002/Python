from pydantic import BaseModel

class ItemsSchema(BaseModel):
    id:int
    name:str
    order_id:int
    price:int
    quantity:int

    