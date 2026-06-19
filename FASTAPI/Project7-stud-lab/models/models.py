from sqlalchemy.orm import relationship
from database.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    course = Column(String)

    posts = relationship(
        "Post",
        back_populates="owner",
        cascade="all, delete"
    )


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String)

    owner = relationship("User", back_populates="posts")