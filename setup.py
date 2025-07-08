

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    page_description = f.read()

setup(
    name="pacote_de_processamento_de_imagem_com_python",
    version="0.0.1",
    author="Erivania Leal De Souza",
    author_email="erivanial.s1507@gmail.com",
    description="Processador de imagem simples, criado para fins educativos apenas",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Erivanialeal/pacote_de_processamento_de_imagem_com_python.git",
    packages=find_packages(),
    install_requires=[
        "contourpy==1.3.2",
        "cycler==0.12.1",
        "fonttools==4.58.4",
        "kiwisolver==1.4.8",
        "matplotlib==3.10.3",
        "numpy==2.3.0",
        "packaging==25.0",
        "pillow==11.2.1",
        "pyparsing==3.2.3",
        "python-dateutil==2.9.0.post0",
        "setuptools==80.9.0",
        "six==1.17.0"
    ],
    python_requires=">=3.8",
)
