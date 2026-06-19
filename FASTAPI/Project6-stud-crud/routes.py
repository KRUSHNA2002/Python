from fastapi import APIRouter,Depends,HTTPException
from  schemas import StudentCreate
from models import Student
from database import engine,Base
from sqlalchemy.orm import Session
from config import get_db


router=APIRouter(
    prefix="/students"
)

@router.get("/")
def get_students(db:Session=Depends(get_db)):
   
   students=db.query(Student).all()

   return students

@router.post("/")
def add_students(
   data:StudentCreate,
   db:Session=Depends(get_db)
):
   
   students=Student(
      name=data.name,
      email=data.email,
      course=data.course

   )

   db.add(students)
   db.commit()

   return {
    "message":"Student Added"
    }

@router.put("/{student_id}")
def update_student(
   student_id:int,
   data:StudentCreate,
   db:Session=Depends(get_db)
):
   
   student=db.query(Student).filter(Student.id==student_id).first()

   if not student:
      
      raise HTTPException(status_code=404, detail="Student Not found")
   
   student.name=data.name
   student.email=data.email
   student.course=data.course

   db.commit()
   db.refresh(student)


   return{
      "msg":"Student Updated Succesfully",
      "data":student
   }


@router.delete("/{student_id}")
def delete_user(
   student_id:int,
   db:Session=Depends(get_db)
):
   
   student=db.query(Student).filter(Student.id==student_id).first()

   if not student:
      
      raise HTTPException(status_code=404, detail="Student Not found")
   
   db.delete(student)
   db.commit()

   return{
      "msg":"Student deleted Succesfully",
      "data":student
   }
