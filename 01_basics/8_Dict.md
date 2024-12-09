# Dictionary:--
>>> dict = {"Masala":"Spicy", "Ginger":"Zesty", "Green":"mild"}
>>> dict
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'mild'}
>>> dict["Masala"]
'Spicy'
>>> dict["Green"]  
'mild'
>>> dict.get("Ginger")
'Zesty'
>>> dict.get("Green")  
'mild'
>>> dict.get("Greeen") 
>>> dict["Greeen"]     
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Greeen'
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

>>> dict["Green"]="Fresh"
>>> dict
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
>>>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

>>> for chai in dict:
...   print(chai)
...
Masala
Ginger
Green
>>> for chai in dict:
...   print(chai, dict[chai]) 
...
Masala Spicy
Ginger Zesty
Green Fresh
>>> for key, value in dict.items():
...   print(key, value)             
...
Masala Spicy
Ginger Zesty
Green Fresh
>>>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
>>> if "Masala" in dict:
...   print("I have Masala Tea")
...
I have Masala Tea
>>>

+++++++++++++++++++++++++++++++++++++++++++++++++
# add new item
>>> dict["Earl Grey"]="Citrus"
>>> dict
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}
>>>
>>>
>>> dict.pop("Masala")
'Spicy'
>>>
>>> dict.popitem()
('Earl Grey', 'Citrus')

>>> dict
{'Ginger': 'Zesty', 'Green': 'Fresh'}
>>>
>>> del dict("Ginger")
  File "<stdin>", line 1
    del dict("Ginger")
        ^^^^^^^^^^^^^^
SyntaxError: cannot delete function call
>>> del dict["Ginger"]
>>> dict
{'Green': 'Fresh'}

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

>>> tea_shop={
... "Chai":{"Masala":"Spicy", "Ginger":"Zesty"},
... "Tea": {"Black":"Strong", "Green": "mild"}
... }
>>> tea_shop
{'Chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Black': 'Strong', 'Green': 'mild'}}
>>>
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
>>> sq_nums= {x:x**2 for x in range(6)}
>>> sq_nums                             
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
>>>
>>>
>>> sq_nums.clear() 
>>>
>>> sq_nums
{}
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
>>>
>>> keys=["Masala","Ginger","Green"]
>>> keys
['Masala', 'Ginger', 'Green']
>>> default=["Delicious"]
>>> default
['Delicious']
>>> new = dict.fromkeys(keys,default)
>>> new
{'Masala': ['Delicious'], 'Ginger': ['Delicious'], 'Green': ['Delicious']}
>>>
>>>
>>>
>>>
>>>
>>>
>>> keys=["Masala","Ginger","Green"]
>>> keys
['Masala', 'Ginger', 'Green']
>>> default="Delicious"  
>>> default
'Delicious'
>>> new = dict.fromkeys(keys,default)
>>> new
{'Masala': 'Delicious', 'Ginger': 'Delicious', 'Green': 'Delicious'}
>>>
>>>
>>> default_2 = ["Spicy","Zesty","Mild"]
>>> default_2
['Spicy', 'Zesty', 'Mild']
>>>
>>> new = dict.fromkeys(keys,default_2) 
>>> new
{'Masala': ['Spicy', 'Zesty', 'Mild'], 'Ginger': ['Spicy', 'Zesty', 'Mild'], 'Green': ['Spicy', 'Zesty', 'Mild']}
>>>