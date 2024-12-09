#1.check positive numbers:
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
count = 0

for num in numbers:
    print(num, end=" ")
    if num >0:
        count+=1

print("\nTotal positive num:",count)  

#2.Sum of even:
n = 3
sum_num = 0

for i in range(1, n+1):
    if i%2==0:
        sum_num+=i

print("Sum of total till", n , "is", sum_num)
            
#3.Multiplication table:
n = 3

for i in range(1, 11):
    if i == 5:
        continue
    print(n,"X",i, " is ", n*i)

#4.Reverse a String:
character = "Python"
rev_str = ""

# print(character[::-1])

for char in character:
    rev_str = char + rev_str
print(rev_str)    


#it-1:"p"->rev_string("p")
#it-2:"y"->"y"+"p"="yp"
#it-3:"y"->"t"+"yp"="typ"..........

#+++++++++++++++++++++++++++++++++++++++++++++++++

##5.first non_rep char:

string = "teeteracdcad"

for strr in string:
    print(strr)
    if string.count(strr)==1:
        print("First Non_repeated string:", strr)
        break
    
#6.Factorial calculator:-
n = 5
fac= 1
num = 1

# while num<=n:
#     fac = fac * num
#     num+=1    
    
# print("Factoraial of number(", n, ") is", fac)

#+++++++++++++++++++OR+++++++++++++++

while n>0:
    fac = fac*n
    n-=1
print("factorial =", fac)

##7.Validate Input

while True:
    inp = int(input("Enter a num:"))

    if 1<=inp<=10:
        print("Thanks")
        break
    else:
        print("Invalid, try again")


#9.List uniqueness checker:--
items = [ "banana", "orange", "mango","apple", "mango"]

unique_check = set()

for item in items:
    if item in unique_check:
        print("duplicate: ", item)
    else:
        unique_check.add(item)

##10.Exponential backoff:--
import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts<max_retries:
    print("attempts:-", attempts+1, "-Wait timw:-", wait_time)
    time.sleep(wait_time)
    wait_time*=2
    attempts+=1
