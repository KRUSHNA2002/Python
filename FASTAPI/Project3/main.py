from fastapi import FastAPI,HTTPException
from pydantic import  BaseModel
import requests
from typing import List

import json

FILE_NAME="student.json"

app=FastAPI()

class APICRUD(BaseModel):

    id:int
    name:str
    course:str


def load_student():
       
    try:
        with open(FILE_NAME,"r") as file:

          return json.load(file)
       
    except FileNotFoundError:
        return[]
           

        
def save_student(data):

        with open(FILE_NAME,"w") as file:

          json.dump(data,file,indent=4)




@app.get("/students",response_model=List[APICRUD])
def get_student():

    students = load_student()

    return students



@app.post("/students")
def add_student(student:APICRUD):

    students=load_student()

    for s in students:

        if s["id"]==student.id:

            raise HTTPException(status_code=400,detail="Student with this ID already exits")
        
    students.append(student.model_dump())
    save_student(students)

    return {
        "msg":"Student Added succesfully",
        "data":student
        }


@app.put("/students/{student_id}")
def update_student(student_id:int,data:APICRUD):
    students=load_student()
    for s in students:

        if s["id"]==student_id:

            s.update(data.model_dump())
            save_student(students)
            return {"message": "Updated", "student": s}

    raise HTTPException(status_code=404, detail="ID not found")

@app.delete("/students/{student_id}")
def delete_student(student_id:int):
    students=load_student()
    for s in students:

        if s["id"]==student_id:

            students.remove(s)
            save_student(students)
            return {"message": "Deleted Student", "student": s}

    raise HTTPException(status_code=404, detail="ID not found")
