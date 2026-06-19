class CreditCard:

    def pay(self,amount):
        print(f"Paid {amount} using Credit Card")

class UPI:

    def pay(self,amount):
        print(f"Paid {amount} using UPI")

class Cash:

    def pay(self,amount):
        print(f"Paid {amount} using Cash")


c1=CreditCard()

c1.pay(5000)

b1=UPI()
b1.pay(4000)

a1=Cash()
a1.pay(3000)