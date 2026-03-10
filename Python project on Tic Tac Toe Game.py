import random

def display_board(board):
    # This scrolls the old board out of view for a "clear" effect in terminals
    print('\n' * 100)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1: Do you want to be 'X' or 'O'? ").upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # left
    (board[8] == mark and board[5] == mark and board[2] == mark) or # mid-v
    (board[9] == mark and board[6] == mark and board[3] == mark) or # right
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diag1
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diag2

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        try:
            choice = input('Choose your next position: (1-9) ')
            position = int(choice)
        except ValueError:
            print("Please enter a valid number.")
    return position

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

# --- MAIN GAME LOOP ---
print('Welcome to Tic Tac Toe!')

while True:
    theBoard = [' '] * 10
    p1_marker, p2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? (Yes/No): ')
    game_on = play_game.lower().startswith('y')

    while game_on:
        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, p1_marker, position)

            if win_check(theBoard, p1_marker):
                display_board(theBoard)
                print('Congratulations! Player 1 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, p2_marker, position)

            if win_check(theBoard, p2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break