import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
from pylab import *
import sys
from absl import app, flags, logging
from absl.flags import FLAGS

def mudarDiretorios():
    dirImgEntrada = "C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\1imagensEntrada"
    dirPlotHistEntrada = "C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\2histoImagensEntrada\\"
    dirClassificacaoEntrada = "C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\3ClassificacaoImagem\\"

    dirImgSaida = "C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\4imagensSaida\\"
    dirPlotHistSaida = "C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\5histoImagensSaida\\"

    # dirImgEntrada = "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\1imagensEntrada"
    # dirPlotHistEntrada = "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\2histoImagensEntrada\\"
    # dirClassificacaoEntrada = "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\3ClassificacaoImagem\\"
    #
    # dirImgSaida = "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\4imagensSaida\\"
    # dirPlotHistSaida = "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\5histoImagensSaida\\"

    return dirImgEntrada, dirPlotHistEntrada, dirClassificacaoEntrada, dirImgSaida, dirPlotHistSaida

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

def criarHisto(listaImg, dirPlot):
    histosEntrada = []
    listaTotalHistoEntrada = []
    for i in range (1, len(listaImg)+1):
        cam = dirPlot+str(i)+".jpg"
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

def verificarPorcetagem(listaImagensEntrada,classe, i):
    print(i, classe, listaImagensEntrada)

def identificarPicos(listaImagensEntrada, lista, total, dirClassificacaoEntrada, i):

    suber = lista[0]
    dffSuber = total - suber

    super = lista[3]
    dffSuper = total - super

    meio = lista[1] + lista[2]

    if i<10:
        i = str(0)+ str(i)

    output = dirClassificacaoEntrada+str(i)+".txt"
    f = open(output, "w")  # Pessoal

    if( suber > dffSuber ):
        verificarPorcetagem(listaImagensEntrada, (suber*100)/total, 1)

        f.write("1 Essa imagem tem suberexposicao")
        f.close()
        #print("1 Essa imagem tem suberexposicao")

        return (suber*100)/total

    elif( super > dffSuper ):

        verificarPorcetagem(listaImagensEntrada, (super * 100)/total, 2)
        f.write("2 Essa imagem tem superexposicao")
        f.close()
        #print("2 Essa imagem tem superexposicao")

        return (super * 100) / total

    elif( super > meio and suber > meio ):
        f.write("3 E uma com dois picos")
        f.close()
        #print("3 E uma com dois picos")

        return -1

    else:
        f.write("4 E uma imagem normal")
        f.close()
        #print("4 E uma imagem normal")
        return -1

def classificarImage(listaImagensEntrada, histosEntrada, listaTotalHistoEntrada, dirClassificacaoEntrada):
    lista = []
    for i in range(1, len(histosEntrada)+1):
        lista.append(identificarPicos(listaImagensEntrada[i-1], dividirHistograma(histosEntrada[i-1]), listaTotalHistoEntrada[i-1], dirClassificacaoEntrada, i))
    return lista

def functionEqualization(imagem):
    #aplicando a equalização pelo histograma
    img_yuv = cv2.cvtColor(imagem, cv2.COLOR_BGR2YUV)

    # equalize the histogram of the Y channel
    img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

    # convert the YUV image back to RGB format
    equ = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

    return equ      #cv2_imshow(res)

def funcionSquare (imagem, A):
    img = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
    height, width = img.shape  # dimensões da imagem

    if (A == 0 ):
        A = 0.005

    # transformação Quadratica
    for i in range(0, height):
        for j in range(0, width):
            pixel = imagem[i, j].astype(int)
            saida = A * np.square(pixel)

            if( saida[0] >= 255 ):
                saida[0] = 255
            if (saida[1] >= 255):
                saida[1] = 255
            if (saida[2] >= 255):
                saida[2] = 255
            imagem[i,j] = saida

    return imagem

def filtro2(img,dirImgSaida, parametro, i, dirPlotHistSaida):

    imgSquare = funcionSquare(img, parametro)
    output = functionEqualization(imgSquare)

    camSaidaHisto = dirPlotHistSaida + str(i) + "_" + str(parametro) + ".jpg"
    Histograma(imgSquare, camSaidaHisto)

    camSaida = dirImgSaida+str(i)+"_"+str(parametro)+".png"
    cv2.imwrite(camSaida, output)

def correcaoGamma(img, gamma):

  lookUpTable = np.empty((1,256), np.uint8)
  for i in range(256):
    lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)

  res = cv2.LUT(img, lookUpTable)

  return res

def filtro1(img,dirImgSaida, parametro, i, dirPlotHistSaida):

    img_gamma_corrected = correcaoGamma(img, 1.2)

    if ( i == 1 ):
        texto = dirImgSaida+"teste.png"
        print(texto)
        cv2.imwrite(texto, img_gamma_corrected)

    imgSquare = funcionSquare(img_gamma_corrected, parametro)

    camSaidaHisto = dirPlotHistSaida + str(i) + "_" + str(parametro) + ".jpg"
    Histograma(imgSquare, camSaidaHisto)

    camSaida = dirImgSaida + str(i) + "_" + str(parametro) + ".png"
    cv2.imwrite(camSaida, imgSquare)

def aplicarFiltro(listaImagensEntrada, dirClassificacaoEntrada, dirImgSaida, listaPorcetagemImgEntrada, dirPlotHistSaida):
    listaClassificacaoImg = lerDiretorio(dirClassificacaoEntrada)

    for i in range(0, len(listaClassificacaoImg)):
        CamProblema = listaClassificacaoImg[i]
        linha = open(CamProblema, "r")
        problema = linha.read()
        problema =problema.split()
        problema = problema[0]

        img = cv2.imread(listaImagensEntrada[i])
        #print(problema, " - ", listaClassificacaoImg[i], " - ", listaImagensEntrada[i])

        if (problema == "1"):  # aplicar filtro de suberexposição
            a=1
        elif (problema == "2"):  # aplicar filtro de superexposição
            print("peguei: ", listaImagensEntrada[i])

            if (listaPorcetagemImgEntrada[i] >= 87):
                parametro = 0.004
                filtro1(img, dirImgSaida, parametro, i + 1, dirPlotHistSaida)
            else:
                parametro = 0.004
                filtro2(img, dirImgSaida, parametro, i + 1, dirPlotHistSaida)
        elif (problema == "3"):  # aplicar filtro de dois pico
            a=1
        elif (problema == "4"):  # aplicar filtro de realce, pq é uma imagem normal
            a=1
        else:
            a=1

dirImgEntrada, dirPlotHistEntrada, dirClassificacaoEntrada, dirImgSaida, dirPlotHistSaida = mudarDiretorios()

listaImagensEntrada = lerDiretorio(dirImgEntrada)

histosEntrada, listaTotalHistoEntrada = criarHisto(listaImagensEntrada, dirPlotHistEntrada)

listaPorcetagemImgEntrada =  classificarImage(listaImagensEntrada, histosEntrada, listaTotalHistoEntrada, dirClassificacaoEntrada)

aplicarFiltro(listaImagensEntrada, dirClassificacaoEntrada, dirImgSaida, listaPorcetagemImgEntrada, dirPlotHistSaida)

