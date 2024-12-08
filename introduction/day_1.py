# 2024/11/5
# variable rules

# variable1 - ok
# _variable - ok
# 1variable - wrong

# normally we are not use CAPITAL letters for variables but when we considering about constant we use capital letters
# PI_VALUE = 3.14

# python data types
# Numeric: int,float,complex(2+3i)
# String: str
# Sequence Types (multiple values in one variable like java array in python no arrays we use sequence): list,tuple, range
# binary: bytes,bytearray,memoryview
# mapping: dict
# Boolean: bool
# set data type: set, frozenset

# int: unlimited data size
# float: 15 decimal places
# complex: hold complex numbers


# python list

my_list = [1,2,3,4]
print(my_list,type(my_list))
# my_list[5] #to access list index

# my_list[5] = 10 #assign index  to new value

my_list = [1,"abc","3",True]


# python list allows duplicate.python list can have any type of data.
# To find a length of a list we use print(len(my_list)).
print(len(my_list))
print(my_list[-2])


# get 3 middle values from a list
print(my_list[1:4])
# using these syntax we can get 1 to 3 values. we put 1 number more than the index we want,


print(my_list[:4])
# this is start with index 0 to index 3

my_list[2:4] = ["Dog",19.0]
print(my_list)
# using above one line we can assign 2 values to the list

my_list.insert(2,"Dog")
print(my_list)
# to insert new item value to list (any place of list)

my_list.append("car")
print(my_list)
# to insert a value to end of the list

new_list = [1,10,10,"cat",]
my_list.extend(new_list)
print(my_list,len(my_list)) 
# to merge two list (extend the list)

my_list.pop(2)
# if we want to remove a specific element "2" is the index number

del my_list[2]
print(my_list) 
# also we use this method for delete a value from a list

my_list.clear()
# we can clear whole array by this method

my_list = ["green","red","blue","cat","dog","apple"]
my_list.sort()
print(my_list)
# can sort the list this is case sensitive

my_list = ["green","red","blue","cat","dog","apple"]
my_list.sort(key=str.lower)
print(my_list)
# by using this we can turn off case sensitive

my_list = ["green","red","blue","cat","dog","apple"]
my_list.sort(reverse=True)
print(my_list)
# Reverse the order of the list

my_list = ["green","red","blue","cat","dog","apple"]
my_list.reverse()
print(my_list)
# change the full order like above method
