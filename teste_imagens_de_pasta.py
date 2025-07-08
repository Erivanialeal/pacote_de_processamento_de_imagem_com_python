from PIL import Image
from processador_imagem.utils.io import carregar_imagens_de_pastas

# camilho da pasta onde as imagens estão localizadas
caminho_pasta = "imagens"
pasta= carregar_imagens_de_pastas(caminho_pasta)
for i, img in enumerate(pasta, start=1):
    print(f"Imagem {i}: tamanho = {img.size}, modo = {img.mode}")
    