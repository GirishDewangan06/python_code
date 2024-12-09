  
                         (send query to apply
|---------------------|    loop on iter. obj)    |------------------------------|
|  (iteration tool)   |------------------------->|   (iterable Object)          |
|   -for              |      iter()#method       |   -list                      |
|   -comprehensive    |                          |   -file                      |   
|_____________________|                          |______________________________|
do{     |                                                     | 
 next() |                                                     |(point only on start loc)
 next() |                                                     |(we get memory add at start)
 next() |                                                     |
}, till |                                                     |
exceptin|          |---------------|                          |
 raise  |--------->|  __next__     |<-------------------------|
                   |_______________|#response
                   (here it check or apply loops 
                   for further values)

>>> f = open('code.py')## file loaded in variable
>>> f.readline()
'import time\n'
>>> f.readline()
'\n'
>>> f.readline()
'print("Hi, Everyone!!")\n'
>>> f.readline()
'username = "Girish"\n'
>>> f.readline()
'print(username)'
>>> f.readline() ## exception raise
''
>>> f.readline()
''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##use core syntax for iteration:--"__next__()"
>>> f = open('code.py')
>>> f.__next__()
'import time\n'
>>> f.__next__()
'\n'
>>> f.__next__()
'print("Hi, Everyone!!")\n'
>>> f.__next__()
'username = "Girish"\n'
>>> f.__next__()
'print(username)'
>>> f.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration 
>##exception raise by providingg string

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

## file is a iterable object, then we can use loop:- open() use to make iterable
for line in open('code.py'):
...   print(line)
...
import time


print("Hi, Everyone!!")

username = "Girish"

print(username)
>>> ## how python knows that after this '', we stop,.bcozof iterable tools(for)->here, at the time of making, makers already done programming#

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

>>> f = open('code.py')
>>> while True:
...   line = f.readline()
...   if not line: break
...   print(line, end='')
... 
import time

print("Hi, Everyone!!")
username = "Girish"
print(username)>>>

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

>>> test = "Girish" 
>>> if not  test:   
...   print("chai")
...
>>> test = ""       
>>> if not  test:   ## it just checked empty line
...   print("chai") 
...
chai
>>>
>>> myList = [1,2,3,4]
>>> I = iter(myList)
>>> I
<list_iterator object at 0x00B53A90>
>>> I.__next__()
1
>>>
>>> I.__next__()
2
>>> I.__next__()
3
>>> I
<list_iterator object at 0x00B53A90>
# iterable obj always point from starting with new ref add memory
>>> I = iter(myList)
>>> I.__next__()       
1
>>> I.__next__()
2
>>> I.__next__()
3
>>> I
<list_iterator object at 0x00B53478>
>>> I.__next__()
4
>>> I.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
++++++++++++++++++++++++++++++++++++++++++++++++++++++
## differnce b/w FILE & LIST:
#file has bydefault iter()obj if you assign in Variable(f)/
#if you stored file in var.,i.e,it's iter() obj itself 
>>> f = open('code.py')
>>> iter(f) is f
True
>>> iter(f) is f.__iter__()
True
>>>
#List :- if you assign in var that not means iter()obj 
#if you give memory ref to list , that not means it has iter() obj, it's only actual file refernce 
>>> myList = [1,2,3,4]
>>> iter(myList) is myList
False
>>> iter(myList) is myList.__iter__()
False

+++++++++++++++++++++++++++++++++++++++++++++++

>>> D={'a':1, 'b':2}
>>> for key in D.keys():
...   print(key)
...
a
b
>>> I = iter(D)  
>>> I
<dict_keyiterator object at 0x0150AB68>
>>> next(I)
'a'
>>> next(I)
'b'
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>>

+++++++++++++++++++++++++++++++++++++++

>>> range(5)
range(0, 5)
>>> R=range(5) 
>>> R
range(0, 5)
>>> I = iter(R)
>>> I
<range_iterator object at 0x00B53B00>
>>> next(I)
0
>>> next(I)
1
>>> next(I)
2
>>> next(I)
3
>>> next(I)
4
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>

##XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX##