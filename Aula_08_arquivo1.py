import numpy as np
import cv2

def circulo(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(imagem, (x, y), 100, (0, 255, 255), thickness=10)
        #cv2.rectangle(imagem, pt1=(x, x), pt2=(y, y), color=(255, 0, 0), thickness=10)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(imagem, (x, y), 100, (255, 255, 0), -1)


cv2.namedWindow(winname='minha_imagem')

cv2.setMouseCallback('minha_imagem', circulo)

#Apresentação da imagem com o Open cv

imagem = np.zeros((600, 600, 3), dtype=np.uint8)
while True:
    cv2.imshow('minha_imagem', imagem)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
