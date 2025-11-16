import cv2  
import numpy as np
import random
random.random()

global img
global points
global lines
global matrix
global corC
global pointC

corC = -1
pointC = -1
lines = []
matrix = [[0]*51 for i in range(51)]

for i in range(50):
    lines.append([[i*20,0],[i*20,1000]])
    lines.append([[0,i*20],[1000,i*20]])

def atualizaImg():
    
    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", click_event)
    cv2.waitKey(1)

def click_event(event, x, y, flags, param):
    global img
    global matrix
    global corC
    global pointC

    if event == cv2.EVENT_MBUTTONDOWN:
        aleatorio()

    #evento de click
    if event == cv2.EVENT_LBUTTONDOWN:

        pol = [[int(x/20)*20, int(y/20)*20], [int(x/20)*20 + 20, int(y/20)*20], [int(x/20)*20+20, int(y/20)*20+20], [int(x/20)*20, int(y/20)*20+20]]
        print(pol)
        aux = np.array(pol, np.int32)
        aux = aux.reshape((-1,1,2))
        print(aux)
        cv2.fillPoly(img, pts=[aux], color=(0,0,0))

        matrix[int(x/20)][int(y/20)] = 1
    
    if event == cv2.EVENT_RBUTTONDOWN:

        if(pointC == -1):
            pointC = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            corC = (int(x/20)*20+10,int(y/20)*20+10)
            cv2.circle(img, corC, 15, pointC, -1)
        else:
            aux = (int(x/20)*20+10,int(y/20)*20+10)
            cv2.circle(img,aux, 15, pointC, -1)

            lines2 = floodFill([int(corC[0]/20), int(corC[1]/20)], [int(aux[0]/20), int(aux[1]/20)])            

            for i in range(len(lines2)-1):
                cv2.line(img, [lines2[i][0]*20+10,lines2[i][1]*20+10], [lines2[i+1][0]*20+10,lines2[i+1][1]*20+10] ,pointC,2)

            atualizaImg()

            pointC = -1


    atualizaImg()

def floodFill(start, end):
    aux = [[1,0],[0,1],[-1,0],[0,-1]]

    auxM = [[0]*51 for i in range(51)]
    fila = [[start, [start]]]

    while len(fila) >0:
        #print(fila[0])
        for i in aux:
            x = fila[0][0][0]+i[0]
            y = fila[0][0][1]+i[1]
            if(x == end[0] and y == end[1]): 
                temp = fila[0][1].copy()
                temp.append([x,y])
                return temp 
            if x < 50 and x >= 0 and y < 50 and y >= 0 and auxM[x][y] == 0 and matrix[x][y] == 0:
                auxM[x][y] = fila[0][1]
                temp = fila[0][1].copy()
                temp.append([x,y])
                fila.append([[x,y], temp])
        fila.pop(0)
    return False

def geraImg():
        
    global img

    #pinta a tela de branco
    img = np.zeros((1000,1000,3), np.uint8)
    img[:,0:1000] = (255, 255, 255)

    #pinta linhas
    for i in range(len(lines)):
        cv2.line(img, lines[i][0], lines[i][1] ,(0,0,0),1)

    #atualiza imagem
    atualizaImg()

def aleatorio():
    global img
    global matrix
    matrix = [[0]*51 for i in range(51)]

    geraImg()
    for i in range(500):
        x = random.randint(0, 50)
        y = random.randint(0, 50)

        if matrix[x][y] == 1:
            i -= 1
            pass

        matrix[x][y] = 1

        pol = [[x*20, y*20], [x*20 + 20, y*20], [x*20+20, y*20+20], [x*20, y*20+20]]

        aux = np.array(pol, np.int32)
        aux = aux.reshape((-1,1,2))
        cv2.fillPoly(img, pts=[aux], color=(0,0,0))


    for i in range(10):
        while True:
            x1 = random.randint(0, 50)
            y1 = random.randint(0, 50)

            if matrix[x1][y1] == 0:
                break

        rc = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        aux = (int(x1)*20+10,int(y1)*20+10)
        cv2.circle(img,aux, 15, rc, -1)

        while True:
            x2 = random.randint(0, 50)
            y2 = random.randint(0, 50)

            if matrix[x2][y] == 0:
                break

        aux = (int(x2)*20+10,int(y2)*20+10)
        cv2.circle(img,aux, 15, rc, -1)

        lines2 = floodFill([x1, y1], [x2, y2])            

        for i in range(len(lines2)-1):
            cv2.line(img, [lines2[i][0]*20+10,lines2[i][1]*20+10], [lines2[i+1][0]*20+10,lines2[i+1][1]*20+10] ,rc,2)

    atualizaImg()
    

geraImg()


while True:
    k = cv2.waitKey(1)

    # para execução
    if(k == 27):
        break
    elif(k == ord('a')):
        aleatorio()

cv2.destroyAllWindows()