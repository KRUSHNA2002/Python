from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
import os
import uuid
import shutil
from fastapi.responses import FileResponse
from pathlib import Path
from db.database import get_db, engine, Base
from db.models import Image

router = APIRouter()

# create tables
Base.metadata.create_all(bind=engine)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


# ✅ Upload image
@router.post("/upload")
async def upload_image(
    files:list[UploadFile] = File(...),
    db: Session = Depends(get_db)
):

  uploaded_file=[]

  for file in files: 

        file_ext = file.filename.split(".")[-1]
        unique_name = f"{uuid.uuid4()}.{file_ext}"

        file_path = os.path.join(UPLOAD_DIR, unique_name)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        img = Image(
                filename=file.filename,
                content_type=file.content_type,
                file_path=file_path
            )

        db.add(img)
        db.commit()
        db.refresh(img)

        uploaded_file.append({
                "id": img.id,
                "filename": img.filename,
                "url": f"/uploads/{unique_name}"
            })
  return uploaded_file
  




@router.get("/file/{image_id}")
def get_file(image_id: int, db: Session = Depends(get_db)):

    img = db.query(Image).filter(Image.id == image_id).first()

    if not img:
        return {"error": "not found"}

    file_path = Path(img.file_path)

    return FileResponse(file_path)

@router.get("/images")
def get_all_images(db: Session = Depends(get_db)):
    images = db.query(Image).all()
    return images