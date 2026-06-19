from database import students
import addStudent
import deletestudent
import viewStudent

while True:
    print("Press 1:For Add student")
    print("Press 2:For view student")
    print("Press 3:For delete student")
    print("Press 4:exit")

    number=input("Enter you Action...")

    match number:
        case "1":
            addStudent.add_student()
        case "2":
             viewStudent.viewstudent()
        case "3":
            deletestudent.deletestudent()
        case "4":
            break

print(students)