# Importando as bibliotecas necessárias
import numpy as np
import cv2
import math

# O Parâmetro -1 permite carregar a imagem com informações
# de todos os seus canais, incluindo o alpha
img = cv2.imread("Cubo_original.jpg", -1)

# Imprime as proporções originais da imagem
print("Imagem original:", img.shape)

'''
    h (height) = Altura
    w (width) = Largura
    c (channels) = Canais da imagem    
'''
h, w, c = img.shape

# Redimensiona a imagem para metade do seu tamanho
img_n = cv2.resize(img, (w//2, h//2), interpolation = cv2.INTER_NEAREST)
cv2.imshow("Cubo com proporções pela metade", img_n)

# Imprime as novas proporções da imagem
print("Imagem redimensionada (metade):", img_n.shape)

# Obtém a altura (rows) e largura (cols) da nova imagem
rows, cols = img_n.shape[:2]

img_output = np.zeros_like(img_n)

# Aplica uma distorção do tipo "onda" (warping)
for i in range(rows):
    for j in range(cols):
        offset_x = int(25.0 * math.sin(2 * 3.14 * i / 180))
        offset_y = 0

        if j + offset_x < h:
            img_output[i, j] = img[i, (j+offset_x)%cols]
        else:
            img_output[i, j] = 0

# Exibe a imagem distorcida
cv2.imshow("Cubo com distorção vertical", img_output)

# Salva a imagem distorcida
cv2.imwrite("Cubo_reducao_distorcao.jpg", img_output)

# Aguarda o pressionamento de uma tecla antes de fechar as janelas
cv2.waitKey(0)
cv2.destroyWindow()