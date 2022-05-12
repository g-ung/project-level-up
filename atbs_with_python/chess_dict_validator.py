'''
REQUIREMENTS:
1. Valid board must have exactly one black king and exactly one white king
2. Each player can only have at most 16 pieces, 8 pawns, and all pieces must
be on valid tile from '1a' to '8h'
3 Pieces name begine with a 'w' or 'b' to represent white or black followed
by name of the pieces, i.e. 'pawn', 'knight', 'bishop' etc. eg. 'wpawn'
4. The funtion should detect when a bug has reulsted in an impropter chess board 
'''

def is_valid_chess_board():
    # create empty chess board to store key: coordinates, value: chess pieces
    chess_board_dict = {}

    # Build the chess board
    chess_board_list = []
    for num in range(len(board_yaxis)):
        for char in range(len(board_xaxis)):
            chess_board_list.append(char + num)


# chess board represented in a dictionary
chess_board = {'a1': ' ', 'b1': ' ', 'c1': ' ', 'd1': ' ', 'e1': ' ', 'f1': ' ', 'g1': ' ', 'h1': ' ',
               'a2': ' ', 'b2': ' ', 'c2': ' ', 'd2': ' ', 'e2': ' ', 'f2': ' ', 'g2': ' ', 'h2': ' ',
               'a3': ' ', 'b3': ' ', 'c3': ' ', 'd3': ' ', 'e3': ' ', 'f3': ' ', 'g3': ' ', 'h3': ' ',
               'a4': ' ', 'b4': ' ', 'c4': ' ', 'd4': ' ', 'e4': ' ', 'f4': ' ', 'g4': ' ', 'h4': ' ',
               'a5': ' ', 'b5': ' ', 'c5': ' ', 'd5': ' ', 'e5': ' ', 'f5': ' ', 'g5': ' ', 'h5': ' ',
               'a6': ' ', 'b6': ' ', 'c6': ' ', 'd6': ' ', 'e6': ' ', 'f6': ' ', 'g6': ' ', 'h6': ' ',
               'a7': ' ', 'b7': ' ', 'c7': ' ', 'd7': ' ', 'e7': ' ', 'f7': ' ', 'g7': ' ', 'h7': ' ',
               'a8': ' ', 'b8': ' ', 'c8': ' ', 'd8': ' ', 'e8': ' ', 'f8': ' ', 'g8': ' ', 'h8': ' '}
               
# building the chess board from it's constituent parts
# coordinates that represent the chess board, 64 tiles
board_xaxis = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
board_yaxis = (1, 2, 3, 4, 5, 6, 7, 8)
# all possible peices, 61 pieces
pieces = ('pawn', 'rook', 'knight', 'bishop', 'queen', 'king')
piece_colour = ('b', 'w')
