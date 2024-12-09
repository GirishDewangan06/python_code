       
#10.Pet food Recommendation:
species = str(input("Enter a species:")).lower()
age = int(input("Enter an age:"))

if species == "dog":
    if age < 2 :
        print("Puppy food")
    else:
        print("Peddygree food")    
elif(species == "cat"):
    if age > 5:
        print("Senior cat food")
    else:
        print("Local Dal-Bhat")    
else:
    print("No provided info")        
