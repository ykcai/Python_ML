# Introduction to NumPy
# NumPy or numpy is Linear Algebtra Library for Python
# Numpy is built on C libraries which makes it extremely fast for certain computations

import numpy as np

# Numpy Arrays

# Numpy arrays come in two flavors: vectors and matrices.
# Vectors are strictly 1-d arrays.
# Matrics are 2-d arrays, they have still be 1-d though.

# Vector
my_list = [1, 2, 3]
print(my_list)
np_list = np.array(my_list)
print(np_list)

# Matrix
my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
np_matrix = np.array(my_matrix)
print(np_matrix)

# Built-in Methods
# arange
print(np.arange(0, 10))
print(np.arange(0, 11, 2))

# zeros and ones
print(np.zeros(3))
print(np.zeros((5, 5)))
print(np.ones(3))
print(np.ones((3, 3)))

# linspace
print(np.linspace(0, 1, 20))

# eye
print(np.eye(4))

# Random
# rand - [0,1) uniform distribution
print(np.random.rand(2))
print(np.random.rand(5, 5))

# randn - standard normal distribution
print(np.random.randn(2))
print(np.random.randn(4, 4))

# randint - low (inclusive) high (exclusive)
print(np.random.randint(1, 100))
print(np.random.randint(1, 100, 10))
print(np.random.rand(1, 100, 10))
