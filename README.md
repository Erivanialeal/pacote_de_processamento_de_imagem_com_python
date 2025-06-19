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

---

## 📂 Estrutura do projeto

pacote_de_processamento_de_imagem_com_python/
├── ambiente_processador_imagem/              # Ambiente virtual (não é versionado no Git)
│
├── imagens/                                   # Imagens usadas como entrada nos testes
│   ├── imagem1.jpg
│   ├── imagem2.jpg
│   ├── imagem3.jpg
│   └── imagem4.jpg
│
├── processador_imagem/                        # Pacote principal do projeto
│   ├── __init__.py
│   ├── processo/
│   │   ├── __init__.py
│   │   ├── combinação.py                      # Funções de junção (lado a lado, em grade, etc.)
│   │   └── transformação.py                   # (em breve) funções de transformação de imagem
│   └── utils/
│       ├── io.py                              # (em breve) carregamento e salvamento
│       └── plot.py                            # (em breve) visualização de imagens
│
├── testes/                                    # Resultados gerados pelos testes (imagens combinadas)
│   ├── grade.png
│   ├── sai

