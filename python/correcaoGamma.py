import cv2
import numpy as np
from matplotlib import pyplot as plt
from pylab import *

def correcaoGamma(img, gamma):

  lookUpTable = np.empty((1,256), np.uint8)
  for i in range(256):
    lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)

  res = cv2.LUT(img, lookUpTable)

  return res

img = cv2.imread("./1imagensEntrada/04.jpg")

parametro = 1.7
out = correcaoGamma(img, parametro)

texto = "output_gamma_"+str(parametro)+".png"
cv2.imwrite(texto, out)
