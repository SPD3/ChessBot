from BoardEvaluator import BoardEvaluator
import random

class RandomBoardEvaluator(BoardEvaluator):
    def getIndexOfBestBoard(self, boards):
        return int(random.random() * len(boards))
