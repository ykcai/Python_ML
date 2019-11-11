import pandas as pd
import numpy as np

print("# Numpy Array Selection\
\n# Go over how to use brackets for selection based off of comparion operators.\n# < > <= >= == etc.\n")

arr = np.arange(1, 11)

print(arr)
# Similar to filter functions in regular Python
bool_arr = arr > 4
print(bool_arr)
# Selecting values from arr that are "True" in the bool_arr
print(arr[bool_arr])
print(arr[arr > 9])
x = 2
print(arr[arr > x])

print("# Arithmetic")
print("# Perform array with array arithmetic, or scalar (normal values, not arrays) with array arithmetics.\n")

lst = [1, 2, 3, 4]
print(lst + lst)
arr = np.arange(0, 10)
# addition
print(arr + arr)
# multiplication
print(arr * arr)
# subtraction
print(arr - arr)
# division - zero division throws NOT A NUMBER warning!
print(arr/arr)
# 1/zero division throws INF warning!
print(1/arr)
# exponents
print(arr ** 3)

print("Universal Array Functions\
\nEssentially just mathematical operations you can use to perform the operation across the array")
# Taking square roots
print(np.sqrt(arr))

# Calculating exponential (e^ - natural number)
print(np.exp(arr))

# Max, Min, etc
print(np.max(arr))

# Trigonometry
print(np.sin(arr))
print(np.cos(arr))
print(np.tan(arr))

# Logarithm
print(np.log(arr))

print("# Practice\n")
mat = np.arange(1, 26).reshape(5, 5)
print(mat)
print("\n[[12, 13, 14, 15]\n\
 [17, 18, 19, 20]\n\
 [22, 23, 24, 25]]")

answer = mat[2:, 1:]
print(answer)

# Introduction to Pandas
# Use pandas for data analysis, basically an extremely powerful version of Excel/Google Sheets just with more features!
# Series, DataFrames, Missing Data, GroupBy, Merging, joining, and Conatenating, Operations, Data Input and Output

print("# Series Defintion:\
\n# Very similar to Numpy array (it is built on top of the Numpy array object). \n# What is different is that series can have axis labels, meaning it can be \n# indexed by a label, instead of just a number location. It also doesn't need to hold numeric data, it can hold any arbitrary Python Object.\n")

labels = ['a', 'b', 'c']
my_list = [10, 20, 30]
arr = np.array([40, 50, 60])
d = {'key1': 70, 'key2': 80, 'key3': 90}

print(pd.Series(data=my_list))
print(pd.Series(data=my_list, index=labels))

print(pd.Series(arr))
print(pd.Series(arr, labels))

print(pd.Series(d))

# Data in a Series
# Pandas Series can hold a variety of object types:

print(pd.Series(data=labels))
print(pd.Series([sum, print, len, max]))

ser1 = pd.Series([1, 2, 0, 3, 4], index=[
                 "USA", "GERM", "ITALY", "USSR", "CHINA"])
ser2 = pd.Series([1, 2, 5, 0, 4], index=[
                 "USA", "GERM", "ITALY", "USSR", "CHINA"])
print(ser1, "\n", ser2)
print(ser1 + ser2)

# DataFrames Defintion:
# The workhorses of pandas and are directly inspired by the R programming language. DataFrames are a bunch of Series objects, put together to share the same index!

np.random.seed(101)
print(np.random.randn(5, 4))
df = pd.DataFrame(np.random.randn(
    5, 4), index='A B C D E'.split(), columns='W X Y Z'.split())
print(df)

# Selection of columns
print(df['W'])
print(df[["W", "Z"]])
# print(df.W) Don't use this syntax!

print(type(df), type(df['W']))
# Creating a new column
df['Michael'] = df["W"] + df["Y"]
print(df)

# Remove existing column/row
# df = df.drop('Michael', axis=1) or the line below
df.drop('Michael', axis=1, inplace=True)
# Drop rows
df.drop('E', axis=0, inplace=True)
print(df)

# Selection of rows
print(df.loc['A'])
#  select based off of position instead of label, 0 indexed
print(df.iloc[2])

# Selecting subset of rows and columns
print(df.loc["B", "Y"])
print(df.loc[['A', 'B'], ['W', "Y"]])
