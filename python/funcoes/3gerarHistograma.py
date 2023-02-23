import cv2
from pylab import *

def Histograma(imagem, dirPlot):
    img = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
    hist = cv2.calcHist([img], [0], None, [256], [0, 256]).astype(int)

    #plt.plot(hist)
    #plt.savefig(fname=dirPlot)  # Projeto
    #plt.show()
    #plt.close()

    total = 0
    for i in range(len(hist)):
        total += hist[i]

    return hist, total

#img = cv2.imread("./../7imagensEntradaTeste/15.jpg")
img = cv2.imread("./../1imagensEntrada/28.jpg")
#img = cv2.imread("./../6casoSuuuper/result_foreground.png")
#img = cv2.imread("./../teste.png")

histo, total = Histograma(img, "./../histograma_output_foreground.jpg")

print(total)

# Convertendo para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
mean_val = np.mean(gray)
std_val = np.std(gray)

# Calculando o brilho e o contraste
brightness = mean_val
contrast = std_val / mean_val

print("Brilho: ", brightness)
print("Contraste: ", contrast)
print(np.std(histo))




