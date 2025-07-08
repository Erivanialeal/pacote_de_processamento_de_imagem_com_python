from PIL import Image
from processador_imagem.utils.io import carregar_imagens


camilho = [
    "imagens/imagem1.jpg"
]

imagens = carregar_imagens(camilho)
for i, img in enumerate(imagens, start= 1):
    print(f"Imagem {i}: tamanho = {img.size}, modo = {img.mode}")