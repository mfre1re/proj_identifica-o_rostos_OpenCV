import cv2

import_algoritmo = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

imagem = cv2.imread('_img/img 02.jpg')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
rostos = import_algoritmo.detectMultiScale(imagemCinza, scaleFactor=1.11, minNeighbors=4, minSize=(50, 50))

print(rostos)

for (x, y, l, a) in rostos:
    cv2.rectangle(imagem, (x, y), (x + l, y + a), (255, 0, 255), 2)

cv2.imshow('Faces', imagem)
cv2.waitKey()
