students = []


while True:
    print("Enter 1 : you want to add student")
    print("Enter 2 : you want to delete student")
    print("Enter 3 : you want to view student")
    print("Enter 4 : you want to exit game")

    choice= input("Enter you choice")

    match choice:
        case "1":
           name=input("Enter student name")
           age=int(input("Enter student age"))
           course=input("Enter student course")

           student={
               "name":name,
               "age":age,
               "course":course
           }
           students.append(student)
          
           print("Student is added succesfully")

           
        case  "2":
            delete_stud=input("Enter name of student you want to delete")
            Found = False
            for x in students:
                if(x["name"]==delete_stud):
                    students.remove(x)
                    Found=True
                    print("Student deleted")
                    break

            if Found == False:
                print("Student not Found")
 
        case "3":
            for x in students:
                print(x["name"])
                print(x["age"])
                print(x["course"])
        case "4":
            break
        case _:
            print("invalid option")


print(students)