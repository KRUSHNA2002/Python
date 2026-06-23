from pydantic import BaseModel

class RegisterSchema(BaseModel):
    id:int
    name:str
    email:str
    password:str
    role:str
    