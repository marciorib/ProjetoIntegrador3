# Projeto Integrador III — Busca Inteligente de Arquivos

## Objetivo

Este projeto tem como objetivo melhorar a experiência do usuário na busca e visualização de manuais. A aplicação permite ao usuário cadastrar, visualizar e interagir com manuais diretamente pelo navegador, utilizando uma interface simples e integrada a uma IA que responde perguntas sobre o conteúdo.

## Fluxo da aplicação:
1. O usuário acessa a interface web via navegador.
2. Pode cadastrar novos manuais no sistema.
3. Visualiza o conteúdo diretamente sem baixar arquivos.
4. Realiza perguntas em linguagem natural sobre um manual específico.
5. O backend utiliza o modelo BERT (IA) para encontrar e exibir a resposta mais relevante com base no conteúdo do manual.

## Processamento:
- A pergunta e o conteúdo do manual são processados com o modelo **BERT (`bert-base-uncased`)**.
- O texto do manual é dividido em blocos de até 512 tokens para garantir compatibilidade com o modelo.
- A resposta de maior relevância é retornada ao usuário, com base nas pontuações calculadas pelo modelo.

## Tecnologias utilizadas:
- **Flask** – Framework web para construção da aplicação.
- **SQLite** – Banco de dados leve e local para armazenar os manuais.
- **Transformers (HuggingFace)** – Para uso do modelo pré-treinado BERT.
- **PyTorch** – Biblioteca usada para inferência com o modelo de IA.

## Como Executar
1. Clone este repositório:
   ```bash
   git clone https://github.com/marciorib/ProjetoIntegrador3

2. Instale as dependencias:
   ```bash
   pip install -r requirements.txt


3. Inicialize o banco de dados e execute o app:
   ```bash
   python app.py
   
4. Acesse no navegador:
    ```bash
    http://localhost:5000/

## Funcionalidades

    📥 Cadastrar manuais (/cadastrar_manual)

    📖 Visualizar conteúdo dos manuais (/manual/<nome>)

    ❓ Perguntar sobre o conteúdo com IA (/pergunta)

    📄 Páginas auxiliares para manuais em construção

