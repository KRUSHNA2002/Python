class BankAccount:

    def __init__(self,Account_no,Holder_name,balance):
        self.__Account_no=Account_no
        self.__Holder_name=Holder_name
        self.__balance=balance

    def deposit(self,amount):
        self.__balance+=amount
        print("Amount credited in account is : ", amount)
        print("Account Total balance is :  ",self.check_balance())
    
    def withdraw(self,amount):
        
        if self.__balance > amount:
            self.__balance-=amount
            print("Amount debited in account is : ", amount)
            print("Account Total balance is :  ",self.check_balance())

            return

        print("Account balance insufficient,Please Enter valid amount...")
    
    def check_balance(self):

        return self.__balance
    
    def transfer_money(self,receiver,amount):

        if self.__balance > amount:
            self.__balance-=amount
            
            receiver.deposit(amount)

            print("Amount debited in account is : ", amount)
            print("Account Remaining balance is :  ",self.check_balance())   

            return     

        print("Amount balance insufficient  ",self.check_balance())

    def show_details(self):
        print("Account Holder Name : ",self.__Holder_name)
        print("Remaining balance : ",self.__balance)

acc1 = BankAccount(123456,"Krushna",50000)
acc2 = BankAccount(121212,"Sandip",10000)

print("Remaining Balance : ",acc1.check_balance())

acc1.deposit(2000)
acc1.withdraw(20000)
acc1.transfer_money(acc2,10000)
acc2.show_details()