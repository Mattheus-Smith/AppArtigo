import numpy as np
import tensorflow as tf
from tensorflow import keras
from absl import app, flags, logging
from absl.flags import FLAGS
import cv2
import os

# Criação do modelo
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(16, input_shape=(3,), activation='relu'),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(4, activation='softmax')
])

# Compilação do modelo
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Treinamento do modelo
x_train = np.array([[2, 1.2, 0.0045],
                    [2, 1.2, 0.0045],
                    [2, 4, 0.004, 0],
                    [2, 0.004, 0.8, 0],
                    [1, 0.8, 2, 10],
                    [1, 0.8, 2, 12],
                    [1, 0.8, 3, 8],
                    [2, 1.75, 0.0045, 0],
                    [2, 2.2, 0.004, 0],
                    [1, 0.85, 2, 8]])

# Saída esperada para o exemplo de entrada
y_train = np.array([[8, 1.2, 0.0045, 0],
                    [8, 1.2, 0.0045, 0],
                    [8, 4, 0.004, 0],
                    [9, 0.004, 0.8, 0],
                    [10, 0.8, 2, 10],
                    [10, 0.8, 2, 12],
                    [10, 0.8, 3, 8],
                    [8, 1.75, 0.0045, 0],
                    [8, 2.2, 0.004, 0],
                    [10, 0.85, 2, 8]])

model.fit(x_train, y_train, epochs=10)