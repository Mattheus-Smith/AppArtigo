# teoria: https://www.lume.ufrgs.br/bitstream/handle/10183/6748/000446124.pdf?sequence=1
# teoria: https://www.cin.ufpe.br/~ags/Sinais/Aplica%C3%A7%C3%A3o%20da%20Transformada%20de%20Fourier%20no%20processamento%20digital%20de%20imagens.pdf
# teoria: https://valci.com.br/download/Transformada-de-Fourier-e-Aplicacoes.pdf

import cv2
import numpy as np
from matplotlib import pyplot as plt
from pylab import *

img = cv2.imread("./../1imagensEntrada/10.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)    # Converte para escala de cinza

B, G, R = cv2.split(img)

# # https://hicraigchen.medium.com/digital-image-processing-using-fourier-transform-in-python-bcb49424fd82
plt.figure(figsize=(10,5), constrained_layout=False)
plt.subplot(321), plt.imshow(R, "gray"), plt.title("Original Image")

original = np.fft.fft2(R)
plt.subplot(322), plt.imshow(np.log(1+np.abs(original)), "gray"), plt.title("Spectrum")

center = np.fft.fftshift(original)
plt.subplot(323), plt.imshow(np.log(1+np.abs(center)), "gray"), plt.title("Centered Spectrum")

inv_center = np.fft.ifftshift(center)
plt.subplot(324), plt.imshow(np.log(1+np.abs(inv_center)), "gray"), plt.title("Decentralized")

processed_img = np.fft.ifft2(inv_center)
plt.subplot(325), plt.imshow(np.abs(processed_img), "gray"), plt.title("Processed Image")

plt.show()
