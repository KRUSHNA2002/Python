
import json

from database import students,save_students

def deletestudent():
    
    name=input("Enter the name of student")

    for x in students:
        if(x["name"]==name):
            
            students.remove(x)

            save_students()

            print("Student Deleted succesfully")
            return
    
print("Student not found")