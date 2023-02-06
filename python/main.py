import cv2
import numpy as np
from matplotlib import pyplot as plt
from pylab import *
import sys
from absl import app, flags, logging
from absl.flags import FLAGS

flags.DEFINE_string('img', None, 'path to image file')
flags.DEFINE_string('pc', None, 'identifiy wich pc')

def mudarDiretorios():
    if (FLAGS.pc == "0"):#pessoa
        dirTxt = "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\saidas\\saida.txt"
        dirPlot = r"H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\saidas\\saida.png"
    elif (FLAGS.pc == "1"):#projeto
        dirTxt = "C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\saidas\\saida.txt"
        dirPlot = r"C:\Users\Smith Fernandes\Documents\4 - github\AppArtigo\python\\saidas\\saida.png"

    return dirPlot, dirTxt

def histo(imagem, dirPlot):
    img = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
    hist = cv2.calcHist([img], [0], None, [256], [0, 256]).astype(int)
    plt.plot(hist)
    plt.savefig(fname=dirPlot) #Projeto
    #plt.show()

    total = 0
    for i in range(len(hist)):
        total += hist[i]

    return hist, total

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

def identificarPicos(lista, total, dirTxt):
    suber = lista[0]+lista[1]+lista[2]
    dffSuber = total - suber

    super = lista[7] + lista[8] + lista[9]
    dffSuper = total - super

    meio = lista[3] + lista[4] + lista[5] + lista[6]
    f = open(dirTxt, "w")  # Pessoal

    if( suber > dffSuber ):
        f.write("1 Essa imagem tem suberexposicao")
        f.close()
        print("1 Essa imagem tem suberexposicao")
    elif( super > dffSuper ):
        f.write("2 Essa imagem tem superexposicao")
        f.close()
        print("2 Essa imagem tem superexposicao")
    elif( super > meio and suber > meio ):
        f.write("3 E uma com dois picos")
        f.close()
        print("3 E uma com dois picos")
    else:
        f.write("4 E uma imagem normal")
        f.close()
        print("4 E uma imagem normal")

def main(_args):

    dirPlot, dirTxt = mudarDiretorios()

    sol = cv2.imread(FLAGS.img)  # projeto
    #sol = cv2.imread("./imagens/26.jpg")  # projeto
    hist, total = histo(sol, dirPlot)

    identificarPicos(dividirHistograma(hist), total, dirTxt)

if __name__ == '__main__':
    try:
        app.run(main)
    except SystemExit:
        pass