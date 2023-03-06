import cv2
import numpy as np
from matplotlib import pyplot as plt
from pylab import *
import sys
from absl import app, flags, logging
from absl.flags import FLAGS

flags.DEFINE_string('img', None, 'path to image file')
flags.DEFINE_string('pc', None, 'identifiy wich pc')
flags.DEFINE_string('problema', None, 'identify which filter we are going to use')

def mudarDiretorios():
    if (FLAGS.pc == "0"):#pessoa
        dirTxt = "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\saidas\\imgFiltrada.png"
        #dirTxtOutput= "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\saidas\\flagOutput.txt"
    elif (FLAGS.pc == "1"):#projeto
        dirTxt = "C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\saidas\\imgFiltrada.png"
        #dirTxtOutput="a"

    return dirTxt

def functionEqualization(imagem):
    #aplicando a equalização pelo histograma
    img_yuv = cv2.cvtColor(imagem, cv2.COLOR_BGR2YUV)

    # equalize the histogram of the Y channel
    img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

    # convert the YUV image back to RGB format
    equ = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

    return equ      #cv2_imshow(res)

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

def correcaoGamma(img, gamma):

  lookUpTable = np.empty((1,256), np.uint8)
  for i in range(256):
    lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)

  res = cv2.LUT(img, lookUpTable)

  return res

def filtro1(img,dirTxt):
    imgSquare = funcionSquare(img, 0.004)
    output = functionEqualization(imgSquare)
    cv2.imwrite(dirTxt, output)

    # f = open(dirTxtOutput, "w")  # Pessoal
    # f.write("1")
    # f.close()

def filtro2(img,dirTxt):
    output_gamma = correcaoGamma(img, 2.2)
    output = funcionSquare(output_gamma, 0.004)
    cv2.imwrite(dirTxt, output)

    # f = open(dirTxtOutput, "w")  # Pessoal
    # f.write("1")
    # f.close()

def aplicarFiltro(img, dirTxt):
    if(FLAGS.problema == "1"): #aplicar filtro de superexposição
        print("problema 1")
        #filtro1(img,dirTxt)
        filtro2(img, dirTxt)
    elif (FLAGS.problema == "2"):  # aplicar filtro de suberexposição
        a = 1
    elif (FLAGS.problema == "3"):  # aplicar filtro de dois pico
        a = 1
    elif (FLAGS.problema == "4"):  # aplicar filtro de realce, pq é uma imagem normal
        a = 1

def main(_args):

    dirTxt= mudarDiretorios()
    imgEntrada = cv2.imread(FLAGS.img)  # projeto

    aplicarFiltro(imgEntrada, dirTxt)

if __name__ == '__main__':
    try:
        app.run(main)
    except SystemExit:
        pass