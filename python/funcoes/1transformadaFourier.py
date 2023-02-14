# teoria: https://www.lume.ufrgs.br/bitstream/handle/10183/6748/000446124.pdf?sequence=1
# teoria: https://www.cin.ufpe.br/~ags/Sinais/Aplica%C3%A7%C3%A3o%20da%20Transformada%20de%20Fourier%20no%20processamento%20digital%20de%20imagens.pdf
# teoria: https://valci.com.br/download/Transformada-de-Fourier-e-Aplicacoes.pdf

import cv2
import numpy as np
from matplotlib import pyplot as plt
from pylab import *

img = cv2.imread("./../1imagensEntrada/10.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)    # Converte para escala de cinza

# https://medium.com/turing-talks/transformada-de-fourier-b1775e891cc5
# Computando a fft2 do gatinho
D = np.fft.fft2(img_gray)
result = np.fft.fftshift(np.log(np.abs(D)))
img_inversa = np.fft.ifftshift(result)

figura = plt.figure(figsize=(10,5))
plt.subplot(131), plt.title(" entrada"), plt.axis('off'), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(132), plt.title("img transformada"), plt.axis('off'), plt.imshow(result, cmap = 'gray')
plt.subplot(133), plt.title("transformada inversa"), plt.axis('off'), plt.imshow(img_inversa, cmap = 'gray')
plt.show()
