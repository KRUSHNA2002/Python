from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from Security.deps import get_cur_user
from Models.Order import OrderModel
from Schemas.order import OrderSchema
from Database.config import get_db
from Security.roles import allow_roles

from Services import order_service

router=APIRouter(
    prefix="/orders",
    tags=["Orders"],

)

@router.post("/")
def add_order(
    data: OrderSchema,
    db: Session = Depends(get_db),
    user=Depends(allow_roles("admin"))
):

   return order_service.add_order(data,db)

@router.get("/")
def get_order(
    user=Depends(get_cur_user),
    db: Session = Depends(get_db),
    skip:int=0,limit:int=5
):



    return order_service.getall_order(db,user,skip,limit)

@router.get("/{user_id}")
def get_order(
    user_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_cur_user)
):

   return order_service.getone_user(user_id,db,user)