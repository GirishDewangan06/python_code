# 7.Function with *args:
# Problem:- Write a function that takes a variable no. of arguments and return their sum.

# def sum_all(args):
#     pass

def sum_all(*args):
    print(args)# it gives me tuples
    return sum(args)

print(sum_all(1,2))
print(sum_all(1,2, 3,4,5))
print(sum_all(1,2,3,4,5,6,7,8))

def sum_all(*args):
    print(args)
    for i in args:
        print(i*2)
    return sum(args)

print(sum_all(1,2,3))