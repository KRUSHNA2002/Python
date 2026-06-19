class Vehicle:

    def __init__(self,model,brand):
        self.model=model
        self.brand=brand

class Car(Vehicle):

    def __init__(self,model,brand, door):
        super().__init__(model, brand)  # Call parent constructor
        self.door=door


    def start(self):
        print("Car is start")

    def show_car(self):

        print("Model of car",self.model)
        print("brand of car",self.brand)
        print("door of car",self.door)

class Bike(Vehicle):

    def __init__(self,model, brand, engine_cc):
        super().__init__(model, brand)  # Call parent constructor      

        self.engine_cc=engine_cc


    def start(self):
        print("Bike is start")

    def show_bike(self):

        print("Model of bike",self.model)
        print("bike",self.brand)
        print("bike engine_cc",self.engine_cc)




c1=Car("2026","Verna","4")

c1.show_car()

b1=Bike("2020","Pulsur","125")

b1.show_bike()
b1.start()

    
    