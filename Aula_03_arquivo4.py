import numpy as np

np.random.seed(101)

vetor = np.random.randint(0, 100, 10)

print(vetor.shape)

print(vetor)

print(vetor.reshape(2, 5))

#print(vetor.reshape(2, 9))# erro

print(vetor.reshape(5, 2))
