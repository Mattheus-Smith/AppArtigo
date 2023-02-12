import cv2
import numpy as np
from pylab import *

def funcitonLinear4(imgI,A, B, limiarMin):
    img = cv2.cvtColor(imgI, cv2.COLOR_RGB2GRAY)
    height, width = img.shape  # dimensões da imagem

    # transformação linear
    for i in range(0, height):
        for j in range(0, width):
            cinza = img[i, j]

            if( cinza >= limiarMin ):
                pixel = imgI[i, j]
                saida = []
                saida.append( np.clip(A * pixel[0] + B, 0, 255) )
                saida.append( np.clip(A * pixel[1] + B, 0, 255) )
                saida.append( np.clip(A * pixel[2] + B, 0, 255) )
                imgI[i, j] = saida

    return imgI

img = cv2.imread("./../caso10/result_foreground.png")

# paraA = 2
# paraB = -40

paraA = 0.7
paraB = +40
limiarMax = 120

out = funcitonLinear4(img, paraA, paraB, limiarMax)

texto = "./../output_linear_("+str(limiarMax)+").png"
cv2.imwrite(texto, out)