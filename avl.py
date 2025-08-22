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

# percurso

    def in_ordem(self, raiz):
        if raiz:
            self.in_ordem(raiz.esq)
            print(raiz.livro)
            self.in_ordem(raiz.dir)

    def pre_ordem(self, raiz):
        if raiz:
            print(raiz.livro)
            self.pre_ordem(raiz.esq)
            self.pre_ordem(raiz.dir)

    def pos_ordem(self, raiz):
        if raiz:
            self.pos_ordem(raiz.esq)
            self.pos_ordem(raiz.dir)
            print(raiz.livro)

    def em_largura(self, raiz):
        if raiz is None:
            return
        fila = deque([raiz])
        while fila:
            atual = fila.popleft()
            print(atual.livro)
            if atual.esq:
                fila.append(atual.esq)
            if atual.dir:
                fila.append(atual.dir)
