from PIL import Image
import os



def carregar_imagens(caminho):
    imagens = []
    for caminho in caminho:
        imagem = Image.open(caminho)
        imagens.append(imagem)
    return imagens

def carregar_imagens_de_pastas(caminho_pasta):
    imagens = []
    listar = os.listdir(caminho_pasta)
    for arquivo in listar:
        nome,extensao = os.path.splitext(arquivo)
        if extensao.lower() in (".jpg", ".jpeg", ".png", ".bmp", ".gif"):
            caminho_completo = os.path.join(caminho_pasta, arquivo)
            imagens.append(Image.open(caminho_completo))
    return imagens

def salvar_imagens(lista_imagens, pasta_destino,nome_base='imagem'):
    # verificar se a pasta existe
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
    #interar sobre cada imagem salvando cada uma como um número unico
    for i, imagem in enumerate(lista_imagens, start= 1):
        nome_arquivo= f"{nome_base}_{i}.png"
        caminho_completo =os.path.join(pasta_destino,nome_arquivo)
        #salvar imagem no camilho definido.
        imagem.save(caminho_completo)
def salvar_uma_imagem(imagem,caminho):
    imagem.save(caminho)
    print(f"Imagem salva com sucesso em {caminho}")
def criar_pasta_se_nao_existir(pasta):
    if not os.path.exists(pasta):
        os.makedirs(pasta)
