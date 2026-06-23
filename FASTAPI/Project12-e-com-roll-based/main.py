from fastapi import FastAPI
from Database.db import Base,engine
from Routes.auth import router as auth_router
from Routes.orders import router as order_router
from Routes.items import router as item_router
from Routes.products import router as product_router
from Models import RegisterModel, OrderModel, ProductModel, ItemsModel
app = FastAPI()



Base.metadata.create_all(bind=engine)


app.include_router(auth_router)
app.include_router(order_router)
app.include_router(item_router)
app.include_router(product_router)