import cv2
import numpy as np
import matplotlib.pyplot as plt

def apresentaImg(imagem):
    img = plt.figure(figsize=(30, 20))
    ax = img.add_subplot(111)
    ax.imshow(imagem, cmap='gray')
    plt.show()

leite_condensado = cv2.imread('leite_condensado.jpeg')
leite_condensado = cv2.cvtColor(leite_condensado, cv2.COLOR_BGR2GRAY)

apresentaImg(leite_condensado)

pratileira_leite = cv2.imread('prateleira_de_leite.jpeg')
pratileira_leite = cv2.cvtColor(pratileira_leite, cv2.COLOR_RGB2GRAY)
apresentaImg(pratileira_leite)

# Detecção de força bruta
# objeto de detecção!
orb = cv2.ORB_create()

#Retorna os pontos chaves e destinos
kpt1, des1 = orb.detectAndCompute(leite_condensado, None)
kpt2, des2 = orb.detectAndCompute(leite_condensado, None)

forca_bruta = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = forca_bruta.match(des1, des2)

print(matches[20].distance)





