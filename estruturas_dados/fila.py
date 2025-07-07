import collections

class Fila:
    
    def __init__(self):
        self._dados = collections.deque()

    def enfileirar(self, item):
        # Complexidade de Tempo: O(1), pois append em deque é constante.
        self._dados.append(item)

    def desenfileirar(self):
        # Complexidade de Tempo: O(1), pois popleft em deque é constante.
        if self.esta_vazia():
            raise IndexError("Não é possível desenfileirar de uma fila vazia.")
        return self._dados.popleft()

    def esta_vazia(self) -> bool:
        # Complexidade de Tempo: O(1).
        return len(self._dados) == 0

    def __len__(self) -> int:
        return len(self._dados)