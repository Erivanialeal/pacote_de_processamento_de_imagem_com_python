import matplotlib.pyplot as plt



def exibir_imagem(imagem):
    
    nova_figura= plt.figure(figsize=(10, 5))
    plt.imshow(imagem)
    plt.axis("off")
    # plt.show só funciona em ambientes Tkinter
    plt.show()
    pass
def exibir_varias_imagens(lista_imagens):
    total = len(lista_imagens)
    figura, axs = plt.subplots(1, total, figsize=(5* total, 5))
    # se houver apenas uma imagem axs não será uma lista
    if total == 1:
        axs = [axs]
    for i, imagem in enumerate(lista_imagens):
        axs[i].imshow(imagem)
        axs[i].axis('off') #remover os eixos

    plt.tight_layout()#ajustar o espaçamento
    plt.show()
def comparar_imagens(lista_imagens):
    quantidade = len(lista_imagens)
    figura,axs = plt.subplots(nrows= 1, ncols= quantidade, figsize=(5 * quantidade, 5))
    if quantidade == 1:
        axs=[axs]
    for i, imagem in enumerate(lista_imagens):
        axs[i].imshow(imagem)
        axs[i].axis('off') #remover os eixos

    plt.tight_layout()#ajustar o espaçamento
    plt.show()
