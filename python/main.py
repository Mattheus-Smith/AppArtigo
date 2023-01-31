from absl import app, flags, logging
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
    plt.savefig(r"C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\saidas\\saida.png")
    #plt.show()

    total = 0
    for i in range(len(hist)):
        total += hist[i]

    return hist, total

def resultado(hist):
    porcetagemMenor = 0.25
    porcetagemMaior = 0.75
    parteE = 0;
    meio = 0;
    parteD = 0

    for i in range(len(hist)):
        if (i < int(len(hist) * porcetagemMenor)):
            parteE += hist[i]
        elif (i > int(len(hist) * porcetagemMaior)):
            parteD += hist[i]
        else:
            meio += hist[i]

    # print("Esq ",parteE)
    # print("Meio ", meio)
    # print("Dir ",parteD )

    f = open("C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\saidas\\saida.txt", "w")    #projeto
    # f = open("C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\saidas\\saida.txt", "w")  #Pessoal
    if (parteD > parteE + meio):
        f.write("Essa imagem tem superexposição")
        f.close()
        print("Essa imagem tem superexposição")
    elif (parteE > parteD + meio):
        f.write("Essa imagem tem suberexposição")
        f.close()
        print("Essa imagem tem suberexposição")
    else:
        f.write("É uma imagem normal")
        f.close()
        print("É uma imagem normal")

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