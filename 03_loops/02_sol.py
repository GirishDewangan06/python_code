# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

n = int(input("Enter a number:"))
sum_even_num = 0

for i in range(1, n+1):
    if i%2 == 0:
        sum_even_num+=i

print("Sum of even numbers:", sum_even_num)


#it-1:"p"->rev_string("p")
#it-2:"y"->"y"+"p"="yp"
#it-3:"y"->"t"+"yp"="typ"..........
