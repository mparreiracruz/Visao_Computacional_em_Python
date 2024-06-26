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

FLAN_INDEX_KDTREE = 0

index_params = dict(algorithm=FLAN_INDEX_KDTREE, tress=5)
search_params = dict(checks=50)

flann = cv2.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(des1, des2, k=2)

good = []

for match1, match2 in matches:
    if match1.distance < 0.75 * match2.distance:
        good.append([match1])

print(len(good))

flann_matches = cv2.drawMatchesKnn(leite_condensado, kp1, pratileira_leite, kp2, good, None, flags=2)
apresentaImg(flann_matches)

matchesMask = [[0, 0]for i in range(len(matches))]

print(matchesMask)

for i, (match1, match2) in enumerate(matches):
    if match1.distance < 0.75 * match2.distance:
        matchesMask[i] = [1, 0]

draw_params = dict(matchColor=(0, 0, 255), singlePointColor=(255, 0, 0), matchesMask = matchesMask, flags=0)

flann_matches = cv2.drawMatchesKnn(leite_condensado, kp1, pratileira_leite, kp2, matches, None, **draw_params)

apresentaImg(flann_matches)

