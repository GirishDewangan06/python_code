#5.polymorphism: ##kitne rup dharan kar sakta hai.
# Problem:-Demonstrate Polymorphism by defining a method fuel_type on both Car and ElectricCar but different behavior.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model} "
    
    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def  __init__(self,brand, model,  battery_size):        
        super().__init__(brand, model)
    
    def fuel_type(self):
        return "Electric Charge"

my_EV = ElectricCar("Tesla", "Model S", "85KWh")
print(my_EV.fuel_type())
# print(my_EV.brand)        
# print(my_EV.model)        
# print(my_EV.full_name()) 

my_car = Car("TATA", "Safari")
print(my_car.fuel_type())

