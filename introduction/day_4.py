def myFunctionAribitraryPosition(*args):
    print(args, type(args))

# myFunction(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);


def summaries_grades(name, *marks):
    if len(marks) < 1 :
        print("No marks found")
        return
    print("Student",name)
    print("Max",max(marks))
    print("Min",min(marks))
    print("Average",sum(marks) / len(marks))

# summaries_grades("Dasun", 10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

def myFunctionAribitraryKeyWord(**kwargs):
    print(kwargs, type(kwargs))

# myFunctionAribitraryKeyWord(name="Dasun", age=21, country="Sri Lanka",address="Ragama")

def employee_info(name, **kwargs):
    print("Employee Name", name)
    for key, value in kwargs.items():
        print(f'{key} = {value}')
    kwargs['name'] = name
    print("Employee Info", kwargs)

# employee_info("Dasun", age=21, salary=20000,phone_number='0715744202')

# Built In FUnctions
# abs()
# map()
# filter()

# print(abs(-152))

# Map
def find_square(num):
    return num * num
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = map(find_square, my_list)
# print(result)
# print(list(result))

list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]

def sum_lists(a, b):
    return a + b

result = map(sum_lists, list1, list2)
newlist = list(result)
# print(newlist)

# Celsius to Fahrenheit
temp = [20.30,40.50]

def fahrenheit(celsius):
    return celsius * 9/5 + 32

result = map(fahrenheit, temp)
# print(list(result))


# Filter

# Filter the odd numbers from the list
random_list = [5,7,8,3,12,14]

def is_even(num):
    return num % 2 != 1
result = filter(is_even, random_list)
# print(list(result))


# Lambda Functions

# Lambda with assigning to a variable
sum = lambda x,y: x + y
# print(sum(10,20))

# Call the lambda function directly
result = (lambda x,y: x + y)(10,20)
# print(result)

# Filter the people who are above 18 years old
people = [["John", 15], ["Doe", 25], ["Jane", 18], ["Smith", 30]]
# print(list(filter(lambda age: age[1] >= 18,people)))

def myFunction(x):
    return lambda a: a * x

myDoubleer = myFunction(2)
# print(myDoubleer(11)) # 22

max_number = lambda a,b : max(a,b)
# print(max_number(10,20))


def factorial(n):
    if n == 0:
        return 1
    for i in range(1, n):
        n *= i
    return n

# print(factorial(5)) 

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
# print(factorial_recursive(10))

# Find the sum of the list using recursive function
recursoin_list = [10,20,30]
def sum_of_list_recursive(recursoin_list):
    if len(recursoin_list) == 0:
        return 0 
    return sum(recursoin_list[0],sum_of_list_recursive(recursoin_list[1:]))
print(sum_of_list_recursive(recursoin_list)) 