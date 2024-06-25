import cv2
import numpy as np
import matplotlib.pyplot as plt


def apresentaImg(imagem):
    img = plt.figure(figsize=(30, 20))
    ax = img.add_subplot(111)
    ax.imshow(imagem, cmap='gray')
    plt.show()


vinho = cv2.imread('vinho_aurora_rose_zoom.jpeg')
vinho = cv2.cvtColor(vinho, cv2.COLOR_BGR2GRAY)

prateleira_vinho = cv2.imread('prateleira_vinhos.jpeg')
prateleira_vinho = cv2.cvtColor(prateleira_vinho, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT.create()

kp1, des1 = sift.detectAndCompute(vinho, None)
kp2, des2 = sift.detectAndCompute(prateleira_vinho, None)

forcaBruta = cv2.BFMatcher()

matches = forcaBruta.knnMatch(des1, des2, k=2)

good = []

for match1, match2 in matches:
    if match1.distance < 0.6 * match2.distance:
        good.append([match1])

print(len(matches))
print(len(good))

sift_matches = cv2.drawMatchesKnn(vinho, kp1, prateleira_vinho, kp2, good, None, flags=2)

apresentaImg(sift_matches)
