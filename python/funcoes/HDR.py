import cv2 as cv
import numpy as np

# Loading exposure images into a list
img_fn = ["./../caso10/10.jpg", "./../caso10/output_gamma_3.png", "./../caso10/output_gamma_4.png",
          "./../caso10/output_Square_0.001.png" , "./../caso10/output_Square_0.004.png", "./../caso10/output_Square_0.004_0.0032_252_por_parte.png"]
img_list = [cv.imread(fn) for fn in img_fn]

# Exposure fusion using Mertens
merge_mertens = cv.createMergeMertens()
res_mertens = merge_mertens.process(img_list)

# Convert datatype to 8-bit and save
res_mertens_8bit = np.clip(res_mertens*255, 0, 255).astype('uint8')
cv.imwrite("./../fusion_mertens.jpg", res_mertens_8bit)