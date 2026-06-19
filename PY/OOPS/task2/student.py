import json
import os

class StudentManager:
    def __init__(self):
        self.students=[]

        self.file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "oops",
            "task2",
            "students.json"
        )

        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

        self.load_students()


        
    
    def load_students(self):
        try:
            with open(self.file_path,"r") as file:
                self.students = json.load(file)

        except FileNotFoundError:

            self.students=[]

    def save_student(self):
        with open(self.file_path,"w") as file:

            json.dump(self.students,file,indent=4)
    
    def add_student(self):
        name=input("Enter the student name")
        age=int(input("Enter the student age"))
        course=input("Enter the student course")

        student={
            "name":name,
            "age":age,
            "course":course,
        }

        self.students.append(student)
        self.save_student()

        print("Student added succesfully")

        return

    def view_student(self):

        if not self.students:
            print("student not found")
            return

        for x in self.students:
            print("<------------------>")
            print("name of student : ",x["name"])
            print("age of student : ",x["age"])
            print("course of student : ",x["course"])

 

    def delete_student(self):
        name=input("Enter the name of student you want to delete :")

        for x in self.students:

            if x["name"]==name:
                self.students.remove(x)

                self.save_student()

                print("Student Deleted Succesfully")

                return
            
        print("student not found...")

    def update_student(self):
        name=input("Enter the name of student you want to update :")

        for x in self.students:

            

            if x["name"]==name:

                x["name"]=input("Enter the name")            
                x["age"]=int(input("Enter the age"))             
                x["course"]=input("Enter the course")   

                self.save_student()

                print("Student Updated succesfully")

                return

        print("student not found...")     

     
                  
