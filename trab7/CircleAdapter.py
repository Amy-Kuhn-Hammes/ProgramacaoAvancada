from Point import Point

class CircleAdapter(Point):

    def __init__(self, circle):
        self.__circle = circle

    def getX(self):
        return self.__circle.getPoint().getX()

    def getY(self):
        return self.__circle.getPoint().getY()