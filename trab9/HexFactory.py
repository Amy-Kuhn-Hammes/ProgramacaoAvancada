from FigureFactory import FigureFactory
from Hex import Hex

class HexFactory(FigureFactory):
    @staticmethod
    def createFigure(points, color, r):
        return Hex(points, color, r)