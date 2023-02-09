import cv2
import numpy as np
from matplotlib import pyplot as plt
from pylab import *

def equalizeCLAHE(img, parametroCLAHE, CLAHE_matriz):
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = hsv_img[:, :, 0], hsv_img[:, :, 1], hsv_img[:, :, 2]

    clahe = cv2.createCLAHE(clipLimit=parametroCLAHE, tileGridSize=(CLAHE_matriz, CLAHE_matriz))
    v = clahe.apply(v)
    result = np.dstack((h, s, v))

    bgr = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)
    return  bgr


img = cv2.imread("./../1imagensEntrada/01.jpg")

parametroCLAHE = 2
CLAHE_matriz = 18
output_CLAHE = equalizeCLAHE(img, parametroCLAHE, CLAHE_matriz)

texto = "./../output_CLAHE_"+str(parametroCLAHE)+"_("+str(CLAHE_matriz)+").png"
cv2.imwrite(texto, output_CLAHE)
