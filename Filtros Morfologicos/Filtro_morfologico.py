# Importando as bibliotecas necessárias
import numpy as np
import cv2

# Carregando a imagem
img = cv2.imread("Fotografo_original.png")

elem_estr = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))

# Recebe a imagem modificada
img_output = cv2.erode(img, elem_estr, iterations= 2)

# Salva a imagem com as alterações
cv2.imwrite("Fotografo_morfologico.png", img_output)

# Exibe ambas as imagens de comparação
cv2.imshow("Imagem Original", img)
cv2.imshow("Imagem com Erosão", img_output)

# Impedem que as janelas sejam fechadas sem um comando
cv2.waitKey()
cv2.destroyAllWindows()
