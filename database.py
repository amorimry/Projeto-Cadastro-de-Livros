import json
import os

ARQUIVO = "dados_livros.json"

def carregar_livros():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo_json:
        return json.load(arquivo_json)

def salvar_livro(lista_livros):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(lista_livros, arquivo, indent=4, ensure_ascii=False)

def adicionar_livro(titulo, autor, ano):
    livros = carregar_livros()
    novo_livro = {
        "título": titulo,
        "autor": autor,
        "ano": ano
    }
    livros.append(novo_livro)
    salvar_livro(livros)

def atualizar_livro(indice, titulo, autor, ano):
    livros = carregar_livros()
    livros[indice] = {
        "título": titulo,
        "autor": autor,
        "ano": ano
    }
    salvar_livro(livros)

def excluir_livro(indice):
    livros = carregar_livros()
    if 0 <= indice < len(livros):
        livros.pop(indice)
        salvar_livro()
