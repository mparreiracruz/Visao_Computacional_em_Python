'''
https://www.youtube.com/watch?v=2DlySk9y5gE&list=PLM_FW0E1SLbF34weofkSvKMVNMIsYd1hq&index=9
'''
import cv2

captura_imagem = cv2.VideoCapture(0)

largura = int(captura_imagem.get(cv2.CAP_PROP_FRAME_WIDTH))
altura = int(captura_imagem.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret, frame = captura_imagem.read()
    #rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', cinza)

    if cv2.waitKey(10) & 0xFF == ord('s'):
        break

captura_imagem.release()
cv2.destroyAllWindows()