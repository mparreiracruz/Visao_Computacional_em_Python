# Harris Corner Detection
# Para identificação de bordas na imagem

import cv2
import numpy as np
import matplotlib.pyplot as plt

xadrez = cv2.imread('xadrez.jpeg')
xadrez = cv2.cvtColor(xadrez, cv2.COLOR_BGR2RGB)

# plt.imshow(xadrez)
# plt.show()
#
cinza_xadrez = cv2.cvtColor(xadrez, cv2.COLOR_RGB2GRAY)
# plt.imshow(cinza_xadrez, cmap='gray')
# plt.show()

xadrez_real = cv2.imread('xadrez_real.jpeg')
xadrez_real = cv2.cvtColor(xadrez_real, cv2.COLOR_BGR2RGB)
# plt.imshow(xadrez_real)
# plt.show()

cinza_xadrez_real = cv2.cvtColor(xadrez_real, cv2.COLOR_RGB2GRAY)
plt.imshow(cinza_xadrez_real, cmap='gray')
plt.show()

# print(cinza_xadrez_real)

cinza = np.float32(cinza_xadrez)

print(cinza)
# Aplicando o algoritmo Harris Corner Detection
destino = cv2.cornerHarris(src= cinza_xadrez, blockSize=2, ksize=3, k=0.04)

# Transformação morfológica pelo cv2.dilate()

plt.show(destino)

# parei em 15:34
