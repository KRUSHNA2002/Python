from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from Security.deps import get_cur_user
from Models.Order import OrderModel
from Schemas.order import OrderSchema
from Database.config import get_db
from Security.roles import allow_roles

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

    order = OrderModel(
        user_id=data.user_id,
        name=data.name
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    return {
        "msg": "Order added Successfully",
        "order": order
    }

@router.get("/")
def get_order(
    user=Depends(get_cur_user),
    db: Session = Depends(get_db)
):

    if user["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="Not allowed to access these orders"
        )

    orders = db.query(OrderModel).all()

    return {
        "msg": "Fetched Orders",
        "orders": orders
    }

@router.get("/{user_id}")
def get_order(
    user_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_cur_user)
):

    if user["role"] != "admin" and user["id"] != user_id:
        raise HTTPException(
            status_code=403,
            detail="Not allowed to access these orders"
        )

    orders = db.query(OrderModel).filter(
        OrderModel.user_id == user_id
    ).all()

    return {
        "msg": "Fetched Orders",
        "orders": orders
    }