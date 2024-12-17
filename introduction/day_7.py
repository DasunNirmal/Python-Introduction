#Python Libraries and Data Processing

# 1. Numpy

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
sumArray = a+b
subArray = a-b
mulArray = a*b

# print("Sum",sumArray)
# print("Sub",subArray)
# print("Mul",mulArray)


# Square root
c = 16
result_sqrt = np.sqrt(c)
# print("Square of",c,"-",result_sqrt)

# Maximum and Minimum
result_max = np.max(a)
result_min = np.min(a)
# print("Maximum of",a,"-",result_max)
# print("Minimum of",a,"-",result_min)

# Multidimanional Array
array_1 = np.array([[1, 2], [3, 4]])
print("Array 2D",array_1)
print(array_1.size)

array_2 = np.array([[[5, 6], [7, 8], [9, 10]]])
print("Array 3D",array_2)
print(array_2.size)