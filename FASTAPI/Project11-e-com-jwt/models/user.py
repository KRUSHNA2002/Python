from sqlalchemy import Column,Integer,String
from database.db import BASE
from sqlalchemy.orm import relationship


class UserModel(BASE):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    orders = relationship(
        "OrderModel",
        back_populates="user"
    )