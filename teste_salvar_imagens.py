from PIL import Image
from processador_imagem.utils.io import salvar_imagens


lista_imagens = [
    Image.open("imagens/imagem1.jpg"),
    Image.open("imagens/imagem2.jpg")
]

salvar_imagens(lista_imagens, "testes", nome_base= "saindas_teste" )