from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session,joinedload
from models.product import ProductModel
from database.config import get_db
from schemas.productschema import ProductSchema


router=APIRouter(
    prefix="/E_commerce",
    tags=["Products"]
)

@router.get("/products")
def get_products(db:Session=Depends(get_db)):

    products=db.query(ProductModel).all()

    return {
        "msg":"Products fetched succesfuly",
        "products":products
    }

@router.post("/products")
def add_product(
    data: ProductSchema,
    db: Session = Depends(get_db)
):
    product = ProductModel(
        name=data.name,
        price=data.price,
        stock=data.stock
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return {
        "msg": "Product added successfully",
        "data": product

    }

@router.put("/products/{product_id}")

def update_product(
    data:ProductSchema,
    product_id:int,
    db:Session=Depends(get_db),
    
):
    
    product=db.query(ProductModel).filter(ProductModel.id==product_id).first()

    product.name=data.name
    product.price=data.price
    product.stock=data.stock

    db.commit()
    db.refresh(product)

    return {
        "msg":"Product Updated succesfully",
        "data":product
    }


@router.delete("/products/{product_id}")

def delete_product(
product_id:int,
db:Session=Depends(get_db)
):
    product=db.query(ProductModel).filter(ProductModel.id==product_id).first()

    if not product:
        raise HTTPException(status_code=404,detail="Product Not FOubd")

    db.delete(product)
    db.commit()



    return {
        "msg":"Product Deleted Succesfully",
        "data":product
    }