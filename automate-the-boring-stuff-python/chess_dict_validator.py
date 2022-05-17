'''
REQUIREMENTS:
1. Valid board must have exactly one black king and exactly one white king
2. Each player can only have at most 16 pieces, 8 pawns, and all pieces must
be on valid tile from '1a' to '8h'
3 Pieces name begin with a 'w' or 'b' to represent white or black followed
by name of the pieces, i.e. 'pawn', 'knight', 'bishop' etc. e.g. 'wpawn'
4. The funtion should detect when a bug has resulted in an impropter chess board

NOTE: This script is only conserned with validating whether a tile position and
chess piece is valid or invalid.  It is not conserned with the rules of the game
of chess
'''
from itertools import zip_longest

def is_valid_chess_board(user_input):
    chess_board_list = [] # empty chess board list to store coordinates
    
    # Building the chess board
    for num in range(1, 9): # iterate to build board y-axis, numbers
        for char in range(97, 105): # iterate to build board x-axis, letters
            '''
            Took me to AGES figure out how to do this section until I found this neat 
            little built-in Python function. The range(97, 105) represent lower 
            case characters in decimal, use ascii table to look up the key mappings. 
            Use chr() to convert decimal values to their corresponding string 
            characters to build board x-axis
            REFERENCE:
            https://docs.python.org/3/library/functions.html?highlight=chr#chr
            https://www.programiz.com/python-programming/methods/built-in/chr
            '''
            chess_board_list.append(chr(char) + str(num))
           
    # build chess pieces by marrying chess piece colours to chess piece set
    colourcoded_pieces = [] # empty list to stored the completed chess pieces (with colours)
    chess_pieces = ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']
   
    # list comprehension for practice :)
    # colourcoded_pieces = ['b' + item for item in pieces if item == 'king' or item == 'queen'] 
    for piece in range(2):
        if piece == 0:
           # build black pieces and add to colorcoded_pieces list
            for item in chess_pieces:
                if item == 'king' or item == 'queen':
                    colourcoded_pieces.append('b' + item)
                elif item == 'rook' or item == 'knight' or item == 'bishop':
                    for i in range(1, 3): # use range to concatinate index i to items in elif statment b/c each player has 2x(rooks, knights, and bishops)
                        colourcoded_pieces.append('b' + item + str(i))
                else: # colour code for pawns
                    for i in range(1, 9):
                        colourcoded_pieces.append('b' + item + str(i))
        else:
            # build white pieces and add to colorcoded_pieces list
            for item in chess_pieces:
                if item == 'king' or item == 'queen':
                    colourcoded_pieces.append('w' + item)
                elif item == 'rook' or item == 'knight' or item == 'bishop':
                    for i in range(1, 3): 
                        colourcoded_pieces.append('w' + item + str(i))
                else:
                    for i in range(1, 9):
                        colourcoded_pieces.append('w' + item + str(i)) 

    # add colourcoded_pieces and chess_board_list to chess_board_dict
    '''
    We want to combine two lists of different lengths, colourcoded_pieces and chess_board_list 
    to build the chess_board_dict. Use zip_longest() from the itertools module to combine the
    two uneven lists.  The empty values will default to None, I used fillfalue = ' ' to create
    empty key-value pairs when all chess pices have been exhausted from colouredcoded_pieces and 
    empty key-value are created as place holder, i.e. the rest of the chess_board_dict is
    populated with empty values after the max no. of chess pieces, 32, were populated as key-value
    pairs from the two lists
    REFERENCE:
    https://docs.python.org/3/library/itertools.html?highlight=fillvalue
    https://betterprogramming.pub/10-ways-to-convert-lists-to-dictionaries-in-python-d2c728d2aeb8

    '''
    board_dict = zip_longest(chess_board_list, colourcoded_pieces, fillvalue = ' ')
    chess_board_dict = dict(board_dict) # use dict() constructor to build chess board dictionary

    # chess board and chess piece validation
    '''
    Create two variables to accept and store user input in the format 'bking a1' 
    use split() with [0] and [1] to segment key: 'bking' and value: 'a1' to check 
    if the chess piece and tile position is in chess_board_dict if, the chess pieces 
    and tile position are found in the chess board board dictionary it is valid and
    returns True, else it is invalid and returns False
    '''
    is_valid_chesspiece = user_input.split()[0]
    is_valid_tile = user_input.split()[1]

    # attestation if chess pieces and tile position are in chess_board_dict
    if is_valid_tile in chess_board_dict:
        if is_valid_chesspiece in chess_board_dict.values():
            result = True
        else:
            result = False
    else:
        result = False
    
    print(result)

    # check with
    # return print(colourcoded_pieces)
    # return print(chess_board_list)
    # return print(chess_board_dict)

try:
    input_validation = input("Please enter a chess piece name and tile position in format [e.g. 'wking a1' or 'bpawn2 b2']: ")
except IndexError as e:
    print("Error: Invalid input! {}".format(e))

is_valid_chess_board(input_validation)