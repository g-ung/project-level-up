'''
REQUIREMENTS:
1. Valid board must have exactly one black king and exactly one white king
2. Each player can only have at most 16 pieces, 8 pawns, and all pieces must
be on valid tile from '1a' to '8h'
3 Pieces name begine with a 'w' or 'b' to represent white or black followed
by name of the pieces, i.e. 'pawn', 'knight', 'bishop' etc. eg. 'wpawn'
4. The funtion should detect when a bug has resulted in an impropter chess board 
'''

def is_valid_chess_board():
    chess_board_dict = {} # create empty chess board to store key: coordinates, value: chess pieces
    chess_board_list = [] # empty chess board list to store coordinates
    
    # Building the chess board
    for num in range(1, 9): # iterate to build board y-axis, numnbers
        for char in range(97, 105): # iterate to build board x-axis, letters
            '''
            Took me AGES to find this neat little built-in Pythong function.
            The range(97, 105) represent lower case characters in decimal,
            use ascii table to look up the key mappings. Use chr() to convert
            decimal values to their corresponding string characters to
            build board x-axis
            REFERENCE:
            https://docs.python.org/3/library/functions.html?highlight=chr#chr
            https://www.programiz.com/python-programming/methods/built-in/chr
            '''
            chess_board_list.append(chr(char) + str(num))
            for tile_coord in chess_board_list: # use get() to build chess_board_dict
                chess_board_dict[tile_coord] = chess_board_dict.get(tile_coord, ' ')
    
    # build chess pieces by marryiing chess piece colours to chess piece set
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

    # adding chess pieces to chess_board_dict



    print(colourcoded_pieces)
    # check with
    # return print(chess_board_list)

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
# building the chess board from it's constituent parts
# coordinates that represent the chess board, 64 tiles
# board_xaxis = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
# board_yaxis = (1, 2, 3, 4, 5, 6, 7, 8)
# all possible peices, 61 pieces
# pieces = ('pawn', 'rook', 'knight', 'bishop', 'queen', 'king')
# piece_colour = ('b', 'w')
is_valid_chess_board()