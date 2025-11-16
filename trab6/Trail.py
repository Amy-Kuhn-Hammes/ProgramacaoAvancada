import cv2  

class Trail():
    def __init__(self, start, end, color):
        self.__start = start
        self.__end = end
        self.__path = []
        self.__color = color

    def floodFill(self, matrix, diagonal):
        aux = [[1,0],[0,1],[-1,0],[0,-1]]
        if(diagonal):
            aux = [[1,0],[0,1],[-1,0],[0,-1], [1,1],[-1,-1],[-1,1],[1,-1]]

        auxM = [[0]*51 for i in range(51)]
        temp = [int(self.__start.getX()/20), int(self.__start.getY()/20)]
        fila = [[temp, [temp]]]

        while len(fila) >0:

            for i in aux:
                x = fila[0][0][0]+i[0]
                y = fila[0][0][1]+i[1]
                if x == int(self.__end.getX()/20) and y == int(self.__end.getY()/20): 
                    temp = fila[0][1].copy()
                    temp.append([x,y])
                    self.__path = temp
                    return temp 
                if x < 50 and x >= 0 and y < 50 and y >= 0 and auxM[x][y] == 0 and matrix[x][y] == 0:
                    auxM[x][y] = len(fila[0][1])
                    temp = fila[0][1].copy()
                    temp.append([x,y])
                    fila.append([[x,y], temp])
            fila.pop(0)
        return []
    
    def showPath(self, img):
        for i in range(len(self.__path)-1):
            cv2.line(img, [self.__path[i][0]*20+10,self.__path[i][1]*20+10], [self.__path[i+1][0]*20+10,self.__path[i+1][1]*20+10] ,self.__color,2)