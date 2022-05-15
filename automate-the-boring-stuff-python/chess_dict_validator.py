'''
REQUIREMENTS:
1. Valid board must have exactly one black king and exactly one white king
2. Each player can only have at most 16 pieces, 8 pawns, and all pieces must
be on valid tile from '1a' to '8h'
3 Pieces name begine with a 'w' or 'b' to represent white or black followed
by name of the pieces, i.e. 'pawn', 'knight', 'bishop' etc. eg. 'wpawn'
4. The funtion should detect when a bug has resulted in an impropter chess board 
'''
from itertools import zip_longest


def is_valid_chess_board(user_input):
    #chess_board_dict = {} # create empty chess board to store key: coordinates, value: chess pieces
    chess_board_list = [] # empty chess board list to store coordinates
    
    # Building the chess board
    for num in range(1, 9): # iterate to build board y-axis, numnbers
        for char in range(97, 105): # iterate to build board x-axis, letters
            '''
            Took me AGES figure out how to do this section until I found this neat 
            little built-in Pythong function. The range(97, 105) represent lower 
            case characters in decimal, use ascii table to look up the key mappings. 
            Use chr() to convert decimal values to their corresponding string 
            characters to build board x-axis
            REFERENCE:
            https://docs.python.org/3/library/functions.html?highlight=chr#chr
            https://www.programiz.com/python-programming/methods/built-in/chr
            '''
            chess_board_list.append(chr(char) + str(num))
            '''
            Had to pivot from this approach as I found it difficult to add values to
            existing keys in chess_board_dict, to make things harder the value length 
            is shorter than the existing keys in the dictionary.  I've commented the 
            code out instead of removing it in case I couldn't find a another way to 
            populate the chess_board_dict...  The rest is history :)
            # use get() to build chess_board_dict, i.e. add chess_ board_list to chess_board_dict as dict. key
            # for tile_coord in chess_board_list: 
                # chess_board_dict[tile_coord] = chess_board_dict.get(tile_coord, ' ')
            '''
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
    We want to combine two list of different lengths, colourcoded_pieces and chess_board_list 
    to build the chess_board_dict. Use zip_longest() from the itertools module to combine the
    two uneven lists.  The empty values will default to None, I used villfalue = ' ' to create
    empty key-values pairs all chess pices have been exhausted from colouredcoded_pieces and 
    empty key-value is created as place holder
    REFERENCE:
    https://docs.python.org/3/library/itertools.html?highlight=fillvalue
    https://betterprogramming.pub/10-ways-to-convert-lists-to-dictionaries-in-python-d2c728d2aeb8

    '''
    board_dict = zip_longest(chess_board_list, colourcoded_pieces, fillvalue = ' ')
    chess_board_dict = dict(board_dict)

    # chess board and chess piece validation
    '''
    Create two variables to accept user input in the format 'bking a1' use split()
    to segment key: 'bking' and value: 'a1' to check in chess_board_dict if the
    chess pieces and tile position are valid
    '''
    is_valid_chesspiece = user_input.split()[0]
    is_valid_tile = user_input.split()[1]

    # check if chess pieces and tile position are in chess_board_dict
    if is_valid_tile in chess_board_dict:
        if is_valid_chesspiece in chess_board_dict.values():
            result = True
        else:
            result = False
    else:
        result = False
    
    return print(result)

    # check with
    # return print(colourcoded_pieces)
    # return print(chess_board_list)
    # return print(chess_board_dict)

'''
# chess board represented in a dictionary  
# expected output
{'a1': ' ', 'b1': ' ', 'c1': ' ', 'd1': ' ', 'e1': ' ', 'f1': ' ', 'g1': ' ', 'h1': ' ',
'a2': ' ', 'b2': ' ', 'c2': ' ', 'd2': ' ', 'e2': ' ', 'f2': ' ', 'g2': ' ', 'h2': ' ',
'a3': ' ', 'b3': ' ', 'c3': ' ', 'd3': ' ', 'e3': ' ', 'f3': ' ', 'g3': ' ', 'h3': ' ',
'a4': ' ', 'b4': ' ', 'c4': ' ', 'd4': ' ', 'e4': ' ', 'f4': ' ', 'g4': ' ', 'h4': ' ',
'a5': ' ', 'b5': ' ', 'c5': ' ', 'd5': ' ', 'e5': ' ', 'f5': ' ', 'g5': ' ', 'h5': ' ',
'a6': ' ', 'b6': ' ', 'c6': ' ', 'd6': ' ', 'e6': ' ', 'f6': ' ', 'g6': ' ', 'h6': ' ',
'a7': ' ', 'b7': ' ', 'c7': ' ', 'd7': ' ', 'e7': ' ', 'f7': ' ', 'g7': ' ', 'h7': ' ',
'a8': ' ', 'b8': ' ', 'c8': ' ', 'd8': ' ', 'e8': ' ', 'f8': ' ', 'g8': ' ', 'h8': ' '}
# colourcoded_pieces
# expect output
['bpawn1', 'bpawn2', 'bpawn3', 'bpawn4', 'bpawn5', 'bpawn6', 'bpawn7', 'bpawn8', 
'brook1', 'brook2', 'bknight1', 'bknight2', 'bbishop1', 'bbishop2', 'bqueen', 'bking', 
'wpawn1', 'wpawn2', 'wpawn3', 'wpawn4', 'wpawn5', 'wpawn6', 'wpawn7', 'wpawn8', 
'wrook1', 'wrook2', 'wknight1', 'wknight2', 'wbishop1', 'wbishop2', 'wqueen', 'wking']
'''           

try:
    attestation = input("Please enter a chess piece and tile position on chess board in format ['wking a1' or 'bpawn2 b2] (blank to quie): ")
except IndexError as e:
    print("Error: Invalid input! {}".format(e))

is_valid_chess_board(attestation)