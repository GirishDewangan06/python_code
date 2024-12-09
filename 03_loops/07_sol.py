#7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True:
    number = int(input("Enter a Number:"))

    if 1<=number<=10:
        print("thanks")
        break
    else:
        print("Invalid, try again") 
    