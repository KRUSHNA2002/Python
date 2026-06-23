from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from Security.roles import allow_roles
from Models.Product import ProductModel
from Schemas.products import ProductSchema
from Database.config import get_db


from Services import product_service

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
    # product = ProductModel(
    #     name=data.name,
    #     order_id=data.order_id
    # )

    # db.add(product)
    # db.commit()
    # db.refresh(product)

    return product_service.add_product(data,db)


@router.get("/")
def get_products(
    skip:int=0,limit:int=5,
    keyword:str | None=None,
    db: Session = Depends(get_db),
    user=Depends(allow_roles("admin")
                 )
):
    return product_service.getall_product(db,skip,limit,keyword)


