#9. List Uniqueness Checker
# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

items = [ "banana", "orange","mango", "apple", "mango"]

unique_item= set()

for i in items:
    if i in unique_item:
        print("Duplicate:", i)
        break
    else:
        unique_item.add(i)