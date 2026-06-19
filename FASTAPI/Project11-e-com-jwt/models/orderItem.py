from sqlalchemy import Column,Integer,String,ForeignKey,Float
from database.db import BASE
from sqlalchemy.orm import relationship


class OrderItem(BASE):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True)

    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)

    order = relationship("OrderModel", back_populates="items")
    product = relationship("ProductModel", back_populates="order_items")