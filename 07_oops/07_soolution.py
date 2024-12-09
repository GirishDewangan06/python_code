#7.Static Method: # method that belongs to Class rather than instance(obj) of class 
#Problem:-Add a Static method to the Car class that returns the genearl decription of car

# class Car:
#     def __init__(self, brand, model ):
#         self.brand = brand
#         self.model = model

#     def general_description(self):
#         return "Cars are amazing."    
    
# myCar = Car("TESLA", "model S")
# print(myCar.general_description())    
## above we use refence for obj 

class Car:
    def __init__(self, brand, model ):
        self.brand = brand
        self.model = model
    
    @staticmethod
    def general_description():
        return "Cars are amazing."    
    
myCar = Car("TESLA", "model S")
 
print(myCar.general_description())  
print(Car.general_description())  