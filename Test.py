import chess

print("Hello World") 

board = chess.Board()
square = 0
print("Piece: " , board.piece_at(square))
print("type(Piece): " , type(board.piece_at(square).piece_type))
print("PieceType: " , board.piece_at(square).piece_type)
print("Square: ", chess.SQUARE_NAMES[square])
print(board)