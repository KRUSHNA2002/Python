
class BankAccount:

    def __init__(self,account_no,balance):
        self.__account_no=account_no;
        self.__balance=balance;


    def deposite(self,addbalance):

        self.__balance+=addbalance;
        print("balance added in account is : ",addbalance)
        print("Total balance in account is : ",self.check_balance())

    def withdraw(self,subbalance):

        self.__balance-=subbalance;
        print("balance withdraw in account is : ",subbalance)
        print("Total balance in account is : ",self.check_balance())

    def check_balance(self):

        return self.__balance;

acc1=BankAccount(123456,50000);

acc1.deposite(5000);
acc1.withdraw(1000);
