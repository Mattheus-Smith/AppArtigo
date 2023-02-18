# teoria: https://www.lume.ufrgs.br/bitstream/handle/10183/6748/000446124.pdf?sequence=1
# teoria: https://www.cin.ufpe.br/~ags/Sinais/Aplica%C3%A7%C3%A3o%20da%20Transformada%20de%20Fourier%20no%20processamento%20digital%20de%20imagens.pdf
# teoria: https://valci.com.br/download/Transformada-de-Fourier-e-Aplicacoes.pdf

import cv2
import numpy as np
from matplotlib import pyplot as plt
from pylab import *

def caso1_por_canal():
    img = cv2.imread("./../1imagensEntrada/10.jpg")
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  # Converte para escala de cinza

    B, G, R = cv2.split(img)

    # # https://hicraigchen.medium.com/digital-image-processing-using-fourier-transform-in-python-bcb49424fd82
    plt.figure(figsize=(10, 5), constrained_layout=False)
    plt.subplot(321), plt.imshow(R, "gray"), plt.title("Original Image")

    img_transformed = np.fft.fft2(R)
    plt.subplot(322), plt.imshow(np.log(1 + np.abs(img_transformed)), "gray"), plt.title("Spectrum")

    img_transformed_shift = np.fft.fftshift(img_transformed)
    plt.subplot(323), plt.imshow(np.log(1 + np.abs(img_transformed_shift)), "gray"), plt.title("Centered Spectrum")

    # H
    # filter: low passa filter
    M, N = img_transformed.shape
    H = np.zeros((M, N), dtype=np.float32)
    D0 = 50
    for u in range(M):
        for v in range(N):
            D = np.sqrt((u - M / 2) ** 2 + (v - M / 2) ** 2)
            if (D <= D0):
                H[u, v] = 1
            else:
                H[u, v] = 0

    # g = img_transformed_shift * H
    Gshiht = img_transformed_shift * H

    inv_transformed = np.fft.ifftshift(Gshiht)
    # inv_transformed= np.fft.ifftshift(img_transformed_shift)
    plt.subplot(324), plt.imshow(np.log(1 + np.abs(inv_transformed)), "gray"), plt.title("Decentralized")

    processed_img = np.fft.ifft2(inv_transformed)
    plt.subplot(325), plt.imshow(np.abs(processed_img), "gray"), plt.title("Processed Image")

    plt.show()

def novo_caso():
    #https://www.youtube.com/watch?v=YVBxM64kpkU&ab_channel=MadePython
    img = cv2.imread("./../1imagensEntrada/10.jpg")
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)    # Converte para escala de cinza

    plt.figure(figsize=(10,5), constrained_layout=False)
    plt.subplot(321), plt.imshow(img_gray, "gray"), plt.title("Original Image")

    img_transformed = np.fft.fft2(img_gray)
    plt.subplot(322), plt.imshow(np.log(1+np.abs(img_transformed)), "gray"), plt.title("Spectrum")

    img_transformed_shift = np.fft.fftshift(img_transformed)
    plt.subplot(323), plt.imshow(np.log(1+np.abs(img_transformed_shift)), "gray"), plt.title("Centered Spectrum")

    #H
    # filter: low passa filter
    M, N = img_gray.shape
    H = np.zeros((M,N), dtype=np.float32)
    D0 = 50
    for u in range(M):
        for v in range(N):
            D = np.sqrt((u-M/2)**2 + (v-N/2)**2)
            if( D <= D0):
                H[u,v] = 1
            else:
                H[u, v] = 0


    # g = img_transformed_shift * H
    Gshiht = img_transformed_shift * H
    plt.subplot(324), plt.imshow(np.log(1+np.abs(Gshiht)), "gray"), plt.title("Decentralized")

    inv_transformed= np.fft.ifftshift(Gshiht)
    plt.subplot(325), plt.imshow(np.abs(inv_transformed), "gray"), plt.title("Processed Image")

    output = np.abs(np.fft.ifft(inv_transformed))
    plt.subplot(325), plt.imshow(np.abs(output), "gray"), plt.title("Processed Image")
    plt.show()

novo_caso()