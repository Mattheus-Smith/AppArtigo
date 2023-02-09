import cv2
import numpy as np
from pylab import *

def funcionQuadrada(imgI, A, maximo):
    img = cv2.cvtColor(imgI, cv2.COLOR_RGB2GRAY)
    height, width = img.shape  # dimensões da imagem
    if (A == 0 ):
        A = 0.005
    if (maximo == 0 ):
        maximo = 255
  # transformação Quadratica
    for i in range(0, height):
        for j in range(0, width):
            pixel = imgI[i, j].astype(int)

            saida =  A*(pixel)**2
            if( saida[0] >= 255 ):
                saida[0] = maximo
            if (saida[1] >= 255):
                saida[1] = maximo
            if (saida[2] >= 255):
                saida[2] = maximo

            imgI[i,j] = saida

    return imgI

#
# #img = cv2.imread("./../1imagensEntrada/18.jpg")
# img = cv2.imread("./../output_gamma(0.8)_output_CLAHE_2_(4).png")
#
# parametroQuadrado = 0.05
# out = funcionQuadrada(img, parametroQuadrado, 255)
#
# texto = "./../output_quadrada_"+str(parametroQuadrado)+".png"
# cv2.imwrite(texto, out)