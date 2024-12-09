#10.Recursive function:
#Problem:-Create a recursive function to calcalate the factotial of given number

def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)

print(factorial(5))