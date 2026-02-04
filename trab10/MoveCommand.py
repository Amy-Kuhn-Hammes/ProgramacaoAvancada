from Command import Command
import cv2  
import random


class MoveCommand(Command):
    def __init__(self, trail, ch, co,pos, positions, matrix):
        self.__trail = trail
        self.__pos = pos
        self.__ch = ch
        self.__co = co
        self.__positions = positions
        self.__state = 0
        self.__matrix = matrix

    def execute(self, img):

        path = self.__trail.getPath()
        if self.__pos < len(path)-1:
            self.__ch.push(self)
            if(self.__positions[path[self.__pos+1][0]][path[self.__pos+1][1]] == 1):
                print('peixe')
                if random.randint(0,1) == 1:

                    self.__co.subinscribeWait(self)
                else:
                    self.__positions[path[self.__pos][0]][path[self.__pos][1]] = 0
                    self.__trail.floodFill(self.__matrix, self.__pos, [path[self.__pos+1][0], path[self.__pos+1][1]])
                    self.__pos = 0
                    self.__positions[path[self.__pos+1][0]][path[self.__pos+1][1]] = 1
                    cv2.line(img, self.__trail.getCentralPoint(self.__pos), self.__trail.getCentralPoint(self.__pos+1) ,self.__trail.getColor(),2)
                    self.__co.subinscribeWait(MoveCommand(self.__trail, self.__ch, self.__co, self.__pos+1, self.__positions, self.__matrix ))

                    
            else:
                self.__positions[path[self.__pos][0]][path[self.__pos][1]] = 0
                self.__positions[path[self.__pos+1][0]][path[self.__pos+1][1]] = 1
                cv2.line(img, self.__trail.getCentralPoint(self.__pos), self.__trail.getCentralPoint(self.__pos+1) ,self.__trail.getColor(),2)
                self.__co.subinscribeWait(MoveCommand(self.__trail, self.__ch, self.__co, self.__pos+1, self.__positions, self.__matrix ))
        else:
            self.__positions[path[self.__pos][0]][path[self.__pos][1]] = 0
