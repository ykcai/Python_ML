# Machine Learning Class Week 9 Homework Answers
import numpy as np

mat = np.arange(1, 26).reshape(5, 5)
print(mat)
'''0  1  2  3  4 
[[ 1  2  3  4  5] 0
 [ 6  7  8  9 10] 1
 [11 12 13 14 15] 2
 [16 17 18 19 20] 3
 [21 22 23 24 25]]4
'''
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
print(mat[3:])
