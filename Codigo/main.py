from livro import Livro
from bst import BST
from avl import AVL
from utils import carregar_livros_csv


def menu():
    bst = BST()
    avl = AVL()

    while True:
        print("\n===== Catálogo de Livros =====")
        print("1 - Inserir livro manualmente")
        print("2 - Carregar livros de arquivo")
        print("3 - Buscar livro por ID (BST)")
        print("4 - Remover livro (BST)")
        print("5 - Listar livros (BST)")
        print("6 - Listar livros (AVL)")
        print("7 - Comparar BST vs AVL")
        print("0 - Sair")
        op = input("Escolha uma opção: ")

        if op == "1":
            id = int(input("ID: "))
            titulo = input("Título: ")
            autor = input("Autor: ")
            livro = Livro(id, titulo, autor)
            bst.adicionar(livro)
            avl.adicionar(livro)

        elif op == "2":
            nome = input("Nome do arquivo (ex: livros.csv): ")
            livros = carregar_livros_csv(nome)
            for l in livros:
                bst.adicionar(l)
                avl.adicionar(l)
            print("Livros carregados com sucesso!")

        elif op == "3":
            id = int(input("Digite o ID para buscar: "))
            no = bst.buscar(bst.raiz, id)
            print(no.livro if no else "Livro não encontrado.")

        elif op == "4":
            id = int(input("Digite o ID para remover: "))
            bst.deletar(id)
            print("Removido na BST (AVL não implementa remoção).")

        elif op == "5":
            print("\n--- BST ---")
            print("1 - Pré-Ordem\n2 - In-Ordem\n3 - Pós-Ordem\n4 - Em Largura")
            sub = input("Escolha: ")
            if sub == "1":
                bst.pre_ordem(bst.raiz)
            elif sub == "2":
                bst.in_ordem(bst.raiz)
            elif sub == "3":
                bst.pos_ordem(bst.raiz)
            elif sub == "4":
                bst.em_largura(bst.raiz)

        elif op == "6":
            print("\n--- AVL ---")
            print("1 - Pré-Ordem\n2 - In-Ordem\n3 - Pós-Ordem\n4 - Em Largura")
            sub = input("Escolha: ")
            if sub == "1":
                avl.pre_ordem(avl.raiz)
            elif sub == "2":
                avl.in_ordem(avl.raiz)
            elif sub == "3":
                avl.pos_ordem(avl.raiz)
            elif sub == "4":
                avl.em_largura(avl.raiz)

        elif op == "7":
            print(f"Comparações BST: {bst.comparacoes}")
            print(f"Comparações AVL: {avl.comparacoes}")
            print(f"Rotações AVL: {avl.rotacoes}")

        elif op == "0":
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
