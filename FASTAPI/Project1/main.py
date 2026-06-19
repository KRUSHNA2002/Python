from fastapi import FastAPI


app=FastAPI()

students=[{
    "id":1,
    "name":"Krushna",
    "course":"Python",
    "age":23
},
{
    "id":2,
    "name":"Sandip",
    "course":"PHP",
    "age":33  
}]

@app.get("/")
def home():
    return {
        "meassage":"Hello FastAPi"
    }

@app.get("/students")
def get_student():
    return students


@app.get("/students/{student_id}")
def getbyid(student_id:int):

    for student in students:

      if student["id"] == student_id:
          
          return student
      
    return {"Student Not Found"}