#Function with **kwargs:
#Problem:-Create a function that accepts any number of keyword arguments and print them in format key:value

# def print_kwargs(name, power):
#     print("Name:", name, "Power:", power)

# print_kwargs( power="Lazer", name ="Shaktiman")
# print_kwargs( power="Lazer", name ="Shaktiman", enemy = "Dr. Jackaal")

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")



print_kwargs( power="Lazer", name ="Shaktiman")
print_kwargs( power="Lazer", name ="Shaktiman", enemy = "Dr. Jackaal")