# https://code.adonline.id.au/structural-similarity-index-ssim-in-python/

import cv2
import numpy as np
#from brisque import BRISQUE
from matplotlib import pyplot as plt
from skimage.metrics import mean_squared_error
from skimage.metrics import structural_similarity as ssim
from pylab import *

import imquality.brisque as brisque #pip install --upgrade --force-reinstall -U git+https://github.com/ocampor/image-quality@master
from skimage import io, img_as_float

def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the sum of the squared difference between the two images
    mse_error = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    mse_error /= float(imageA.shape[0] * imageA.shape[1])

    return mse_error

def compare(imageA, imageB):
    # Calculate the MSE and SSIM
    # m = mse(imageA, imageB)

    m = np.sqrt(mse(imageA, imageB))
    s = ssim(imageA, imageB)

    return m, s

def caso01():
    img = cv2.imread("./../caso01/01.jpg")
    img_output1 = cv2.imread("./../caso01/output_CLAHE_2_(8).png")
    img_output2 = cv2.imread("./../caso01/output_CLAHE_2_(18).png")
    img_output3 = cv2.imread("./../caso01/output_CLAHE_4_(12).png")
    img_output4 = cv2.imread("./../caso01/output_gamma_2.png")
    img_output5 = cv2.imread("./../caso01/fusion_mertens.jpg")
    img_output6 = cv2.imread("./../caso01/fusion_mertens_sem_4_12.jpg")

    # # Convert the images to grayscale
    gray0 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray1 = cv2.cvtColor(img_output1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img_output2, cv2.COLOR_BGR2GRAY)
    gray3 = cv2.cvtColor(img_output3, cv2.COLOR_BGR2GRAY)
    gray4 = cv2.cvtColor(img_output4, cv2.COLOR_BGR2GRAY)
    gray5 = cv2.cvtColor(img_output5, cv2.COLOR_BGR2GRAY)
    gray6 = cv2.cvtColor(img_output6, cv2.COLOR_BGR2GRAY)

    m1, s1 = compare(gray0, gray1)
    m2, s2 = compare(gray0, gray2)
    m3, s3 = compare(gray0, gray3)
    m4, s4 = compare(gray0, gray4)
    m5, s5 = compare(gray0, gray5)
    m6, s6 = compare(gray0, gray6)

    # m1,s1 = compare(gray1, gray0)
    # m2,s2 = compare(gray2, gray0)
    # m3,s3 = compare(gray3, gray0)
    # m4,s4 = compare(gray4, gray0)

    print("m1: ", m1, " - s1: ", s1)
    print("m2: ", m2, " - s2: ", s2)
    print("m3: ", m3, " - s3: ", s3)
    print("m4: ", m4, " - s4: ", s4)
    print("m5: ", m5, " - s5: ", s5)
    print("m6: ", m6, " - s6: ", s6)

def caso18():
    img = cv2.imread("./../caso18/18.jpg")

    img_output1 = cv2.imread("./../caso18/18_output_gamma(0.8)_output_CLAHE_2_(10).png")
    img_output2 = cv2.imread("./../caso18/output_gamma(0.8)_output_CLAHE_2_(8).png")
    img_output3 = cv2.imread("./../caso18/output_gamma(0.8)_output_CLAHE_2_(12).png")
    img_output4 = cv2.imread("./../caso18/output_gamma_0.6.png")

    # Convert the images to grayscale
    gray0 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray1 = cv2.cvtColor(img_output1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img_output2, cv2.COLOR_BGR2GRAY)
    gray3 = cv2.cvtColor(img_output3, cv2.COLOR_BGR2GRAY)
    gray4 = cv2.cvtColor(img_output4, cv2.COLOR_BGR2GRAY)

    m1, s1 = compare(gray0, gray1)
    m2, s2 = compare(gray0, gray2)
    m3, s3 = compare(gray0, gray3)
    m4, s4 = compare(gray0, gray4)

    print("m1: ", m1, " - s1: ", s1)
    print("m2: ", m2, " - s2: ", s2)
    print("m3: ", m3, " - s3: ", s3)
    print("m4: ", m4, " - s4: ", s4)

def caso28():
    img = cv2.imread("./../caso28/28.jpg")

    img_output1 = cv2.imread("./../caso28/output_CLAHE_2_(8).png")
    img_output2 = cv2.imread("./../caso28/output_CLAHE_2_(12).png")
    img_output3 = cv2.imread("./../caso28/output_gamma(0.7)_output_CLAHE_2_(8).png")
    img_output4 = cv2.imread("./../caso28/output_gamma(0.85)_output_CLAHE_2_(8).png")

    # Convert the images to grayscale
    gray0 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray1 = cv2.cvtColor(img_output1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img_output2, cv2.COLOR_BGR2GRAY)
    gray3 = cv2.cvtColor(img_output3, cv2.COLOR_BGR2GRAY)
    gray4 = cv2.cvtColor(img_output4, cv2.COLOR_BGR2GRAY)

    m1, s1 = compare(gray0, gray1)
    m2, s2 = compare(gray0, gray2)
    m3, s3 = compare(gray0, gray3)
    m4, s4 = compare(gray0, gray4)

    print("m1: ", m1, " - s1: ", s1)
    print("m2: ", m2, " - s2: ", s2)
    print("m3: ", m3, " - s3: ", s3)
    print("m4: ", m4, " - s4: ", s4)

# caso01()
# caso18()
# caso28()

#image = cv2.imread("./../caso01/01.jpg") #18.76060435910503
image = cv2.imread("./../caso01/01.tiff") #18.76060435910503 - acho q processou mais rapido q o .jpg
#grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #137.38920851487123

score1 = brisque.score(image)
#score2 = brisque.score(img2)

print(score1)
#print(score2)


# obj = BRISQUE(img, url=False)
# obj.score()

# Mean Squared Error
# MSE1 = np.square(np.subtract(img,img_output1)).mean()
# MSE2 = np.square(np.subtract(img,img_output2)).mean()
# MSE3 = np.square(np.subtract(img,img_output3)).mean()
# MSE4 = np.square(np.subtract(img,img_output4)).mean()
#
#
# print("mse1: ", MSE1)
# print("mse2: ", MSE2)
# print("mse3: ", MSE3)
# print("mse4: ", MSE4)

# ssim_output1 = ssim(img, img_output1,data_range=img_output1.max() - img_output1.min())
# ssim_output2 = ssim(img, img_output2,data_range=img_output2.max() - img_output2.min())
# ssim_output3 = ssim(img, img_output3,data_range=img_output3.max() - img_output3.min())
# ssim_output4 = ssim(img, img_output4,data_range=img_output4.max() - img_output4.min())
#
# print("ssim1: ", ssim_output1)
# print("ssim2: ", ssim_output2)
# print("ssim3: ", ssim_output3)
# print("ssim4: ", ssim_output4)

# ======================gamma -> square -> equaliza
# parametroGamma = 0.6
# out_gamma = correcaoGamma(img, parametroGamma)
#
# parametroSquare = 0.004
# out_square = funcionSquare(out_gamma, parametroSquare)
#
# #out_equalize = functionEqualization(out_square)
#
# texto = "./../output_gamma("+str(parametroGamma)+")_Square("+str(parametroSquare)+").png"
# cv2.imwrite(texto, out_square)


