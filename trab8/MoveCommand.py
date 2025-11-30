from Command import Command
import cv2  


class MoveCommand(Command):
    def __init__(self, trail, ch, co,pos):
        self.__trail = trail
        self.__pos = pos
        self.__ch = ch
        self.__co = co

    def execute(self, img):
        print('cavalo')
        self.__ch.push(self)
        if self.__pos < len(self.__trail.getPath())-1:
            cv2.line(img, self.__trail.getCentralPoint(self.__pos), self.__trail.getCentralPoint(self.__pos+1) ,self.__trail.getColor(),2)
            self.__co.subinscribeWait(MoveCommand(self.__trail, self.__ch, self.__co, self.__pos+1))
