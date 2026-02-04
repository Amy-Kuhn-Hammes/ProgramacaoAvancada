from FigureFactory import FigureFactory
from Square import Square

class SquareFactory(FigureFactory):
    @staticmethod
    def createFigure(points, color, r):
        return Square(points, color, r)