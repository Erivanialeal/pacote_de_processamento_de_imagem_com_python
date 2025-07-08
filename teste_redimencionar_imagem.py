from PIL import Image
from processador_imagem.processo.tranformacao import redimensionar_imagem


lista_imagens = [
    Image.open("imagens/imagem1.jpg"),
    Image.open("imagens/imagem2.jpg")
]

resuntado = redimensionar_imagem(lista_imagens,largura=200, altura= 300)
resuntado[0].save("testes/saida_redimensionar.png")