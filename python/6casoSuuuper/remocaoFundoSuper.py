import numpy as np
import cv2

roi = cv2.imread("10.jpg")

# Convert Image to Image HSV
img_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

#============== mascaras de cores
# lower mask (0-10)
lower_red_foreground = np.array([0,2,0])
upper_red_foreground = np.array([179,255,255])
mask_foreground = cv2.inRange(img_hsv, lower_red_foreground, upper_red_foreground)

# # upper mask (170-180)
lower_red_background = np.array([0,0,0])
upper_red_background = np.array([0,0,255])
mask_background = cv2.inRange(img_hsv, lower_red_background, upper_red_background)

result = cv2.bitwise_and(roi, roi, mask=mask_background)

cv2.imwrite("result_background.png", result)

