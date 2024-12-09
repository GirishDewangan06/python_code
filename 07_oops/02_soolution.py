##2.Class Mehtod and Self:
#Problem:- Add a method to th Car class that displays the full name of Car(brand and model)
##still we add attribute and now add a functionality on the class

class Car:
    def __init__(self, brand, model):  
        self.brand = brand## self.brand->attribute(variable) and brand -> parameter
        self.model = model## self.model->attribute(variable) and model -> parameter

# init here is "contructor"(method call __init__ as new obj forms)
##above we made a blank form , any one can use..


#to add functionality we use function of any name
    def full_name(self):
        return f"{self.brand} {self.model}"

my_obj = Car("Toyota", "Corolla")
print(my_obj.brand)
print(my_obj.model)
print(my_obj.full_name()) #here full_name is function, not an attribute(var)
##Toyota
##Corolla

my_new_obj = Car("Mercedes", "Maybach")
print(my_new_obj.brand)
print(my_new_obj.model)
print(my_new_obj.full_name())