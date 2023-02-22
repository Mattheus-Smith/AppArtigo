import cv2
import numpy as np
from pylab import *

def functionEqualization(imagem):
    #aplicando a equalização pelo histograma
    img_yuv = cv2.cvtColor(imagem, cv2.COLOR_BGR2YUV)

    # equalize the histogram of the Y channel
    img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

    # convert the YUV image back to RGB format
    equ = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

    return equ

# img = cv2.imread("./../1imagensEntrada/01.jpg")
#
# out_equalize = functionEqualization(img)
#
# texto = "./../output_equalize.png"
# cv2.imwrite(texto, out_equalize)
