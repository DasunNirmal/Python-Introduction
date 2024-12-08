## Ternary Operator
# It simply allows to test a condition in a single line replacing the multiline if-else making the code compact.

# x = 10
# result = "Even" if x % 2 == 0 else "Odd"
# print(result)


# z = int(input("Enter a number: "))
# result = "OK" if z % 2 == 0 and z % 3 == 0 else "Not OK"
# print(result)

## Swticth Case Statement
# Python does not have switch case statement. We can use dictionary to implement switch case statement.

# response_code = 200

# match response_code:
#     case 200:
#         print("OK")
#     case 201:
#         print("Created")
#     case 404: 
#         print("Not Found")
#     case 500: 
#         print("Internal Server Error")
#     case _:
#         print("Unknown Error")

# x = int(input("Enter a number: "))

# match x:
#     case x if x == 0:
#         print("Zero")
#     case x if x == -1:    
#         print("Negative One")
#     case x if x == 1:
#         print("Positive One")
#     case x if x > 1: 
#         print("Positive number is greater than 1")
#     case x if x < 0:
#         print("Negative number is less than 0")
#     case _:
#         print("Unknown")

# number = [4, 5, 6]

# match number:
#     case [x, y]:
#         print(x*y)
#     case [x, y, z]:
#         print(x+y+z)
#     case _:
#         print("Unknown")

# myList = [4,5]

# match myList:
#     case []:
#         print("Empty List")
#     case [x]:
#         print("List with one element")
#     case [x, y]:
#         print("List with two elements")
#     case _:
#         print("Unknown")

# ### Loops

# Loops are fundamental programming constructs that allow us to repeat a block of code as long as a condition is True.  

## For Loop

# for i in range(5): # range(5) returns a sequence of numbers starting from 0 to 4

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)     


# myList = [1, 2, 3, 4, 5]

# newList = []

# for i in myList:
#     newList.append(i*i)

#     print(newList)

## List Comprehension

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# #[x**2 for x in range(1, 11) if x % 2 == 0]

# print([x*x for x in range(1, 11) if x % 2 == 0])

## While Loop

#The while loop is used to execute a block of code as long as the condition is True.

# m = 5
# i = 0;

# while i < m:
#     print(i, end=" ")
#     i += 1
# print("End")

# x = int(input("Enter a number: "))
# y = 2
# while y < x:
#     if y == 10: # if y is equal to 10, break the loop, we can use break statement to exit the loop
#         break
#     print(y)
#     y += 2

# sum = 0;
# x = 0;
# while True:
#     sum = sum + x;
#     x = int(input("Enter a number: "))
#     if x <= 0:
#         break
# print(sum)


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for x in my_list:
#     if x % 2 == 1:
#         print(x)

# # Unpacking
# # Unpacking is a way to assign the elements of an iterable to multiple variables in a single statement.

# my_list2 = [1, 2, 3]
# x, y, z = my_list2

# print(x, y, z)

#Dictionary Unpacking

# person = {"name": "John", "age": 25}

# {name, age} = person

# print(name, age)

# above code will give an error because dictionary unpacking is not supported in python.

# To unpack a dictionary, we can use the items() method.

# person = {"name": "John", "age": 25}

# for key, value in person.items():
#     print(key, value) #this will print the key value pair of the dictionary

# for value in person.values():
#     print(value) #this will print the values of the dictionary

# my_dict = {"a": 1, "b": 3, "c": 8}

# print(my_dict.get("a")) #this will print the value of key a

# print(my_dict.get("d", "Not found")) #this will print None because key d is not present in the dictionary


### Python fuction declaration

# def function_name(parameters):
#     # statements
#    return value

#def: keyword to declare a function
#function_name: name of the function
#parameters: input to the function
#return: keyword to return a value from the function

# def sum(a, b): #function to add two numbers
#     return a + b #return the sum of two numbers

# print(sum(5, 10)) # when calling the function, it will return 15

# PI = 22/7 #this is a global variable

# def calculate_area(r): #this function will calculate the area of a circle
#     return (PI) * (r ** 2) #

# print(calculate_area(5)) 

# Calculate the mean of a list of numbers

# number_list = [1, 2, 3, 4, 5]

# def mean(number_list):
#     return sum(number_list) / len(number_list)

# print(mean(number_list))

# def mean1(list):
#     total = 0
#     for x in list:
#         total += x  
#     return total / len(list)

# print(mean1(number_list))

# my_list = [10, 2, 5, 8, 9, 11, 13]

# print(my_list[1:5:1]) #this will print [2, 5, 8, 9]
# print(my_list[1:6:2]) #this will print [2, 8, 11]

## Python function arguments
# add_two_numbers(5, 10) 5 and 10 are arguments

##Default arguments
# A default argument is an argument that assumes a default value if a value is not provided in the function call for that argument.

# def greet(name, message="Good Morning!"):
#      return f"Hello {name}, {message}"

# print(greet("John")) #this will print Hello John, Good Morning!

# Any number of arguments in a function can have a default value. But once we have a default argument, all the arguments to its right must also have default values.

##Keyword arguments

# Keyword arguments are arguments that are passed by name. We can pass the arguments in any order.

# def greet(name, message):
#     return f"Hello {name}, {message}"

# print(greet(message="Good Morning!", name="John")) #this will print Hello John, Good Morning!


# Define a function calculate_total_cost, with the parameters:
# item_price: mandatory, price of the item
# quantity: mandatory, quantity of the item
# discount: optional, discount percentage on the item price, default value is 0.
# tax: optional, tax percentage on the total cost, default value is 0.
# ** Note: A discount is applied first, then tax is applied on the discounted price.

# def calculate_total_cost(item_price, quantity, discount=0, tax=0):
#    subTotal = (item_price * quantity)
#    discountedTotal = subTotal - (subTotal * discount / 100)
#    finalTotal = discountedTotal + (discountedTotal * tax / 100)
#    return finalTotal

# print(calculate_total_cost(100, 1, 10, 5)) 