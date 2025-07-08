from PIL import Image
from processador_imagem.utils.io import salvar_uma_imagem

img = Image.open("imagens/imagem3.jpg")
salvar_uma_imagem(img, "testes/saida_uma_imagem.jpg")