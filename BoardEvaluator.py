import abc

class BoardEvaluator (metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getIndexOfBestBoard(self, boards):
        pass