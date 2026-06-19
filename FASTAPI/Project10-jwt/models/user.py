from sqlalchemy import Integer, Column, String,ForeignKey
from database.db import BASE

class usermodel(BASE):

    __tablename__="users"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email=Column(String,unique=True)
    password=Column(String)