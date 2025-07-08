from PIL import Image
from processador_imagem.processo.combinacao import juntar_verticalmente

lista_imagem = [
    Image.open('imagens/imagem3.jpg'),
    Image.open('imagens/imagem4.jpg'),
]
imagem_resultado = juntar_verticalmente(lista_imagem)
imagem_resultado.save('testes/saida_juntar_verticalmente.png')