from fastapi import FastAPI
from database.db import BASE,engine
from routes.auth import router as auth_router
from routes.dashboard import router as dashboard_router



app=FastAPI()

BASE.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(dashboard_router)