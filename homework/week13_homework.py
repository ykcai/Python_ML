# Machine Learning Class Week 13 Homework
# 1. Positive Count / Negative Sum

# Create a function that takes a list of positive and negative numbers. Return a list where the first element is the count of positive numbers and the second element is the sum of negative numbers.
# Examples
# sum_neg([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]) ➞ [10, -65]
# There are a total of 10 positive numbers.
# The sum of all negative numbers equals -65.
# sum_neg([92, 6, 73, -77, 81, -90, 99, 8, -85, 34]) ➞ [7, -252]
# sum_neg([91, -4, 80, -73, -28]) ➞ [2, -105]
# sum_neg([]) ➞ []

# Notes: If given an empty list, return an empty list: []


def sum_neg(num_list):
    pass


print(sum_neg([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
print(sum_neg([92, 6, 73, -77, 81, -90, 99, 8, -85, 34]))
print(sum_neg([91, -4, 80, -73, -28]))
print(sum_neg([]))

# 2. Count Letters in a Word Search
# Create a function that counts the number of times a particular letter shows up in the word search.
# Examples

# letter_counter([
#   ["D", "E", "Y", "H", "A", "D"],
#   ["C", "B", "Z", "Y", "J", "K"],
#   ["D", "B", "C", "A", "M", "N"],
#   ["F", "G", "G", "R", "S", "R"],
#   ["V", "X", "H", "A", "S", "S"]
# ], "D") ➞ 3
# # "D" shows up 3 times: twice in the first row, once in the third row.
# letter_counter([
#   ["D", "E", "Y", "H", "A", "D"],
#   ["C", "B", "Z", "Y", "J", "K"],
#   ["D", "B", "C", "A", "M", "N"],
#   ["F", "G", "G", "R", "S", "R"],
#   ["V", "X", "H", "A", "S", "S"]
# ], "H") ➞ 2


def letter_counter(lst, letter):
    pass


print(letter_counter([
    ["D", "E", "Y", "H", "A", "D"],
    ["C", "B", "Z", "Y", "J", "K"],
    ["D", "B", "C", "A", "M", "N"],
    ["F", "G", "G", "R", "S", "R"],
    ["V", "X", "H", "A", "S", "S"]
], "D"))
print(letter_counter([
    ["D", "E", "Y", "H", "A", "D"],
    ["C", "B", "Z", "Y", "J", "K"],
    ["D", "B", "C", "A", "M", "N"],
    ["F", "G", "G", "R", "S", "R"],
    ["V", "X", "H", "A", "S", "S"]
], "H"))
