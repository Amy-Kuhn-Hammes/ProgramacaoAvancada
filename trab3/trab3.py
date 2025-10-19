import cv2  
import numpy as np
import random
random.random()
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import time
from PIL import Image
import fitz
from fpdf import FPDF
import os

global img
global points
global lines

points = []
lines = []

def geraImg():
        
        global img
        global points

        #pinta a tela de branco
        img = np.zeros((500,500,3), np.uint8)
        img[:,0:500] = (255, 255, 255)

        #pinta linhas
        for i in range(len(lines)):
            cv2.line(img, lines[i], lines[(i+1)%len(lines)] ,[0,0,255],5)

        #pinta pontos
        for i in points:
            cv2.circle(img,i, 5, [0,0,0], -1)

        #atualiza imagem
        cv2.imshow("Image", img)
        cv2.setMouseCallback("Image", click_event)
        cv2.waitKey(0)

#evento de clcik
def click_event(event, x, y, flags, param):
    global points
    #evento de click
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append([x,y])

        if(len(points) >= 3):
            
            giftWarping()

        geraImg()

# acha ponto mais a esquerda 
def leftmost():
    global points
    m = 0
    for i in range(1,len(points)):
        if points[i][0] < points[m][0]:
            m = i

        #se tiverem dois pontos mais a esquerda, pega o mais a cima 
        elif points[i][0] == points[m][0]:
            if points[i][1] > points[m][1]:
                m = i
    return m

#ve se 3 pontos então no sentido anti-horário
def det(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) \
        -(p2[1] - p1[1]) * (p3[0] - p1[0])

def giftWarping():
    global lines
    lines.clear()

    l = leftmost()
    leftMost = points[l]
    atual = leftMost
    lines.append(atual)
    proximo = points[1]
    i = 2
    proximoi = -1
    while True:
        checking = points[i]

        crossProduct = det(atual, proximo, checking)

        if crossProduct < 0:
            proximo = checking
            proximoi = i
        i+=1
        if i == len(points):
            if proximo == leftMost:
                break
            i = 0
            lines.append(proximo)
            atual = proximo
            proximo = leftMost
    print(lines)

def doc():
    global lines
    global points

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 5, txt=f"Total de pontos: {len(points)}", ln=True, align="L")
    pdf.cell(200, 5, txt=f"Tempo de pontos na envoltória: {len(lines)}", ln=True, align="L")
    pdf.cell(200, 5, txt=f"Tempo de pontos dentro envoltória: {len(points)-len(lines)}", ln=True, align="L")
    pdf.output("text.pdf")

    result = fitz.open()

    with fitz.open("docBase.pdf") as mfile:
        result.insert_pdf(mfile)

    with fitz.open("text.pdf") as mfile:
        result.insert_pdf(mfile)

    result.save("doc.pdf")
    os.remove("text.pdf") 


geraImg()

while True:
    k = cv2.waitKey(0)
#gera uma nova imagem sempre que preciona 'a'
    if(k == ord('a')):
        lines.clear()
        points.clear()
        geraImg()

    if(k == ord('s')):
        lines.clear()
        points.clear()
        for i in range(10):
            points.append([random.randint(0, 500), random.randint(0, 500)])
        giftWarping()
        geraImg()

    # para execução
    elif(k == 27):
        break

doc()

cv2.destroyAllWindows()
