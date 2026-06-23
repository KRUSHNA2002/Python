from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Database.config import get_db
from Models.Items import ItemsModel
from Schemas.items import ItemsSchema
from Security.roles import allow_roles
from Services import items_service

router = APIRouter(
    prefix="/items", 
    tags=["Items"],
    dependencies=[Depends(allow_roles("admin"))]
    )

@router.post("/")
def add_item(
    data: ItemsSchema,
    db: Session = Depends(get_db)
):

  return items_service.additems(data,db)


@router.get("/")
def get_items(db: Session = Depends(get_db),skip:int=0,limit:int=5):
    
   return items_service.getitems(db,skip,limit)