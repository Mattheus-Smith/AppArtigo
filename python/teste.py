import copy
import cv2
import numpy as np
from matplotlib import pyplot as plt

def histo(imagem, out):
    img = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
    hist = cv2.calcHist([img], [0], None, [256], [0, 256]).astype(int)

    total = 0
    for i in range(len(hist)):
        total += hist[i]

    if (out == 1):
        return hist, total
    elif (out == 0):
        plt.plot(hist)
        plt.show()

def functionSuperExposicao(hist):
    porcetagem = 0.75
    parteE = 0;
    parteD = 0

    for i in range(len(hist)):
        if (i < int(len(hist) * porcetagem)):
            parteE += hist[i]
        else:
            parteD += hist[i]

    if (parteD > parteE):
        return 1
    else:
        return 0

def functionSuberExposicao(hist):
    porcetagem = 0.25
    parteE = 0;
    parteD = 0

    for i in range(len(hist)):
        if (i < int(len(hist) * porcetagem)):
            parteE += hist[i]
        else:
            parteD += hist[i]

    if (parteE > parteD):
        return 1
    else:
        return 0

def resultado(hist):
    suber, super = (functionSuberExposicao(hist), functionSuperExposicao(hist))

    if( suber == 1 ):
        print("Essa imagem tem suberexposição")
    elif( super == 1 ):
        print("Essa imagem tem superexposição")
    else:
        print("É uma imagem normal")

sol = cv2.imread("caraSol.jpg")
hist, total = histo(sol, 1)
resultado(hist)

#cv2.imshow("image",sol)
cv2.waitKey(0)
cv2.destroyAllWindows()