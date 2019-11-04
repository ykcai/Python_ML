# Numpy Array Attributes and Methods
from numpy.random import randn
import pandas as pd
import numpy as np
import random

arr = np.arange(25)
ranarr = np.random.randint(0, 50, 10)

print(arr)
print(ranarr)

print(arr.reshape(5, 5))
# max() | min() returns the max and min
# argmax() | argmin() returns the index of the max and min

print(ranarr.max(), ranarr.min())
print(ranarr.argmax(), ranarr.argmin())

print(arr.reshape(1, 25))
print(arr.reshape(1, 25).shape)

print(arr.reshape(25, 1))
print(arr.reshape(25, 1).shape)

# dtype
# You can grab the data type of the object in the array

print(arr.dtype)

# Numpy Indexing and Selection
# Discuss how to seelct elements or groups from an array

arr = np.arange(0, 11)

# Get a value at an index
print(arr[8])

# Get values in a range
print(arr[1:5])
print(arr[0:8])

# Broadcasting
# Numpy arrays differ from a normal Python list because of their ability to broadcast

# Setting a value with index range (Broadcasting)
arr[0:5] = 100
print(arr)

# Reset to remove broadcast
arr = np.arange(0, 11)
print(arr)

slice_of_arr = arr[0:6]
print(slice_of_arr)

slice_of_arr[:] = 99
print(slice_of_arr)
# Data is not copied, it's a view of the original array!
# This avoids memory problems!
print(arr)

# To get a copy, need to be explicit
arr_copy = arr.copy()
arr_copy[0:3] = 909
print("arr_copy: ", arr_copy)
print("arr: ", arr)

# Indexing a 2D array (matrices)
# General format is arr_2drow or arr2drow,col.
# Use the comma notation for clarity

arr_2d = np.array([[5, 10, 15],
                   [20, 25, 30],
                   [35, 40, 45]])
print(arr_2d)

# Indexing a row
print(arr_2d[1])

# Format is arr_2d[row][col] or arr_2d[row,col]
# Getting an individual element value
print(arr_2d[1, 0])
print(arr_2d[2, 2])
print(arr_2d[2, 0])

# 2D array slicing
# Shape (2,2) from top right corner
print(arr_2d[:2, 1:])

print(arr_2d[2, :])
# The above and below are the same, grabs all columns
print(arr_2d[2])

# Using numpy with pandas
np.random.seed(101)

df = pd.DataFrame(randn(5, 4), index="A B C D E".split(),
                  columns="W X Y Z".split())
print(df)

# Fancy Indexing
# Fancy indexing allows you to select entire rows or colums OUT OF ORDER

# Set up matrix
# arr2d = np.zeros((10, 10))
arr2d = np.array([np.random.randint(1, 10, 10), np.random.randint(
    1, 10, 10), np.random.randint(1, 10, 10), np.random.randint(1, 10, 10)])
print(arr2d)

# Length of the array
# arr_length = arr2d.shape[1]

# Set up array
# for i in range(arr_length):
#     arr2d[i] = i

print(arr2d[[2, 3]])
print(arr2d[[2, 3], 4])
print(arr2d[[3, 1, 2], [8, 4, 7]])
