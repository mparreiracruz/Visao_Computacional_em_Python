import cv2
import numpy as np
import matplotlib.pyplot as plt

def apresentaImg(imagem):
    img = plt.figure(figsize=(30, 20))
    ax = img.add_subplot(111)
    ax.imshow(imagem, cmap='gray')
    plt.show()


leite_condensado = cv2.imread('zuzu_lapte_zoom.jpeg')
leite_condensado = cv2.cvtColor(leite_condensado, cv2.COLOR_BGR2RGB)

# apresentaImg(leite_condensado)

pratileira_leite = cv2.imread('prateleira_de_leite.jpeg')
pratileira_leite = cv2.cvtColor(pratileira_leite, cv2.COLOR_RGB2BGR)
# apresentaImg(pratileira_leite)

# Detecção de força bruta
# objeto de detecção!

orb = cv2.ORB.create()
#Retorna os pontos chaves e destinos
kp1, des1 = orb.detectAndCompute(leite_condensado, None)
kp2, des2 = orb.detectAndCompute(pratileira_leite, None)

forca_bruta = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = forca_bruta.match(des1, des2)

print(matches[1].distance)

matches = sorted(matches, key=lambda x:x.distance)

leite_matches = cv2.drawMatches(leite_condensado, kp1, pratileira_leite, kp2, matches[:10], None, flags=2)

apresentaImg(leite_matches)
