import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
from pylab import *
import sys
from absl import app, flags, logging
from absl.flags import FLAGS

def Histograma(imagem, dirPlot):
    img = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
    hist = cv2.calcHist([img], [0], None, [256], [0, 256]).astype(int)

    plt.plot(hist)
    plt.savefig(fname=dirPlot)  # Projeto
    plt.close()

    total = 0
    for i in range(len(hist)):
        total += hist[i]

    return hist, total

img = cv2.imread("./output_CLAHE_2_(8).png")

histo, total = Histograma(img, "./histograma_output_CLAHE_2_(8).jpg")



