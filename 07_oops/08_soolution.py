#8.property Decorator:
#Problem:- Use a property decorator to the Car class to make model attribute read only:\

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model
   
    @property
    def model(self):
        return self.__model  + "!"  

myCar = Car("TATA", "Nexon")
# myCar.model = "Safari"
print(myCar.model)    