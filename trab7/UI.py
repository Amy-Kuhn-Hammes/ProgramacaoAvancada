import cv2  
import numpy as np
import random
random.random()
from LineFactory import LineFactory
from Point import Point
from SquareFactory import SquareFactory
from CircleFactory import CircleFactory
from Trail import Trail
from SquareGrid import SquareGrid
from HexGrid import HexGrid

class UI:
    _instance = None

    def __new__(cls, typeGrid):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.init(typeGrid)
        return cls._instance

    def init(self, typeGrid):
        if typeGrid == 'square':
            self.__grid = SquareGrid(50, 50)
        else:
            self.__grid = HexGrid(33, 110)
            
        self.geraImg()
    
    def geraImg(self):
        self.__img = np.zeros((1000,1000,3), np.uint8)
        self.__img[:,0:1000] = (255, 255, 255)

        self.__grid.draw(self.__img)

        self.atualizaImg()


    def atualizaImg(self):
        def click_event(event, x, y, flags, param):

            if event == cv2.EVENT_RBUTTONDOWN:
                #self.aleatorio()
                pass

            #evento de click
            if event == cv2.EVENT_LBUTTONDOWN:
                self.__grid.leftClick(x,y, self.__img)
            
            if event == cv2.EVENT_MBUTTONDOWN:
                self.__grid.middleClick(x,y, self.__img)

            self.atualizaImg()

        cv2.imshow("Image", self.__img)
        cv2.setMouseCallback("Image", click_event)
        cv2.waitKey(1)

    def closeWindows():
        cv2.destroyAllWindows()

    def readKeys(self):
        k = cv2.waitKey(1)

        if(k == 27):
            self.closeWindows()
        elif(k == ord('a')):
            self.aleatorio()

'''
    def aleatorio(self):
        self.__matrix = [[0]*51 for i in range(51)]

        self.geraImg()
        for i in range(500):
            x = random.randint(0, 50)
            y = random.randint(0, 50)

            if self.__matrix[x][y] == 1:
                i -= 1
                pass

            self.__matrix[x][y] = 1

            square = SquareFactory.createFigure(Point(x*20, y*20), (0,0,0), 20)
            square.draw(self.__img)


        for i in range(10):
            while True:
                x1 = random.randint(0, 50)
                y1 = random.randint(0, 50)

                if self.__matrix[x1][y1] == 0:
                    break

            circle = CircleFactory.createFigure(Point(x1*20+10,y1*20+10),(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 10)
            circle.draw(self.__img)

            while True:
                x2 = random.randint(0, 50)
                y2 = random.randint(0, 50)

                if self.__matrix[x2][y2] == 0:
                    break

            circle2 = CircleFactory.createFigure(Point(x2*20+10,y2*20+10),circle.getColor(), 10)
            circle2.draw(self.__img)

            trail = Trail(circle.getPoint(), circle2.getPoint(), circle.getColor())      
            trail.floodFill(self.__matrix, False)
            trail.showPath(self.__img)

        self.atualizaImg()
'''

