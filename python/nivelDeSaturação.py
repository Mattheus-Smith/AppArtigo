import numpy as np
import cv2

img = cv2.imread("./cidadeClara/cidadeClara.jpg")
img2 = cv2.imread("./cidadeClara/imgFiltrada-0.003.png")
img3 = cv2.imread("./cidadeClara/imgFiltrada-0.004.png")

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
saturation1 = img_hsv[:, :, 1].mean()

img_hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
saturation2 = img_hsv[:, :, 1].mean()

img_hsv = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)
saturation3 = img_hsv[:, :, 1].mean()

print(saturation1)
print(saturation2)
print(saturation3)