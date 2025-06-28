from PIL import Image
from processador_imagem.processo.tranformacao import rotacionar_imagem

lista_imagens = [
    Image.open("imagens/imagem3.jpg"),
    Image.open("imagens/imagem4.jpg")
]
resultado = rotacionar_imagem(lista_imagens,angulo = 80, expand= True)
resultado[0].save("testes/saida_rotacionar.png")