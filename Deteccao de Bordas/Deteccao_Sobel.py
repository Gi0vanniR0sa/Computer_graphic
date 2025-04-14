# Sem entrar na explicação matemática do funcionamento do filtro
# de Sobel, pode-se dizer que o mesmo trabalha detectando bordas em
# duas direções: horizontal e vertical

# Importação da biblioteca open-cv
import cv2

# Abre a imagem
img = cv2.imread("Valve_original.png")

''' 
Aplica o filtro Sobel no sentido vertical da imagem 

Args: 
    img (Object): Recebe a variável na qual a imagem foi atribuida
    img_cv2.CV_8U (Callable): Função que especifica o tipo de profundidade
    dx (int): Ordem da derivada em X
    dy (int): Ordem da derivada em Y
    dst (int): Tamanho do kernel Sobel
    
Returns: 
    Object: Cópia da Imagem com o filtro aplicado na direção indicada
'''

sobel_y = cv2.Sobel(img, cv2.CV_8U, 1, 0, 7)

cv2.imwrite('Valve_Sobel.png', sobel_y)

# Abre uma janela com o nome indicado exibindo a imagem modificada
cv2.imshow("Sobel_Y", sobel_y)
cv2.waitKey()