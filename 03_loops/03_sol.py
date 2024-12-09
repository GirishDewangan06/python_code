# 3. Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

num = 2

for i in range(1,11):
    if i==5:
        continue # used for skiping the value
    print(num, "X", i, "=", num*i)
