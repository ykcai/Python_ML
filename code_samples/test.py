# Machine Learning Class Week 5 Homework Answers
# 1.


def count_primes(num):
    '''
    COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
    count_primes(100) --> 25
    By convention, 0 and 1 are not prime.
    '''
    # Write your code here
    # --------------------------------Code between the lines!--------------------------------
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3, x, 2):  # test all odd factors up to x-1
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)
    # ---------------------------------------------------------------------------------------


def count_primes2(num):
    '''
    COUNT PRIMES FASTER
    '''
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:  # use the primes list!
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


# Check
print(count_primes(100))


# 2.

def palindrome(s):
    '''
    Write a Python function that checks whether a passed in string is palindrome or not.

    Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
    '''
    # Write your code here
    # --------------------------------Code between the lines!--------------------------------
    # This replaces all spaces ' ' with no space ''. (Fixes issues with strings that have spaces)
    s = s.replace(' ', '')
    return s == s[::-1]   # Check through slicing

    # ---------------------------------------------------------------------------------------


print(palindrome('helleh'))
print(palindrome('nurses run'))
print(palindrome('abcba'))

# 3.


def ran_check(num, low, high):
    '''
    Write a function that checks whether a number is in a given range (inclusive of high and low)
    '''
    # Write your code here
    # --------------------------------Code between the lines!--------------------------------
    # Check if num is between low and high (including low and high)
    if num in range(low, high+1):
        print('{} is in the range between {} and {}'.format(num, low, high))
    else:
        print('The number is outside the range.')

    # ---------------------------------------------------------------------------------------


# Check
print(ran_check(5, 2, 7))
# 5 is in the range between 2 and 7 => True
