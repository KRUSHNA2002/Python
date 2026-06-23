from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from Database.db import Base

class OrderModel(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship(
        "RegisterModel",
        back_populates="orders"
    )

    products = relationship(
        "ProductModel",
        back_populates="order",
        cascade="all, delete-orphan"
    )

    items = relationship(
        "ItemsModel",
        back_populates="order",
        cascade="all, delete-orphan"
    )