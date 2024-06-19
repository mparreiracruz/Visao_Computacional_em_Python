import numpy as np

import cv2

#Variáveis
#Desenho é falso quando o clique não estiver acionado
#Desenho é verdadeiro quando o clique estiver pressionado
desenho = False

ix = -1
iy = -1


#Função



#Apresentação

imagem = np.zeros((400, 400, 3))

while True:
    cv2.imshow('minha_tela', imagem)
    if cv2. waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
