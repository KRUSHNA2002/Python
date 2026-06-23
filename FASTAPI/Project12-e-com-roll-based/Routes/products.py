from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from Security.roles import allow_roles
from Models.Product import ProductModel
from Schemas.products import ProductSchema
from Database.config import get_db

router = APIRouter(
    prefix="/products",
    tags=["Products"],
    dependencies=[Depends(allow_roles("admin"))]
)


@router.post("/")
def add_product(
    data: ProductSchema,
    db: Session = Depends(get_db),
    user=Depends(allow_roles("admin"))
):
    product = ProductModel(
        name=data.name,
        order_id=data.order_id
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return {
        "msg": "Product added successfully",
        "product": product
    }


@router.get("/")
def get_products(
    db: Session = Depends(get_db),
    user=Depends(allow_roles("admin"))
):
    products = db.query(ProductModel).all()

    return {
        "msg": "Products fetched",
        "products": products
    }