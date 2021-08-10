from Main import playAGame
from RandomBoardEvaluator import RandomBoardEvaluator
import chess

print("Hello World") 

board = chess.Board()
whiteBoardEvaluator = RandomBoardEvaluator()
blackBoardEvaluator = RandomBoardEvaluator()
board = playAGame(whiteBoardEvaluator, blackBoardEvaluator)

print(board.outcome())
print(type(board.outcome()))
print(board.outcome().result())
print("All Done")