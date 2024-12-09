# 4. Reverse a String
# Problem: Reverse a string using a loop

string = "Python"
rev_string = " "

for char in string:
    rev_string = char + rev_string

print(rev_string)



# Step-by-step changes to rev_string:

# Iteration 1: char = 'P' → rev_string = 'P' + '' → rev_string = "P"
# Iteration 2: char = 'y' → rev_string = 'y' + 'P' → rev_string = "yP"
# Iteration 3: char = 't' → rev_string = 't' + 'yP' → rev_string = "tyP"
# Iteration 4: char = 'h' → rev_string = 'h' + 'tyP' → rev_string = "htyP"
# Iteration 5: char = 'o' → rev_string = 'o' + 'htyP' → rev_string = "ohtyP"
# Iteration 6: char = 'n' → rev_string = 'n' + 'ohtyP' → rev_string = "nohtyP"