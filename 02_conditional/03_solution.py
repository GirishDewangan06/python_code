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

