import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

imagem = Image.open('cachorro-mini-pet.jpg')

# print(type(imagem))
#
imagem_vetor = np.asarray(imagem)
#
# print(type(imagem_vetor))
#
# print(imagem_vetor.shape)


plt.imshow(imagem_vetor[:, :, 0], cmap='Blues')

plt.show()

copia_imagem = imagem_vetor.copy()

print(type(copia_imagem))

plt.imshow(copia_imagem)

#RGB - Vermelho, Verde, Azul

print(copia_imagem.shape)

plt.imshow(copia_imagem[:, :, 0], cmap='gray')

plt.show()

print(copia_imagem.shape)

print(copia_imagem[:, :, 0])

print(copia_imagem.shape)

print(copia_imagem[:, :, 2])

copia_imagem[:, :, 0] = 0

print(copia_imagem[:, :, 0])

copia_imagem[:, :, 2] = 0

#print(copia_imagem[:, :, 2])

plt.imshow(copia_imagem)

plt.show()
