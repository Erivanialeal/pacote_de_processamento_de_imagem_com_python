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
├── ambiente_processador_imagem/
├── imagens/
│   ├── imagem1.jpg
│   ├── imagem2.jpg
│   ├── imagem3.jpg
│   └── imagem4.jpg
├── processador_imagem/
│   ├── __init__.py
│   ├── processo/
│   │   ├── __init__.py
│   │   ├── combinação.py
│   │   └── transformação.py
│   └── utils/
│       ├── io.py
│       └── plot.py
├── testes/
│   ├── grade.png
│   ├── saida_juntar_lado_a_lado.png
│   └── saida_visualização.png
├── teste_juntar_lado_a_lado.py
├── teste_juntar_em_grade.py
├── .gitignore
├── README.md
├── requirements.txt
└── setup.py
