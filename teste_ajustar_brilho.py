from PIL import Image
from processador_imagem.processo.tranformacao import ajustar_brilho

lista_imagens = [
    Image.open("imagens/imagem3.jpg"),
    Image.open("imagens/imagem4.jpg")
]

resultado = ajustar_brilho(lista_imagens,fator=7.0)
resultado[1].save("testes/ajustar_brilho.jpg")
