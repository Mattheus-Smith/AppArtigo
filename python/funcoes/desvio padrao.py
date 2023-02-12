import cv2
import numpy as np
from matplotlib import pyplot as plt

def Histograma(imagem):
    img = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
    hist = cv2.calcHist([img], [0], None, [256], [0, 256]).astype(int)

    return hist

img_output1 = cv2.imread("./../caso5/output_gamma(2.2)_Square(0.004).png")      # 298991.9880088407
img_output2 = cv2.imread("./../caso5/output_gamma(3)_Square(0.004).png")        # 298645.15028845635
img_output3 = cv2.imread("./../caso5/output_gamma(4)_Square(0.004).png")        # 298959.3957219734
img_output4 = cv2.imread("./../caso5/output_gamma_9.png")                       # 298456.9114311048

img_output1 = cv2.imread("./../caso18/18_output_gamma(0.8)_output_CLAHE_2_(10).png")    # 98856.83700894978
img_output2 = cv2.imread("./../caso18/output_gamma(0.8)_output_CLAHE_2_(8).png")        # 92428.63533331067
img_output3 = cv2.imread("./../caso18/output_gamma(0.8)_output_CLAHE_2_(12).png")       # 96359.52546660053
img_output4 = cv2.imread("./../caso18/output_gamma_0.6.png")                            # 109594.14863208083

img_output1 = cv2.imread("./../caso28/output_CLAHE_2_(8).png")                      # 5508.258327612362
img_output2 = cv2.imread("./../caso28/output_CLAHE_2_(12).png")                     # 5544.556480145498
img_output3 = cv2.imread("./../caso28/output_gamma(0.7)_output_CLAHE_2_(8).png")    # 4786.548109411514
img_output4 = cv2.imread("./../caso28/output_gamma(0.85)_output_CLAHE_2_(8).png")   # 5294.1007011010315

histo1 = Histograma(img_output1)
histo2 = Histograma(img_output2)
histo3 = Histograma(img_output3)
histo4 = Histograma(img_output4)

print(np.std(histo1))
print(np.std(histo2))
print(np.std(histo3))
print(np.std(histo4))