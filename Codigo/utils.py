from livro import Livro

def carregar_livros_csv(nome_arquivo):
    livros = []
    with open(nome_arquivo, "r", encoding="utf-8") as f:
        for i, linha in enumerate(f):
            # Ignora cabeçalho, caso exista
            if i == 0 and not linha[0].isdigit():
                continue
            partes = linha.strip().split(";")
            if len(partes) == 3:
                try:
                    livros.append(Livro(int(partes[0]), partes[1], partes[2]))
                except ValueError:
                    pass
    return livros
