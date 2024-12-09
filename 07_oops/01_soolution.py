# 1.Basic Class & objects:
# Problem:-Create a Car class with attributes like brand and model , then cretes instnace of the class

# class Car:                       # std: use always first letter capital
#     brand = None#attribute
#     model = None#attribute

# my_obj = Car()# here, my_obj is object(variable)
# print(my_obj)##<__main__.Car object at 0x01C327B0>

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# class Car:
#     def __init__(userBrand, userModel):
#         brand = userBrand
#         model = userModel

# my_obj = Car()
# print(my_obj.brand)

# in above , there is no linkage b/w my_obj(object) and Car(class), so we use "Self"(context, this->) keyword (who one call)

class Car:
    def __init__(self, brand, model):  
        self.brand = brand## self.brand->attribute(variable) and brand -> parameter
        self.model = model## self.model->attribute(variable) and model -> parameter

# init here is "contructor"(method call __init__ as new obj forms)
##above we made a blank form , any one can use..

my_obj = Car("Toyota", "Corolla")
print(my_obj.brand)
print(my_obj.model)
##Toyota
##Corolla

my_new_obj = Car("Mercedes", "Maybach")
print(my_new_obj.brand)
print(my_new_obj.model)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##someone make a separate file for CLASS , and for using just import it
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


