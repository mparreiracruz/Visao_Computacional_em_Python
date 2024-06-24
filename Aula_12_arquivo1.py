import cv2
import numpy as np
import matplotlib.pyplot as plt

# print(sum([4, 3, 1]))
#
# string = 'sum'
#
# print(string)
#
# print(eval(string))
#
# funcaoS = eval(string)
#
# print(funcaoS([5, 6, 2]))

golden = cv2.imread('Cachorro_Golden.jpeg')

golden = cv2.cvtColor(golden, cv2.COLOR_BGR2RGB)

# plt.imshow(golden)
#
# plt.show()

rosto_golden = cv2.imread('golden_rosto.jpeg')

rosto_golden = cv2.cvtColor(rosto_golden, cv2.COLOR_BGR2RGB)

# plt.imshow(rosto_golden)
#
# plt.show()

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

# print(golden.shape)
#
# print(rosto_golden.shape)

meu_metodo = eval('cv2.TM_CCOEFF_NORMED')
res = cv2.matchTemplate(golden, rosto_golden, meu_metodo)

# plt.imshow(res)
#
# plt.show()

for m in methods:
    # criar cópia da imagem
    copia_golden = golden.copy()

    method = eval(m)

    # Template Matching
    res = cv2.matchTemplate(copia_golden, rosto_golden, method)

    # Pegar os valores mínimos e máximos, assim como as localizações mínimas e máximas
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_esquerdo = min_loc #(x, y)

    else:
        top_esquerdo = max_loc

    # Definir a forma do retangulo
    altura, largura, canais = rosto_golden.shape

    base_direita = (top_esquerdo[0] + largura, top_esquerdo[1] + altura)

    cv2.rectangle(golden, top_esquerdo, base_direita, (255, 0, 0), 20)

    #Apresentar as imagens
    plt.subplot(121)
    plt.imshow(res)
    plt.title('Mapa de Calor')

    plt.subplot(122)
    plt.imshow(golden)
    plt.title('Detecção')

    #Nome do método
    plt.suptitle(m)
    plt.show()
    print('\n')
