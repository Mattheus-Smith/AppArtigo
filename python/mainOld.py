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
    plt.savefig(r"H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\saidas\\saida.png") #pessoal
    #plt.show()

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
        f.write("1 Essa imagem tem superexposição")
        f.close()
        print("1 Essa imagem tem superexposição")
    elif (parteE > parteD):
        f.write("2 Essa imagem tem suberexposição")
        f.close()
        print("2 Essa imagem tem suberexposição")
    else:
        f.write("3 É uma imagem normal")
        f.close()
        print("3 É uma imagem normal")

def main(_args):
    sol = cv2.imread(FLAGS.img)  # projeto
    #sol = cv2.imread("./imagens/26.jpg")  # projeto
    hist, total = histo(sol)
    resultado(hist)


if __name__ == '__main__':
    try:
        app.run(main)
    except SystemExit:
        pass