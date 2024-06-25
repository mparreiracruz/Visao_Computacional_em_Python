import cv2
import numpy as np
import matplotlib.pyplot as plt


def apresentaImg(imagem):
    img = plt.figure(figsize=(30, 20))
    ax = img.add_subplot(111)
    ax.imshow(imagem, cmap='gray')
    plt.show()


leite_condensado = cv2.imread('zuzu_lapte_zoom.jpeg')
leite_condensado = cv2.cvtColor(leite_condensado, cv2.COLOR_BGR2GRAY)

pratileira_leite = cv2.imread('prateleira_de_leite.jpeg')
pratileira_leite = cv2.cvtColor(pratileira_leite, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT.create()

kp1, des1 = sift.detectAndCompute(leite_condensado, None)
kp2, des2 = sift.detectAndCompute(pratileira_leite, None)

forcaBruta = cv2.BFMatcher()

matches = forcaBruta.knnMatch(des1, des2, k=2)

print(matches)

good = []

for match1, match2 in matches:
    if match1.distance < 0.6 * match2.distance:
        good.append([match1])

print(len(matches))

print(len(good))

sift_matches = cv2.drawMatchesKnn(leite_condensado, kp1, pratileira_leite, kp2, good, None, flags=2)

apresentaImg(sift_matches)
