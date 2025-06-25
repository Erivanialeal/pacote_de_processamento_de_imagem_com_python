from PIL import Image
from processador_imagem.processo.combinacao import adicionar_borda

#adicionar as imagens na lista para testar e em seguinda abrindo-as
lista_de_imagens = [
    Image.open('imagens/imagem1.jpg'),
    Image.open('imagens/imagem2.jpg'),

]
# adicionando bordas as imagens da lista
com_borda = adicionar_borda(lista_de_imagens, tamanho=20, cor=(255,0,0))
# salvando as imagens com bordas em arquivos separados.
for i, imagem in enumerate(com_borda):
    imagem.save(f'testes/imagem_com_borda_{i}.png')
