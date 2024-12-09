#10.Multiple inheritance:
#Problem:-Create 2 classes "Battery" and "Engine" & let ElectricCar class inherit from both
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model} "


class Battery:
    def battery_info(self):
        return "This is battery!"

class Engine:
    def engine_info(self):
        return "This is Engine."

class ElectricCartwo(Battery, Engine, Car):
    pass

my_car = ElectricCartwo("Tesla", "Model S")
print(my_car.engine_info())
print(my_car.battery_info())