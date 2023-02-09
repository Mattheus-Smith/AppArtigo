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
    dirPlotHistSaida = "C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\pythonn\\5histoImagensSaida\\"

    # dirImgEntrada = "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\1imagensEntrada"
    # dirPlotHistEntrada = "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\2histoImagensEntrada\\"
    # dirClassificacaoEntrada = "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\3ClassificacaoImagem\\"
    #
    # dirImgSaida = "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\4imagensSaida\\"
    # dirPlotHistSaida = "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\5histoImagensSaida\\"

    return dirImgEntrada, dirPlotHistEntrada, dirClassificacaoEntrada, dirImgSaida, dirPlotHistSaida

def histo(imagem):
    img = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
    hist = cv2.calcHist([img], [0], None, [256], [0, 256]).astype(int)
    plt.plot(hist)
    plt.show()

    total = 0
    for i in range(len(hist)):
        total += hist[i]

    return hist, total



histo(cv2.imread("./1imagensEntrada/04.jpg"))