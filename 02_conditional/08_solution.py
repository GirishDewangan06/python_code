# #8.Password Strength Checker:

password = len(str(input("Enter a pasword:")))
print(password)

if password < 6:
    strengths = "Weak"

elif password < 10:
    strengths = "Medium"

else:
    strengths = "strong"      

print("Password strength is :", strengths)      