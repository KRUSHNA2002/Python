
from Reposetories.order_repo import getallorders,addtheorder,getoneuser
from fastapi import HTTPException

def add_order(data,db):

   return addtheorder(data,db)

def getall_order(db,user,skip:int=0,limit:int=5):
   
    if user["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="Not allowed to access these orders"
        )
   
    return getallorders(db,skip,limit)

def getone_user(user_id,db,user):

    
    if user["role"] != "admin" and user["id"] != user_id:
        raise HTTPException(
            status_code=403,
            detail="Not allowed to access these orders"
        )

    
    return getoneuser(
        user_id,
        db
    )