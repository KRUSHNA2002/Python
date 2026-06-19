from database.db import engine
from database.base import Base
from fastapi import FastAPI
from routes.api import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)