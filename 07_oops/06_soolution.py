#6.Class Variables:
#Problem:-Add class variable to the class car that keeps track the number of car created.

class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

        Car.total_car +=1

Car("TATA","Safari")
Car("TATA", "Nexon")
Car("TATA", "tiago")
        
print(Car.total_car)        