"""
enfileirar: O(1)

desenfileirar: O(n) (devido ao pop(0))

esta_vazia: O(1)

    """


class Fila:
    def __init__(self):
        self.__dados = []

    def enfileirar(self, item):
        self.__dados.append(item)  # O(1)

    def desenfileirar(self):
        if not self.esta_vazia():
            return self.__dados.pop(0)  # O(n), mas aceitável para listas pequenas
        return None

    def esta_vazia(self):
        return len(self.__dados) == 0

    def __len__(self):
        return len(self.__dados)

    def __str__(self):
        return f"Fila({self.__dados})"
