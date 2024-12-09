# Tuples:--
>>>
>>> tea_types =("Black", "Ginger", "Oolong")
>>> tea_types
('Black', 'Ginger', 'Oolong')
>>> tea_types[0]
'Black'
>>> tea_types[-1] 
'Oolong'
>>> tea_types[1:2] 
('Ginger',)
>>> tea_types[1:1] 
()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>>
>>> more_tea =("Herbal", "Earl Grey")
>>> more_tea
('Herbal', 'Earl Grey')
>>> all_tea = more_tea + tea_types
>>> all_tea
('Herbal', 'Earl Grey', 'Black', 'Ginger', 'Oolong')
>>>
>>>
>>>
>>> if "Ginger" in all_tea:
...   print("I have Ginger Tea")
...
I have Ginger Tea
>>>
++++++++++++++++++++++++++++++++++++++++++
>>> diff_tea = ("Herbal","Earl Grey", "Herbal")
>>> diff_tea
('Herbal', 'Earl Grey', 'Herbal')
>>> diff_tea.count("Herbal")
2
>>> diff_tea.count("Herbals") 
0
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# we can assign variable to each items values
>>> tea_types
('Black', 'Ginger', 'Oolong')
>>> (one,two,three)=tea_types
>>> one
'Black'
>>> three
'Oolong'
>>>
>>> type(tea_types)
<class 'tuple'>
>>>     
