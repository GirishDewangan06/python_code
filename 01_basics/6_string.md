# Strings:-
>>> chai ="Lemon Chai"
>>> chai
'Lemon Chai'
>>> print(chai)
Lemon Chai
>>> 
>>> first_char = chai[0]
>>> print(first_char) 
L
>>> 
>>> slicing_chai = chai[:6]
>>> print(slicing_chai)
Lemon 
+++++++++++++++++++++++++++++++++++++++++++++++
>>> num_list = "0123456789"
>>> num_list
'0123456789'
>>> num_list[:]
'0123456789'
>>> num_list[3:] 
'3456789'
>>> num_list[3:7] 
'3456'
>>> num_list[0:7:2] 
'0246'
>>> num_list[0:7:3] 
'036'
>>> num_list[0:7:-1] 
''
+++++++++++++++++++++++++++++++++++++++++
>>>>>>>>>># lower/upper:-
>>> chai = "Masala Chai"
>>> chai.lower()
'masala chai'
>>> chai.upper()  
'MASALA CHAI'

+++++++++++++++++++++++++++++++++++++++++
>>># strip:-
>>> chai = "      Masala Chai      "
>>> chai
'      Masala Chai      '
>>> print(chai.strip())
Masala Chai
>>>
++++++++++++++++++++++++++++++++++

>>>>>>>>># replace:-
>>> chai = "Masala Chai" 
>>> chai
'Masala Chai'
>>> print(chai.replace("Masala", "ginger")
... )
ginger Chai
>>> chai
'Masala Chai'
>>>
+++++++++++++++++++++++++++++++++++++++++++++++++++

# split(",")
>>> chai= "Lemon, Mint, Masala, Ginger"
>>> chai
>>> print(chai.split())
['Lemon,', 'Mint,', 'Masala,', 'Ginger']
>>>
'Lemon, Mint, Masala, Ginger'
>>> print(chai.split(", "))
['Lemon', 'Mint', 'Masala', 'Ginger']
>>>
++++++++++++++++++++++++++++++++++++++++++++++++++++++

# find:-
>>> chai="Masala Chai"
>>> chai
'Masala Chai'
>>> print(chai.find("Chai")) 
7
>>>
>>> print(chai.find("chai"))
-1  #notfound = -1
++++++++++++++++++++++++++++++++++++++++++++++++

# count:-
>>> chai ="Masala Chai Chai Chai"
>>> chai
'Masala Chai Chai Chai'
>>> chai.count("Chai")
3
>>> chai.count("chai") 
0
>>>
+++++++++++++++++++++++++++++++++++++++++++++++

# format
>>> chai_type="Masala"
>>> quantity =2
>>> order = "I have ordered {} cups of {} chai"
>>> order
'I have ordered {} cups of {} chai'
>>> print(order.format(quantity,chai_type))
I have ordered 2 cups of Masala chai
>>>
++++++++++++++++++++++++++++++++++++++++++++++++++++
# list to string(.join)
>>> l1= ["Lemon","Ginger","Mint"]  
>>> l1
['Lemon', 'Ginger', 'Mint']
>>> print(" ".join(l1))
Lemon Ginger Mint
>>> print("-".join(l1)) 
Lemon-Ginger-Mint
>>> print(",".join(l1)) 
Lemon,Ginger,Mint
++++++++++++++++++++++++++++++++++++++++++++++++
>>># length/ letter print
>>> chai ="Masala Chai"
>>> chai
'Masala Chai'
>>> len(chai)
11
>>>
>>> for letter in chai:
...   print(chai)# "it printed chai["Masala Chai"] letters till the no. of letters in chai"
...
Masala Chai
Masala Chai
Masala Chai
Masala Chai
Masala Chai
Masala Chai
Masala Chai
Masala Chai
Masala Chai
Masala Chai
Masala Chai
>>> for letter in chai:
...   print(letter)
...
M
a
s
a
l
a

C
h
a
i
>>>
+++++++++++++++++++++++++++++++++++++++++++++++++++++
# double coat 2 times:-
>>> chai = "he said,"its awesome" "
  File "<stdin>", line 1
    chai = "he said,"its awesome" "
                     ^^^
SyntaxError: invalid syntax
>>> chai = "he said,\"its awesome\" " 
>>> chai
'he said,"its awesome" '
>>>
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
>>> chai = "Masala\nChai"
>>> chai
'Masala\nChai'
>>> print(chai)
Masala
Chai
00000000000000000000000000000000000000000000000000000000
>>># it  happens and that create lots of difficult in like:
>>> chai = "c:\\user\\pwd"
>>> chai
'c:\\user\\pwd'
>>> print(chai)
c:\user\pwd
00000000000000000000000000000000000000000000
>>> chai = r"c:\user\pwd" # r'->indicates raw srings
>>> chai
'c:\\user\\pwd'
>>> print(chai)
c:\user\pwd
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

>>> chai ="Masala Chai"
>>> chai
'Masala Chai'
>>> print("Masala" in chai) 
True
>>> print("Masaala" in chai)  
False