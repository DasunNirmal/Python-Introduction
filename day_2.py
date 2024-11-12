# mylist_1 = [10,20,"dasun"];
# mylist_2 = [10,True,"Nirmal"];

# Copy Lists
# mylist_2 = mylist_1.copy();
# print("using copy method",mylist_1);
# print()

# mylist_2 = list(mylist_1);
# print("using list constructor method",mylist_1);
# print()

# Another Way of Extending Lists
# mylist_3 = mylist_1 + mylist_2;
# print(mylist_3);
# print()

# Python Tuples
# my_tuple_1 = ("Dasun",21,True);
# print(my_tuple_1)
# print("Length is :",len(my_tuple_1))
# print(type(my_tuple_1))
# print()

# my_tuple_2 = ("Human")
# print(type(my_tuple_2))
# print()

# Tuples are normaly unchangeable but there is a way
# my_tuple_3 = (50,54,"Dog")
# my_tuple_3[2] = "Cat"
# print(my_tuple_3) #unchangeable

# my_tuple_4 = list(my_tuple_3) # Changin tuple to a list
# my_tuple_4[2] = "Cat"
# print("Type will will be list",type(my_tuple_4))
# my_tuple_3 = tuple(my_tuple_4) # Changing list to a tuple
# print(my_tuple_3)
# print("Type will will be tuple",type(my_tuple_3))
# print()


# Test
# tuple_1 = (10,8,20,5)
# tuple_2 = (5,9,-1)

# tuple_3 = list(tuple_1)
# tuple_3.pop(2) # Removing a element
# tuple_1 = tuple(tuple_3)
# print(tuple_1)

# tuple_4 = list(tuple_1)
# tuple_5 = list(tuple_2)
# extended = tuple_4 + tuple_5 # Extending the Two Tuples
# print("extended tuple",extended)

# extended.sort() # Sorting the New Tuple
# final_tuple = tuple(extended)
# print(final_tuple)


# Nested Tuples
# nested_tuple = ((1,10,8),("Dog","Cat","Rat"),(True,False))
# print(nested_tuple[0][1],nested_tuple[1][2],nested_tuple[2][0])


# Python Range
# r1 = range(2,14,3)
# print(r1,type(r1))
# print(r1[2])

# Python Dictionaries
# dict_1 = {
#     "name":"Suger",
#     "weight":"1kg",
#     "price":120
# }
# print(dict_1)
# print(len(dict_1))
# print(dict_1["price"])

# dict_1["price"] = 560
# print(dict_1)

# To Update a Dictionary
# dict_1.update({"weight":"2kg","price":"240"})
# print(dict_1)

# To Add a new Item
# dict_1["color"] = "white"
# print(dict_1)

# To Add a remove Item
# dict_1.pop("color")
# print(dict_1)

#dict_1.popitem()
#print(dict_1)

#del dict_1["weight"]
#print(dict_1)

#del dict_1
#print(dict_1)

#dict_1.clear()
#print(dict_1)


# Coping Dictionaries
# dict_2 = dict_1.copy()
# print("using the normal way",dict_2)

# dict_2 = dict(dict_1)
# print("using constructor",dict_2)

# dict_3 = {
#     "name":"Dasun",
#     "Address":"Ragama"
# }

# print(dict_3.keys())

# Arithmetic Operators
# a = 17//4
# print(a)

# User Inputs
#x = int(input("Enter a Value :"))
#y = x % 7
#print(y==0)

# Logical Operators

# and operator
# u = 5
# o = 6
# print(u > 1 and o < 10)

# print(u > 5 and o < 10)

# or operator
# k = 5
# l = 6
# print(k > 5 or l < 10)

# not operator
# j = 5
# print(not j > 2)
# print()

# Test
# number = int(input("Enter a Value :"))
# print(number < 100 and number > 0 and number % 2 == 1)

# Identity Operators

# is
# n = 5
# m = 6
# print(n is m)

# is not
# v = 5
# b = 5
# print(n is not m)

# Membership Operators

# in
# z = [10,2,56,5,80]
# print(10 in z)
# print(450 in z)

# not in
# a = [10,2,56,5,80]
# print(10 not in z)
# print(450 not in z)

# Control Flow Statement

# Conditional Statements

# x = 12
# if x % 2 == 0 :
#     print("This is a Even Number")
# else : 
#     print("This is an Odd Number")

# y = 6
# if y < 0 :
#     print("This is a Negetive Number")
# elif y > 0 :
#     print("Thsi is a Positive Number")
# else : 
#     print("This is 0")


# marks = int(input("Enter your marks :"))
# if 85 <= marks <= 100 :
#     print("A")
# elif marks >= 75 :
#     print("B")
# elif marks >= 65 :
#     print("C")
# elif marks >= 55 :
#     print("D")
# elif marks < 45 :
#     print("F")

a = 300
b = 100
c = 1.25

if a > b and a > c :
    print("Largest Number is",a)
elif b > c :
    print("Largest Number is",b)
else :
    print("Largest Number is",c)