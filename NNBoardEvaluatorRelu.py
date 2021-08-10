from PlayAGame import playAGame
from BoardEvaluator import BoardEvaluator
from ChessNNModel import ChessNNModel
import numpy as np
import tensorflow as tf

class NNBoardEvaluatorRelu(BoardEvaluator):

    def __init__(self):
        super().__init__()
        self.INPUT_SIZE = 768
        self.chessNNModel = ChessNNModel("relu")
        self.optimizer = tf.keras.optimizers.Adam()
        self.allBoardOptionsValues = []

    def getIndexOfBestBoard(self, boards):
        bestBoardIndex = 0
        firstInputArr = self.convertBoardToNumpyArray(boards[0])
        bestBoardValue = self.chessNNModel(tf.convert_to_tensor(firstInputArr))
        bestBoardValue = bestBoardValue.numpy()
        boardOptionValues = [bestBoardValue[0][0]]
        if(not len(boards) == 1): 
            for i in range(1, len(boards)):
                inputArr = self.convertBoardToNumpyArray(boards[i])
                output = self.chessNNModel(tf.convert_to_tensor(inputArr))
                if(output > bestBoardValue):
                    bestBoardIndex = i
                    bestBoardValue = output
                boardOptionValues.append(output.numpy()[0][0])
        self.allBoardOptionsValues.append(boardOptionValues)
        return bestBoardIndex
    
    def convertBoardToNumpyArray(self, board):
        arr = np.zeros((1, self.INPUT_SIZE))
        for i in range(64):
            piece = board.piece_at(i)
            if(not piece == None):
                oneHot = self.getPieceOneHotRepresentation(piece)
                arr[:, i*6:(i+1)*6] = oneHot
        return arr

    def getPieceOneHotRepresentation(self, piece):
        arr = np.zeros((1,6))
        if(not piece == None):
            arr[0][piece.piece_type - 1] = 1
        return arr

    def learnFromOneGame(self, boardEvaluator):
        self.allBoardOptionsValues = []
        with tf.GradientTape() as tape:
            outcome = playAGame(self, boardEvaluator).outcome()
            lossValue = tf.Variable(self.computerLoss(outcome))
        grads = tape.gradient(lossValue, self.chessNNModel.trainable_variables)
        print("grads: " , grads)
        self.optimizer.apply_gradients(zip(grads, self.chessNNModel.trainable_variables))
    
    def computerLoss(self, outcome):
        loss = 0
        if(outcome.result() == "1-0"):
            print("We Won!")
            for boardOptionValues in self.allBoardOptionsValues:
                percentages = boardOptionValues / sum(boardOptionValues)
                loss += 1 - max(percentages)
        else:
            print("We Lost!")
            for boardOptionValues in self.allBoardOptionsValues:
                percentages = boardOptionValues / sum(boardOptionValues)
                print("boardOptionValues: ", boardOptionValues)
                print("percentages: ")
                print("max(percentages): " , max(percentages))
                loss += max(percentages)

        
        loss /= len(self.allBoardOptionsValues)
        print("Loss: " , loss)
        print("")
        return loss

