class ArvoreBinariaBusca:
    """
    Implementa uma Árvore de Busca Binária (Binary Search Tree - BST).
    A árvore armazena pares de chave-valor e permite busca, inserção e remoção eficientes.
    O valor pode ser qualquer objeto (neste caso, objetos Conteudo ou Usuario).
    """

    # Classe interna para representar um nó da árvore
    class _No:
        def __init__(self, chave, valor):
            self.chave = chave
            self.valor = valor
            self.esquerda = None
            self.direita = None

    def __init__(self):
        """
        Inicializa a árvore com a raiz como None.
        """
        self.raiz = None

    def inserir(self, chave, valor):
        # Complexidade de Tempo:
        # - Caso Médio (árvore balanceada): O(log n)
        # - Pior Caso (árvore degenerada): O(n)
        self.raiz = self._inserir_recursivo(self.raiz, chave, valor)

    def _inserir_recursivo(self, no_atual, chave, valor):
        """
        Método privado e recursivo para encontrar a posição e inserir o novo nó.
        """
        if no_atual is None:
            return self._No(chave, valor)
        
        if chave < no_atual.chave:
            no_atual.esquerda = self._inserir_recursivo(no_atual.esquerda, chave, valor)
        elif chave > no_atual.chave:
            no_atual.direita = self._inserir_recursivo(no_atual.direita, chave, valor)
        else:
            # Se a chave já existe, apenas atualiza o valor
            no_atual.valor = valor
        
        return no_atual

    def buscar(self, chave):
        """
        Método público para buscar um valor associado a uma chave.
        Retorna o valor ou None se a chave não for encontrada.
        Complexidade de Tempo:
        - Caso Médio (árvore balanceada): O(log n)
        - Pior Caso (árvore degenerada): O(n)
        """
        no = self._buscar_recursivo(self.raiz, chave)
        return no.valor if no else None

    def _buscar_recursivo(self, no_atual, chave):
        """
        Método privado e recursivo para buscar um nó pela chave.
        """
        if no_atual is None or no_atual.chave == chave:
            return no_atual
        
        if chave < no_atual.chave:
            return self._buscar_recursivo(no_atual.esquerda, chave)
        else:
            return self._buscar_recursivo(no_atual.direita, chave)

    def remover(self, chave):
        """
        Método público para remover um nó da árvore pela chave.
        """
        self.raiz = self._remover_recursivo(self.raiz, chave)

    def _remover_recursivo(self, no_atual, chave):
        """
        Método privado e recursivo para encontrar e remover um nó.
        """
        if no_atual is None:
            return no_atual # Chave não encontrada
        
        if chave < no_atual.chave:
            no_atual.esquerda = self._remover_recursivo(no_atual.esquerda, chave)
        elif chave > no_atual.chave:
            no_atual.direita = self._remover_recursivo(no_atual.direita, chave)
        else: # Nó a ser removido encontrado
            # Caso 1: Nó com 0 ou 1 filho
            if no_atual.esquerda is None:
                return no_atual.direita
            elif no_atual.direita is None:
                return no_atual.esquerda
            
            # Caso 2: Nó com 2 filhos
            # Encontra o sucessor em ordem (menor nó da sub-árvore direita)
            sucessor = self._encontrar_minimo(no_atual.direita)
            no_atual.chave = sucessor.chave
            no_atual.valor = sucessor.valor
            # Remove o nó sucessor que foi copiado
            no_atual.direita = self._remover_recursivo(no_atual.direita, sucessor.chave)
            
        return no_atual

    def _encontrar_minimo(self, no):
        """
        Encontra o nó com a menor chave em uma sub-árvore (o nó mais à esquerda).
        """
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def percurso_em_ordem(self) -> list:
        """
        Retorna uma lista de todos os valores (objetos) na árvore,
        ordenados pela chave.

        Complexidade de Tempo: O(n), pois precisa visitar todos os nós.
        Complexidade de Espaço: O(n) para a lista de resultado.
        """
        resultado = []
        self._percurso_em_ordem_recursivo(self.raiz, resultado)
        return resultado

    def _percurso_em_ordem_recursivo(self, no_atual, resultado):
        """
        Percorre a árvore recursivamente no padrão "em ordem" (esquerda, raiz, direita).
        """
        if no_atual is not None:
            self._percurso_em_ordem_recursivo(no_atual.esquerda, resultado)
            resultado.append(no_atual.valor)
            self._percurso_em_ordem_recursivo(no_atual.direita, resultado)

    def __str__(self):
        """
        Retorna uma representação em string da árvore (percurso em ordem).
        """
        return str(self.percurso_em_ordem())