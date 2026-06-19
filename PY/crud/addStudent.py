
from database import students

def add_student():
    
    name=input("Enter the name of student")
    age=int(input("Enter the name of age"))
    course=input("Enter the name of course")

    student={
        "name":name,
        "age":age,
        "course":course
    }
    
    students.append(student)

    print("Student added succesfully")
