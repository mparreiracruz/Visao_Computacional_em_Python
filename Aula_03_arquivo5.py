import numpy as np

matriz = np.arange(0, 100)

#print(matriz)

matriz = matriz.reshape(10, 10)

print(matriz)

linha = 1

coluna = 2

print(matriz[linha, coluna])
