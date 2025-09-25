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

def genColor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def genPoint():
    return (random.randint(0, 500), random.randint(0, 500))

# Gera pontos, linhas e polygonos
def generate(amt):
    
    #limpa a listas
    polygons.clear()
    lines.clear()
    points.clear()

    # gera 5 pontos
    for i in range(amt):
        points.append([genPoint(), genColor()])

    #gera 5 linhas
    for i in range(amt):
        lines.append([genPoint(), genPoint(), genColor()])

    #gera 5 polygonos
    for i in range(amt):
        polygons.append([genColor()])
        aux = []
        for j in range(random.randint(3, 5)):
            aux.append(genPoint())

        polygons[i].append(aux)

#evento de clcik
def click_event(event, x, y, flags, param):

    global clickCount
    global objsClicked

    #evento de click
    if event == cv2.EVENT_LBUTTONDOWN:
        clickCount+=1   

        # para todo poligonos, testa se o click for dentro
        for i in polygons:
            p = Point(x, y)
            pol = Polygon(i[1])
            if(pol.contains(p)):

                # preenche o poligono com a sua cor
                aux = np.array(i[1], np.int32)
                aux = aux.reshape((-1,1,2))
                cv2.fillPoly(img, pts=[aux], color=i[0])

                # atualiza imagem
                cv2.imshow("Image", img)
                cv2.setMouseCallback("Image", click_event)
                cv2.waitKey(1)

                # documenta
                objsClicked.append([i[1], i[0], time.perf_counter() - startTime])

    #mouse move
    if event == cv2.EVENT_MOUSEMOVE:
        cv2.circle(mouse,(x,y), 3, (255,0,0), -1)
        
def geraImg():
        
        global img

        #gera novos polygonos
        generate(2)

        #pinta a tela de branco
        img = np.zeros((500,500,3), np.uint8)
        img[:,0:500] = (255, 255, 255)

        #pinta linhas
        for i in lines:
            cv2.line(img, i[0],i[1],i[2],5)

        #pinta poligonos
        for i in polygons:
            aux = np.array(i[1], np.int32)
            aux = aux.reshape((-1,1,2))
            cv2.polylines(img,[aux],True,i[0], 5)

        #pinta pontos
        for i in points:
            cv2.circle(img,i[0], 15, i[1], -1)

        #atualiza imagem
        cv2.imshow("Image", img)
        cv2.setMouseCallback("Image", click_event)
        cv2.waitKey(0)

def doc():
    global clickCount

    aux = cv2.cvtColor(mouse, cv2.COLOR_BGR2RGB) 
    pil_img = Image.fromarray(aux)

    pil_img.save('img.pdf', save_all=True, resolution=100.0)
    
    doc = fitz.open("img.pdf")
    page = doc[0] # Get the first page

    # Insert text at a specific point
    page.insert_text((10, 10), "Percurso do Mouse", fontsize=12, color=(0, 0, 0))

    # Save the modified PDF
    doc.save("img2.pdf")
    doc.close()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 5, txt=f"Total de clicks: {clickCount}", ln=True, align="L")
    pdf.cell(200, 5, txt=f"Tempo de execução: {time.perf_counter() - startTime}", ln=True, align="L")
    pdf.cell(200, 5, txt="Objetos clickados:", ln=True, align="L")
    for i in objsClicked:
        pdf.cell(200, 5, txt=str(i), ln=True, align="L")

    pdf.output("text.pdf")
    
    result = fitz.open()

    with fitz.open("img2.pdf") as mfile:
        result.insert_pdf(mfile)

    with fitz.open("text.pdf") as mfile:
        result.insert_pdf(mfile)

    result.save("doc.pdf")

    os.remove("text.pdf") 
    os.remove("img.pdf") 
    os.remove("img2.pdf") 

# vars

points = []
lines = []
polygons = []

clickCount = 0;
objsClicked = []
startTime = time.perf_counter()

global img
global mouse

first = True

# paint mouse canvas white

mouse = np.zeros((500,500,3), np.uint8)
mouse[:,0:500] = (255, 255, 255)

while True:
    k = cv2.waitKey(0)

    #gera uma nova imagem sempre que preciona 'a'
    if(first or k == ord('a')):
        first = False
        geraImg()

    # para execução
    elif(k == 27):
        break

doc()

cv2.destroyAllWindows()

