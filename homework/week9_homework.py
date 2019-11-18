# Machine Learning Class Week 9 Homework
import numpy as np

mat = np.arange(1, 26).reshape(5, 5)
print("MAT: \n", mat)

# Question 1
# With the "mat" matrix, produce the given result in the comments
'''
Output: [[12, 13, 14, 15],
         [17, 18, 19, 20],
         [22, 23, 24, 25]]
'''
print(mat[2:, 1:])

# Question 2
# With the "mat" matrix, produce the given result in the comments
'''
Output: 20
'''
print(mat[3, 4])
# Question 3
# With the "mat" matrix, produce the given result in the comments
'''
Output: [[ 2],
         [ 7],
         [12]]
'''
print(mat[0:3, 1].reshape(3, 1))
# Question 4
# With the "mat" matrix, produce the given result in the comments
'''
Output: [[16, 17, 18, 19, 20],
         [21, 22, 23, 24, 25]]
'''
