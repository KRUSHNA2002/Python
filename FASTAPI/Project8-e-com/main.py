from fastapi import FastAPI
from database.db import engine,BASE
from routes.user import router as user_router
from routes.order import router as order_router
from routes.product import router as product_router

# Import models first
from models.user import UserModel
from models.order import OrderModel
from models.product import ProductModel
from models.orderItem import OrderItem

app=FastAPI()



BASE.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(order_router)
app.include_router(product_router)