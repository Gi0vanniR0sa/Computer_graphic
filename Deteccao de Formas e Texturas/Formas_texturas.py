# importando as bibliotecas necessárias
import cv2
import numpy as np

# Abrindo a imagem
img = cv2.imread("Sudoku_original.jpg")

# Convertendo a imagem para tons de cinza
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Realiza a detecção de mudanças bruscas de intensidade (bordas)
canimg = cv2.Canny(img_gray, 50, 200)

# Realiza a detecção de linhas retas na imagem
lines = cv2.HoughLines(canimg, 1, np.pi/180, 120, np.array([]))

# Faz uma cópia da imagem original empregar as linhas de delimitação
img_lines = img.copy()

# Delimita as linhas da imagem original com linhas em vermelho de espessura 2
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)

    x0 = a*rho
    y0 = b*rho

    x1 = int(x0+1000*(-b))
    y1 = int(y0+1000*(a))
    x2 = int(x0-1000*(-b))
    y2 = int(y0-1000*(a))

    cv2.line(img_lines, (x1, y1), (x2, y2), (0,0, 255), 2)

# Salva as imagens processadas
cv2.imwrite("Sudoku_linhas_detectadas.jpg", img_lines)
cv2.imwrite("Sudoku_bordas_canny.jpg", canimg)

# Exibe as imagens obtidas utilizando o Canny e a Transformada de Hough
cv2.imshow("Lines Detected", img_lines)
cv2.imshow("Canny Detection", canimg)

cv2.waitKey(0)
cv2.destroyWindow()