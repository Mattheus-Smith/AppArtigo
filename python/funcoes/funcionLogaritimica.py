import cv2
import numpy as np
from pylab import *

def funcitonLogaritimica(imgI, A, B):
    img = cv2.cvtColor(imgI, cv2.COLOR_RGB2GRAY)
    height, width = img.shape  # dimensões da imagem

    # transformação linear
    for i in range(0, height):
        for j in range(0, width):
            pixel = imgI[i, j]

            c = 1.55
            saida = []
            saida.append( np.clip(c * np.log(1 + pixel[0] / 255), 0, 255) )
            saida.append( np.clip(c * np.log(1 + pixel[1] / 255), 0, 255) )
            saida.append( np.clip(c * np.log(1 + pixel[2] / 255), 0, 255) )
            imgI[i, j] = saida

    return imgI

img = cv2.imread("./../1imagensEntrada/27.jpg")

parametroA = 0.55
parametroB = 25
out = funcitonLogaritimica(img, parametroA, parametroB)

texto = "./../output_logaritimica_("+str(parametroA)+","+str(parametroB)+").png"
cv2.imwrite(texto, out)