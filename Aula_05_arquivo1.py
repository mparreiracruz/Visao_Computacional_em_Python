import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image

imagem = cv2.imread('Cachorro_Golden.jpeg')

print(type(imagem))

print(imagem.shape)

corrigi_imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

# plt.imshow(corrigi_imagem)
#
# plt.show()

imagem_escala_cinza = cv2.imread('Cachorro_Golden.jpeg', cv2.IMREAD_GRAYSCALE)

plt.imshow(imagem_escala_cinza, cmap='gray')

plt.imshow(imagem_escala_cinza, cmap='magma')

plt.show()
