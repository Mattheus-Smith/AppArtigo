# https://code.adonline.id.au/structural-similarity-index-ssim-in-python/

import cv2
import imquality.brisque as brisque #pip install --upgrade --force-reinstall -U git+https://github.com/ocampor/image-quality@master
import time
from datetime import datetime

def caso01():
    img = cv2.imread("./../caso01/01.jpg")                                      #18.76060435910503
    img_output1 = cv2.imread("./../caso01/output_CLAHE_2_(8).png")              #21.88010299698587
    img_output2 = cv2.imread("./../caso01/output_CLAHE_2_(18).png")             #21.37757667515413
    img_output3 = cv2.imread("./../caso01/output_CLAHE_4_(12).png")             #21.987277284586384
    img_output4 = cv2.imread("./../caso01/output_gamma_2.png")                  #10.728166833182144
    img_output5 = cv2.imread("./../caso01/fusion_mertens.jpg")                  #22.1278494343712
    img_output6 = cv2.imread("./../caso01/fusion_mertens_sem_4_12.jpg")         #22.438555780820906

    # # Convert the images to grayscale
    # gray0 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # gray1 = cv2.cvtColor(img_output1, cv2.COLOR_BGR2GRAY)
    # gray2 = cv2.cvtColor(img_output2, cv2.COLOR_BGR2GRAY)
    # gray3 = cv2.cvtColor(img_output3, cv2.COLOR_BGR2GRAY)
    # gray4 = cv2.cvtColor(img_output4, cv2.COLOR_BGR2GRAY)
    # gray5 = cv2.cvtColor(img_output5, cv2.COLOR_BGR2GRAY)
    # gray6 = cv2.cvtColor(img_output6, cv2.COLOR_BGR2GRAY)

    score0 = brisque.score(img)
    score1 = brisque.score(img_output1)
    score2 = brisque.score(img_output2)
    score3 = brisque.score(img_output3)
    score4 = brisque.score(img_output4)
    score5 = brisque.score(img_output5)
    score6 = brisque.score(img_output6)


    print("score0: ", score0)
    print("score1: ", score1)
    print("score2: ", score2)
    print("score3: ", score3)
    print("score4: ", score4)
    print("score5: ", score5)
    print("score6: ", score6)

def caso05():
    img = cv2.imread("./../caso05/05.jpg")  # 42.51341862117849

    img_output1 = cv2.imread("./../caso05/output_gamma(2.2)_Square(0.004).png")     # 32.15675428797053
    img_output2 = cv2.imread("./../caso05/output_gamma(3)_Square(0.004).png")       # 32.23468855145492
    img_output3 = cv2.imread("./../caso05/output_gamma(4)_Square(0.004).png")       # 32.116345290305134
    img_output4 = cv2.imread("./../caso05/output_gamma_9.png")                      # 37.7850239257219

    score0 = brisque.score(img)
    score1 = brisque.score(img_output1)
    score2 = brisque.score(img_output2)
    score3 = brisque.score(img_output3)
    score4 = brisque.score(img_output4)

    print("score0: ", score0)
    print("score1: ", score1)
    print("score2: ", score2)
    print("score3: ", score3)
    print("score4: ", score4)

def caso15():                                                                               #não concordo - 33 min
    img = cv2.imread("./../caso15/15.jpg")                                                  #69.17714425031235

    img_output1 = cv2.imread("./../caso15/fusion_mertens_todos_gammas.jpg")                 # 62.59597911294108
    img_output2 = cv2.imread("./../caso15/fusion_mertens_todos_os_claros_1.8.jpg")          # 63.94684170737227
    img_output3 = cv2.imread("./../caso15/fusion_mertens_todos_os_claros_1.88_4.jpg")       # 63.03895502870907
    img_output4 = cv2.imread("./../caso15/output_gamma(0.6)_output_CLAHE_2_(12).png")       # 54.20248452882683
    img_output5 = cv2.imread("./../caso15/output_gamma(0.7)_output_CLAHE_2_(12).png")       # 54.62975169869114
    img_output6 = cv2.imread("./../caso15/output_gamma(0.7)_output_CLAHE_3_(6).png")        # 56.384319721349215
    img_output7 = cv2.imread("./../caso15/output_gamma(0.7)_output_CLAHE_3_(8).png")        # 54.69756077515464
    img_output8 = cv2.imread("./../caso15/output_gamma(0.7)_output_CLAHE_3_(12).png")       # 52.31263163939204
    img_output9 = cv2.imread("./../caso15/output_gamma(0.7)_output_CLAHE_4_(12).png")       # 50.72097487422636
    img_output10 = cv2.imread("./../caso15/output_gamma_0.6.png")                           # 67.03130664785064
    img_output11 = cv2.imread("./../caso15/output_gamma_0.7.png")                           # 67.03130664785064
    img_output12 = cv2.imread("./../caso15/output_gamma_0.8.png")                           # 67.43493331383738
    img_output13 = cv2.imread("./../caso15/output_gamma_0.45.png")                          # 67.49391514176281
    img_output14 = cv2.imread("./../caso15/output_gamma_1.8.png")                           # 82.22495626350812
    img_output15 = cv2.imread("./../caso15/output_gamma_2.2.png")                           # 88.1881459141662

    score0 = brisque.score(img)
    score1 = brisque.score(img_output1)
    score2 = brisque.score(img_output2)
    score3 = brisque.score(img_output3)
    score4 = brisque.score(img_output4)
    score5 = brisque.score(img_output5)
    score6 = brisque.score(img_output6)
    score7 = brisque.score(img_output7)
    score8 = brisque.score(img_output8)
    score9 = brisque.score(img_output9)
    score10 = brisque.score(img_output10)
    score11 = brisque.score(img_output11)
    score12 = brisque.score(img_output12)
    score13 = brisque.score(img_output13)
    score14 = brisque.score(img_output14)
    score15 = brisque.score(img_output15)

    print("score0: ", score0)
    print("score1: ", score1)
    print("score2: ", score2)
    print("score3: ", score3)
    print("score4: ", score4)
    print("score5: ", score5)
    print("score6: ", score6)
    print("score7: ", score7)
    print("score8: ", score8)
    print("score9: ", score9)
    print("score10: ", score10)
    print("score11: ", score11)
    print("score12: ", score12)
    print("score13: ", score13)
    print("score14: ", score14)
    print("score15: ", score15)

def caso18():                                                                               #não concordo
    img = cv2.imread("./../caso18/18.jpg")                                                  #42.51341862117849

    img_output1 = cv2.imread("./../caso18/18_output_gamma(0.8)_output_CLAHE_2_(10).png")    #32.15675428797053
    img_output2 = cv2.imread("./../caso18/output_gamma(0.8)_output_CLAHE_2_(8).png")        #32.23468855145492
    img_output3 = cv2.imread("./../caso18/output_gamma(0.8)_output_CLAHE_2_(12).png")       #32.116345290305134
    img_output4 = cv2.imread("./../caso18/output_gamma_0.6.png")                            #37.7850239257219

    score0 = brisque.score(img)
    score1 = brisque.score(img_output1)
    score2 = brisque.score(img_output2)
    score3 = brisque.score(img_output3)
    score4 = brisque.score(img_output4)

    print("score0: ", score0)
    print("score1: ", score1)
    print("score2: ", score2)
    print("score3: ", score3)
    print("score4: ", score4)

def caso28():
    img = cv2.imread("./../caso28/28.jpg")                                              #17.371306144740828

    img_output1 = cv2.imread("./../caso28/output_CLAHE_2_(8).png")                      #22.340179947405517
    img_output2 = cv2.imread("./../caso28/output_CLAHE_2_(12).png")                     #22.021109467910122
    img_output3 = cv2.imread("./../caso28/output_gamma(0.7)_output_CLAHE_2_(8).png")    #24.079551408088804
    img_output4 = cv2.imread("./../caso28/output_gamma(0.85)_output_CLAHE_2_(8).png")   #23.339426593858065

    score0 = brisque.score(img)
    score1 = brisque.score(img_output1)
    score2 = brisque.score(img_output2)
    score3 = brisque.score(img_output3)
    score4 = brisque.score(img_output4)

    print("score0: ", score0)
    print("score1: ", score1)
    print("score2: ", score2)
    print("score3: ", score3)
    print("score4: ", score4)

#==================================================================

named_tuplei = time.localtime() # get struct_time
time_stringi = time.strftime("%H:%M:%S", named_tuplei)
ti = datetime.strptime(time_stringi, "%H:%M:%S")
print(time_stringi)

caso15()

named_tuplef = time.localtime() # get struct_time
time_stringf = time.strftime("%H:%M:%S", named_tuplef)
tf = datetime.strptime(time_stringf, "%H:%M:%S")
print(time_stringf)

# get difference
delta = tf - ti
sec = delta.total_seconds()
min = sec / 60
hours = sec / (60 * 60)
print(int(hours),":",int(min),":", int(sec))


