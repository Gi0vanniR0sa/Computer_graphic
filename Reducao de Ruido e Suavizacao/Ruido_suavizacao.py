# Importando Bibliotecas e Métodos
from pathlib import Path
from PIL import Image, ImageFilter

# Abre a imagem
img = Image.open("Pato_original.jpg")

# Passa a função MedianFilter() do módulo ImageFilter com o valor
# da intensidade do filtro de red. de ruído para a função .filter()
img_median = img.filter(ImageFilter.MedianFilter(7))

# Passa a imagem "Limpa" para aplicação do filtro de suavização
img_boxblur = img_median.filter(ImageFilter.BoxBlur(3))
img_boxblur.save("Pato_ruido_suavizacao.jpeg")

# Exibe a imagem modificada
img_boxblur.show()

