from database.db import engine,BASE,SessionLocal

from fastapi import Depends

def get_db():

    db=SessionLocal()

    try:
        yield db
    finally:
        db.close()