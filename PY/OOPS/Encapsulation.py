
class Bank:
    def __init__(self,balance,account_no):
        self.__balance=balance
        self.__account_no=account_no

    def debit(self,amount):
        self.__balance -= amount
        print("Balance debited", amount)
        print(self.get_balance())


    def credit(self,amount):
        self.__balance += amount
        print("Balance credited", amount)        
        print(self.get_balance())


    def get_balance(self):

        return self.__balance
    

    def set_balance(self,new_balance):

        self.__balance = new_balance

acc1 = Bank(10000,111111)


acc1.debit(1000)
acc1.credit(500)
acc1.credit(4000)


acc1.set_balance(50000)


acc1.debit(1000)
acc1.credit(500)
acc1.credit(4000)

