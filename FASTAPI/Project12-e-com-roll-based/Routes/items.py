from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Database.config import get_db
from Models.Items import ItemsModel
from Schemas.items import ItemsSchema
from Security.roles import allow_roles
router = APIRouter(
    prefix="/items", 
    tags=["Items"],
    dependencies=[Depends(allow_roles("admin"))]
    )

# ➕ ADD ITEM
@router.post("/")
def add_item(
    data: ItemsSchema,
    db: Session = Depends(get_db)
):
    item = ItemsModel(
        name=data.name,
        price=data.price,
        quantity=data.quantity,
        order_id=data.order_id
    )

    db.add(item)
    db.commit()
    db.refresh(item)

    return {
        "msg": "Item added successfully",
        "item": item
    }


# 📥 GET ITEMS
@router.get("/")
def get_items(db: Session = Depends(get_db)):
    items = db.query(ItemsModel).all()

    return {
        "msg": "Items fetched",
        "items": items
    }