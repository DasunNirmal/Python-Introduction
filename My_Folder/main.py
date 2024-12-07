# Importing the entire module
# import my_calculator.addition
# import my_calculator.subtraction

# result_1 = my_calculator.addition.add(5, 3)
# result_2 = my_calculator.subtraction.substrac(20, 4)

# print("result",result_1)
# print("result",result_2)

# Importing the entire module
# from my_calculator import addition
# from my_calculator import subtraction

# result_1 = addition.add(5, 3)
# result_2 = subtraction.substrac(20, 4)

# print("result",result_1)
# print("result",result_2)

# Importing the entire module
# from my_calculator.addition import add
# from my_calculator.subtraction import substrac

# result_1 = add(5, 3)
# result_2 = substrac(20, 4)

# print("result",result_1)
# print("result",result_2)

from my_calculator import add, substrac

result_1 = add(5, 3)
result_2 = substrac(20, 4)

print("result",result_1)
print("result",result_2)