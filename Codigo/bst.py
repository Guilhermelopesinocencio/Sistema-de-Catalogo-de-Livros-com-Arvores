from no import No
from collections import deque

class BST:
    def __init__(self):
        self.raiz = None
        self.comparacoes = 0  # usado para análise comparativa

    def inserir(self, raiz, livro):
        self.comparacoes += 1
        if raiz is None:
            return No(livro)
        if livro.id < raiz.livro.id:
            raiz.esq = self.inserir(raiz.esq, livro)
        elif livro.id > raiz.livro.id:
            raiz.dir = self.inserir(raiz.dir, livro)
        return raiz

    def adicionar(self, livro):
        self.raiz = self.inserir(self.raiz, livro)

    def buscar(self, raiz, id):
        self.comparacoes += 1
        if raiz is None or raiz.livro.id == id:
            return raiz
        if id < raiz.livro.id:
            return self.buscar(raiz.esq, id)
        return self.buscar(raiz.dir, id)

    def minimo(self, raiz):
        atual = raiz
        while atual.esq:
            atual = atual.esq
        return atual

    def remover(self, raiz, id):
        if raiz is None:
            return raiz
        if id < raiz.livro.id:
            raiz.esq = self.remover(raiz.esq, id)
        elif id > raiz.livro.id:
            raiz.dir = self.remover(raiz.dir, id)
        else:
            if raiz.esq is None:
                return raiz.dir
            elif raiz.dir is None:
                return raiz.esq
            temp = self.minimo(raiz.dir)
            raiz.livro = temp.livro
            raiz.dir = self.remover(raiz.dir, temp.livro.id)
        return raiz

    def deletar(self, id):
        self.raiz = self.remover(self.raiz, id)

    # Percursos
    def pre_ordem(self, raiz):
        res = []
        if raiz:
            res.append(raiz.livro)
            res += self.pre_ordem(raiz.esq)
            res += self.pre_ordem(raiz.dir)
        return res

    def in_ordem(self, raiz):
        res = []
        if raiz:
            res += self.in_ordem(raiz.esq)
            res.append(raiz.livro)
            res += self.in_ordem(raiz.dir)
        return res

    def pos_ordem(self, raiz):
        res = []
        if raiz:
            res += self.pos_ordem(raiz.esq)
            res += self.pos_ordem(raiz.dir)
            res.append(raiz.livro)
        return res

    def em_largura(self, raiz):
        res = []
        if raiz is None:
            return res
        fila = deque([raiz])
        while fila:
            atual = fila.popleft()
            res.append(atual.livro)
            if atual.esq:
                fila.append(atual.esq)
            if atual.dir:
                fila.append(atual.dir)
        return res
