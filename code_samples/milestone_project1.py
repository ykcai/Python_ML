# You've already learned a ton and are ready to work on a real project.

# Your assignment: Create a Tic Tac Toe game. You are free to use any IDE you like.

# Here are the requirements:

# 2 players should be able to play the game (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board

# Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.

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


# test_board = ["#", 'X', 'O', 'X', 'X', 'O', 'X', 'O', 'X', 'O']
# display_board(test_board)

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


# player_input()

# Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.


def place_marker(board, marker, position):
    board[position] = marker


# place_marker(test_board, "MICHAEL", 9)
# display_board(test_board)

# Step 4: Write a function that takes in a board and checks to see if someone has won.


def win_check(board, mark):
    if [mark, mark, mark] in (board[7:10], (board[4:7], board[1:4], [board[1], board[4], board[7]], [board[2], board[5], board[8]], [board[3], board[6], board[9]], [board[1], board[5], board[9]], [board[7], board[5], board[3]])):
        # if (board[7:10] == [mark, mark, mark]  # across the top
        #         or (board[4:7] == [mark, mark, mark])  # across the middle
        #         or board[1:4] == [mark, mark, mark]  # across the bottom
        #         or [board[1], board[4], board[7]] == [mark, mark, mark]  # down the left
        #         # down the midlde
        #         or [board[2], board[5], board[8]] == [mark, mark, mark]
        #         # down the right
        #     or [board[3], board[6], board[9]] == [mark, mark, mark]
        #     or [board[1], board[5], board[9]] == [mark, mark, mark]  # diagonal
        #     or [board[7], board[5], board[3]] == [mark, mark, mark]  # diagonal
        #     ):
        print(f" Player {mark} has won!")
        return True
    else:
        print(f"Player {mark} did not win!")
        return False


test_board2 = ["#", 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'X']
display_board(test_board2)
win_check(test_board2, 'X')
win_check(test_board2, 'O')
