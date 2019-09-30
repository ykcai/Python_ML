# Partice Functions 
# Warmup 

def lesser_of_two(a,b):
    '''
    A function that returns:
    the lesser of two given numbers if BOTH are even
    But returns the greater if one or both numbers are odd.
    '''
    # if a and b are even, then return min
    if a % 2 == 0 and b % 2 == 0:
        return min(a,b)
    else:
        return max(a,b)

print(lesser_of_two(2,4))
# returns 2
print(lesser_of_two(2,5))
# returns 5

def animal_crackers(text):
    '''
    This function takes a two-word string and returns True if
    BOTH words being with the same letter
    *Hint: use .split()
    '''
    wordlist = text.lower().split()
    print(wordlist)
    # compare the fist letter of the two words
    result = (wordlist[0][0] == wordlist[1][0])
    return result

print(animal_crackers('Levelheaded Llama'))
# return True
print(animal_crackers('Crazy Kangaroo'))
# return False
print(animal_crackers('Crazy croc'))

def makes_twenty(n1, n2):
    '''
    Given two integers, return True if the sum of the integers is 20
    or if one of the integers is 20.
    If not, return False
    '''
    return (n1+n2)==20 or n1==20 or n2==20

print(makes_twenty(20,10))
# True

print(makes_twenty(12,8))
# True

print(makes_twenty(2,3))
# False

# HARD LEVEL 1

def old_macdonald(name):
    '''
    Write a function that capitalizes the FIRST and FOURTH letters of name
    If the name is less than 4 characters, return the string
    "Name is too short!"
    *Hint: len(object) checks the lenght of a object
           object.capitalize() makes the current character Capital
    '''
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return "Name is too short!"

print(old_macdonald("bob"))
print(old_macdonald("macdonald"))
print(old_macdonald("michael"))

def fake_master_yoda(sentence):
    '''
    Given a sentence, return another sentence with the words reversed
    *Hint: use .split() and .join()
            reverse ordering through indexing: [::-1]
    '''
    wordlist = sentence.split(" ")
    return " ".join(wordlist[::-1])

print(fake_master_yoda('I am home'))
# returns home am I
print(fake_master_yoda('We are ready'))
# returns ready are We
print(fake_master_yoda('Ricky wants to break now'))


def real_master_yoda(sentence):
    '''
    Given a sentence, return another sentence with the first 2 or 3 words added to the end of the sentence
    'You will find what you are looking for' turns into 'Find what you are looking for, you will.'
    '''
    import random
    number_of_words = random.randint(2, 3)
    wordlist = sentence.split()

    if len(wordlist) > 3:
        return " ".join(wordlist[number_of_words:] + wordlist[:number_of_words])
    else:
        return "Sentence is too short for Yoda"

print(real_master_yoda("You will find what you are looking for"))
print(real_master_yoda("You are short"))

def we_are_almost_there(n):
    '''
    Given an integer n, return True if n is within 10 
    of either 100 or 200
    90 <= n <= 110, 190 <= n <= 210
    *Hint: use abs(object) takes the absolute value of the object
    '''
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)

print(we_are_almost_there(90),we_are_almost_there(104), we_are_almost_there(150), we_are_almost_there(209))

def print_big(letter):
    '''
    Write a function that takes in a single letter and returns a 5x5 represetation of that letter

    print_big('a')

    out:      *  
             * *
            *****
            *   *
            *   *
    HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns.
    For purposes of this exercise, it's ok if your dictionary stops at "E".
    '''
    patterns = {
        1: '  *  ',
        2: ' * * ',
        3: '*   *',
        4: '*****',
        5: '**** ',
        6: '   * ',
        7: ' *   ',
        8: '*  * ',
        9: '*    ',
        10:'* ***'
    }

    alphabet = {
        'A': [1,2,4,3,3],
        'B': [5,3,5,3,5],
        'C': [4,9,9,9,4],
        'D': [5,3,3,3,5],
        'E': [4,9,4,9,4],
        'F': [4,9,4,9,9],
        'G': [4,9,10,3,4]
    }

    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

print_big('a')
print_big('b')
print_big('c')
print_big('d')
print_big('e')
print_big('f')
print_big('g')