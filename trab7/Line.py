from Figure import Figure
import cv2  

class Line(Figure):
    def __init__(self, points, color, r):
        self.__points = points
        self.__color = color
        self.__r = r

    def getPoints(self):
        return self.__points

    def draw(self, img):
        aux = self.__points
        cv2.line(img, [aux[0].getX(),aux[0].getY()],[aux[1].getX(),aux[1].getY()] ,self.__color, self.__r)

    def getColor(self):
        return self.__color