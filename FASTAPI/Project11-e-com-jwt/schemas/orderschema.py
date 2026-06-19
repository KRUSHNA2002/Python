from pydantic import BaseModel

class OrderSchema(BaseModel):
    id: int
    user_id:int
    status: str

