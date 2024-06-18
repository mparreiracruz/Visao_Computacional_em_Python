import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

imagem = Image.open('Cachorro_Golden_Girado.jpeg')

#print(type(imagem))

# plt.imshow(imagem)
#
# plt.show()

#imagem_vetor = np.asarray(imagem)

#print(imagem_vetor.shape)

# redimensionar_imagem = imagem.resize((320, 480))
#
# #print(imagem_vetor.shape)
#
# plt.imshow(redimensionar_imagem)
#
# plt.show()

#print(redimensionar_imagem.size)

largura_atual, altura_atual = imagem.size

proporcao_largura = 1.0
proporcao_altura = 1.0

nova_largura = int(largura_atual * proporcao_largura)
nova_altura = int(altura_atual * proporcao_altura)

outra_imagem = imagem.resize((nova_largura, nova_altura))

# plt.imshow(outra_imagem)
#
# plt.show()

imagem_girada = imagem.rotate(180)

plt.imshow(imagem_girada)
plt.show()

imagem_girada.save('Cachorro_Golden_Girado.jpeg')

img = plt.figure(figsize=(10, 8))
ax = img.add_subplot(111)
ax.imshow(imagem_girada)
plt.show()
