from Figure import Figure
import cv2  

class Cicle(Figure):
    def __init__(self, point, color, r):
        self.__point = point
        self.__color = color
        self.__r = r

    def getPoints(self):
        return [self.__point]

    def getPoint(self):
        return self.__point

    def draw(self, img):
        cv2.circle(img, [self.__point.getX(), self.__point.getY()], self.__r, self.__color, -1)

    def getColor(self):
        return self.__color