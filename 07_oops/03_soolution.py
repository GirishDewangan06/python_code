#3.Inheritance  ##ancester ki property jo mujhe mila vhi (inheritance)
#Problem:-Create an Electric Car class that inherits from class Car and has an additional attribute(battery_size)

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model} "

class ElectricCar(Car):
    def  __init__(self,brand, model,  battery_size):        
        super().__init__(brand, model)
        self.battery_size = battery_size

my_EV = ElectricCar("Tesla", "Model S", "85KWh")
print(my_EV.brand)        
print(my_EV.model)        
print(my_EV.battery_size)        
print(my_EV.full_name())        