import numpy as np
import cv2

#Variáveis
#Desenho é falso quando o clique não estiver acionado
#Desenho é verdadeiro quando o clique estiver pressionado
desenho = False

ix = -1
iy = -1
#Função
def retangulo(event, x, y, flags, params):
    global ix, iy, desenho
    #Condicional
    if event == cv2.EVENT_LBUTTONDOWN: #Quando o botão esquerdo é clicado
        ix = x
        iy = y
        desenho = True

    elif event == cv2.EVENT_MOUSEMOVE: #Quando o botão está clicado e o mouse sendo movido
        if desenho == True:
            cv2.rectangle(imagem, (ix, iy), (x, y), (255, 255, 255), -1)
    elif event == cv2.EVENT_LBUTTONUP: #Quando o botão do lado esquerdo do mouse deixa de ser clicado
        desenho = False
        cv2.rectangle(imagem, (ix, iy), (x, y), (0, 255, 255), -1)


cv2.namedWindow(winname='minha_tela')
cv2.setMouseCallback('minha_tela', retangulo)

#Apresentação

imagem = np.zeros((400, 400, 3))
while True:
    cv2.imshow('minha_tela', imagem)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
