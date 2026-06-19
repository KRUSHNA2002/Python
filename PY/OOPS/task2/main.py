from student import StudentManager
import json

app=StudentManager()

while True:

    print("Choose correct input: 1 for  addition,/n 2 for view/n 3 for delete /n 4 for update /n 5 for exit")
    operation=input("Enter your choice")


    match operation:

        case "1":
            app.add_student()

        case "2":
            app.view_student()

        case "3":
            app.delete_student()
        case "4":
            app.update_student()
        case _:
            print("Please enter valid choice")
            break