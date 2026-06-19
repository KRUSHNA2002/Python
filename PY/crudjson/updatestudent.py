
from database import students,save_students

def updatestudent():
    
    try:
        name=input("Enter the student name of you want update")



        for x in students:

          if x["name"]==name:
                name=input("Enter the name of student")
                age=int(input("Enter the age of student"))
                course=input("Enter the course of student")

              
                x["name"]=name
                x["age"]=age
                x["course"]=course
                

                save_students()

                print("Student added succesfully")
                return
        
    except Exception as e:
        print("Error",e)
