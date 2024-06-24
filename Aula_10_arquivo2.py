'''
https://www.youtube.com/watch?v=s0B0QB-9B20&list=PLM_FW0E1SLbF34weofkSvKMVNMIsYd1hq&index=10
'''
import cv2

# Função par desenhar um retangulo no vídeo

def desenha_retangulo(event, x, y, flags, params):
    global pt1, pt2, topo, base
    if event == cv2.EVENT_LBUTTONDOWN:
        # Apagar o retangulo que estará sendo apresentado na tela
        if topo == True and base == True:
            pt1 = (0, 0)
            pt2 = (0, 0)
            topo = False
            base = False
        if topo == False:
            pt1 = (x, y)
            topo = True
        elif base == False:
            pt2 = (x, y)
            base = True

# Variáveis Globais
pt1 = (0, 0)
pt2 = (0, 0)
topo = False
base = False

# Apresentação
video = cv2.VideoCapture(0)

cv2.namedWindow('frame')
cv2.setMouseCallback('frame', desenha_retangulo)

# largura = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
# altura = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
#
# # Ponto Inicial
# x = 10
# y = 10
#
# # Ponto Final
#
# x1 = largura // 2
# y1 = altura // 2

# Ponto de baixo é dado por x + x1 e y + y1

while True:
    ret, frame = video.read()
    # cv2.circle(frame, center=(x1, y1), radius=x + y, color=(0, 0, 0), thickness=-1)
    # cv2.rectangle(frame, pt1=(x, y), pt2=(x1, y1), color=(255, 0, 0), thickness=5)

    # Desenhar no Frame
    if topo:
        cv2.circle(frame, center=pt1, radius=3, color=(0, 255, 0), thickness=-1)

    if topo and base:
        cv2.rectangle(frame, pt1, pt2, color=(0, 0, 0), thickness=6)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

video.release()
cv2.destroyAllWindows()
