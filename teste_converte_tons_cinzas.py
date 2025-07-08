from PIL import Image
from processador_imagem.processo.tranformacao import converter_para_tons_cinza

lista_imagens = [
    Image.open("imagens/imagem3.jpg"),
    Image.open("imagens/imagem4.jpg")
]
resultado= converter_para_tons_cinza(lista_imagens, modo="L")
resultado[0].save("testes/saida_tons_cinza.jpg")