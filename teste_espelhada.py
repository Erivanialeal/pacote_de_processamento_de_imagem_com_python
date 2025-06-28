from PIL import Image
from processador_imagem.processo.tranformacao import espelhar_imagem


lista_imagens = [
    Image.open("imagens/imagem1.jpg"),
    Image.open("imagens/imagem2.jpg")
]

resultado = espelhar_imagem(lista_imagens, modo="horizontal")
resultado[0].save("testes/saida_espelhada.png")