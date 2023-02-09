import cv2
import numpy as np
from matplotlib import pyplot as plt
from pylab import *

def functionEqualization(imagem):
    #aplicando a equalização pelo histograma
    img_yuv = cv2.cvtColor(imagem, cv2.COLOR_BGR2YUV)

    # equalize the histogram of the Y channel
    img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

    # convert the YUV image back to RGB format
    equ = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

    return equ      #cv2_imshow(res)

def correcaoGamma(img, gamma):

  lookUpTable = np.empty((1,256), np.uint8)
  for i in range(256):
    lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)

  res = cv2.LUT(img, lookUpTable)

  return res

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

def equalizeCLAHE(img, parametroCLAHE, CLAHE_matriz):
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = hsv_img[:, :, 0], hsv_img[:, :, 1], hsv_img[:, :, 2]

    clahe = cv2.createCLAHE(clipLimit=parametroCLAHE, tileGridSize=(CLAHE_matriz, CLAHE_matriz))
    v = clahe.apply(v)
    result = np.dstack((h, s, v))

    bgr = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)
    return  bgr
#
# img = cv2.imread("./../1imagensEntrada/18.jpg")

# ======================gamma -> square -> equaliza
# parametroGamma = 0.6
# out_gamma = correcaoGamma(img, parametroGamma)
#
# parametroSquare = 0.004
# out_square = funcionSquare(out_gamma, parametroSquare)
#
# #out_equalize = functionEqualization(out_square)
#
# texto = "./../output_gamma("+str(parametroGamma)+")_Square("+str(parametroSquare)+").png"
# cv2.imwrite(texto, out_square)


# =============== square -> gamma
# parametroSquare = 0.005
# out_square = funcionSquare(img, parametroSquare)
#
# parametroGamma = 0.4
# out_gamma = correcaoGamma(out_square, parametroGamma)
#
# texto = "./../output_Square("+str(parametroSquare)+")_gamma("+str(parametroGamma)+").png"
# cv2.imwrite(texto, out_gamma)

# =======================gamma -> equalize
# parametroGamma = 0.6
# out_gamma = correcaoGamma(img, parametroGamma)
#
# out_equalize = functionEqualization(out_gamma)
#
# texto = "./../output_gamma("+str(parametroGamma)+")_out_equalize).png"
# cv2.imwrite(texto, out_equalize)



# =======================gamma -> equalize
#
# parametroGamma = 0.8
# out_gamma = correcaoGamma(img, parametroGamma)
#
# parametroCLAHE = 2
# CLAHE_matriz = 12
# out_clahe = equalizeCLAHE(out_gamma, parametroCLAHE, CLAHE_matriz)
#
# texto = "./../output_gamma("+str(parametroGamma)+")_output_CLAHE_"+str(parametroCLAHE)+"_("+str(CLAHE_matriz)+").png"
# cv2.imwrite(texto, out_clahe)