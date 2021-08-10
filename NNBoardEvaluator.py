from BoardEvaluator import BoardEvaluator
from ChessNNModel import ChessNNModel
import numpy as np
import tensorflow as tf

class NNBoardEvaluator(BoardEvaluator):

    def __init__(self):
        super().__init__()
        self.INPUT_SIZE = 768
        self.chessNNModel = ChessNNModel()
        self.optimizer = tf.keras.optimizers.Adam()

    def getIndexOfBestBoard(self, boards):
        bestBoardIndex = 0
        if(not len(boards) == 1): 
            for i in range(1, len(boards)):
                inputArr = self.convertBoardsToNumpyArray(boards[bestBoardIndex], boards[i])
                output = self.chessNNModel(tf.convert_to_tensor(inputArr))
                if(output >= 0.5):
                    bestBoardIndex = i
        return bestBoardIndex
    
    def convertBoardsToNumpyArray(self, board1, board2):
        arr = np.zeros((1, self.INPUT_SIZE))
        for i in range(64):
            piece = board1.piece_at(i)
            if(not piece == None):
                oneHot = self.getPieceOneHotRepresentation(piece)
                arr[:, i*6:(i+1)*6] = oneHot
        for i in range(64, 128):
            piece = board2.piece_at(i - 64)
            if(not piece == None):
                arr[:, i*6:(i+1)*6] = self.getPieceOneHotRepresentation(piece)
        return arr

    def getPieceOneHotRepresentation(self, piece):
        arr = np.zeros((1,6))
        if(not piece == None):
            arr[0][piece.piece_type - 1] = 1
        return arr
