import cv2

# Criar a nossa função que apresentará o círculo
def desenha_circulo(event, x, y, flags, param):

    # Criar variáveis do tipo global:
    global centro, clique

    # Condicionais que irão verificar o clique do mouse
    if event == cv2.EVENT_LBUTTONDOWN:
        centro = (x, y)
        clique = False

    if event == cv2.EVENT_LBUTTONUP:
        clique = True

# Atribuição de valores
centro = (0, 0)
clique = (False)

#Captura do vídeo
cap = cv2.VideoCapture(0)

# Criar uma janela par o vídeo
cv2.namedWindow('Janela')

# Juntar a janela a função desenha_círculo
cv2.setMouseCallback('Janela', desenha_circulo)

while True:
    # Capturar frame a frame
    ret, frame = cap.read()

    # Verificar se algo já foi clicado
    if clique:
        # Desenhar o círculo
        cv2. circle(frame, center = centro, radius=80, color=(0, 250, 0), thickness = 10)

    # Apresentar o frame resultante
    cv2.imshow('Janela', frame)

    #Comando de saída
    if cv2. waitKey(2) & 0xFF == ord('s'):
        break

# Quando finalizar, destruir os elementos
cap.release()
cv2.destroyAllWindows()
