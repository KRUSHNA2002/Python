from pydantic import BaseModel, ConfigDict
from typing import List, Optional


class PostCreate(BaseModel):
    user_id: int
    title: str


class UserSchema(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    course: str
    posts: Optional[List[PostCreate]] = []

    model_config = ConfigDict(from_attributes=True)

