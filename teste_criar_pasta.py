import os
from processador_imagem.utils.io import criar_pasta_se_nao_existir
#passar o caminho
pasta="testes/teste_pasta_tem"

#chamar a função
criar_pasta_se_nao_existir(pasta)
#verificar se a pasta foi criada
if os.path.exists(pasta):
    print(f"pasta criada com sucesso: {pasta}")
else:
    print("Erro, a pasta não foi criada.")