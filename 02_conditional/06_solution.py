#6.Transport Mode selection:
dist = int(input("Enter a distance:"))

if dist < 3:
    transport = "Walk"
elif dist < 15 :
    transport  = "Bike"
else :
    transport = "Car"       

print("Sugegst by an AI is: ", transport)