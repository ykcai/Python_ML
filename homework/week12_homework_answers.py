# Machine Learning Class Week 12 Homework Answers
# 1. Calculate the Median
# Create a function that takes a list of numbers and return its median. If the input list is even length, take the average of the two medians, else, take the single median.
# Examples

# median([2, 5, 6, 2, 6, 3, 4]) ➞ 4
# median([21.4323, 432.54, 432.3, 542.4567]) ➞ 432.4
# median([-23, -43, -29, -53, -67]) ➞ -43

# Notes: Input can be any negative or positive number. Input list will contain at least four numbers.

# Without Numpy
def median(nums):
    nums.sort()
    n = len(nums)
    m = n // 2
    if n % 2 == 0:
        return (nums[m - 1] + nums[m]) / 2
    else:
        return nums[m]


# With Numpy
import numpy as np

def median_numpy(lst):
    return np.median(lst)

print(median([2, 5, 6, 2, 6, 3, 4]))
print(median([21.4323, 432.54, 432.3, 542.4567]))
print(median([-23, -43, -29, -53, -67]))

print(median_numpy([2, 5, 6, 2, 6, 3, 4]))
print(median_numpy([21.4323, 432.54, 432.3, 542.4567]))
print(median_numpy([-23, -43, -29, -53, -67]))

# 2. Sort Numbers in Descending Order
# Create a function that takes any non-negative number as an argument and returns it with its digits in descending order. Descending order is when you sort from highest to lowest.
# Examples
# sort_decending(123) ➞ 321
# sort_decending(1254859723) ➞ 9875543221
# sort_decending(73065) ➞ 76530

# Notes: You can expect non-negative numbers for all test cases.

def sort_decending(nums):
    numList = list(str(nums))
    numList = reversed(sorted(numList))
    return int(''.join(numList))

print(sort_decending(123))
print(sort_decending(1254859723))
print(sort_decending(73065))