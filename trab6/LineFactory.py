from FigureFactory import FigureFactory
import Line

class LineFactory(FigureFactory):
    @staticmethod
    def createFigure(points, color, r):
        return Line.Line(points, color, r)