# Chess board (dictionary) validator 😎
# A valid board will have exactly one black king and exactly one white king
# Each player can only have at most 16 pieces, at most 8 pawns,
# and all pieces must be on a valid space from '1a' to '8h'
# that is, a piece can’t be on space '9z'.
# The piece names begin with either a 'w' or 'b' to represent white or black,
# followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'
def isValidChessBoard(user_input):
    is_valid = True

    # Possible moves and pieces check
    for key, value in user_input.items():
        if key not in possible_moves:
            return False
        if value not in possible_pieces:
            return False

    # Check for total pieces count and pieces limit
    pieces_count = {
        "white_pieces_count": 0,
        "black_pieces_count": 0,
    }

    for value in user_input.values():
        if value in white_pieces:
            pieces_count["white_pieces_count"] += 1
        if value in black_pieces:
            pieces_count["black_pieces_count"] += 1
        pieces_count.setdefault(value, 0)
        pieces_count[value] += 1

    if pieces_count['white_pieces_count'] > 16:
        return False
    if pieces_count['black_pieces_count'] > 16:
        return False

    return is_valid


row_sequence = [1, 2, 3, 4, 5, 6, 7, 8]
col_sequence = ["a", "b", "c", "d", "e", "f", "g", "h"]
piece_color = ["w", "b"]
pieces = ["king", "queen", "bishop", "rook", "knight", "pawn"]
possible_moves = []
possible_pieces = []

# Generating all possible moves
for row in row_sequence:
    for col in col_sequence:
        possible_moves.append(str(row) + col)

# Generating all possible pieces and color combination
for color in piece_color:
    for piece in pieces:
        possible_pieces.append(color + piece)

# Storing white and black pieces in separate lists
white_pieces = possible_pieces[:6]
black_pieces = possible_pieces[6:]

# Sample chess board dictionary
user_board = {
    '1h': 'bking',
    '6c': 'wqueen',
    '2g': 'bbishop',
    '5h': 'bqueen',
    '3e': 'wking',
    '1a': 'bqueen',
    '1b': 'bqueen',
    '1c': 'bqueen',
    '1d': 'bqueen',
    '1e': 'bqueen',
    '1f': 'bqueen',
    '1g': 'bqueen',
    '2a': 'bqueen',
    '2b': 'bqueen',
    '2c': 'bqueen',
    '2d': 'bqueen',
    '3a': 'bqueen',
    '3b': 'bqueen',
    # '3c': 'bqueen',
}

print(isValidChessBoard(user_board))
