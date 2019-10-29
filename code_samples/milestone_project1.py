# You've already learned a ton and are ready to work on a real project.

# Your assignment: Create a Tic Tac Toe game. You are free to use any IDE you like.

# Here are the requirements:

# 2 players should be able to play the game (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board

# Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.

import random
from IPython.display import clear_output
# if you see an error run pip3 install IPython


def display_board(board):
    print('        |   |')
    print('      ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('        |   |')
    print('     -----------')
    print('        |   |')
    print('      ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('        |   |')
    print('     -----------')
    print('        |   |')
    print('      ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('        |   |')
    print('             ')

# Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while loops to continually ask until you get a correct answer.


def player_input():
    marker = ''

    while not (marker == "X" or marker == "O"):
        marker = input("Player 1: Do you want to be X or O? ").upper()

    if marker == "X":
        print("Player 1 => X", "Player 2 => O")
        return ("X", "O")
    else:
        print("Player 1 => O", "Player 2 => X")
        return ("O", "X")


# Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.


def place_marker(board, marker, position):
    board[position] = marker


# Step 4: Write a function that takes in a board and checks to see if someone has won.


def win_check(board, mark):
    if (board[7:10] == [mark, mark, mark]  # across the top
        or (board[4:7] == [mark, mark, mark])  # across the middle
        or board[1:4] == [mark, mark, mark]  # across the bottom
        # down the left
                or [board[1], board[4], board[7]] == [mark, mark, mark]
                # down the midlde
            or [board[2], board[5], board[8]] == [mark, mark, mark]
            # down the right
            or [board[3], board[6], board[9]] == [mark, mark, mark]
            or [board[1], board[5], board[9]] == [mark, mark, mark]  # diagonal
            or [board[7], board[5], board[3]] == [mark, mark, mark]  # diagonal
        ):
        print(f" Player {mark} has won!")
        return True
    else:
        print(f"Player {mark} did not win!")
        return False

# Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.


def space_check(board, position):
    return board[position] == " "

# Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

# Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if its a free position. If it is, then return the position for later use.


def player_choice(board):
    position = 0

    while position not in range(1, 10) or not space_check(board, position):
        position = int(input("Choose your next position: (1-9) "))

    return position

# Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.


def replay():
    return input("Do you want to play again? Enter Yes or No: ").lower().startswith("y")

# Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!


print("---WELCOME TO TIC TAC TOE!---")

while True:
    # Reset the board
    game_board = [" "] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(f"{turn} will go first!")

    play_game = input(
        "Are you ready to play? Enter Yes or No. ").lower().startswith("y")

    while play_game:
        if turn == "Player 1":
            # Player1's turn

            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board, player1_marker, position)

            if win_check(game_board, player1_marker):
                display_board(game_board)
                print("Congratulations! You have won the game!")
                play_game = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print("The game is a draw!")
                    break
                else:
                    turn = "Player 2"

        else:
            # Player2's turn

            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board, player2_marker, position)

            if win_check(game_board, player2_marker):
                display_board(game_board)
                print("Congratulations! You have won the game!")
                play_game = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print("The game is a draw!")
                    break
                else:
                    turn = "Player 1"

    if not replay():
        break
