from no import No
from collections import deque

class AVL:
    def __init__(self):
        self.raiz = None
        self.comparacoes = 0
        self.rotacoes = 0

    def altura(self, no):
        if not no:
            return 0
        return no.altura

    def fator_balanceamento(self, no):
        if not no:
            return 0
        return self.altura(no.esq) - self.altura(no.dir)

    # Rotações
    def rotacao_direita(self, y):
        self.rotacoes += 1
        x = y.esq
        T2 = x.dir
        x.dir = y
        y.esq = T2
        y.altura = 1 + max(self.altura(y.esq), self.altura(y.dir))
        x.altura = 1 + max(self.altura(x.esq), self.altura(x.dir))
        return x

    def rotacao_esquerda(self, x):
        self.rotacoes += 1
        y = x.dir
        T2 = y.esq
        y.esq = x
        x.dir = T2
        x.altura = 1 + max(self.altura(x.esq), self.altura(x.dir))
        y.altura = 1 + max(self.altura(y.esq), self.altura(y.dir))
        return y

    # Inserção com balanceamento
    def inserir(self, raiz, livro):
        self.comparacoes += 1
        if not raiz:
            return No(livro)
        if livro.id < raiz.livro.id:
            raiz.esq = self.inserir(raiz.esq, livro)
        elif livro.id > raiz.livro.id:
            raiz.dir = self.inserir(raiz.dir, livro)
        else:
            return raiz

        raiz.altura = 1 + max(self.altura(raiz.esq), self.altura(raiz.dir))
        fb = self.fator_balanceamento(raiz)

        # LL
        if fb > 1 and livro.id < raiz.esq.livro.id:
            return self.rotacao_direita(raiz)
        # RR
        if fb < -1 and livro.id > raiz.dir.livro.id:
            return self.rotacao_esquerda(raiz)
        # LR
        if fb > 1 and livro.id > raiz.esq.livro.id:
            raiz.esq = self.rotacao_esquerda(raiz.esq)
            return self.rotacao_direita(raiz)
        # RL
        if fb < -1 and livro.id < raiz.dir.livro.id:
            raiz.dir = self.rotacao_direita(raiz.dir)
            return self.rotacao_esquerda(raiz)

        return raiz

    def adicionar(self, livro):
        self.raiz = self.inserir(self.raiz, livro)

    # Busca
    def buscar(self, raiz, id):
        self.comparacoes += 1
        if raiz is None or raiz.livro.id == id:
            return raiz
        if id < raiz.livro.id:
            return self.buscar(raiz.esq, id)
        return self.buscar(raiz.dir, id)

    # Remoção com rebalanceamento
    def minimo(self, raiz):
        atual = raiz
        while atual.esq:
            atual = atual.esq
        return atual

    def remover(self, raiz, id):
        if not raiz:
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

        if not raiz:
            return raiz

        raiz.altura = 1 + max(self.altura(raiz.esq), self.altura(raiz.dir))
        fb = self.fator_balanceamento(raiz)

        # LL
        if fb > 1 and self.fator_balanceamento(raiz.esq) >= 0:
            return self.rotacao_direita(raiz)
        # LR
        if fb > 1 and self.fator_balanceamento(raiz.esq) < 0:
            raiz.esq = self.rotacao_esquerda(raiz.esq)
            return self.rotacao_direita(raiz)
        # RR
        if fb < -1 and self.fator_balanceamento(raiz.dir) <= 0:
            return self.rotacao_esquerda(raiz)
        # RL
        if fb < -1 and self.fator_balanceamento(raiz.dir) > 0:
            raiz.dir = self.rotacao_direita(raiz.dir)
            return self.rotacao_esquerda(raiz)

        return raiz

    def deletar(self, id):
        self.raiz = self.remover(self.raiz, id)

    # Percursos
    def in_ordem(self, raiz):
        res = []
        if raiz:
            res += self.in_ordem(raiz.esq)
            res.append(raiz.livro)
            res += self.in_ordem(raiz.dir)
        return res

    def pre_ordem(self, raiz):
        res = []
        if raiz:
            res.append(raiz.livro)
            res += self.pre_ordem(raiz.esq)
            res += self.pre_ordem(raiz.dir)
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
