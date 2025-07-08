from PIL import Image


def juntar_lado_a_lado(imagem1, imagem2):
    # garantir que ambas as imagens estejam no modo RGBA
    imagem1 = imagem1.convert("RGBA")
    imagem2 = imagem2.convert("RGBA")
    # pegando as dimenções das imagems
    largura1, altura1 = imagem1.size
    largura2, altura2 = imagem2.size
    # calcular as novas dimenções
    nova_largura = largura1 + largura2
    nova_altura = max (altura1, altura2)
    #criar uma nova imagem em branco
    nova_imagem = Image.new('RGBA', (nova_largura,nova_altura))
    # colar a nova imagem na nova imagem
    nova_imagem.paste(imagem1, (0, 0))
    nova_imagem.paste(imagem2, (largura1, 0))
    #Retornar a nova imagem
    return nova_imagem

def juntar_em_grade(lista_de_imagens, linhas, colunas):
    # Verifica se o número de imagens corresponde ao tamanho da grade
    if len(lista_de_imagens) != linhas * colunas:
        raise ValueError("O número de imagens não corresponde ao tamanho da grade especificada.")
    # pegar o tamanho padrao das imagens
    largura1, altura1 = lista_de_imagens[0].size # pegando a primeira imagem de referencia
    # calcular dimensões da nova imagem
    largura_total = largura1 * colunas
    altura_total = altura1 * linhas
    # criar uma nova imagem em branco
    nova_imagem = Image.new("RGBA", (largura_total, altura_total))
    # colar as imagens na posição correta
    for indice , img in enumerate(lista_de_imagens):
        linha= indice // colunas
        coluna= indice % colunas
        x = coluna * largura1
        y = linha * altura1
        print(f"Colando imagem {indice+1} na posição ({x}, {y})")
        nova_imagem.paste(img, (x, y))
    return nova_imagem
def sobrepor_imagens(imagem1, imagem2, alpha=0.5):
   #1. Converter ambas as imagens para o modo RGBA, garantindo que tenham canal de transparência.
   imagem1 = Image.open('imagens/imagem1.jpg')
   imagem2 = Image.open('imagens/imagem2.jpg')
   # Converter ambas para RGBA
   imagem1 = imagem1.convert('RGBA')
   imagem2 = imagem2.convert('RGBA')
   #2. Redimensionar uma das imagens para que ambas tenham exatamente o mesmo tamanho.
   #pegando o tamanho de referência 
   largura, altura = imagem1.size
   imagem2 = imagem2.resize((largura, altura))
   #3. Usar a função Image.blend(imagem1, imagem2, alpha) para mesclar as duas imagens.
   imagem_resultado = Image.blend(imagem1, imagem2, alpha=0.5)
   #4. Retornar a nova imagem resultante da mesclagem.
   return imagem_resultado


def juntar_verticalmente(lista_imagens):
    #garantir que as imagens estejam no modo RGBA.
    lista_imagens = [imagem.convert('RGBA') for imagem in lista_imagens]
    # criar dimenções finais
    largura_total = max(imagem.width for imagem in lista_imagens)
    altura_total = sum(imagem.height for imagem in lista_imagens)
    # criar uma nova imagem em branco
    nova_imagem = Image.new('RGBA', (largura_total, altura_total))
    #colar as imagens em suas expectivos lugares
    pocicao_y = 0
    for imagem in lista_imagens:
        nova_imagem.paste(imagem, (0, pocicao_y))
        pocicao_y += imagem.height
    #retornar imagem.
    return nova_imagem

def adicionar_borda(lista_imagems, tamanho=10, cor=(0, 0, 0)):
    imagens_com_bordas = []
    # Para cada imagem na lista:
    # Garantir que a imagem esteja no modo RGBA
    # Definir o tamanho da borda.
    for imagem in lista_imagems:
        imagem = imagem.convert('RGBA')
        largura_total = imagem.width + tamanho * 2
        altura_total =  imagem.height + tamanho * 2
    # Criar uma nova imagem com a cor da borda e com as novas dimensões
        nova_imagem = Image.new('RGBA', (largura_total, altura_total), cor)
    # Colar a imagem original no centro da nova imagem
        nova_imagem.paste(imagem,(tamanho, tamanho))
        imagens_com_bordas.append(nova_imagem)
    # Retornar a lista de imagens com bordas
    return imagens_com_bordas
