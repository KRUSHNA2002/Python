from fastapi import FastAPI
from database.db import BASE,engine
from routes.auth import router



app=FastAPI()

BASE.metadata.create_all(bind=engine)

app.include_router(router)