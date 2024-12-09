# Datatype/Object types:-

1)Number:-1234, 3.14, 0+4i,0b111, decimal(), fraction()
2)String:-'spam',"bob's",b"xa\cdv", u"ax\wed"
3)List:-[1,[2,'three'],3],list(range(10))
4)Tuples:- (1,'spam', 4,'U'), namedTuples, tuple('spam')
5)Dictionary:-{'food':'Rice','fruit':'orange'}, dict(hours=10)
6)Set:-set("abc"), {'a','b','c'}
7)Boolean:-T/F

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

8)file:- open("exist.txt"), open(r'c://.......)
9)None:- none

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#functions, modules, classes
#Advance:
 ->decorators, generator, iterator,metaprogramming

# Numbers:-
>>> 12+23  
35
>>> 1.2*5
6.0
>>> 2**100
1267650600228229401496703205376
>>>
>>>
>>> import math
>>> math.pi
3.141592653589793
>>>
>>> import random
>>> random.random()
0.8460165988897269
>>>
>>> random.choice([1,2,3,4,5])
2
>>> random.choice([1,2,3,4,5])
1
>>> random.choice([1,2,3,4,5])
1
>>> random.choice([1,2,3,4,5])
1
>>> random.choice([1,2,3,4,5])
3
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# String:-
>>> username = "girish"
>>> username
'girish'
>>> len(username)
6
>>> username[0]
'g'
>>> username[-1] 
'h'
>>> username[-2] 
's'
>>> username[1:3] 
'ir'
>>> dir(username)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', ...

# List:-
>>> mylist=[1,"chai", 3.14]
>>> len(mylist)
3
>>> mylist[1]
'chai'

# Dictionary:-
>>> dic={'one':"ginger chai", 'two':"lemon tea"}
>>> len(dic)
2
>>> dic[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 1
>>> dic['one'] 
'ginger chai'
>>> dic['two'] 
'lemon tea'
>>> dic['ginger chai'] 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'ginger chai'

# Tuples:-
>>> tup = (1,"chai",4.14)
>>> tup
(1, 'chai', 4.14)
>>> tup[2] 
4.14
>>> tup[-2] 
'chai'
