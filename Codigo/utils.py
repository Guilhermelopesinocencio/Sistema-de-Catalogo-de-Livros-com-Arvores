from livro import Livro

def carregar_livros_csv(nome_arquivo):
    livros = []
    with open(nome_arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            partes = linha.strip().split(";")
            if len(partes) == 3:
                livros.append(Livro(int(partes[0]), partes[1], partes[2]))
    return livros
