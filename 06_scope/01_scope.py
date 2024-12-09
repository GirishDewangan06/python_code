username = "Chaiaurcode"#globally declared

# def func():
#     username = "chai"

# print(username)    ##gives chaiaurcode

# def func():
#     username = "chai"
#     print(username)
# print(username) ## it gives only chaiaurcode bcoz we acnnot call a function(func)   

# def func():
#     username = "chai"
#     print(username)
# print(username) 
# func()
##Chaiaurcode
##chai
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++

# def func():
#     # username = "chai"
#     print(username)
# print(username)
# func()    
# ##Chaiaurcode
# ##Chaiaurcode
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# x = 99

# def func2(y):
#     z= x+y
#     return z
# result = func2(1)
# print(result) ##100

# ++++++++++++++++++++++++++++++++++++++++++++++++++

#overwrite global var
# x=99
# def func3():
#     global x
#     x=19
# func3()    
# print(x)

# x=99
# def f1():
#     # x=88
#     def f2():
#         print(x)
#     f2()    
# f1()    
##88->bcoz it climbe to upward side

##++closure/factory function:-
# def f1():
#     x=88
#     def f2():
#         print(x)
#     return f2 #->here, it takes all definition of f2 with memory referce,f2()->function execution
# myResult = f1()    
# myResult()

def chaicoder(num):
    def actual(x):
        return x**num
    return actual

print((chaicoder(5)))

f= chaicoder(2)##here it return actual function and referred by f
g= chaicoder(3)


print(f)
print(g)

print(f(5))##it takes memory refernce of actual with chaicoder(num) and holds it refernce
print(g(5))##it takes memory refernce of actual with chaicoder(num) and holds it refernce

# The connection lies in closures: f "remembers" the value of num (2) from the chaicoder call. So, f(5) applies the logic of actual with the preserved value of num.