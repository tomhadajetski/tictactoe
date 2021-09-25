import random

board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
test_board = ['#','X','O','X','O','X','O','X','O','X']

def choose_first():
    if random.randint(0,1) == 0:
        print('Player 2')
        return 'Player 2'
    else:
        print('Player 1')
        return 'Player 1'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


def display_board(board):
    print('\n'*100)
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-+-+-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-+-+-')
    print(board[1]+'|'+board[2]+'|'+board[3])



def player_marker_input():
    marker = ''

    #keep asking player 1 to choose X or O

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O')
    
    #assign player 2 to the opposite marker

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    
    return (player1, player2)
    




def player_position_input():

    position = 'invalid'
    while position not in ['1','2','3','4','5','6','7','8','9']:
        position = input('Pick a position (1-9: ')
        if position not in ['1','2','3','4','5','6','7','8','9']:
            print('Sorry, invalid position!')
    return int(position)

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,mark):
    return ((board[1] == board[2] == board[3] == mark) or 
    (board[4] == board[5] == board[6] == mark) or
    (board[7] == board[8] == board[9] == mark) or
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[3] == board[6] == board[9] == mark) or
    (board[1] == board[5] == board[9] == mark) or
    (board[7] == board[5] == board[3] == mark))



#player1_marker, player2_marker = player_marker_input()

def replay():
    choice = input("Do you want to play again? (Y/N) ")
    return choice == 'Yes'

replay()