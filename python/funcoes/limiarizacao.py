import cv2
import numpy as np
from pylab import *

def funcitonLimiarUnico(imgI,limiar):
    img = cv2.cvtColor(imgI, cv2.COLOR_RGB2GRAY)
    height, width = img.shape  # dimensões da imagem

    # transformação linear
    for i in range(0, height):
        for j in range(0, width):
            cinza = img[i, j]

            if( cinza > limiar ):
                imgI[i, j] = 0

    return imgI

def funcitonEntreDoisLimiar(imgI,limiarMin, limiarMax):
    img = cv2.cvtColor(imgI, cv2.COLOR_RGB2GRAY)
    height, width = img.shape  # dimensões da imagem

    # transformação linear
    for i in range(0, height):
        for j in range(0, width):
            cinza = img[i, j]

            if( cinza <= limiarMin or cinza>=limiarMax ):
                imgI[i, j] = 0

    return imgI

#img = cv2.imread("./../6casoSuuuper/result_foreground.png")
img = cv2.imread("./../1imagensEntrada/10.jpg")

limiar = 247
out = funcitonLimiarUnico(img,limiar)
texto = "./../output_limiarizacao_("+str(limiar)+").png"
cv2.imwrite(texto, out)

# limiarMin = 45
# limiarMax = 100
# out = funcitonEntreDoisLimiar(img,limiarMin, limiarMax)
# texto = "./../output_limiarizacao_("+str(limiarMin)+"_"+str(limiarMax)+").png"
# cv2.imwrite(texto, out)