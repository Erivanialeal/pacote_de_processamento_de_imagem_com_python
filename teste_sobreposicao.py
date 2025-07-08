from PIL import Image
from processador_imagem.processo.combinacao import sobrepor_imagens

#abrir as imagens de entrada.
imagem1 = Image.open('imagens/imagem1.jpg')
imagem2 = Image.open('imagens/imagem2.jpg')

#chamar a função
resultado = sobrepor_imagens(imagem1, imagem2, alpha = 0.5)
#salvar os resultados.
resultado.save('testes/saida_sobreposicao.png')