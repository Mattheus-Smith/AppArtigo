import cv2
import numpy as np

def funcionHDR (img_list):
    # Exposure fusion using Mertens
    merge_mertens = cv2.createMergeMertens()
    res_mertens = merge_mertens.process(img_list)

    # Convert datatype to 8-bit and save
    res_mertens_8bit = np.clip(res_mertens * 255, 0, 255).astype('uint8')
    #cv2.imwrite("./../fusion_mertens.jpg", res_mertens_8bit)

    return res_mertens_8bit