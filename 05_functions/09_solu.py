#generator Function with yield:
# Problem:- write a genrator function that yield even no. up to a specified limit

# limit = 10
# for i in range(2,limit+1, 2):
#     print(i)

# def even_generator(limit):
#     for i in range(2,limit+1, 2):
#         return i
# print(even_generator(10))   
#above gives only 2

# def even_genrator(limit):
#     li =[]
#     for i in range(2,limit+1, 2):
#         li.append(i)
#     return li

# print(even_genrator(10))
#but we dont want list



# def even_generator(limit):
#   for i in range(2,limit+1, 2):
#     print(i)

# for num in even_generator(10):
#   print(num)##non-type obj not iterable

##if we run and weget 2 and after that i run then i want further value not including 2 , that means first result stored in memory ands store different result to differnr memory loc
# (so, we use keyword "yield")

# def even_generator(limit):
#   for i in range(2, limit+1, 2):
#     return i

# print(even_generator(10)) ##it gives memory add of obj even_genrator##

# for num in even_generator(10):
#   print(num)

##########  
def even_generator(limit):
  for i in range(2, limit+1, 2):
    yield i

# print(even_generator(10)) ##it gives memory add of obj even_genrator##

for num in even_generator(10):
  print(num)