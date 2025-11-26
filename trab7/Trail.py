import cv2  
import random
random.random()

class Trail():
    def __init__(self, start, end, color, type):
        self.__type = type
        self.__start = start
        self.__end = end
        self.__path = []
        self.__color = color

    def floodFill(self, matrix):
        # not even God can debug or implement this anymore 

        aux = [[0, -2], [0, -1], [0, 1],[0, 2], [1, -1], [1, 1]]
        aux2 = [[0, -2], [0, -1], [0, 1],[0, 2], [-1, -1], [-1, 1]]
        if(self.__type == 'dia'):
            aux = [[1,0],[0,1],[-1,0],[0,-1], [1,1],[-1,-1],[-1,1],[1,-1]]
        elif(self.__type == 'sq'):
            aux = [[1,0],[0,1],[-1,0],[0,-1]]

        auxM = [[0]*len(matrix[0]) for i in range(len(matrix))]

       
        temp = [int(self.__start.getX()/20), int(self.__start.getY()/20)]
        endP = [int(self.__end.getX()/20), int(self.__end.getY()/20)]
        if type(self.__type) != str:
            for i in range(len(self.__type)):
                for j in range(len(self.__type[0])):
                    if self.__type[i][j].getCentralPoint().getX() == self.__start.getX() and self.__type[i][j].getCentralPoint().getY() == self.__start.getY():
                        temp = [i, j]       

                    if self.__type[i][j].getCentralPoint().getX() == self.__end.getX() and self.__type[i][j].getCentralPoint().getY() == self.__end.getY():
                        endP = [i, j]        

        fila = [[temp, [temp]]]


        while len(fila) >0:

            for i in range(len(aux)):
                x = fila[0][0][0]+aux[i][0]
                y = fila[0][0][1]+aux[i][1]
                if type(self.__type) != str and fila[0][0][1]%2 == 0:
                    x = fila[0][0][0]+aux2[i][0]
                    y = fila[0][0][1]+aux2[i][1]
                if x == endP[0] and y == endP[1]: 
                    temp = fila[0][1].copy()
                    temp.append([x,y])
                    self.__path = temp
                    return temp 
                if x < len(matrix) and x >= 0 and y < len(matrix[0]) and y >= 0 and auxM[x][y] == 0 and matrix[x][y] == 0:
                    auxM[x][y] = 1
                    temp = fila[0][1].copy()
                    temp.append([x,y])
                    fila.append([[x,y], temp])
            fila.pop(0)
        return []
    
    def showPath(self, img):

        if type(self.__type) == str:
            for i in range(len(self.__path)-1):
                cv2.line(img, [self.__path[i][0]*20+10,self.__path[i][1]*20+10], [self.__path[i+1][0]*20+10,self.__path[i+1][1]*20+10] ,self.__color,2)
        else:
            for i in range(len(self.__path)-1):

                aux1 = self.__type[self.__path[i][0]][self.__path[i][1]].getCentralPoint().getIntPoint()
                aux2 = self.__type[self.__path[i+1][0]][self.__path[i+1][1]].getCentralPoint().getIntPoint()

                cv2.line(img, aux1, aux2 ,self.__color,2)

