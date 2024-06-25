# Importação das Bibliotecas Necessárias
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Leitura e Conversão da Imagem "xadrez.jpeg"
xadrez = cv2.imread('xadrez.jpeg')
xadrez = cv2.cvtColor(xadrez, cv2.COLOR_BGR2RGB)

# Conversão para Escala de Cinza
cinza_xadrez = cv2.cvtColor(xadrez, cv2.COLOR_RGB2GRAY)

# Leitura e Conversão da Imagem "xadrez_real.jpeg"
xadrez_real = cv2.imread('xadrez_real.jpeg')
xadrez_real = cv2.cvtColor(xadrez_real, cv2.COLOR_BGR2RGB)

# Conversão para Escala de Cinza
cinza_xadrez_real = cv2.cvtColor(xadrez_real, cv2.COLOR_RGB2GRAY)

# Aplicação do Algoritmo Harris Corner Detection na Imagem "xadrez.jpeg"
# Conversão para Float32
cinza = np.float32(cinza_xadrez)
print(cinza)

# Aplicação do Algoritmo Harris Corner
destino = cv2.cornerHarris(src=cinza_xadrez, blockSize=20, ksize=3, k=0.04)

# Transformação Morfológica
destino = cv2.dilate(destino, None)

# Marcação das Esquinas na Imagem Original
xadrez[destino > 0.01 * destino.max()] = [0, 255, 0]
print(destino.max())
print(destino)

# Exibição da Imagem com Esquinas Detectadas
plt.imshow(xadrez)
plt.show()

# Aplicação do Algoritmo Harris Corner Detection na Imagem "xadrez_real.jpeg"
# Conversão para Float32
cinza = np.float32(cinza_xadrez_real)
print(cinza)

# Aplicação do Algoritmo Harris Corner
destino = cv2.cornerHarris(src=cinza_xadrez_real, blockSize=3, ksize=3, k=0.04)

# Transformação Morfológica
destino = cv2.dilate(destino, None)

# Marcação das Esquinas na Imagem Original
xadrez_real[destino > 0.01 * destino.max()] = [255, 255, 0]

# Exibição da Imagem com Esquinas Detectadas
plt.imshow(xadrez_real)
plt.show()
