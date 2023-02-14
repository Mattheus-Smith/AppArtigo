import cv2
import numpy as np
from matplotlib import pyplot as plt
from pylab import *

img = cv2.imread("./../1imagensEntrada/10.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)    # Converte para escala de cinza

# Computando a fft2 do gatinho
D = np.fft.fft2(img_gray)

figura = plt.figure(figsize=(10,5))
plt.subplot(121), plt.title(" entrada"), plt.axis('off'), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(122), plt.title("img transformada"), plt.axis('off'), plt.imshow(np.fft.fftshift(np.log(np.abs(D))))
plt.show()
# cv2.imwrite("saida.png", np.fft.fftshift(np.log(np.abs(D))))

