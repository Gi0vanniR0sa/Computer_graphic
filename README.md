# Computer Graphics 🖼️

Este repositório contém implementações práticas de técnicas fundamentais em **processamento digital de imagens**, desenvolvidas como parte de um projeto de estudo em Computação Gráfica.

🔗 [Repositório no GitHub](https://github.com/Gi0vanniR0sa/Computer_graphic)

## Atividades Implementadas

---

### 1. 🎚️ Realce e Ajuste de Intensidade
**Objetivo:** Melhorar o contraste e o brilho da imagem para destacar regiões de interesse.

**Técnicas utilizadas:**
- Brilho: Clareia imagens escuras
- Contraste: Destaca bordas e detalhes
  
**Bibliotecas:** Pillow (`PIL.Image`, `PIL.ImageEnhance`).

---

### 2. 🧼 Redução de Ruído e Suavização
**Objetivo:** Remover imperfeições e suavizar detalhes irrelevantes da imagem.

**Técnicas utilizadas:**
- Mediana: Remove os ruídos do tipo sal e pimenta da imagem
- Média (BoxBlur): Realiza a redução de ruído de maneira uniforme

**Bibliotecas:** Pillow(`PIL.Image`, `PIL.ImageFilter`).

---

### 3. 🪞 Detecção de Bordas
**Objetivo:** Identificar contornos e formas de objetos presentes nas imagens.

**Técnicas utilizadas:**
- Sobel: Extrai contornos em visão computacional (gradiente em y)

**Bibliotecas:** OpenCV (`cv2.Sobel`).

---

### 4. 🌀 Detecção de Formas e Texturas
**Objetivo:** Analisar padrões visuais presentes na imagem.

**Técnicas utilizadas:**
- Canny: Realiza a segmentação em reconhecimento de padrões
- Sobel: Extrai contornos em visão computacional

**Bibliotecas:** OpenCV (`cv2.Sobel`, `cv2.Canny`) e Numpy (`np.pi`, `np.array`, `np.cos`, `np.sin`).

---

### 5. 🔄 Transformações Geométricas
**Objetivo:** Alterar a geometria da imagem, como redimensionamento, rotação e distorções.

**Técnicas utilizadas:**
- Interpolação Bilinear/Bicúbica: Realiza o redimensionamento de imagens 
- Warping: Aplica distorções na imagem 

**Bibliotecas:** OpenCV (`cv2.resize`), Numpy (`np.zeros_like`), Math (`marh.sin`)

---

### 6. 🔲 Filtros Morfológicos
**Objetivo:** Processar imagens binárias (segmentadas) para refinar regiões e estruturas.

**Técnicas utilizadas:**
- Erosão: Separação de elementos que compõem a imagem

**Bibliotecas:** OpenCV (`cv2.erode`, `cv2.getStructuringElement`, `cv2.MORPH_RECT`).

