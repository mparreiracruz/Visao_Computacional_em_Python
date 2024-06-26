import cv2
import numpy as np
import matplotlib.pyplot as plt

face_cascade_barcelona = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_default.xml')

def face_detector(imagem):
    cont = 0
    face_imagem = imagem.copy()
    face_retangulo = face_cascade_barcelona.detectMultiScale(face_imagem, scaleFactor=1.2, minNeighbors=1)

    for(x, y, w, h)in face_retangulo:
        cv2.rectangle(face_imagem, (x, y), (x + w, y + h), (255, 0, 0), 10)
        cont = cont + 1
    print(cont)
    return face_imagem


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read(0)
    frame = face_detector(frame)
    cv2.imshow('Detecçâo Facial', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


