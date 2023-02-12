import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
from pylab import *
import sys
from absl import app, flags, logging
from absl.flags import FLAGS

def Histograma(imagem):
    img = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
    hist = cv2.calcHist([img], [0], None, [256], [0, 256]).astype(int)

    total = 0
    for i in range(len(hist)):
        total += hist[i]

    return hist, total

def dividirHistograma(hist):

    tam = 4
    histDividido = np.array_split(hist, tam)

    cont = 0
    lista=[]
    for i in range(0, tam):
        somar=0
        for j in range(0, len(histDividido[i])):
            somar += int(histDividido[i][j])
            cont +=1
        lista.append(somar)
    #print(lista)

    return lista

def identificarPicos(lista, total):
    suber = lista[0]; dffSuber = total - suber
    super = lista[3]; dffSuper = total - super
    meio = lista[1] + lista[2]

    if( suber > dffSuber ):
        print("1 Essa imagem tem suberexposicao com ", (suber*100)/total, "%")
    elif( super > dffSuper ):
        print("2 Essa imagem tem superexposicao com ", (super * 100) / total, "%")
    elif( super > meio and suber > meio ):
        print("3 Essa imagem tem superexposicao com suber: ", (suber * 100) / total, "%", "e super: ", (super * 100) / total,"%")
    else:
        print("4 E uma imagem normal")

img = cv2.imread("./../caso10/10.jpg")
#
histo, total = Histograma(img)
#
identificarPicos(dividirHistograma(histo), total)
