from Figure import Figure
import cv2 
from Point import Point
import numpy as np
from math import sqrt

class Hex(Figure):
    def __init__(self, point, color, r):
        self.__point = point
        self.__points = [point, Point(point.getX()+r/2, point.getY()+(r*sqrt(3))/2), Point(point.getX()+r/2+r, point.getY()+(r*sqrt(3))/2), Point(point.getX()+r*2, point.getY()), Point(point.getX()+r/2+r, point.getY()-(r*sqrt(3))/2), Point(point.getX()+r/2, point.getY()-(r*sqrt(3))/2)]
        self.__color = color
        self.__r = r

    def getPoints(self):
        return self.__points
    
    def getPoint(self):
        return self.__point
    
    def getCentralPoint(self):
        return Point(int(self.__point.getX())+self.__r, int(self.__point.getY()))

    def draw(self, img):

        temp = []
        for i in self.__points:
            temp.append(i.getPoint())

        aux = np.array(temp, np.int32)
        self.__aux = aux.reshape((-1,1,2))
        cv2.polylines(img, [self.__aux], True, color=self.__color)

    def getColor(self):
        return self.__color
    
    def colide(self, point):
        temp = []
        for i in self.__points:
            temp.append([i.getIntPoint()])
        temp = np.array(temp)

        r = cv2.pointPolygonTest(temp, (point.getX(), point.getY()), False)

        if r > 0:
            return True
        return False
    
    def fill(self, img):
        cv2.fillPoly(img, pts=[self.__aux], color=self.__color)
