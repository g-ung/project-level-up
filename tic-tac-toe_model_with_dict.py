# exercise for demonstration excersie to use dictionary to model a naughts and crosses game (not complete game)
def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def main():
    # use dictionary to represent a naughts and crosses, aka tic-tac-toe, board
    # the data strucutre stored in the_board variable represents the naughts 
    # and crosses board
    the_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
                
    turn = "X" # represent the value to the dictionary keys
    for i in range(9):
        print_board(the_board)
        print("Turn for {}. Move on which space?".format(turn))
        move = input() # prompt player to enter their move
        the_board[move] = turn # updates the board with player's move accordingly, note variable move represents dictionary keys
        if turn == "X": # swap player before moving to next turn
            turn = "O"
        else:
            turn = "X"

    print_board(the_board)

if __name__ == '__main__':
    main()