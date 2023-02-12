import numpy as np
import cv2

roi = cv2.imread("./../1imagensEntrada/10.jpg")

# Convert Image to Image HSV
hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

texto = "./../output_HSV.png"
cv2.imwrite(texto, hsv)
