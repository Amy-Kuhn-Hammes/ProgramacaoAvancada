from FigureFactory import FigureFactory
import Circle

class CircleFactory(FigureFactory):        
    @staticmethod
    def createFigure(point, color, r):
        return Circle.Cicle(point, color, r)