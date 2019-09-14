# First, pick a random integer from 1 to 100 using the random module and assign it to a variable
# Note: random.randint(a,b) returns a random integer in range [a, b], including both end points.

import random

num = random.randint(1, 100)

# Next, print an introduction to the game and explain the rules

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

# Create a list to store guesses
# Hint: zero is a good placeholder value. It's useful because it evaluates to "False"

guesses = [0]

# 0 is the same as False

# Write a while loop that asks for a valid guess. Test it a few times to make sure it works.

while True:
    guess = int(input("I'm thinking of a number between 1 and 100. \n What is your guess? ... "))

    if guess < 1 or guess > 100:
        print("OUT OF BOUNDS! Please try again: ... ")
        continue

    # here we will compare user's guess with our random number
    if guess == num:
        print(f"CONGRATULATIONS, YOU GUESSED THE RIGHT NUMBER {num}, IT ONLY TOOK YOU {len(guesses)} GUESSES!!!")
        break

    # if guess is incorrect, add guess in to guesses list
    guesses.append(guess)

    # when testing our first guess, guesses[-2]==0, which is False
    # and brings us down to the second section

    if guesses[-2]:
        if abs(num - guess) < abs(num-guesses[-2]):
            print("WARMER!")
        else: 
            print("COLDER!")
    else:
        if abs(num - guess) <= 10:
            print("WARM!")
        else:
            print("COLD!")



    