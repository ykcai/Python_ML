# Machine Learning Class Week 10 Homework
# 1. List of Multiples
# Create a function that takes two numbers as arguments (num, length) and returns a list of multiples of num up to length.
# Examples
# list_of_multiples(7, 5) ➞ [7, 14, 21, 28, 35]
# list_of_multiples(12, 10) ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
# list_of_multiples(17, 6) ➞ [17, 34, 51, 68, 85, 102]

# Notes: Notice that num is also included in the returned list.


def list_of_multiples(num, length):
    pass


print(list_of_multiples(7, 5))
print(list_of_multiples(12, 10))
print(list_of_multiples(17, 6))


# 2. Is Johnny Making Progress?
# To train for an upcoming marathon, Johnny goes on one long-distance run each Saturday. He wants to track how often the number of miles he runs exceeds the previous Saturday. This is called a progress day.

# Create a function that takes in a list of miles run every Saturday and returns Johnny's total number of progress days.
# Examples
# progress_days([3, 4, 1, 2]) ➞ 2
# # There are two progress days, (3->4) and (1->2)
# progress_days([10, 11, 12, 9, 10]) ➞ 3
# progress_days([6, 5, 4, 3, 2, 9]) ➞ 1
# progress_days([9, 9])  ➞ 0

# Notes: Running the same number of miles as last week does not count as a progress day.


def progress_days(runs):
    pass


print(progress_days([3, 4, 1, 2]))
print(progress_days([10, 11, 12, 9, 10]))
print(progress_days([6, 5, 4, 3, 2, 9]))
print(progress_days([9, 9]))
