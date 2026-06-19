
from database import students

def deletestudent():
    
    name=input("Enter the name of student")

    for x in students:
        if(x["name"]==name):
            students.remove(x)
            print("Student Deleted succesfully")
    
    print("Student not found")