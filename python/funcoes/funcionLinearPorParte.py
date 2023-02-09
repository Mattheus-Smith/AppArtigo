import cv2
import numpy as np
from matplotlib import pyplot as plt
from pylab import *

def funcitonPiecewiseLinear(imagen, out, Ainicio, Amedio, Afim, grauInicio, grauMedio, grauFim, saturacao):
  imgI = imagen.copy()  # leitura da imagem em escala de cinza

  img = cv2.cvtColor(imgI, cv2.COLOR_RGB2GRAY)
  height, width = img.shape  # dimensões da imagem

  hist = cv2.calcHist([img], [0], None, [256], [0, 256]).astype(int)
  plt.plot(hist, color = 'blue')
  #plt.show()

  Gmax = 255;Gmin = 0

  if( Ainicio == 0 ):
    Ainicio=1.05
  if( Ainicio == 0 ):
    Amedio=1.10
  if( Ainicio == 0 ):
    Afim=1.15

  if( grauInicio == 0 ):
    grauInicio=50
  if( grauMedio == 0 ):
    grauMedio=90
  if( grauFim == 0 ):
    grauFim=255

  if( saturacao == 0 ):
    saturacao = 255

  # transformação linear
  for i in range(0, height):
      for j in range(0, width):
          pixel = img[i, j]             #imagem que vai ser alterada em escala de cinza

          if( pixel <= grauInicio ):
            A = Ainicio
          elif(pixel <= grauMedio ):
            A = Amedio
          elif(pixel <= grauFim ):
            A = Afim

          pixel = imgI[i, j]            #imagem que vai ser alterada em escala RGB

          saida = []
          saida.append( np.clip(A * pixel[0] + Gmin, 0, saturacao) )
          saida.append( np.clip(A * pixel[1] + Gmin, 0, saturacao) )
          saida.append( np.clip(A * pixel[2] + Gmin, 0, saturacao) )
          imgI[i, j] = saida


  img = cv2.cvtColor(imgI, cv2.COLOR_RGB2GRAY)
  hist = cv2.calcHist([img], [0], None, [256], [0, 256]).astype(int)
  plt.plot(hist, color = 'red')
  plt.legend(['Histo Imagem Original', 'Histo Imagem Editada'])
  plt.show()

  if( out == 1 ):
    #cv2_imshow(imgI)
    return imgI
  elif( out == 0 ):
    res = np.hstack((imagen, imgI))
    #cv2.imshow(res)