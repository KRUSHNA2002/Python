
db_username = "admin"
db_pass = "add123"

user =input("ENTER THE USERNAME : ")
password =input("ENTER THE PASSWORD : ")




if db_username==user:

    if db_pass == password:
        print("Login succesfully")

    else:
        print("Invalid Password")

else:

    print("Invalid Username")