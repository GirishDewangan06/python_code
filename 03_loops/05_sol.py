# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

charac = "teeterabcacb"

for char in charac:
    print(char)
    if charac.count(char)==1:
        print("First Non rep char:",char)
        break

# Step-by-Step Execution:

# Iteration 1: char = 't' → charac.count('t') = 2 → Does not satisfy the condition → Continues.
# Iteration 2: char = 'e' → charac.count('e') = 3 → Does not satisfy the condition → Continues.
# Iteration 3: char = 'e' → Same as above → Continues.
# Iteration 4: char = 't' → Same as above → Continues.
# Iteration 5: char = 'e' → Same as above → Continues.
# Iteration 6: char = 'r' → charac.count('r') = 1 → Satisfies the condition.
# Prints: First Non rep char: r
# Breaks the loop.