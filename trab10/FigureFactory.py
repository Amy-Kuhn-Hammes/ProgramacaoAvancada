from abc import ABC, abstractmethod

class FigureFactory(ABC):

    @abstractmethod
    def createFigure():
        pass
