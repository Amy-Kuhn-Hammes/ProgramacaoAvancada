
class Point():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def getIntPoint(self):
        return [int(self.__x), int(self.__y)]
    
    def getPoint(self):
        return [self.__x, self.__y]
        
    def updatePoint(self, x, y):
        self.__x = x
        self.__y = y

    def getOnMatrix(self):
        return (int(self.__x/20),int(self.__y/20))