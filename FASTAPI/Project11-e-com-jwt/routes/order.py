from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session,joinedload
from models.order import OrderModel
from models.user import UserModel
from models.product import ProductModel
from models.orderItem import OrderItem
from database.config import get_db
from schemas.orderschema import OrderSchema
from schemas.orderitemschema import OrderItemSchema
from security.deps import get_current_user

router=APIRouter(
    prefix="/E_commerce",
    tags=["Orders"],
    dependencies=[Depends(get_current_user)]
)


@router.post("/order")
def add_order(
    data:OrderSchema,
    db:Session=Depends(get_db)
):
    
    user = db.query(UserModel).filter(UserModel.id == data.user_id).first()


    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    order=OrderModel(
        
        status=data.status,
        user_id=data.user_id ,  
    )


    db.add(order)
    db.commit()
    db.refresh(order)
    return {
        "msg":"Order added succesfully",
        "data":order
    }


@router.get("/orders")
def get_order(db:Session=Depends(get_db)):

    # orders=db.query(OrderModel).options(joinedload(OrderModel.orders)).all()
    orders=db.query(OrderModel).all()

    return orders

@router.get("/order/{user_id}")
def get_orderbyuser(user_id:int,db:Session=Depends(get_db)):

    user=db.query(UserModel).options(joinedload(UserModel.orders)).filter(UserModel.id==user_id).first()
    
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "msg":"Orders fetched",
        "data":user.orders
    }


@router.post("/orders/items")
def add_order_item(
    data: OrderItemSchema,
    db: Session = Depends(get_db)
):

    order = db.query(OrderModel).filter(
        OrderModel.id == data.order_id
    ).first()

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    product = db.query(ProductModel).filter(
        ProductModel.id == data.product_id
    ).first()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    if product.stock < data.quantity:
        raise HTTPException(
            status_code=400,
            detail="Insufficient stock"
        )

    item = OrderItem(
        order_id=data.order_id,
        product_id=data.product_id,
        quantity=data.quantity
    )

    product.stock -= data.quantity

    db.add(item)
    db.commit()
    db.refresh(item)

    return {
        "msg": "Product added to order successfully",
        "data": item
    }


@router.get("/orders/{order_id}")
def get_order_details(
    order_id: int,
    db: Session = Depends(get_db)
):

    order = (
        db.query(OrderModel)
        .options(
            joinedload(OrderModel.user),
            joinedload(OrderModel.items)
                .joinedload(OrderItem.product)
        )
        .filter(OrderModel.id == order_id)
        .first()
    )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return {
        "id": order.id,
        "user": {
            "name": order.user.name
        },
        "items": [
            {
                "product": {
                    "name": item.product.name,
                    "price": item.product.price
                },
                "quantity": item.quantity
            }
            for item in order.items
        ]
    }