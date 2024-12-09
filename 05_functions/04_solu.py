# 4.Function returning multiple values:
# Problem:-Create a function that returns both area and circumference of th circle given its radius.

import math

def circle_stats(radius):
    add = math.pi*(radius**2)
    circumference = 2*(math.pi)*radius
    return add, circumference
    print("Hi")

a,c = circle_stats(3)
print("Area :", a, "Circumfernce:", c)

# def areaAndCircumference(radius):
#     print("Area of circle with radius", radius, "is", 3.14*(radius**2))
#     print("Circumference of circle with radius", radius, "is", 2*3.14*(radius))

# areaAndCircumference(3)