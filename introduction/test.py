# c = 100+5j
# print("the type of variable having value",c,"is",type(c))

# x = 25e4 # 25*10^4
# y = -67.6e100
# print("variable x having value",x,"is",type(x))
# print("variable y having value",y,"is",type(y))

# z = pow(2,3)
# print(z)

# my_list = [1,2,3,4]
# print(len(my_list))

# new_list = list(range(1,10))
# new_list = list(("apple","banana","cherry",1))
# print(new_list)

my_list = [1,2,3,4]
print(my_list[0])
print(my_list[-2])
print(my_list[1:3])
my_list[1] = "dog"
print(my_list)
my_list[1:3] = ["cat","dog"]
print(my_list)
my_list.insert(2,"apple")
print(my_list)
my_list.append("apple")
print(my_list)

new_list = ["Orange","banana","cherry"]
my_list.extend(new_list)
print(my_list)

new_list.remove("banana")
print(new_list)

all_new_list = ["apple","banana","cherry","orange"]
print("removed item is",all_new_list.pop(1))
print(all_new_list)

sorted_list = [5,20,85,10,15,1]
sorted_list.sort()
print(sorted_list)

sorted_list.sort(reverse=True)
print(sorted_list)

sorted_list = ["dog","apple","cat","banana","Rat"]
# sorted_list.sort(key=str.lower)
# print(sorted_list)

sorted_list.reverse()
print(sorted_list)

new_copy = ["apple","banana","cherry"]
co = sorted_list.copy()
print(co)
print("=====================================")

my_tuple = (1,2,3,4)
print(my_tuple[-1])
print(my_tuple[1:3])

x = list(my_tuple)
x[1] = "dog"
# my_tuple = tuple(x)
# print(my_tuple)

new_tuple = (10,20,30,40)
y = list(new_tuple)
y.extend(x)
print(y)

nested_tuple = ((1,2,3),(4,5,6),(True,False))
print(nested_tuple[0][1])
print(nested_tuple[1][1])

print("=====================================")

my_range = range(1,10,2)
print(my_range[2])

print("=====================================")

new_dict = {
    "name":"John",
    "age":30,
    "city":"New York"
}
print(new_dict)

new_dict["name"] = "Jane"
print(new_dict)

new_dict.update({"name":"Dasun"})
print(new_dict)

new_dict["country"] = "Sri Lanka"
print(new_dict)

# new_dict.pop("city")
# print(new_dict)

# new_dict.popitem()
# print(new_dict)

my_dict = new_dict.copy()
print(my_dict)

print("=====================================")

x = 10
y = 20
z = x^y
print(z) 

print("=====================================")

fruits = ["apple","banana","cherry"]

for furit in fruits:
    print(furit)

# for j in range(1,10):
#     print(j)

list1 = [1,2,3,4]
for i in range(len(list1)):
    print(list1[i])

count = 0
while count < 5:
    print("count is",count)
    if count == 3:
        break
    count += 1
else:
    print("loop completed")

print("=====================================")

def my_function(*numbers):
    total = sum(numbers)
    return total
    

print(my_function(10,10))

print("=====================================")


def my_function(**person):
    for key,value in person.items():
        print(f"{key} = {value}")

my_function(name="John",age=30,city="New York")

numbers = [1,2,3,4,5]
def my_function(n):
    return n**2
squared = map(my_function,numbers)
print(list(squared))

print("=====================================")

st_list = ["1","2","3"]
m = list(map(int,st_list))
print(m)

print("=====================================")

new_numbers = [1,2,3,4,5,10,20,30,8]
def is_even(n):
    return n % 2 == 0

even_numbers = filter(is_even,new_numbers)
print(list(even_numbers))
