import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

imagem = Image.open('Cachorro_Golden.jpeg')

#imagem_escala_cinza = plt.imread('Cachorro_Golden.jpeg')

imagem_vetor = np.asarray(imagem)

plt.imshow(imagem_vetor[:, :, 0], cmap='gray')

plt.show()
