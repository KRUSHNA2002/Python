from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.image import router as img_router
from routes.exportcsv import router as csv_router
from routes.backtask import router as backtask_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include routes
app.include_router(img_router)
app.include_router(csv_router)
app.include_router(backtask_router)

@app.get("/")
def health():
    return {"status": "ok"}