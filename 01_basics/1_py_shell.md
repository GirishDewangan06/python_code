>>python
>>>print("chai")
chai
>>>2*2
4
>>>"chai"*2
chaichai
###########################################################################

>>>score = 100
>>>score
100
###########################################################################

>>>import os
>>>os.getcwd()
c://................

>>>import sys
>>>sys.platform
'win32'

#############################################################
>>>import hello
>>>hello.mycode("Simple")
Simple

>>> hello.one             
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'hello' has no attribute 'one'
>>>##so we have reload for saving, because this only give the saved binaries.
>>> from importlib import reload
>>> reload(hello)
hii Girish
4
<module 'hello' from 'C:\\Users\\GIRISH\\OneDrive\\Desktop\\Python_chai\\01_basics\\hello.py'>

>>>hello.one
'green tea'

>>> hello.three
'ginger Chai'