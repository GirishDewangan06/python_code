# list:-
>>> l1 = ['lemon','mint','Green','Oolng']
>>> l1
['lemon', 'mint', 'Green', 'Oolng']
>>> print(l1[2]
... )
Green
>>> print(l1[-2])
Green
>>> print(l1[1:3]) 
['mint', 'Green']
>>> print(l1[:3])  
['lemon', 'mint', 'Green']
>>>
>>> l1[3]="Herbal"
>>> l1
['lemon', 'mint', 'Green', 'Herbal']
>>> l1[1:2]
['mint']
>>> l1[1:2]="Black"
>>> l1
['lemon', 'B', 'l', 'a', 'c', 'k', 'Green', 'Herbal']
>>>
>>> l1[1:2]=["Black"]# we add as a list
>>> l1
['lemon', 'Black', 'l', 'a', 'c', 'k', 'Green', 'Herbal']
>>>
# we can replace 2 places at a time:-
>>> l1 = ['lemon','mint','Green','Oolng']
>>> l1
['lemon', 'mint', 'Green', 'Oolng']
>>> l1[1:3]
['mint', 'Green']
>>> l1[1:3]=['Black', "Masala"]
>>> l1
['lemon', 'Black', 'Masala', 'Oolng']
>>>
++++++++++++++++++++++++++++++++++++++++++++++++++++++
>>> l1 = ['lemon','mint','Green','Oolng']
>>> l1
['lemon', 'mint', 'Green', 'Oolng']
>>> l1[1:1]
[]
>>> l1[1:3]
['mint', 'Green']
>>> l1[1:1]       
[]
>>> l1[1:1]=["test","test"]
>>> l1
['lemon', 'test', 'test', 'mint', 'Green', 'Oolng']
>>> l1[1:3]
['test', 'test']
>>> l1[1:3]=[]
>>> l1
['lemon', 'mint', 'Green', 'Oolng']
>>>
++++++++++++++++++++++++++++++++++++++++++++++++++++++
# for used in this:-
>>> for tea in l1:
...   print(tea)
...
lemon
mint
Green
Oolng
>>>
>>>for tea in l1:
...   print(tea, end="-")
...
lemon-mint-Green-Oolng->>>
>>>
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
# conditionals:-
>>> if "Black" in l1:
...    print("I have Black tea")
...
>>> l1.append("Black")
>>> l1
['lemon', 'mint', 'Green', 'Oolng', 'Black']
>>> if "Black" in l1:
...    print("I have Black tea")
...
I have Black tea
>>>
>>> l1
['lemon', 'mint', 'Green', 'Oolng', 'Black']
>>> l1.pop() # delete one value of last in list
'Black'
>>> l1
['lemon', 'mint', 'Green', 'Oolng']
>>> l1.remove("mint")
>>> l1
['lemon', 'Green', 'Oolng']
>>>
>>> l1.insert(1,"Ginger")
>>> l1
['lemon', 'Ginger', 'Green', 'Oolng']
>>>

++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++
>>> l1_copy = l1
>>> l1_copy     
['lemon', 'Ginger', 'Green', 'Oolng']
>>> l1
['lemon', 'Ginger', 'Green', 'Oolng']
>>> l1_copy = l1.copy()
>>> l1_copy
['lemon', 'Ginger', 'Green', 'Oolng']
>>> l1
['lemon', 'Ginger', 'Green', 'Oolng']
>>>
# here, the differnce is normal "l1_copy = l1" it menas we provide same refence, but in "l1_copy = l1.copy()", it means we make a copy of that and changes doesn't affect the main list(l1) or changes doesn't reflect #
>>> l1_copy.append('Masala')
>>> l1_copy
['lemon', 'Ginger', 'Green', 'Oolng', 'Masala']
>>> l1
['lemon', 'Ginger', 'Green', 'Oolng']
>>>
+++++++++++++++++++++++++++++++++++++++++++++++++++++
>>> range(10)
range(0, 10)
>>>
>>>
>>> squared_nums = [X**2 for X in range(10)]
>>> squared_nums                              
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>>
>>> cube_nums = [X**3 for X in range(5)]
>>> cube_nums
[0, 1, 8, 27, 64]
>>>
+++++++++++++++++++++++++++++++++++++++++++++++++++++++