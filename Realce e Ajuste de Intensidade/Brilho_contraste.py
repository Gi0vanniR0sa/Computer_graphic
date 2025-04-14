# Importando Bibliotecas e Métodos
from pathlib import Path
from PIL import Image, ImageEnhance


# Caminho base (pasta onde está o script atual)
base = Path.cwd()

# Caminho da imagem original
img_path = base / "Gatos_filhotes_original.jpeg"

# Abrindo a imagem e atribuindo a uma variável
img = Image.open(img_path)

# Passa a imagem como argumento para função ImageEnhance que devolve
# uma cópia para aplicar o brilho
brilho = ImageEnhance.Brightness(img)
img_brilho = brilho.enhance(2) # 0 - Cinza / 1 - Original / 2 - Mais brilho

# Retorna uma cópia para aplicar o contraste
contraste = ImageEnhance.Contrast(img_brilho)
contraste.enhance(1.5).save("Gatos_brilho_contraste.jpeg")


# Abrindo a nova imagem
img2 = Image.open("Gatos_brilho_contraste.jpeg")

# Exibindo a imagem
img2.show()