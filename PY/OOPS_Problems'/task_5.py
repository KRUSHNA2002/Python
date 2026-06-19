
def account(name,balance,acco_no):

    print("Account no is : ",acco_no)
    print("Name of Account Holder : ",name)
    print("Remaining balance  : ",balance)

    def deposit(amount):
        nonlocal balance

        balance +=amount

        return balance

    def withdraw(amount):
        nonlocal balance

        balance -=amount

        return balance

    def showbalance():
        nonlocal balance
        print("Account Holder name is:", name)
        print("Remaining balance is:", balance)
        return balance


    
    return deposit,withdraw,showbalance

deposit_fn,withdraw_fn,showbalance_fn=account("krushna",50000,123456)

print("After deposite balance is : ",deposit_fn(2000) )
print("After withdraw balance is : ",withdraw_fn(10000) )
print(" showbalance balance is : ",showbalance_fn() )


