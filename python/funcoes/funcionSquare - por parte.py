import cv2
import numpy as np
from pylab import *

def funcionSquare (imagem, limiar,Amin, Amax):
    img = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
    height, width = img.shape  # dimensões da imagem

    # transformação Quadratica
    for i in range(0, height):
        for j in range(0, width):
            pixel = img[i,j]

            if ( pixel > limiar ):
                pixel = imagem[i, j].astype(int)
                saida = Amax * np.square(pixel)

                if (saida[0] >= 255):
                    saida[0] = 255
                if (saida[1] >= 255):
                    saida[1] = 255
                if (saida[2] >= 255):
                    saida[2] = 255
                imagem[i, j] = saida

            else:
                pixel = imagem[i, j].astype(int)
                saida = Amin * np.square(pixel)

                if (saida[0] >= 255):
                    saida[0] = 255
                if (saida[1] >= 255):
                    saida[1] = 255
                if (saida[2] >= 255):
                    saida[2] = 255
                imagem[i, j] = saida

    return imagem

img = cv2.imread("./../1imagensEntrada/10.jpg")

limiar = 249
paramSquareMin = 0.004
paramSquareMax = 0.0032
out = funcionSquare(img, limiar ,paramSquareMin, paramSquareMax)

texto = "./../output_Square_"+str(paramSquareMin)+"_"+str(paramSquareMax)+"_por_parte.png"
cv2.imwrite(texto, out)




