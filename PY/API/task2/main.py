from operation import APIClient


api= APIClient()

while True:

    print("Enter your choice, 1 for view, 2 for add , 3 for delete, 4 update")

    choice=input("ENter your choice")

    match choice:
        case "1":
            api.viewuser()
        case "2":
            api.adduser()
        case "3":
            api.deleteuser()
        case "4":
            api.updateuser()
        case _:
            print("Enter Valid choice")
            break
        