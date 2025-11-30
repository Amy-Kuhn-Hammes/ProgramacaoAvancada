import random
random.random()
from LineFactory import LineFactory
from Point import Point
from SquareFactory import SquareFactory
from CircleFactory import CircleFactory
from Trail import Trail
from Grid import Grid
from MoveCommand import MoveCommand

class SquareGrid(Grid):
    
    def __init__(self, width, height, co, ch):
        self.__co = co
        self.__ch = ch
        self.__width = width
        self.__height = height
        self.__matrix = [[0]*width for i in range(height)]
        self.__trails = []
        self.__circle = -1
        self.__lines = []
        for i in range(50):
            self.__lines.append(LineFactory.createFigure([Point(i*20,0),Point(i*20,1000)],(0,0,0),1))
            self.__lines.append(LineFactory.createFigure([Point(0,i*20),Point(1000,i*20)],(0,0,0),1))



    def draw(self, img):
        for i in self.__lines:
            i.draw(img)

    def leftClick(self,x, y, img):
        square = SquareFactory.createFigure(Point(int(x/20)*20, int(y/20)*20), (0,0,0), 20)
        square.draw(img)

        self.__matrix[int(x/20)][int(y/20)] = 1

    def middleClick(self, x, y, img):
        if(self.__circle == -1):
            colorP = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            cordsP = Point(int(x/20)*20+10,int(y/20)*20+10)

            self.__circle = CircleFactory.createFigure(cordsP, colorP, 10)
            self.__circle.draw(img)
        else:
            circle = CircleFactory.createFigure(Point(int(x/20)*20+10,int(y/20)*20+10), self.__circle.getColor(), 10)
            circle.draw(img)

            trail = Trail(self.__circle.getPoint(), circle.getPoint(),circle.getColor(), 'dia')
            trail.floodFill(self.__matrix)
            self.__co.subinscribeNext(MoveCommand(trail, self.__ch, self.__co, 0))


            self.__trails.append(trail)

            self.__circle = -1