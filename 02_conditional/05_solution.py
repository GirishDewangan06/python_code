# #5.whether activity suggestion:
whether = str(input("Enter whether: ")).upper()

if whether == "SUNNY":
    activity = "Go for a walk"
elif whether == "RAINY":
    activity = "Read a book"
else:
    activity = "Build a snow"

print("Suggest by an AI : ",activity )
