# Numbers:-----
>>> x=2
>>> y=3
>>> z=4
>>> x+y
5
>>> 40+2.23
42.23
>>> # its not good to use mismatch datatypes , we can use as below:
>>> int(2.23)
2
>>> float(40
... )
40.0
>>> # here one concept operator overloading:
>>> "chai" + "code"
'chaicode'

>>> x,y,z
(2, 3, 4) 
# we get tuples result
>>>
>>> x+1,y*2
(3, 6)
>>>  
>>>
>>> y%2
1
>>> z**2
16
>>> z**5
1024
>>> x**10
1024
>>> 100**2
10000
>>> 2**100
1267650600228229401496703205376
>>> 2**1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
# python is capable on working with large numbers

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

>>> 1/3.0
0.3333333333333333
>>> # in string , we'll investigate this that tillwhere we want precision.       
>>>
>>> x,y,z
(2, 3, 4)
>>> x<y
True
>>> # internally, python give result in 0/1, but it uses rapr and give boolean values
>>> #CHAIN COMPARISON:-
>>> x<y<z
True
>>> #i.e:-
>>> x<y and y<z
True
>>> 1==2<3
False
>>> 1==2 and 2<3
False
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
>>> True == 1
True
>>> True==1  and 2<3 
True
#it happens but not good

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# trunc:-towards zero & floor:-below number side
>>> import math
>>> math.floor(3.2)
3
>>> math.floor(-3.2) 
-4
>>> math.floor(-3.9)  
-4
>>> math.floor(3.9)  
3
>>>
>>> math.trunc(3.5)
3
>>> math.trunc(-3.5) 
-3

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# complex no.:
>>> 2+3j
(2+3j)
>>> 2+3j*2
(2+6j)
>>> (2+3j)*2
(4+6j)
>>>

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# octal, hexa, & binary nos.:-
>>> 0o100
64
>>> 0xFF
255
>>> 0b1000
8
           (-:OR:-)

>>> int('100',8)       
64
>>> int('64',8)
52
>>> int('64',16) 
100
>>> int('100000000',2)  
256
            (-:OR:-)

>>> oct(64)
'0o100'
>>> hex(255)
'0xff'
>>> bin(64)  
'0b1000000'
>>>
++++++++++++++++++++++++++++++++++++++++++++++++++++++
# bitwise :-
>>> x=1
>>> x<<2
4
++++++++++++++++++++++++++++++++++++++++++++++++++++++
>>> import random
>>> random.random()
0.7509328881786205
>>> random.random()
0.5629602216580798

>>>>>>>># randint 
>>> random.randint(1,10)
9
>>> random.randint(1,10)
3

>>>>>>># random choice:
>>> l1=['lemon','ginger','mint','masala']
>>> l1
['lemon', 'ginger', 'mint', 'masala']
>>> random.choice(l1)
'lemon'
>>> random.choice(l1)
'masala'
>>>
>>> random.choice(l1)
'mint'

>>>>>># random shuffle:
>>> random.shuffle(l1)
>>> l1                 
['mint', 'ginger', 'lemon', 'masala']
>>> random.shuffle(l1)
>>> l1
['ginger', 'lemon', 'masala', 'mint']
>>>

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

>>> from decimal import Decimal
>>> Decimal('0.1')+Decimal('0.1')+Decimal('0.1')
Decimal('0.3')
>>> Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3')
Decimal('0.0')

>>> from fractions import Fraction  
>>> myFra = Fraction(2,7)
>>> myFra
Fraction(2, 7)
>>>


+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# SET:-
>>> setone ={1,2,3,4}
>>> setone
{1, 2, 3, 4}
>>> setone & {1,2,7} #intersection(&)
{1, 2}
>>> setone | {1,2,7} #Union(|)
{1, 2, 3, 4, 7}
>>>
>>> setone - {1,2,3,4}
set()
>>> type({})
<class 'dict'>
>>>

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 # Boolean:-

>>> type(True)
<class 'bool'

>>> True==1
True
>>> False == 0
True
>>> True is 1
<stdin>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
False

>>> True +4
5