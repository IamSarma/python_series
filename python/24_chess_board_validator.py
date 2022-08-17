# Chess board (dictionary) validator 😎
# A valid board will have exactly one black king and exactly one white king
# Each player can only have at most 16 pieces, at most 8 pawns,
# and all pieces must be on a valid space from '1a' to '8h'
# that is, a piece can’t be on space '9z'.
# The piece names begin with either a 'w' or 'b' to represent white or black,
# followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'
def isValidChessBoard(user_input):
    is_valid = True

    # Main program
    for key, value in user_input.items():
        # Check for move which is out of possible moves
        if key not in possible_moves:
            is_valid = False
            break
        # Check for piece which is out of possible pieces
        if value not in possible_pieces:
            is_valid = False
            break

    return is_valid


row_sequence = [1, 2, 3, 4, 5, 6, 7, 8]
col_sequence = ["a", "b", "c", "d", "e", "f", "g", "h"]
price_color = ["w", "b"]
pieces = ["king", "queen", "bishop", "rook", "knight", "pawn"]
possible_moves = []
possible_pieces = []

# Generating all possible moves
for row in row_sequence:
    for col in col_sequence:
        possible_moves.append(str(row) + col)

# Generating all possible pieces and color combination
for color in price_color:
    for piece in pieces:
        possible_pieces.append(color + piece)


# Sample chess board dictionary
user_board = {
    '1h': 'bking',
    '6c': 'wqueen',
    '2g': 'bbishop',
    '5h': 'bqueen',
    '3e': 'wking'
}

print(isValidChessBoard(user_board))
