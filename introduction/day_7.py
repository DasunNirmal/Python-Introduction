#Python Libraries and Data Processing

# 1. Numpy

import numpy as np
import pandas as pd

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
# print("Array 2D",array_1)
# print("Dimantion",array_1.shape)
# print("Data type",array_1.dtype)
# print("Direct Dimatoin",array_1.ndim)

array_2 = np.array([[[1,2,5],[2,3,5]], [[3,4,4],[5,8,8]]])
# print("Array 3D",array_2)
# print("Dimantion",array_2.shape)
# print("Data type",array_2.dtype)
# print("Direct Dimatoin",array_2.ndim)

# Numpy Indexing
# print('2nd Elemt on 1st row',array_1[0,1])


# Task
#1.create a 2d numpy arrray which has daimentions 4,5 which contains the numbers 1 to 20
array_3 = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
# print("2D Array:\n", array_3)

# Add 10 to every element
array_add_10 = array_3 + 10
# print("Array after adding 10:\n", array_add_10)

# Multiply every element by 2
array_multiply_2 = array_3 * 2
# print("Array after multiplying by 2:\n", array_multiply_2)

# Calculate square of each element
array_square = np.square(array_3)
# print("Array after squaring each element:\n", array_square)


# Boolean indexing in numpy
array_4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# condition = array_4 > 5
# print(condition)
# print("Elements greater than 5:", array_4[condition])

filtered_array = array_4[array_4 > 5]
# print("Filtered Array:", filtered_array)

filtered_combined = array_4[(array_4 > 5) & (array_4 < 10)]
# print("Filtered Combined Array:", filtered_combined)


# Array Initialization

array_5 = np.zeros(4, dtype=int, order='C')
array_6 = np.zeros((2, 3))
# print("Array of zeros:", array_5)
# print("Array of zeros 2D:", array_6)

array_7 = np.full(4, 5)
array_7 = np.full((2, 3), 5)
# print("Array of full:\n", array_7)
# print("Array of full 2D:\n", array_7)

array_8 = np.empty((2, 3))
# print("Empty Array:\n", array_8)


# Task
# Create a numpy 1D array with values form 1-20 use boolean indexing to get the even numbers
# Create a numpy 1D array with values form 10-20-30-40-50 use boolean indexing to get the grater than mean of the array

array_9 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
filtered_even = array_9[array_9 % 2 == 0]
# print("Filtered Even Array:", filtered_even)

array_10 = np.array([10, 20, 30, 40, 50])
filtered_greater = array_10[array_10 > np.mean(array_10)]
# print("Filtered Greater Array:", filtered_greater)


# 2. Pandas