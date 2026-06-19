
from database import students,save_students

def add_student():
    
    try:
        name=input("Enter the name of student")
        age=int(input("Enter the name of age"))
        course=input("Enter the name of course")

        student={
            "name":name,
            "age":age,
            "course":course
        }
        
        students.append(student)

        save_students()

        print("Student added succesfully")
        
    except Exception as e:
        print("Error",e)
