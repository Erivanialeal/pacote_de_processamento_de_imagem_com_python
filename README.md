# pacote_de_processamento_de_imagem_com_python
Pequeno projeto da plataforma  DIO do Bootcamp  Suzano - Python Developer

# 📦 processador_imagem

Pacote Python simples para processamento de imagens, com foco em combinações visuais. Criado com o objetivo de aprendizado e prática em manipulação de imagens utilizando a biblioteca Pillow.

---

## ✅ Funcionalidades até agora

### 1. `juntar_lado_a_lado(imagem1, imagem2)`
Une duas imagens horizontalmente, mantendo as alturas alinhadas.

### 2. `juntar_em_grade(lista_de_imagens, linhas, colunas)`
Organiza uma lista de imagens em uma grade (ex: 2x2), formando uma nova imagem composta.

### 3. `sobrepor_imagens(imagem1, imagem2, alpha=0.5)`
Combina duas imagens aplicando transparência na imagem de cima.A imagem1 fica sobre a imagem2. Quanto menor o alpha, mais transparente ela fica.

### 4. `juntar_verticalmente(lista_imagens):`
Junta uma imagem embaixo da outra


---

## 📂 Estrutura do projeto
| Arquivo/Pasta                         | Tipo              | Descrição                                      |
|--------------------------------------|-------------------|------------------------------------------------|
| ambiente_processador_imagem/         | Pasta             | Ambiente virtual local (não versionado)        |
| imagens/                              | Pasta             | Imagens de entrada para os testes              |
| ├── imagem1.jpg                      | Arquivo de imagem | Imagem de exemplo                              |
| ├── imagem2.jpg                      | Arquivo de imagem | Imagem de exemplo                              |
| ├── imagem3.jpg                      | Arquivo de imagem | Imagem de exemplo                              |
| └── imagem4.jpg                      | Arquivo de imagem | Imagem de exemplo                              |
| processador_imagem/                  | Pacote Python     | Pacote principal                               |
| ├── __init__.py                      | Arquivo Python    | Inicializa o pacote                            |
| ├── processo/                        | Subpacote         | Funções de processamento de imagem             |
| │   ├── __init__.py                  | Arquivo Python    | Inicializa o subpacote                         |
| │   ├── combinação.py                | Arquivo Python    | Funções de combinação de imagens               |
| │   └── transformação.py             | Arquivo Python    | Transformações (em breve)                      |
| └── utils/                           | Subpacote         | Utilitários (em breve)                         |
|     ├── io.py                        | Arquivo Python    | Entrada e saída de imagens                     |
|     └── plot.py                      | Arquivo Python    | Visualização de imagens                        |
| testes/                               | Pasta             | Saída dos testes realizados                    |
| ├── grade.png                        | Imagem gerada     | Resultado da função de grade                   |
| ├── saida_juntar_lado_a_lado.png    | Imagem gerada     | Resultado da função de junção lado a lado      |
| └── saida_visualização.png          | Imagem gerada     | Resultado de visualização                      |
| teste_juntar_lado_a_lado.py          | Arquivo Python    | Script de teste da função lado a lado          |
| teste_juntar_em_grade.py             | Arquivo Python    | Script de teste da função em grade             |
| .gitignore                            | Arquivo texto     | Arquivos/pastas ignoradas pelo Git             |
| README.md                             | Markdown          | Documentação do projeto                        |
| requirements.txt                      | Arquivo texto     | Lista de bibliotecas necessárias               |
| setup.py                              | Arquivo Python    | Script de configuração do pacote               |

