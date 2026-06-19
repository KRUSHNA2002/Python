class User:

    def __init__(self,username,password):
        self.__username=username
        self.__password=password

    def login(self,username,password):
        
        if username==self.__username and password==self.__password:
            print("Login Succesfully")
        else:
            print("Invalid Username or password")


    def change_password(self,new_password):
        
        self.__password=new_password

        print("Password updated succesfully")



user1=User("Krushna",111111)

user1.login("Krushna",111111)
user1.change_password(12345)
user1.login("Krushna",111111)
user1.login("Krushna",12345)

