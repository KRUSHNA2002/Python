from sqlalchemy import Integer,String,Column
from Database.db import Base
from sqlalchemy.orm import relationship

class RegisterModel(Base):
        __tablename__ = "users"
        
        id=Column(
        Integer,
        primary_key=True,
        index=True
        )
        name=Column(
            String
        )
        email=Column(
            String,
            unique=True
        )
        password=Column(
            String
        )
        role=Column(
            String
        )

        orders = relationship(
        "OrderModel",
        back_populates="user",
        cascade="all, delete"
    )