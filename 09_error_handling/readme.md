>>> x = ('masala', 'lemon', 'ginger')
>>> y=enumerate(x) 
>>> y
<enumerate object at 0x00D257D0>
>>> 
##here enumerate helps to give list indexing pair..

>>>list(y)
[(0, 'masala'), (1, 'lemon'), (2, 'ginger')]
>>> 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# There are 2 types of method for file creation and handling:
#method-1:---
> file = open('youtube.text', 'w')

> try:
     file.write("Hii Girish, how are you?")
> finally:
     file.close()

method-2:--##in this syntax , we don't need to close file manually and easy syntax written
>with open('youtube.py', 'w') as file:
    file.write("Hi everyone, I'm girish.")