from Models.Order import OrderModel


def addtheorder(data,db):
        order = OrderModel(user_id=data.user_id,name=data.name)

        db.add(order)
        db.commit()
        db.refresh(order)

        return {
            "msg": "Order added Successfully",
            "order": order
        }

def getallorders(db,skip,limit):
        
    # orders = db.query(OrderModel).all()
    orders=db.query(OrderModel).offset(skip).limit(limit).all()
    return {
        "msg": "Fetched Orders",
        "orders": orders
    }

def getoneuser(user_id,db):
      

    orders = db.query(OrderModel).filter(
        OrderModel.user_id == user_id
    ).all()



    return {
        "msg": "Fetched Orders",
        "orders": orders
    }