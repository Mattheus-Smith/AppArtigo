import cv2 as cv
import numpy as np

# Loading exposure images into a list
#img_fn = ["./../caso15/15.jpg" ,"./../caso15/output_gamma_0.45.png","./../caso15/output_gamma_0.6.png",
#          "./../caso15/output_gamma_0.7.png", "./../caso15/output_gamma_0.8.png", "./../caso15/output_gamma_1.8.png", "./../caso15/output_gamma_4.png"]

img_fn = ["./../caso01/01.jpg" ,"./../caso01/output_CLAHE_2_(8).png","./../caso01/output_CLAHE_2_(18).png",
          "./../caso01/output_gamma_2.png", "./../caso01/output_gamma_3.png"]

img_list = [cv.imread(fn) for fn in img_fn]

# Exposure fusion using Mertens
merge_mertens = cv.createMergeMertens()
res_mertens = merge_mertens.process(img_list)

# Convert datatype to 8-bit and save
res_mertens_8bit = np.clip(res_mertens*255, 0, 255).astype('uint8')
cv.imwrite("./../fusion_mertens.jpg", res_mertens_8bit)