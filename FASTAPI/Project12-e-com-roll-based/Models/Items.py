from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Database.db import Base

class ItemsModel(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price=Column(Integer)
    quantity=Column(Integer)

    order_id = Column(Integer, ForeignKey("orders.id"))

    order = relationship(
        "OrderModel",
        back_populates="items"
    )