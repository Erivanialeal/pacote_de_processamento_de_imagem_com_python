import matplotlib
matplotlib.use("Agg")  # Backend sem interface gráfica
from PIL import Image # Chamando a PIL para manipulação de imagens
import matplotlib.pyplot as plt

# 1. Carregar a imagem
imagem= Image.open("imagens/imagem1.jpg") 

# 2. Mostrar a imagem
plt.imshow(imagem)
plt.title('Imagem 1 casa')
plt.axis('off')  # Desativa os eixos
plt.savefig("testes/saida_visualizacao.png") 
print("Imagem salva como 'testes/saida_visualizacao.png'")