from absl import app, flags, logging
import cv2
import numpy as np
from matplotlib import pyplot as plt
from pylab import *


def histo(imagem, out):
    img = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
    hist = cv2.calcHist([img], [0], None, [256], [0, 256]).astype(int)
    # plt.plot(hist)
    # plt.savefig(r"./saidas/hist.png")
    # plt.show()

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

    if (parteD > parteE + meio):
        f = open("./saidas/saida.txt", "w")
        f.write("Essa imagem tem superexposição")
        f.close()
    elif (parteE > parteD + meio):
        f = open("./saidas/saida.txt", "w")
        f.write("Essa imagem tem suberexposição")
        f.close()
    else:
        f = open("./saidas/saida.txt", "w")
        f.write("É uma imagem normal")
        f.close()

sol = cv2.imread("cidadeEscura.jpg")
hist, total = histo(sol, 1)
resultado(hist)

# cv2.imshow("image",sol)
cv2.waitKey(0)
cv2.destroyAllWindows()