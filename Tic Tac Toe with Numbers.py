'''
Tic Tac Toe Game With Numbers
This game is created by Belal Ahmed
Date: 1 Mar. 2022
'''

board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]
first_player = [1, 3, 5, 7, 9]  # Odd Numbers
second_player = [0, 2, 4, 6, 8]  # Even Numbers


# ------------- Functions -------------


# Display the game board to the terminal
def display_board():
    i = 0
    for row in range(3):
        for column in range(3):
            print(board[row][column], ' | ', end='')
        i += 1  # condition to break the loop before printing the third line(---------)
        if i == 3:
            break
        print('\n-------------')


# Get input from player 1
def player1_input():
    # Get position from the player
    row = int(input('\nPlayer1\nEnter Row Number From 1 To 3: '))
    column = int(input('Enter Column Number From 1 To 3: '))
    # check if it is a valid position and if the position is available on board
    while row not in range(1, 4) or column not in range(1, 4) or board[row - 1][column - 1] != "":
        row = int(input('Player1\nEnter Row Number From 1 To 3: '))
        column = int(input('Enter Column Number From 1 To 3: '))
    # Get the number from player 1
    player_1_input = int(input("Enter an Odd Number From 1 To 9: "))
    # check if it's odd number and in range 1 to 9
    while player_1_input not in first_player:
        player_1_input = int(input("Enter an Odd Number From 1 To 9: "))
    board[row - 1][column - 1] = player_1_input
    first_player.remove(player_1_input)
    display_board()


# Get input from player 2
def player2_input():
    # Get position from the player
    row = int(input('\nPlayer2\nEnter Row Number From 1 To 3: '))
    column = int(input('Enter Column Number From 1 To 3: '))
    # check if it is a valid position and if the position is available on board
    while row not in range(1, 4) or column not in range(1, 4) or board[row - 1][column - 1] != "":
        row = int(input('Player2\nEnter Row Number From 1 To 3: '))
        column = int(input('Enter Column Number From 1 To 3: '))
    # Get the number from player 2
    player_2_input = int(input("Enter an Even Number From 0 To 8: "))
    # check if it's even number from 0 to 8
    while player_2_input not in second_player:
        player_2_input = int(input("Enter an Even Number From 0 To 8: "))
    board[row - 1][column - 1] = player_2_input
    second_player.remove(player_2_input)


# check if any player has won
def check_winner(winner):
    # Check if sum of row = 15
    for i in board:
        if "" in i:
            break
        elif sum(i) == 15:
            display_board()
            print('\nCongratulations !!! ' + winner + ' is the Winner!')
            return True
    # Check if sum of column =15
    for col in range(3):
        columns_sum = 0
        for row in range(3):
            if board[row][col] == "":
                break
            columns_sum += board[row][col]
            if columns_sum == 15 and row == 2:
                display_board()
                print('\nCongratulations !!! ' + winner + ' is the Winner!')
                return True
    # Check if sum of Diagonal = 15
    left_diagonal_sum = 0
    right_diagonal_sum = 0
    for i in range(3):
        if board[i][i] == "":
            break
        left_diagonal_sum += board[i][i]
        if left_diagonal_sum == 15 and i == 2:
            display_board()
            print('\nCongratulations !!! ' + winner + ' is the Winner!')
            return True
    for i in range(3):
        if board[i][2 - i] == "":
            break
        right_diagonal_sum += board[i][2 - i]
        if right_diagonal_sum == 15 and i == 2:
            display_board()
            print('\nCongratulations !!! ' + winner + ' is the Winner!')
            return True
    return False


# Main function to play the game
def play_game():
    while True:  # Loop until the game stops for win or draw
        draw = True
        display_board()  # Show game board
        player1_input()
        if check_winner('Player 1'):
            break
        # Check for Draw
        for row in board:
            if "" in row:
                draw = False
        if draw:
            print("Draw")
            break
        player2_input()
        if check_winner('Player 2'):
            break


play_game()
