import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
from pylab import *
import sys
from absl import app, flags, logging
from absl.flags import FLAGS

flags.DEFINE_string('img', None, 'path to image file')
flags.DEFINE_string('pc', "1", 'identifiy wich pc')

def mudarDiretorios():
    if (FLAGS.pc == "0"):#pessoa
        dirImgEntrada = "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\1imagensEntrada"
        dirPlotHistEntrada = "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\2histoImagensEntrada\\"
        dirClassificacaoEntrada = "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\3ClassificacaoImagem\\"

    elif (FLAGS.pc == "1"):#projeto
        dirImgEntrada = "C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\1imagensEntrada"
        dirPlotHistEntrada = "C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\2histoImagensEntrada\\"
        dirClassificacaoEntrada = "C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\3ClassificacaoImagem\\"


    return dirImgEntrada, dirPlotHistEntrada, dirClassificacaoEntrada

def Histograma(imagem, dirPlot):
    img = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
    hist = cv2.calcHist([img], [0], None, [256], [0, 256]).astype(int)
    plt.plot(hist)
    plt.savefig(fname=dirPlot) #Projeto
    plt.close()
    #plt.show()

    total = 0
    for i in range(len(hist)):
        total += hist[i]

    return hist, total

def lerDiretorio(pasta):
    listaImagensEntrada = []
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            listaImagensEntrada.append(os.path.join(diretorio, arquivo))
            #print(os.path.join(diretorio, arquivo))
    return listaImagensEntrada

def criarHisto(listaImg, dirPlotHistEntrada):
    histosEntrada = []
    listaTotalHistoEntrada = []
    for i in range (1, len(listaImg)+1):
        if i<10:
            cam = dirPlotHistEntrada +str(0)+str(i) + ".jpg"
        else:
            cam = dirPlotHistEntrada + str(i) + ".jpg"
        histo, total = Histograma(cv2.imread(listaImg[i-1]), cam)
        histosEntrada.append(histo)
        listaTotalHistoEntrada.append(total)
    return histosEntrada, listaTotalHistoEntrada

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

def identificarPicos(lista, total, dirClassificacaoEntrada, i):

    suber = lista[0]
    dffSuber = total - suber

    super = lista[3]
    dffSuper = total - super

    meio = lista[1] + lista[2]

    if i<10:
        i = str(0)+ str(i)

    output = dirClassificacaoEntrada+str(i)+".txt"
    f = open(output, "w")

    if( suber > dffSuber ):
        f.write("1 Essa imagem tem suberexposicao")
        f.close()
        #print("1 Essa imagem tem suberexposicao")

    elif( super > dffSuper ):
        f.write("2 Essa imagem tem superexposicao")
        f.close()
        #print("2 Essa imagem tem superexposicao")

    elif( super > meio and suber > meio ):
        f.write("3 E uma com dois picos")
        f.close()
        #print("3 E uma com dois picos")

    else:
        f.write("4 E uma imagem normal")
        f.close()
        #print("4 E uma imagem normal")

def classificarImage(histosEntrada, listaTotalHistoEntrada, dirClassificacaoEntrada):
    for i in range(1, len(histosEntrada)+1):
        identificarPicos(dividirHistograma(histosEntrada[i - 1]), listaTotalHistoEntrada[i - 1], dirClassificacaoEntrada, i)

def main(_args):
    dirImgEntrada, dirPlotHistEntrada, dirClassificacaoEntrada = mudarDiretorios()

    listaImagensEntrada = lerDiretorio(dirImgEntrada)

    histosEntrada, listaTotalHistoEntrada = criarHisto(listaImagensEntrada, dirPlotHistEntrada)

    # classificarImage(listaImagensEntrada, histosEntrada, listaTotalHistoEntrada)
    classificarImage(histosEntrada, listaTotalHistoEntrada, dirClassificacaoEntrada)

if __name__ == '__main__':
    try:
        app.run(main)
    except SystemExit:
        pass


