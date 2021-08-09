import unittest
from ChessNNModel import ChessNNModel
import chess
import numpy as np

class testChessNNModel(unittest.TestCase):

    def test_GetPieceOneHotRepresentation1(self):
        self.chessNNModel = ChessNNModel()
        self.board = chess.Board()
        oneHot = self.chessNNModel.getPieceOneHotRepresentation(self.board.piece_at(0)) # rook
        solution = np.zeros(6)
        solution[3] = 1
        comparison = oneHot == solution
        self.assert_(comparison.all())
    
    def test_GetPieceOneHotRepresentation2(self):
        self.chessNNModel = ChessNNModel()
        self.board = chess.Board()
        oneHot = self.chessNNModel.getPieceOneHotRepresentation(self.board.piece_at(8)) # pawn
        solution = np.zeros((6,1))
        solution[0] = 1
        comparison = oneHot == solution
        self.assert_(comparison.all())

    