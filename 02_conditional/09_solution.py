#9.Leap year Checker:

year = int(input("Enter an Year: "))

if (year%4==0 and year%100!=0 ) or (year%400== 0):
    determine = "Leap year"
else:
    determine = "Not a leap year"

print(year ," is :",determine)