from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Database.db import Base

class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    order_id = Column(Integer, ForeignKey("orders.id"))


    order = relationship(
        "OrderModel",
        back_populates="products"
    )