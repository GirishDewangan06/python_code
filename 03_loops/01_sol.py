# 1. Counting Positive Numbers
# Problem: Given a list of numbers, count how many are positive.


numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
count_number_positive = 0

for num in numbers:
    if (num > 0):
        count_number_positive +=1

print("Positive numbers in list is:", count_number_positive)


# The loop iterates over all elements in numbers:

# Iteration 1: num = 1 → 1 > 0 is True → Increment count_number_positive → count_number_positive = 1
# Iteration 2: num = -2 → -2 > 0 is False → No change
# Iteration 3: num = 3 → 3 > 0 is True → Increment count_number_positive → count_number_positive = 2
# Iteration 4: num = -4 → -4 > 0 is False → No change
# Iteration 5: num = 5 → 5 > 0 is True → Increment count_number_positive → count_number_positive = 3
# Iteration 6: num = 6 → 6 > 0 is True → Increment count_number_positive → count_number_positive = 4
# Iteration 7: num = -7 → -7 > 0 is False → No change
# Iteration 8: num = -8 → -8 > 0 is False → No change
# Iteration 9: num = 9 → 9 > 0 is True → Increment count_number_positive → count_number_positive = 5
# Iteration 10: num = 10 → 10 > 0 is True → Increment count_number_positive → count_number_positive = 6