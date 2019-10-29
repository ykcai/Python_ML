# Machine Learning Class Week 6 Homework Answers
# 1. Write a Python function to check whether a string is a pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
# Hint: Look at the string module and use the issuperset() or issubset() methods for sets
# string.ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'

import string
import sys


def ispangram(str1, alphabet=string.ascii_lowercase):
    pass


print(ispangram('The quick brown fox jumps over the lazy dog'))

# 2. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow


def sort_list(input_string):
    pass


print(sort_list("green-red-black-white"))

# 3. Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).


def printValues():
    pass


printValues()


# 4. Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def unique_list(lst):
    # Also possible to use list(set())
    pass


print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))

# 5. Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output :
# No. of Upper case characters : 4
# No. of Lower case Characters : 33
# I have started this questions and the FOR loop, just fill in the code in the loop to make it work!


def up_low(s):
    d = {"upper": 0, "lower": 0}
    for c in s:
        pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)
