from Figure import Figure
import cv2 
from Point import Point
import numpy as np


class Square(Figure):
    def __init__(self, point, color, r):
        self.__point = point
        self.__points = [point, Point(point.getX()+r, point.getY()), Point(point.getX()+r, point.getY()+r), Point(point.getX(), point.getY()+r)]
        self.__color = color

    def getPoints(self):
        return [self.__point]
    
    def getPoint(self):
        return self.__point

    def draw(self, img):

        temp = []
        for i in self.__points:
            temp.append(i.getPoint())

        aux = np.array(temp, np.int32)
        aux = aux.reshape((-1,1,2))
        cv2.fillPoly(img, pts=[aux], color=self.__color)

    def getColor(self):
        return self.__color