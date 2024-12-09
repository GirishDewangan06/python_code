
#2.Movie ticket pricing:
age = int(input("Enter an age:"))
day = str(input("Enter the day:"))

price = 12 if age>=18 else 8

if (day == "Wednesday"):
    price = price - 2;

print("Ticket price is ",price)



############# or #########################################3
if (day=="Wednesday"):
    if(age>=18):
        print("Ticket price for adult on ",day ,"is", 12-2)
    else:
        print("Ticket Price for childern on ",day ,"is", 8-2)    
else:
    if(age>=18):
        print("Ticket price for adult on ",day ,"is",12)
    else:
        print("Ticket Price childern on ",day, "is", 8)       

