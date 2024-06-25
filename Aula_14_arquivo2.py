import cv2
import numpy as np
import matplotlib.pyplot as plt

xadrez = cv2.imread('xadrez.jpeg')
xadrez = cv2.cvtColor(xadrez, cv2.COLOR_BGR2RGB)
cinza_xadrez = cv2.cvtColor(xadrez, cv2.COLOR_RGB2GRAY)

# plt.imshow(cinza_xadrez, cmap='gray')
# plt.show()

bordas = cv2.goodFeaturesToTrack(cinza_xadrez, 48, 0.01, 10)
print(bordas)

bordas = np.intp(bordas)
print(bordas)

for i in bordas:
    x, y = i.ravel()
    cv2.circle(xadrez, (x, y), 15, (0, 255, 0), -1)

plt.imshow(xadrez)
plt.show()

xadrez_real = cv2.imread('xadrez_real.jpeg')
xadrez_real = cv2.cvtColor(xadrez_real, cv2.COLOR_BGR2RGB)
cinza_xadrez_real = cv2.cvtColor(xadrez_real, cv2.COLOR_RGB2GRAY)

# plt.imshow(xadrez_real)
# plt.show()

bordas = cv2.goodFeaturesToTrack(cinza_xadrez_real, 48, 0.01, 10)
bordas = np.intp(bordas)

for i in bordas:
    x, y = i.ravel()
    cv2.circle(xadrez_real, (x, y), 8, (0, 255, 0), -1)

plt.imshow(xadrez_real)
plt.show()
