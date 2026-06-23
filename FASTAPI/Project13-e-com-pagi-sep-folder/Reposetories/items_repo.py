from Models.Items import ItemsModel

def add_items(data,db):
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

def get_items(db,skip,limit):

    # items = db.query(ItemsModel).all()

    items=db.query(ItemsModel).offset(skip).limit(limit).all()



    return {
        "msg": "Items fetched",
        "items": items
    }