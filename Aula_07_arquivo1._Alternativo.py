import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage.draw import rectangle_perimeter, circle_perimeter
from PIL import Image

nova_imagem = np.zeros(shape=(1024, 1024, 3), dtype=np.int16)

# print(type(nova_imagem))
#
# print(nova_imagem.shape)
#
# print(nova_imagem)

# plt.imshow(nova_imagem)

# plt.show()

nova_imagem[:, :, 0] = 0

# plt.imshow(nova_imagem)
#
# plt.show()

# rr, cc = rectangle_perimeter(start=(200, 250), end=(400, 450), shape=nova_imagem.shape)
# nova_imagem[rr, cc] = [255, 0, 0]
#
# plt.imshow(nova_imagem)
# plt.show()
'''
RETÂNGULOS 01 E 02
'''
def draw_thick_rectangle(image, start, end, thickness, color):
    rr, cc = rectangle_perimeter(start, end, shape=image.shape)
    image[rr, cc] = color
    for i in range(1, thickness):
        rr_inner, cc_inner = rectangle_perimeter((start[0] - i, start[1] - i),
                                                  (end[0] + i, end[1] + i),
                                                  shape=image.shape)
        image[rr_inner, cc_inner] = color

nova_imagem = np.zeros(shape=(1024, 1024, 3), dtype=np.int16)


# Define as coordenadas do retângulo 01
start = (200, 250)
end = (400, 450)
# Desenha o retângulo 01 com borda mais espessa
draw_thick_rectangle(nova_imagem, start, end, thickness=20, color=[255, 255, 0])


# Define as coordenadas do retângulo 02
start = (650, 400)
end = (950, 800)
# Desenha o retângulo 02 com borda mais espessa
draw_thick_rectangle(nova_imagem, start, end, thickness=20, color=[0, 255, 255])

'''
CÍRCULO
'''
def draw_thick_circle(image, center, radius, thickness, color):
    for t in range(thickness):
        rr, cc = circle_perimeter(center[0], center[1], radius + t, shape=image.shape)
        image[rr, cc] = color

draw_thick_circle(nova_imagem, center=(500, 500), radius=50 , thickness=20, color=[255, 255, 255])

plt.imshow(nova_imagem)
plt.show()
