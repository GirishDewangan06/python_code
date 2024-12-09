#1.Age grp categ:

age = 29

if age<13:
    print("Child")
elif age<20:
    print("Teenager")    
elif age<60:
    print("Adult")
else:
    print("Senior")       
print("++++++++++++++++++++++++++++++++")

##

#2.Movie ticket pricing:
age = 29
day = "wednesday"

price = 12 if age>=18 else 8

if day=="wednesday":
    price -=2

print("Price of ticket for ", age, "is", price)
print("+++++++++++++++++++++++++++")

##

#3.Grade calculator:
score = int(input("Enter Score:"))
grade = ""
if score >100:
    print("check marks, and try again")
    
else:
  if score >=90:
    grade = "A"
  elif score >=80:
    grade = "B"    
  elif score >=70:
    grade = "C"    
  elif score >=60:
    grade = "D"
  else:
    grade ="F"  

  print("Grade based on ", score, "is", grade)          
  
  ##
  # 
#4.Friut Ripeness Checker:
fruit = "Banana"
color = "Green"

if fruit == "Banana":
   if color == "Green":
      determine = "Unripe"
   elif color == "Yellow":
      determine = "Ripe"
   else:
      determine = "Overripe"
      
   print("fruit color", color, "that means", determine)        
   
#5.whether activity suggestion:
whether = "Rainy"

if whether == "Sunny":
   activity = "Go for a walk"
elif whether == "Rainy":
   activity = "Read a book"
elif whether == "Snow":
   activity = "Build a snow man"

print("Activity youu do for (", whether, ") is", activity)   

#6.Transport Mode selection:
dist = 15

if dist < 3:
    print("Walk")
elif 3<=dist<=15:
    print("Bike")
else:
    print("Car")   
      
#7 Coffee customization:
size = "Small"
extra_shot = True

if extra_shot == True:
    order = size + " Coffee with extra shot"
else:
    order = size + " Coffee without extra shot"
       
print(order)     

#8.Password Strength Checker:

password = "Secure@122"
strengths = ""

if len(password)< 6:
    print("Weak")
elif len(password) <10:
    print("Medium")
else:
    print("Strong")    

#9.Leap year Checker:
year = int(input("Enter year: "))
leap_year = ""

if (year%4==0 and year%100!=0) or (year%400==0):
    leap_year= True
else:
    leap_year = False
print(year,"is leap year:-", leap_year)        
       
#10.Pet food Recommendation:
species = str(input("Enter Species:")).lower()
age = int(input("Enter Species's age:"))

if species == "dog":
    if age < 2:
        print("Puppy food")
    else:
        print("Dal chawal")    
elif species == "cat":
    if age > 5:
        print("Senior cat food") 
    else:
        print("Milk only")    
               
