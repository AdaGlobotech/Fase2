from estruturas_dados.fila import Fila
from estruturas_dados.arvore_binaria_busca import ArvoreBinariaBusca
from algoritmos.ordenacao import quick_sort

def demonstrar_fila():
    print("--- Demonstração da Fila (FIFO) ---")
    fila_de_tarefas = Fila()

    print("Enfileirando tarefas: 'Gerar a arvore', 'Abrir o LMS', 'Fazer Rubrica'")
    fila_de_tarefas.enfileirar("Gerar a arvore")
    fila_de_tarefas.enfileirar("Abrir o LMS")
    fila_de_tarefas.enfileirar("Fazer Rubrica")

    print(f"\nTamanho atual da fila: {len(fila_de_tarefas)}")

    print("\nProcessando tarefas na ordem de chegada:")
    while not fila_de_tarefas.esta_vazia():
        tarefa = fila_de_tarefas.desenfileirar()
        print(f"  -> Tarefa concluída: {tarefa}")
    
    print(f"\nTamanho final da fila: {len(fila_de_tarefas)}\n")


def demonstrar_arvore():
    print("--- Demonstração da Árvore de Busca Binária (BST) ---")
    arvore_usuarios = ArvoreBinariaBusca()

    print("Inserindo usuários com IDs (chaves): 10, 5, 15, 3, 7")
    arvore_usuarios.inserir(10, "Usuário Bernardo")
    arvore_usuarios.inserir(5, "Usuário Felipe")
    arvore_usuarios.inserir(15, "Usuário Iane")
    arvore_usuarios.inserir(3, "Usuário Ren")
    arvore_usuarios.inserir(7, "Usuário Augusta")

    print("\nBuscando pelo usuário com ID 7:")
    usuario_encontrado = arvore_usuarios.buscar(7)
    print(f"  -> Resultado da busca: {usuario_encontrado}")

    print("\nBuscando por um usuário inexistente (ID 99):")
    usuario_encontrado = arvore_usuarios.buscar(99)
    print(f"  -> Resultado da busca: {usuario_encontrado}")

    print("\nExibindo todos os usuários em ordem de ID (percurso_em_ordem):")
    lista_ordenada = arvore_usuarios.percurso_em_ordem()
    for usuario in lista_ordenada:
        print(f"  -> {usuario}")

def demonstrar_quicksort():
    """
    Função para demonstrar o uso do algoritmo quick_sort com diferentes chaves e ordens.
    """
    print("--- Demonstração do Algoritmo Quick Sort ---")
    
    # Exemplo de dados: uma lista de dicionários representando produtos
    produtos = [
        {'nome': 'Celular', 'preco': 2500, 'avaliacao': 4.5},
        {'nome': 'Notebook', 'preco': 4500, 'avaliacao': 4.8},
        {'nome': 'Fone de Ouvido', 'preco': 350, 'avaliacao': 4.2},
        {'nome': 'Teclado', 'preco': 150, 'avaliacao': 4.9},
        {'nome': 'Mouse', 'preco': 90, 'avaliacao': 4.7},
    ]

    print("Lista original de produtos:")
    for p in produtos:
        print(f"  -> {p}")

    # 1. Ordenando por preço, em ordem crescente (padrão)
    print("\n1. Ordenando por 'preco' (crescente):")
    produtos_por_preco = quick_sort(produtos, chave=lambda item: item['preco'])
    for p in produtos_por_preco:
        print(f"  -> {p}")

    # 2. Ordenando por avaliação, em ordem decrescente
    print("\n2. Ordenando por 'avaliacao' (decrescente):")
    produtos_por_avaliacao = quick_sort(produtos, chave=lambda item: item['avaliacao'], decrescente=True)
    for p in produtos_por_avaliacao:
        print(f"  -> {p}")
    print("")


if __name__ == "__main__":
    demonstrar_fila()
    print("="*50)
    demonstrar_arvore()
    print("="*50)
    demonstrar_quicksort()