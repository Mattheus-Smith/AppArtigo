import cv2
import numpy as np
from matplotlib import pyplot as plt
from pylab import *
import sys
from absl import app, flags, logging
from absl.flags import FLAGS

flags.DEFINE_string('img', None, 'path to image file')

def histo(imagem):
    img = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
    hist = cv2.calcHist([img], [0], None, [256], [0, 256]).astype(int)
    plt.plot(hist)
    #plt.savefig(r"C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\saidas\\saida.png") #Projeto
    #plt.savefig(r"H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\saidas\\saida.png") #pessoal
    plt.show()

    total = 0
    for i in range(len(hist)):
        total += hist[i]

    return hist, total

def resultado(hist):
    porcetagem = 0.5
    parteE = 0;
    parteD = 0

    for i in range(len(hist)):
        if (i < int(len(hist) * porcetagem)):
            parteE += hist[i]
        elif (i > int(len(hist) * porcetagem)):
            parteD += hist[i]

    # print("Esq ",parteE)
    # print("Meio ", meio)
    # print("Dir ",parteD )

    # f = open("C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\saidas\\saida.txt", "w")    #projeto
    f = open("H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\saidas\\saida.txt", "w")  #Pessoal
    if (parteD > parteE):
        f.write("Essa imagem tem superexposição")
        f.close()
        print("Essa imagem tem superexposição")
    elif (parteE > parteD):
        f.write("Essa imagem tem suberexposição")
        f.close()
        print("Essa imagem tem suberexposição")
    else:
        f.write("É uma imagem normal")
        f.close()
        print("É uma imagem normal")

def dividirHistograma(hist):

    histDividido = np.array_split(hist, 10)

    cont = 0
    lista=[]
    for i in range(0, 10):
        somar=0
        for j in range(0, len(histDividido[i])):
            somar += int(histDividido[i][j])
            cont +=1
        lista.append(somar)
    #print(lista)

    return lista

def identificarPicos(lista, total):
    suber = lista[0]+lista[1]+lista[2]
    dffSuber = total - suber

    super = lista[7] + lista[8] + lista[9]
    dffSuper = total - super

    meio = lista[3] + lista[4] + lista[5] + lista[6]

    if( suber > dffSuber ):
        print("suber")
    elif( super > dffSuper ):
        print("super")
    elif( super > meio and suber > meio ):
        print("pico")
    else:
        print("normal")

super = cv2.imread("./imagens/26.jpg")  # projeto
suber = cv2.imread("./imagens/25.jpg")  # projeto
picos = cv2.imread("./imagens/18.jpg")  # projeto
normal = cv2.imread("./imagens/20.jpg")  # projeto

teste = cv2.imread("./imagens/26.jpg")  # projeto

hist, total = histo(teste)

identificarPicos(dividirHistograma(hist), total)
