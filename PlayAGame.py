import itertools
import chess

def playAGame(whiteBoardEvaluator, blackBoardEvaluator, testMode=False):
    board = chess.Board()
    whitesTurn = True
    count = 0
    while(not board.is_game_over()):
        if(whitesTurn):
            nextMove = getNextMove(board, whiteBoardEvaluator)
        else:
            nextMove = getNextMove(board, blackBoardEvaluator)
        
        board.push(nextMove)
        if(count % 50 == 0 and testMode):
            print(board)
            print("-----------------------")

        count += 1
        whitesTurn = not whitesTurn

    if(testMode):
        print("Total Moves: " , count)
        print("Outcome: " , board.outcome())

    return board

def getNextMove(board, boardEvaluator):
    nextBoards = []
    for move in board.legal_moves:
        newBoard = board.copy()
        newBoard.push(move)
        nextBoards.append(newBoard)
    indexOfNextBestBoard = boardEvaluator.getIndexOfBestBoard(nextBoards)
    return next(itertools.islice(board.legal_moves, indexOfNextBestBoard, None))