import cv2
import numpy as np

#link https://stackoverflow.com/questions/58821130/how-to-calculate-the-contrast-of-an-image

# load image as YUV (or YCbCR) and select Y (intensity)
# or convert to grayscale, which should be the same.
# Alternately, use L (luminance) from LAB.
img1 = cv2.imread("./cidadeClara/cidadeClara.jpg")
img2 = cv2.imread("./cidadeClara/imgFiltrada-0.003.png")
img3 = cv2.imread("./cidadeClara/imgFiltrada-0.004.png")

Y1 = cv2.cvtColor(img1, cv2.COLOR_BGR2YUV)[:,:,0]
Y2 = cv2.cvtColor(img2, cv2.COLOR_BGR2YUV)[:,:,0]
Y3 = cv2.cvtColor(img3, cv2.COLOR_BGR2YUV)[:,:,0]

# compute min and max of Y
min = np.min(Y1)
max = np.max(Y1)

# compute contrast 1
contrast = (max-min)/(max+min)
print(min,max,contrast)

# compute min and max of Y
min = np.min(Y2)
max = np.max(Y2)

# # compute contrast 2
# contrast = (max-min)/(max+min)
# print(min,max,contrast)
#
# # compute min and max of Y
# min = np.min(Y3)
# max = np.max(Y3)
#
# # compute contrast 3
# contrast = (max-min)/(max+min)
# print(min,max,contrast)