import cv2  
import numpy as np
import random
random.random()
from LineFactory import LineFactory
from Point import Point
from SquareFactory import SquareFactory
from CircleFactory import CircleFactory
from Trail import Trail

class UI:
    def __init__(self):
        self.__matrix = [[0]*51 for i in range(51)]
        self.__circle = -1
        self.__trails = []
        self.geraImg()
    
    def geraImg(self):
        self.__lines = []
        for i in range(50):
            self.__lines.append(LineFactory.createFigure([Point(i*20,0),Point(i*20,1000)],(0,0,0),1))
            self.__lines.append(LineFactory.createFigure([Point(0,i*20),Point(1000,i*20)],(0,0,0),1))


        self.__img = np.zeros((1000,1000,3), np.uint8)
        self.__img[:,0:1000] = (255, 255, 255)

        for i in self.__lines:
            i.draw(self.__img)

        self.atualizaImg()


    def atualizaImg(self):
        def click_event(event, x, y, flags, param):

            if event == cv2.EVENT_RBUTTONDOWN:
                self.aleatorio()
                pass

            #evento de click
            if event == cv2.EVENT_LBUTTONDOWN:
                square = SquareFactory.createFigure(Point(int(x/20)*20, int(y/20)*20), (0,0,0), 20)
                square.draw(self.__img)

                self.__matrix[int(x/20)][int(y/20)] = 1
            
            if event == cv2.EVENT_MBUTTONDOWN:

                if(self.__circle == -1):
                    colorP = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    cordsP = Point(int(x/20)*20+10,int(y/20)*20+10)

                    self.__circle = CircleFactory.createFigure(cordsP, colorP, 10)
                    self.__circle.draw(self.__img)
                else:
                    circle = CircleFactory.createFigure(Point(int(x/20)*20+10,int(y/20)*20+10), self.__circle.getColor(), 10)
                    circle.draw(self.__img)

                    trail = Trail(self.__circle.getPoint(), circle.getPoint(),circle.getColor())
                    trail.floodFill(self.__matrix, True)
                    trail.showPath(self.__img)

                    self.__trails.append(trail)

                    self.__circle = -1

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
            trail.floodFill(self.__matrix, True)
            trail.showPath(self.__img)

        self.atualizaImg()


