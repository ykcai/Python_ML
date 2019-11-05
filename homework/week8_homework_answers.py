# Machine Learning Class Week 8 Homework

import numpy as np

# 1. Create an array of 10 zeros
print(np.zeros(10))

# 2. Create an array of 10 ones
print(np.ones(10))

# 3. Create an array of 10 fives
print(np.ones(10) * 5)

# 4. Create an array of the integers from 10 to 50
print(np.arange(10, 51))

# 5. Create an array of all the even integers from 10 to 50
print(np.arange(10, 51, 2))

# 6. Create a 3x3 matrix with values ranging from 0 to 8
print(np.arange(9).reshape(3, 3))

# 7. Create a 3x3 identity matrix
print(np.eye(3))

# 8. Use NumPy to generate a random number between 0 and 1
print(np.random.rand(1))

# 9. Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
print(np.random.randn(25))

# 10. Create an array of 20 linearly spaced points between 0 and 1.
print(np.linspace(0, 1, 20))
