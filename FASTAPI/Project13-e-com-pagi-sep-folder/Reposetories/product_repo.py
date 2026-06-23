from Models.Product import ProductModel
import logging

def create_product(
    data,
    db,

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
    }


def get_product(db, skip, limit, keyword):

    query = db.query(ProductModel)

    if not query:

        logging.error("Query failed Product fetched")

    if keyword:
        query = query.filter(ProductModel.name.contains(keyword))

    products = query.offset(skip).limit(limit).all()

    return {
        "msg": "Product Fetched",
        "products": [
            {
                "id": p.id,
                "name": p.name,
                "order_id": p.order_id
            }
            for p in products
        ]
    }