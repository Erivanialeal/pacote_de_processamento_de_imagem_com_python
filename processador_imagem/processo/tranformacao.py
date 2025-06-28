from PIL import Image, ImageEnhance




def redimensionar_imagem(lista_imagens, largura, altura):
    imagens_redimensionadas = []
    #garantir que todas as imagens estejam no modo RGBA
    lista_imagens = [img.convert("RGBA") for img in lista_imagens]
    #redimensionar a imagem com base nos parametros fornecidos
    for imagem in lista_imagens:
        imagem_redimensionada = imagem.resize((largura, altura))
        imagens_redimensionadas.append(imagem_redimensionada)
    #retorna a lista de imagens resimencionadas
    return imagens_redimensionadas
def rotacionar_imagem(lista_imagens, angulo, expand= True):

    imagens_rotacionadas = []
    #percorre cada imagem em lista de imagens, convertendo para RGBA
    for imagem in lista_imagens:
        img= imagem.convert("RGBA")
        # rotaciona a imagem dentro da variavel img aplicando o angulo
        rotacionada=img.rotate(angulo, expand=expand)
        # a imagem já rotacionada adicionamos na lista de imagens rotacionada
        imagens_rotacionadas.append(rotacionada)
    # retornamos a lista de imagens rotacionadas
    return imagens_rotacionadas
def converter_para_tons_cinza(lista_imagens, modo="L"):
    # convertemos para o modo L pecorrendo uma por uma das imagens em lista_imagens
    return [imagem.convert(modo) for imagem in lista_imagens]
def espelhar_imagem(lista_imagens, modo='horizontal'):
    imagens_espelhada = []
    lista_imagens= [imagem.convert("RGBA") for imagem in lista_imagens]
    for imagem in lista_imagens:
        if modo == 'horizontal':
            espelhada=imagem.transpose(Image.FLIP_LEFT_RIGHT)
        elif modo == 'vertical':
            espelhada = imagem.transpose(Image.FLIP_TOP_BOTTOM)
        else:
            raise ValueError("Modo inválido. Use 'horizontal' ou 'vertical'")
        imagens_espelhada.append(espelhada)

    return imagens_espelhada

def ajustar_brilho(lista_imagens, fator):
    imagens_com_brilho = []
    
    for imagem in lista_imagens:
        imagem.convert("RGBA")
        realcador = ImageEnhance.Brightness(imagem)
        nova_imagem = realcador.enhance(fator)
        imagens_com_brilho.append(nova_imagem)
    return imagens_com_brilho


    
    