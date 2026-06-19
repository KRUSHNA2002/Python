from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session,joinedload
from models.user import UserModel
from database.config import get_db
from schemas.userschema import userCreate

router=APIRouter(
    prefix="/E_commerce",
    tags=["Users"]
)


@router.post("/")
def add_user(
    data:userCreate,
    db:Session=Depends(get_db)
):
    
  user=UserModel(      
        name=data.name,
        email=data.email
  )
  db.add(user)
  db.commit()
  db.refresh(user)

  return {
    "msg":"User Added Succesfully",
    "data":user
  }


@router.get("/")
def get_users(db:Session=Depends(get_db)):

  users=db.query(UserModel).options(joinedload(UserModel.orders)).all()
  
  return {
    "msg":"Users Fetched Succesfully",
    "data":users
  }
   
@router.put("/{user_id}")
def update_user(
  user_id:int,
  data:userCreate,
  db:Session=Depends(get_db)
):
  
  user=db.query(UserModel).filter(UserModel.id==user_id).first()

  if  not user:

    raise HTTPException(status_code=404,detail="User Not found")

    
  user.name=data.name
  user.email=data.email

  db.commit()
  db.refresh(user)

  return {
    "msg":"User Updated succesfuly",
    "data":user
  }

@router.delete("/{user_id}")
def delete_user(
  user_id:int,
  db:Session=Depends(get_db)
):
  
  user=db.query(UserModel).filter(UserModel.id==user_id).first()

  db.delete(user)
  db.commit()

  return {
    "msg":"User Deleted Succesfully"
  }