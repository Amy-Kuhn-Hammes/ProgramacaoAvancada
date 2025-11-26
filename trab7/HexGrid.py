from Grid import Grid
from HexFactory import HexFactory
from math import sqrt
from Point import Point
import random
random.random()
from CircleFactory import CircleFactory
from Trail import Trail
from CircleAdapter import CircleAdapter

class HexGrid(Grid):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__matrix = [[0]*height for i in range(width)]
        self.__trails = []
        self.__circle = -1
        self.__hex = [[] for i in range(width)]
        for i in range(width):
            for j in range(height):
                if j % 2 == 0:
                    self.__hex[i].append(HexFactory.createFigure(Point(30*i,(10*sqrt(3))+j*(10*sqrt(3)/2)), (0,0,0), 10))
                else:
                    self.__hex[i].append(HexFactory.createFigure(Point(15+30*i,(10*sqrt(3))+j*(10*sqrt(3)/2)), (0,0,0), 10))


    def draw(self, img):
        for i in self.__hex:
            for j in i:
                j.draw(img)

    def leftClick(self,x, y, img):
        for i in range(self.__width):
            for j in range(self.__height):
                if self.__hex[i][j].colide(Point(x, y)):
                    self.__hex[i][j].fill(img)
                    self.__matrix[i][j] = 1
                    break

    def middleClick(self, x, y, img):
        if(self.__circle == -1):
            cordsP = None
            for i in self.__hex:
                for j in i:
                    if j.colide(Point(x, y)):
                        cordsP = j.getCentralPoint()
                        
                        break

            colorP = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.__circle = CircleFactory.createFigure(cordsP, colorP, 10)
            self.__circle.draw(img)

            # adapter de circle para point
            # circleAdapter = CircleAdapter(self.__circle)
            # print(self.__hex[0][0].colide(circleAdapter))

        else:
            cordsP = None
            for i in self.__hex:
                for j in i:
                    if j.colide(Point(x, y)):
                        cordsP = j.getCentralPoint()
                        break

            circle = CircleFactory.createFigure(cordsP, self.__circle.getColor(), 10)
            circle.draw(img)

            trail = Trail(self.__circle.getPoint(), circle.getPoint(),circle.getColor(),self.__hex)
            trail.floodFill(self.__matrix)
            trail.showPath(img)

            self.__trails.append(trail)

            self.__circle = -1