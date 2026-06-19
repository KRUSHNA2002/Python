from fastapi import FastAPI
from pydantic import BaseModel
from database import get_connection

app=FastAPI()


@app.get("/test-db")
def test_db():
    try:
        conn=get_connection()
        cur = conn.cursor()

        cur.execute("Select 1")
        result = cur.fetchone()

        cur.close()
        conn.close()

        return {"status":"connected","result":result}
    except Exception as e:
        return {"status":"Error","Message":str(e)}