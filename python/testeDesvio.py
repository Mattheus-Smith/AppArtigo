import numpy as np
import cv2

def histo(imagem):
    img = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
    hist = cv2.calcHist([img], [0], None, [256], [0, 256]).astype(int)

    return hist

imgEntrada = cv2.imread("./cidadeClara/cidadeClara.jpg")
histoEntrada = histo(imgEntrada)

imgFiltrada = cv2.imread("./cidadeClara/imgFiltrada.png")
histoFiltrada = histo(imgFiltrada)

print("desvio imgEntrada: ", np.std(histoEntrada))
print("desvio imgFiltrada: ", np.std(histoFiltrada))

cv2.waitKey(0)
cv2.destroyAllWindows()

array = [1.55, 1.70, 1.80]

print(np.std(array))