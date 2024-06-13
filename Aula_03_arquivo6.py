import numpy as np

matriz = np.arange(0, 100).reshape(10, 10)
#
# print(matriz)
#
# print(matriz[2, 6])
#
# print(matriz[:, 2].reshape(10, 1))
#
# print(matriz[2, :])

copiamatriz = matriz.copy()

copiamatriz[0:3, 0:4] = 10

print(copiamatriz)
