
def details(name,total_balance,acc_no):

    print("Acc_no is  : ",acc_no)
    print("Balance of Holder : ",total_balance)
    print("Name of Holder : ",name)
    print("<------------------> ")


    return total_balance


def deposit(remaining_amt,amount):

     total_balance =remaining_amt + amount

     return total_balance

def withdraw(remaining_amt,amount):

     total_balance =remaining_amt - amount

     return total_balance




    

rem_balance=details("krushna",20000,123456)

print("After Deposit balance is:", deposit(rem_balance,5000))

print("After withdraw balance is:", withdraw(deposit(rem_balance,5000),15000))
