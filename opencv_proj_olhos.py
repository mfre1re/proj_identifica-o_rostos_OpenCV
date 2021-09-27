import cv2

import_face = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
import_olhos = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

imagem = cv2.imread('_img/img 07.jpg')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
rostos = import_face.detectMultiScale(imagemCinza, scaleFactor=1.07, minNeighbors=4)

print(rostos)

for (x, y, l, a) in rostos:
    imagem = cv2.rectangle(imagem, (x, y), (x + l, y + a), (255, 0, 255), 2)
    localOlho = imagem[y:y + a, x:x + l]
    localOlhoCinza = cv2.cvtColor(localOlho, cv2.COLOR_BGR2GRAY)
    detectado = import_olhos.detectMultiScale(localOlhoCinza, scaleFactor=1.18, minNeighbors=6)

    for(ox, oy, ol, oa) in detectado:
        cv2.rectangle(localOlho, (ox, oy), (ox + ol, oy + oa), (0, 0, 255), 2)

cv2.imshow('Detecta face e os olhos', imagem)
cv2.waitKey()
