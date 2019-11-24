# Machine Learning Class Week 11 Homework Answers
# 1. An isogram is a word that has no repeating letters, consecutive or nonconsecutive. Create a function that takes a string and returns either True or False depending on whether or not it's an "isogram".

# Examples
# is_isogram("Algorism") ➞ True
# is_isogram("PasSword") ➞ False
# # Not case sensitive.
# is_isogram("Consecutive") ➞ False
# Notes: Ignore letter case (should not be case sensitive). All test cases contain valid one word strings.


def is_isogram(word):
    return len(word) == len(set(word.lower()))


is_isogram("Algorism")
is_isogram("PasSword")
is_isogram("Consecutive")

# 2. What are the 4 different detection models that we covered in class?
# Knowledge
# Feature
# Template Matching
# Appearance
