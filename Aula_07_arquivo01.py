import numpy as np
import matplotlib.pyplot as plt
import cv2

nova_imagem = np.zeros(shape=(1024, 1024, 3), dtype=np.int16)

print(type(nova_imagem))

print(nova_imagem.shape)

# print(nova_imagem)

# plt.imshow(nova_imagem)
#
# plt.show()

nova_imagem[:, :, :] = 0

# plt.imshow(nova_imagem)
#
# plt.show()
#
# print(nova_imagem)

cv2.rectangle(nova_imagem, pt1=(200, 250), pt2=(400, 450), color=(255, 255, 0), thickness=10)
cv2.circle(nova_imagem, center=(750, 750), radius=75, color=(255, 255, 255), thickness=25)
cv2.circle(nova_imagem, center=(500, 500), radius=75, color=(255, 255, 255), thickness=-1)
cv2.rectangle(nova_imagem, pt1=(400, 650), pt2=(800, 950), color=(0, 255, 0), thickness=20)

plt.imshow(nova_imagem)

plt.show()

cv2.line(nova_imagem, pt1)

#parei em 20 minutos
