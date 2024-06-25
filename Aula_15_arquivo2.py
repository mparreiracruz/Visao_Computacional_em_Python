import cv2
import numpy as np
import matplotlib.pyplot as plt

def apresentaImg(imagem):
    img = plt.figure(figsize=(30, 20))
    ax = img.add_subplot(111)
    ax.imshow(imagem, cmap='gray')
    plt.show()


vinho = cv2.imread('vinho_aurora_rose.jpeg')
vinho = cv2.cvtColor(vinho, cv2.COLOR_BGR2GRAY)

apresentaImg(vinho)

prateleira_vinho = cv2.imread('prateleira_vinhos.jpeg')
prateleira_vinho = cv2.cvtColor(prateleira_vinho, cv2.COLOR_BGR2GRAY)
apresentaImg(prateleira_vinho)

orb = cv2.ORB.create()

kp1, des1 = orb.detectAndCompute(vinho, None)
kp2, des2 = orb.detectAndCompute(prateleira_vinho, None)

forcaBruta = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = forcaBruta.match(des1, des2)

print(matches)

matches = sorted(matches, key=lambda x: x.distance)

vinho_matches = cv2.drawMatches(vinho, kp1, prateleira_vinho, kp2, matches[:10], None, flags=2)

apresentaImg(vinho_matches)

