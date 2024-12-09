# 1.Basic function Syntax:
# Problem:Write a function to calculate and return the square of the number.

# def square(number):
#     print(number**2)

# square(int(input("Enter a number:")))    

def square(number):
    return number**2

result = square(int(input("Enter a number:")))
print(result)