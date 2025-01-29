# Pre-requisitos locais (Ubuntu 24.04.1 LTS)
- python 3.12
- python3-pip
- python3-venv

# Primeiros passos

## Instalação do virtualenv
1. Cria o virtualenv: make enable_venv
2. Habilita o virtualenv: source .venv/bin/activate

## Execução
### No arquivo Makefile o primeiro parametro indica o numero maximo de artigos
1. Run make install: make install <max_articles>

## Validação
1. O comando 'make quality' roda todos os hooks de validação do pre-commit.

## Para criar o arquivo output.csv
1. make run

# Link para o repositório
https://github.com/aexpedito/web-scrapper
