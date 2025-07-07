def quick_sort(lista: list, chave, decrescente: bool = False):
    """
    Ordena uma lista de objetos utilizando o algoritmo Quick Sort.

    Args:
        lista (list): A lista a ser ordenada.
        chave (function): Uma função lambda para extrair o valor de comparação de cada objeto.
        decrescente (bool): Se True, ordena em ordem decrescente. Se False, em ordem crescente.

    Complexidade de Tempo:
    - Caso Médio: O(n log n)
    - Pior Caso: O(n^2) (ocorre se o pivô for consistentemente o menor/maior elemento)
    Complexidade de Espaço (pilha de recursão):
    - Caso Médio: O(log n)
    - Pior Caso: O(n)
    """
    if len(lista) < 2:
        return lista
    else:
        pivo = lista[0]
        pivo_valor = chave(pivo)

        if decrescente:
            menores = [i for i in lista[1:] if chave(i) >= pivo_valor]
            maiores = [i for i in lista[1:] if chave(i) < pivo_valor]
        else:
            menores = [i for i in lista[1:] if chave(i) <= pivo_valor]
            maiores = [i for i in lista[1:] if chave(i) > pivo_valor]

        return quick_sort(menores, chave, decrescente) + [pivo] + quick_sort(maiores, chave, decrescente)