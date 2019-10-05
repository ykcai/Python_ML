# Continue our function explorations
# Level 2 Problems...


def has_33(nums):
    '''
    Given a list of integers, return True if the array contains a 3 next to a 3 somewhere (consecutive)
    has_33([1, 3, 3]) -> True
    has_33([1, 3, 1, 3]) -> False
    has_33([3, 1, 3]) -> False
    '''
    # Loop through our list
    for i in range(0, len(nums)-1):
        if nums[2] == 3 and nums[i+1] == 3:
            return True
        # creating a window with splicing
        if nums[i:(i+2)] == [3, 3]:
            return True
    return False


print(has_33([1, 3, 3, 3, 4, 5]))
print(has_33([1, 3, 2, 3, 4, 5]))


def paper_doll(text):
    '''
    Given a string, return a string where for every character in the original there are three characters
    paper_doll('Hello') --> 'HHHeeellllllooo'
    paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
    '''
    result = ""
    for char in text:
        result = result + char * 3
    return result


print(paper_doll('pneumonoultramicroscopicsilicovolcanoconiosis'))
print(paper_doll('Mississippi'))


def blackjack(card1, card2, card3):
    '''
    Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
    If their sum exceeds 21 and there is an 11, reduce the total sum by 10.
    Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

    blackjack(5,6,7) --> 18
    blackjack(9,9,9) --> 'BUST'
    blackjack(9,9,11) --> 19
    '''
    if sum([card1, card2, card3]) <= 21:
        return sum([card1, card2, card3])
    elif sum([card1, card2, card3]) <= 31 and 11 in [card1, card2, card3]:
        return sum([card1, card2, card3]) - 10
    else:
        return "BUST"


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))


def spy_game(nums):
    '''
    Write a function that takes in a list of integers and returns True
    if it contains 007 in ORDER
    '''
    # Loop through nums
    code = [0, 0, 7, 'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)  # remove the 0th element in code list
    return len(code) == 1  # This will return True of False
    # alternatively code[0] = "x"


print(spy_game([0, 0, 0, 7, 0, 0, 5]))
print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))

# Lambda Expressions, Map, and Filter Functions

# Map Function: the map functions allows you to "map" a function to an iterable object. This means you can quickly call the same function for every item in an iterable, such as a list, tuple, string etc..


def square(num):
    return num**2


my_nums = [1, 2, 3, 4, 5]

print([num**2 for num in my_nums])  # list comprehension

print(list(map(square, my_nums)))


def splicer(my_string):
    if len(my_string) % 2 == 0:
        return 'even'
    else:
        return my_string[0]


my_names = ['John', 'Cindy', 'Sarah', 'Kelly', 'Mike']

print(list(map(splicer, my_names)))

# Filter Function: returns an iterator yielding those items of iterable for which function(item) is true. Meaning you need to filter by a function that returns either True of False. Then passing that into filter, along with your iterable, you get back only the results that would return True from the function.


def check_even(num):
    return num % 2 == 0

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Here we are filting the nums list by the check_even function, filtering out odd numbers
print(list(filter(check_even, nums)))

# Lambda Expression: allows us to create "anonymous" functions.The means we can quickly made ad-hoc functions without needing to properly define functions using def.

def square(num):
    result = num**2
    return result
square(2)

# simplify
def square(num):
    return num**2
square(2)

# one liner
def square(num): return num**2
square(2)

# lambda way
square = lambda num: num ** 2
square(2)