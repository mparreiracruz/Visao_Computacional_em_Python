import cv2
import numpy as np
import matplotlib.pyplot as plt

barcelona = cv2.imread('torcedor_sozinho.jpg')
barcelona = cv2.cvtColor(barcelona, cv2.COLOR_BGR2GRAY)

# plt.imshow(barcelona, cmap='gray')
# plt.show()

turma = cv2.imread('torcedores_barcelona_grupo.jpg')
turma = cv2.cvtColor(turma, cv2.COLOR_BGR2GRAY)

# plt.imshow(turma, cmap='gray')
# plt.show()

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


resultado = face_detector(turma)
plt.imshow(resultado, cmap='gray')
plt.show()
