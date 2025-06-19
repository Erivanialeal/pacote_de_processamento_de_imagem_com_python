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
def sobrepor_simples(imagem1, imagem2, alpha=0.5):
    pass

def juntar_verticalmente(imagem1, imagem2):
    pass

def adicionar_borda(imagem, tamanho=10, cor=(0, 0, 0)):
    pass
