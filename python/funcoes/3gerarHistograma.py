import cv2
from pylab import *

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

img = cv2.imread("./../1imagensEntrada/21.jpg")

histo, total = Histograma(img, "./../histograma_output_gamma(0.6).jpg")




