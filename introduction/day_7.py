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
import pandas as pd

# Crating a DataFrame using dictionary

data = {
    'Name': ['Tom', 'Jerry', 'Mickey', 'Donald'],
    'Age': [20, 21, 22, 23]
}

df = pd.DataFrame(data)
# print("Data Frame",df,"\n",type(df))
# print("Age",df.loc[1, 'Age'])
# print("Location",df.iloc[0, 0])
# print("All Details Related to Index Number\n",df.loc[[0,1]])

# Named Indexes
df = pd.DataFrame(data, index=['A', 'B', 'C', 'D'])
# print(df)
# print("Returns Single row\n",df.loc['A'])
# print("Returns Multiple row\n",df.loc[['A', 'B']])
# print(df['Name'])


# Useful Attributes

# print("Shape",df.shape,"\n")
# print("Columns",df.columns,"\n")
# print("List",list(df.columns),"\n")
# print("Elements",df.size,"\n")
# print("Converted numpy array\n",df.values,"\n",type(df.values),"\n")


# Length of DataFrame

# print("Number Of Rows",len(df),"\n")



# Task
# OrderID,  Product,    Category,       Quantity,    Price,     Regin 
#   101      Laptop       electronics       2          50000     North
#   102      Smartphone   electronics       3          20000     South
#   103      Desk,Chair   Furniture         10         10000     East
#   104      Monitor      electronics       4          10000     West
#   105      Bookshelf    Furniture         2          15000     North

# You are a data anilityst at a e-commerce company. You have been given the above data. Create a DataFrame using the above data.
# Calculate the total revenue for the each order and add a new column total_revenue to store the total revenue for each order.
# Identify the best selling product and find the product with thw hights total sales revenue.

data = {
    'OrderID': [101, 102, 103, 104, 105],
    'Product': ['Laptop', 'Smartphone', 'Desk,Chair', 'Monitor', 'Bookshelf'],
    'Category': ['electronics', 'electronics', 'Furniture', 'electronics', 'Furniture'],
    'Quantity': [2, 3, 10, 4, 2],
    'Price': [50000, 20000, 10000, 10000, 15000],
    'Region': ['North', 'South', 'East', 'West', 'North']
}

order = pd.DataFrame(data)
# print(order,"\n")

order['Total_Revenue'] = order['Quantity'] * order['Price']
# print("<<<---With New Column Total Revenue--->>>\n",order,"\n")

best_selling_rpoduct = order['Product'][order['Total_Revenue'].idxmax()]
# print("Best Selling Product is --->>>",best_selling_rpoduct)

# Methods in Pandas
data = {
    'Salary': [10000, 20000, 30000, 40000],
    'Age': [20, 21, 22, 23]
}
ndf = pd.DataFrame(data)
# print("Mean/Average\n",ndf.mean(),"\n")
# print("Sum\n",ndf.sum(),"\n")
# print("Describe",ndf.describe(),"\n")


# Filtering in Pandas

#  Name,         Age,        Score
#   Tom           20          85
#   Jerry         21          70
#   Mickey        22          90
#   Donald        23          88

data = {
    'Name': ['Tom', 'Jerry', 'Mickey', 'Donald'],
    'Age': [20, 21, 22, 23],
    'Score': [85, 70, 90, 88]
}

dfg = pd.DataFrame(data)
filtered_data = dfg[dfg['Age'] > 20]
# print("Filtered Data\n",filtered_data,"\n",type(filtered_data),"\n")


# Data Manipulation

# A         B
# 1         23
# 2         45

dfv = pd.DataFrame({'A': [1, 2], 'B': [23, 45]})
dfv.loc[len(dfv)] = [3, 67]
# print("Adding a column\n",dfv,"\n")

dfv_dropped_column = dfv.drop('B',axis=1)
dfv_dropped_row = dfv.drop(1,axis=0)
# print("Dropped a column\n",dfv_dropped_column,"\n")
# print("Dropped a row\n",dfv_dropped_row,"\n")



# Read CSV files

df = pd.read_csv('customers-1000.csv')
# print(df,type(df),"\n")



# Read JSON files

dcf = pd.read_json('example_2.json')
print(dcf,type(dcf))