# inner working:-
|_____________|
| |--|--------|---->score
| |10|--------|--->a_score
|             |
|ref_cou|5|---|->id
|_____________|
 # here ,we assigning 10 and give it refenrce to two variable .
 # if we delete "id" then for optimization the python garbage collector dealloactes "5".

 #  here,  we assigning two variable and otherside assign to one variable. 
 #  so , there is count store in memory(Yes, called "ref_count")
>>> import sys
>>> sys.getrefcount(3) 
1073741823
>>> sys.getrefcount(26401)
3
>>> sys.getrefcount("Girish") 
1073741823
>>> sys.getrefcount("sh")      
1073741823
>>> sys.getrefcount(1)    
1073741823

# Here, python doesn't provide exact ref count. it has loop that give the same values.

# Datatype always assign to objects/memory/values, not to the variable.

# InCase of numbers & string , garbage collector doesn't remove it immediately.

>>> a=5
>>> b=2
>>> a=a+2
>>> a
7
# Here, python memory make an object "7" and allocate its refernce to "a"

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
>> myListOne =[1,2,3]
>>> myListOne
[1, 2, 3]
>>>
>>> myListTwo = myListOne
>>> myListTwo
[1, 2, 3]
>>>
>>> myListOne= "Chai"
>>> myListOne
'Chai'
>>> myListTwo
[1, 2, 3]
># here we can see that we provide "chai" ref to the myListOne, but we can not give to the myListTwo.

>>> myListOne=[1,2,3]
>>> myListOne
[1, 2, 3]
>>> myListTwo
[1, 2, 3]
>>> myListOne[0]=33
>>> myListOne       
[33, 2, 3]
>>> myListTwo
[1, 2, 3]
># here we give new ref to the "mylistOne" , but for myListTwo , its still provide same ref.

>>> L1 = [1,2,3]
>>> L1
[1, 2, 3]
>>> L2=L1
>>> L2
[1, 2, 3]
>>> L1[0]=33
>>> L1
[33, 2, 3]
>>> L2
[33, 2, 3]
># here, we ain't giving other refernce.


>>> p1=[1,2,3]
>>> p1
[1, 2, 3]
>>> p2=p1
>>> p2
[1, 2, 3]
>>> p2=[1,2,3]
# here [1,2,3] and above [1,2,3] are different bcoz of mutable memory storage
>>> p2
[1, 2, 3]
>>> p2[0]=33
>>> p2
[33, 2, 3]
>>> p1
[1, 2, 3]
>>>
># here [1,2,3] and above [1,2,3] are different reference, bcoz of mutable memory storage of list


>>> h1 =[1,2,3]
>>> h1
[1, 2, 3]
>>> h2=h1[:]
 # here we use "Slicing" and created a copy of h1, i.e., h2 has other reference
>>> h2
[1, 2, 3]
>>> h1[0]=33
>>> h1
[33, 2, 3]
>>> h2
[1, 2, 3]

># for copy, we can use "copy" modules 
>>> import copy
>>> h2= copy.copy(h1)
>>> h2= copy.deepcopy(h1)

# for checking the main reference we can use "is"
>>> m=[1,2,3]
>>> m
[1, 2, 3]
>>> n=m
>>> n
[1, 2, 3]
>>> m==n
True
>>> m is n
True
>>> m=[1,2,3]
>>> m==n
True
>>> m is n
False
>#  here "=" is used for checking value is equal or not, "is" , here used for checking reference is equal or not