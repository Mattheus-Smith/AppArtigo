import cv2
import numpy as np
from matplotlib import pyplot as plt
from pylab import *

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

img = cv2.imread("./../1imagensEntrada/27.jpg")

parametroSquare = 0.004
out = funcionSquare(img, parametroSquare)

texto = "./../output_Square_"+str(parametroSquare)+".png"
cv2.imwrite(texto, out)




