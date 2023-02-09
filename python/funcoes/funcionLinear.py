import cv2
import numpy as np
from pylab import *

def funcitonLinear(imgI, A, B):
    img = cv2.cvtColor(imgI, cv2.COLOR_RGB2GRAY)
    height, width = img.shape  # dimensões da imagem

    # transformação linear
    for i in range(0, height):
        for j in range(0, width):
            pixel = imgI[i, j]
            saida = []
            saida.append( np.clip(A * pixel[0] + B, 0, 255) )
            saida.append( np.clip(A * pixel[1] + B, 0, 255) )
            saida.append( np.clip(A * pixel[2] + B, 0, 255) )
            imgI[i, j] = saida

    return imgI

img = cv2.imread("./../1imagensEntrada/01.jpg")

parametroA = 0.55
parametroB = 25
out = funcitonLinear(img, parametroA, parametroB)

texto = "./../output_linear_("+str(parametroA)+","+str(parametroB)+").png"
cv2.imwrite(texto, out)