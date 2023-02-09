import cv2
import numpy as np
from matplotlib import pyplot as plt
from pylab import *

def funcitonPiecewiseLinear(imgI, Ainicio, Amedio, Afim, grauInicio, grauMedio, grauFim, saturacao):
    img = cv2.cvtColor(imgI, cv2.COLOR_RGB2GRAY)
    height, width = img.shape  # dimensões da imagem

      # transformação linear por parte
    for i in range(0, height):
        for j in range(0, width):
            pixel = img[i, j]             #imagem que vai ser alterada em escala de cinza

            if( pixel <= grauInicio ):
                A = Ainicio
            elif(pixel <= grauMedio ):
                A = Amedio
            elif(pixel <= grauFim ):
                A = Afim

            pixel = imgI[i, j]            #imagem que vai ser alterada em escala RGB

            saida = []
            saida.append( np.clip(A * pixel[0], 0, saturacao) )
            saida.append( np.clip(A * pixel[1], 0, saturacao) )
            saida.append( np.clip(A * pixel[2], 0, saturacao) )
            imgI[i, j] = saida

            # if( i == 5 and j == 5 ):
            #     print("pixel: ", pixel, " - saida: ", saida)
    return imgI

img = cv2.imread("./../1imagensEntrada/01.jpg")

paramA_inicio = 1.2 ; grauA_inicio = 90
paramA_medio = 1.1 ; grauA_medio = 16
paramA_fim = 0.9   ; grauA_fim = 255
saturacao = 255

out = funcitonPiecewiseLinear(img, paramA_inicio, paramA_medio, paramA_fim, grauA_inicio, grauA_medio, grauA_fim, saturacao)

texto = "./../output_linearParte_"+"Ai: "+str(paramA_inicio)+ "_Am: "+str(paramA_medio)+ "_Af: "+str(paramA_fim)+"_grauI: "+str(grauA_inicio)+"_grauM: "+str(grauA_medio)+"_grauF: "+str(grauA_fim)+"_satu: "+str(saturacao)+".png"
texto = "./../teste.png"
cv2.imwrite(texto, out)