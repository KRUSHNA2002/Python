class Product:

    def __init__(self,product_id,name,price,quantity):

        self.product_id=product_id
        self.name=name
        self.price=price
        self.quantity=quantity


    def show_product(self):

            print(self.product_id, self.name, self.price, self.quantity)

        

    
class Customer:

    def __init__(self,customer_id,name):
       self.customer_id=customer_id
       self.name=name

class Cart:

    def __init__(self,customer):

        self.customer=customer
        self.items=[]

    def add_product(self,product,quantity):

        if product.quantity >= quantity:

            product.quantity-=quantity

            self.items.append({
            "product": product,
            "quantity": quantity
            })
            print("Product added in Cart")
        else:
            print("Stock Unavailable")
            return

        for x in self.items:
            print("Name Of customer is : ", self.customer.name)
            p = x["product"]
            print("After added in cart :",p.product_id,p.name,p.price,p.quantity)

    def remove_product(self,product_id):



        for  product in self.items:
            p = product["product"]
            if p.product_id == product_id:
                p.quantity+=product["quantity"]
                self.items.remove(product)
                print("Product Remove from Cart")
                print("Name Of customer is : ", self.customer.name)
                print("After Remove in cart :",p.product_id,p.name,p.price,p.quantity)
                return



    
    def calculate_total(self):

        total=0
        for all in self.items:

            p = all["product"]

            total += p.price * all["quantity"]

        return total





p1=Product(1,"Mouse",50,1)
p2=Product(2,"Laptop",40000,5)

cust1 = Customer(1, "Krushna")

c1=Cart(cust1)


c1.add_product(p2,1)
print(c1.calculate_total())

c1.remove_product(1)

print(c1.calculate_total())

c1.add_product(p2,3)
c1.add_product(p1,1)
print(c1.calculate_total())