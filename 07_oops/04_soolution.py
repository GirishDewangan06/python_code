#4.Encapsulation: ##class access by anyone but its inside attribute only know when I want 
#Problem:-Modify the Car class to encapsulate the brand attribute, making it private and provide a getter method for it

class Car:
    def __init__(self, brand, model ):
        self.__brand = brand
        self.model = model

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def get_brand(self):
        return self.__brand + "!"        


my_obj = Car("mclaren", "artura")

# print(my_obj.__brand)  ##not working bcoz indirect access not allowed
print(my_obj.get_brand())
print(my_obj.model) 
##mclaren!
##artura