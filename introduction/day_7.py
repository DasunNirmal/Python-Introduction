#Python Libraries and Data Processing

# 1. Numpy

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
sumArray = a+b
subArray = a-b
mulArray = a*b


print("Sum",sumArray)
print("Sub",subArray)
print("Mul",mulArray)


# Square root
c = 16
result_sqrt = np.sqrt(c)
print("Square of",c,"-",result_sqrt)

# Maximum and Minimum
result_max = np.max(a)
result_min = np.min(a)
print("Maximum of",a,"-",result_max)
print("Minimum of",a,"-",result_min)