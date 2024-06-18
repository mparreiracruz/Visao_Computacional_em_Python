import numpy as np
import matplotlib.pyplot as plt
import cv2

imagem = cv2.imread('Cachorro_Golden.jpeg')

print(type(imagem))

# plt.imshow(imagem)
#
# plt.show()

nova_imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

# plt.imshow(nova_imagem)
#
# plt.show()

print(nova_imagem.shape)

redimensionada_imagem = cv2.resize(nova_imagem, (640, 480))

# plt.imshow(redimensionada_imagem)
#
# plt.show()

print(redimensionada_imagem.shape)

largura = 0.5

altura = 0.5

outra_imagem = cv2.resize(nova_imagem, (0, 0), nova_imagem, largura, altura)

# plt.imshow(outra_imagem)
#
# plt.show()

print(outra_imagem.shape)

imagem_girada = cv2.flip(nova_imagem, 0)

# plt.imshow(imagem_girada)
#
# plt.show()

cv2.imwrite('Cachorro_Golden_MODIFICADO.jpeg', imagem)

cv2.imwrite('Cachorro_Golden_Girado.jpeg', imagem_girada)

img = plt.figure(figsize=(10, 10))

ax = img.add_subplot(111)

ax.imshow(imagem_girada)

plt.show()
