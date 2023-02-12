import cv2
import numpy as np
import os
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
from absl import app, flags, logging
from absl.flags import FLAGS
from keras.utils import to_categorical

flags.DEFINE_string('pc', "1", 'identifiy wich pc')

def lerDiretorio(pasta):
    listaImagensEntrada = []
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            listaImagensEntrada.append(os.path.join(diretorio, arquivo))
            #print(os.path.join(diretorio, arquivo))
    return listaImagensEntrada

def Histograma(imagem):
    img = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
    hist = cv2.calcHist([img], [0], None, [256], [0, 256]).astype(int)

    total = 0
    for i in range(len(hist)):
        total += hist[i]

    return hist, total

def criarHisto(listaImg):
    histosEntrada = []
    listaTotalHistoEntrada = []
    for i in range (1, len(listaImg)+1):
        histo, total = Histograma(cv2.imread(listaImg[i-1]))
        histosEntrada.append(histo)
        listaTotalHistoEntrada.append(total)
    return histosEntrada, listaTotalHistoEntrada

def getClassificacao(CamProblema):
    linha = open(CamProblema, "r")
    problema = linha.read()
    problema = problema.split()
    problema = problema[0]
    linha.close()

    return problema

inputs=[]

dirImgEntrada = "C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\1imagensEntradaTeste"
dirClassificacaoEntrada = "C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\7ClassificacaoImagem\\"

listaImagensEntrada = lerDiretorio(dirImgEntrada)
listaClassificacaoEntrada = lerDiretorio(dirClassificacaoEntrada)

histosEntrada, listaTotalHistoEntrada = criarHisto(listaImagensEntrada)

# print(listaImagensEntrada[0])
# print(listaClassificacaoEntrada[0])

for i in range(0, len(listaClassificacaoEntrada)):
    classificacao = getClassificacao(listaClassificacaoEntrada[i])
    desvioPadrao = np.std(histosEntrada[i])

    inputs.append([histosEntrada[i], listaTotalHistoEntrada[i] ,classificacao, desvioPadrao])

# print(inputs[0])

#inputs = np.array([inputs])

# Dados de treinamento
outputs = np.array([[8, 1.2, 0.0045, 0],
                    [8, 1.2, 0.0045, 0],
                    [8, 4, 0.004, 0],
                    [9, 0.004, 0.8, 0],
                    [10, 0.8, 2, 10],
                    [10, 0.8, 2, 12],
                    [10, 0.8, 2, 8],
                    [8, 1.75, 0.0045, 0],
                    [8, 2.2, 0.004, 0],
                    [10, 0.85, 2, 8]])

# Transformação dos dados de saída para categóricos
outputs_categorical = to_categorical(outputs)

# Criação da rede neural
model = Sequential()
model.add(Dense(128, input_dim=4, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(6, activation='softmax'))

# Compilação do modelo
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Treinamento da rede
model.fit(inputs, outputs_categorical, epochs=100, batch_size=32)