from FirstMoveBoardEvaluator import FirstMoveBoardEvaluator
from PlayAGame import playAGame
from NNBoardEvaluatorRelu import NNBoardEvaluatorRelu
from RandomBoardEvaluator import RandomBoardEvaluator
from FirstMoveBoardEvaluator import FirstMoveBoardEvaluator

def main():
    whiteBoardEvaluator = RandomBoardEvaluator()
    blackBoardEvaluator = RandomBoardEvaluator()
    #playAGame(whiteBoardEvaluator, blackBoardEvaluator)

    blackBoardEvaluator = FirstMoveBoardEvaluator()
    whiteNNBoardEvaluator = NNBoardEvaluatorRelu()
    for i in range(1):
        whiteNNBoardEvaluator.learnFromOneGame(blackBoardEvaluator)

    print("All Done!")

if __name__ == "__main__":
    main()