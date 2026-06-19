from sqlalchemy import Column,Integer,String,ForeignKey,Float
from database.db import BASE
from sqlalchemy.orm import relationship


class ProductModel(BASE):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name=Column(String)
    price = Column(Float)
    stock = Column(Integer)

    order_items = relationship(
        "OrderItem",
        back_populates="product"
    )