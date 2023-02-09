import cv2
import numpy as np
from matplotlib import pyplot as plt
from pylab import *
import sys
from absl import app, flags, logging
from absl.flags import FLAGS

from correcaoGamma import *
from funcionCLAHE import *
from funcionEqualize import *
from funcionLinear import *
from funcionLinearPorParte import *
from funcionQuadrada import *
from funcionSquare import *

flags.DEFINE_string('img', None, 'path to image file')
flags.DEFINE_string('pc', None, 'identifiy wich pc')
flags.DEFINE_string('problema', None, 'identify which filter we are going to use')

def mudarDiretorios():
    if (FLAGS.pc == "0"):#pessoa
        dirTxt = "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\saidas\\imgFiltrada.png"
        #dirTxtOutput= "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\saidas\\flagOutput.txt"
    elif (FLAGS.pc == "1"):#projeto
        dirTxt = "C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\saidas\\imgFiltrada.png"
        #dirTxtOutput="a"

    return dirTxt

def filtro1_equalize_CLAHE(img, dirTxt):
    parametroCLAHE = 2
    CLAHE_matriz = 8
    output_CLAHE = equalizeCLAHE(img, parametroCLAHE, CLAHE_matriz)
    cv2.imwrite(dirTxt, output_CLAHE)

def filtro2_equalize_normal(img, dirTxt):
    out_equalize = functionEqualization(img)
    cv2.imwrite(dirTxt, out_equalize)

def filtro3_funcion_Linear(img, dirTxt):
    a=1
    # parametroA = 0.55
    # parametroB = 25
    # out = funcitonLinear(img, parametroA, parametroB)
    #
    # texto = "./../output_linear_("+str(parametroA)+","+str(parametroB)+").png"
    # cv2.imwrite(texto, out)

def filtro4_funcion_Linear_por_Parte(img, dirTxt):
    a=1
    # parametroA = 0.55
    # parametroB = 25
    # out = funcitonLinear(img, parametroA, parametroB)
    #
    # texto = "./../output_linear_("+str(parametroA)+","+str(parametroB)+").png"
    # cv2.imwrite(texto, out)

def filtro5_funcion_Quadrado(img, dirTxt):
    parametroQuadrado = 0.075
    out = funcionQuadrada(img, parametroQuadrado, 255)
    cv2.imwrite(dirTxt, out)

def filtro6_funcion_Square(img, dirTxt):
    parametroSquare = 0.004
    out = funcionSquare(img, parametroSquare)
    cv2.imwrite(dirTxt, out)

def filtro7_correcao_de_gamma(img, dirTxt):
    parametro = 9
    out = correcaoGamma(img, parametro)
    cv2.imwrite(dirTxt, out)

def filtro8_gamma_2_square(img, dirTxt):
    parametroGamma =4
    out_gamma = correcaoGamma(img, parametroGamma)

    parametroSquare = 0.004
    out_square = funcionSquare(out_gamma, parametroSquare)

    cv2.imwrite(dirTxt, out_square)

def filtro9_square_2_gamma(img, dirTxt):
    parametroSquare = 0.0045
    out_square = funcionSquare(img, parametroSquare)

    parametroGamma = 0.9
    out_gamma = correcaoGamma(out_square, parametroGamma)

    cv2.imwrite(dirTxt, out_gamma)

def filtro10_gamma_2_equalize_CLAHE(img, dirTxt):
    parametroGamma = 0.8
    out_gamma = correcaoGamma(img, parametroGamma)

    parametroCLAHE = 2
    CLAHE_matriz = 10
    out_clahe = equalizeCLAHE(out_gamma, parametroCLAHE, CLAHE_matriz)

    cv2.imwrite(dirTxt, out_clahe)

def main(_args):

    dirTxt= mudarDiretorios()
    imgEntrada = cv2.imread(FLAGS.img)  # projeto

    if( FLAGS.problema == "1" ):
        filtro1_equalize_CLAHE(imgEntrada, dirTxt)

if __name__ == '__main__':
    try:
        app.run(main)
    except SystemExit:
        pass