from PIL import Image
from processador_imagem.processo.combinação import juntar_em_grade

# Chamar a lista de imagens
lista_de_imagens = [
    Image.open('imagens/imagem1.jpg'),
    Image.open('imagens/imagem2.jpg'),
    Image.open('imagens/imagem3.jpg'),
    Image.open('imagens/imagem4.jpg')
    ]
resultado= juntar_em_grade(lista_de_imagens, linhas = 2, colunas= 2)
resultado.save("testes/grade.png")