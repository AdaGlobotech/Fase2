
class Node:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.esq = None
        self.dir = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    # inserção padrão de BST
    def inserir(self, chave, valor):
        self.raiz = self._inserir_rec(self.raiz, chave, valor)

    def _inserir_rec(self, no, chave, valor):
        if no is None:
            return Node(chave, valor)
        if chave < no.chave:
            no.esq = self._inserir_rec(no.esq, chave, valor)
        elif chave > no.chave:
            no.dir = self._inserir_rec(no.dir, chave, valor)
        else:
            no.valor = valor
        return no

    # busca
    def buscar(self, chave):
        return self._buscar_rec(self.raiz, chave)

    def _buscar_rec(self, no, chave):
        if no is None or no.chave == chave:
            return no.valor if no else None
        if chave < no.chave:
            return self._buscar_rec(no.esq, chave)
        return self._buscar_rec(no.dir, chave)

    # remoção (casos padrão de BST)
    def remover(self, chave):
        self.raiz = self._remover_rec(self.raiz, chave)

    def _remover_rec(self, no, chave):
        if no is None:
            return None
        if chave < no.chave:
            no.esq = self._remover_rec(no.esq, chave)
        elif chave > no.chave:
            no.dir = self._remover_rec(no.dir, chave)
        else:
            # no com um ou nenhum filho
            if no.esq is None:
                return no.dir
            if no.dir is None:
                return no.esq
            sucessor = self._menor_valor(no.dir)
            no.chave, no.valor = sucessor.chave, sucessor.valor
            no.dir = self._remover_rec(no.dir, sucessor.chave)
        return no

    def _menor_valor(self, no):
        atual = no
        while atual.esq is not None:
            atual = atual.esq
        return atual

    # percurso em ordem (in-order) para listar em chave crescente
    def percurso_em_ordem(self):
        resultado = []
        self._in_order(self.raiz, resultado)
        return resultado

    def _in_order(self, no, lista):
        if no:
            self._in_order(no.esq, lista)
            lista.append(no.valor)
            self._in_order(no.dir, lista)
