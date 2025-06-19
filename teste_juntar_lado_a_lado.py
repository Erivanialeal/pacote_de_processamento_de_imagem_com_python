from PIL import Image
from processador_imagem.processo.combinação import juntar_lado_a_lado

# Carregar as imagens
imagem1 = Image.open("imagens/imagem1.jpg")
imagem2 = Image.open("imagens/imagem2.jpg")
# Juntar as imagens lado a lado
resultado = juntar_lado_a_lado(imagem1, imagem2)
#salvar o resultado
resultado.save("testes/saida_juntar_lador_a lado.png")