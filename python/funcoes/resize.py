import cv2

# abre a imagem a ser redimensionada
img = cv2.imread('./../teste/28.jpg')

# redimensiona a imagem
img_resized = cv2.resize(img, (320, 240))

# salva a imagem redimensionada
cv2.imwrite('./../1imagensEntrada/filtro10/imagem_resized.jpg', img_resized)