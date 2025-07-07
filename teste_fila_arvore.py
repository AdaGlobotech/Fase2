from estruturas_dados.fila import Fila
from estruturas_dados.arvore_binaria_busca import ArvoreBinariaBusca

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

if __name__ == "__main__":
    demonstrar_fila()
    print("="*50)
    demonstrar_arvore()