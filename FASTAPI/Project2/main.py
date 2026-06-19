from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

students = []

class Student(BaseModel):
    id:int
    name:str
    course:str


@app.post("/students")
def add_student(student:Student):


    students.append(
        student.model_dump()
    )

    return {
        "message":"Student Added Succesfully",
        "data":student
        }

@app.get("/students")
def show_student():

        return students

@app.put("/students/{student_id}")
def update_student(
     student_id:int,
     data:Student
):
    for student in students:
               if student["id"]==student_id:
                     student.update(data.model_dump())

                     return {
                           "message":"Updated"
                     }
    return { 
            "meassage":"Not Found"
        }

@app.delete("/students/{student_id}")
def delete_student(student_id:int):
      
      for student in students:
            
            if student["id"]==student_id:
                  
                  students.remove(student)

                  return {
                        "msg":"Student Deleted succesfully"
                  }
      return{
            "msg":"Student Not Found"
      }