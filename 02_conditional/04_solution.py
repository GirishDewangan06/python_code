
#4.Friut Ripeness Checker:
fruit = str(input("Enter fruit name:")).upper()
color = str(input("Enter Fruit Color:")).upper()



if fruit == "BANANA":
    if color == "GREEN":
        means = "Unripe"
    elif color == "YELLOW":
        means = "Ripe"
    else:
        means = "Overripe"

print("So the fruit is:",means)