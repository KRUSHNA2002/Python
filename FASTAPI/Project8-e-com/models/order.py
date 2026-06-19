from sqlalchemy import Column,Integer,String,ForeignKey
from database.db import BASE
from sqlalchemy.orm import relationship


class OrderModel(BASE):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )


    status = Column(String)

    user = relationship(
        "UserModel",
        back_populates="orders"
    )

    items = relationship(
        "OrderItem",
        back_populates="order"
    )