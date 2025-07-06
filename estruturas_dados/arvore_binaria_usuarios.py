
class ArvoreBinariaUsuarios:
    def __init__(self):
        # A árvore interna que armazenará os usuários
        self.arvore_usuarios = ArvoreBinariaBusca()

    def inserir_usuario(self, usuario):
        """
        Adiciona um objeto Usuario à árvore usando o atributo id_usuario como chave
        Se um usuário com o mesmo ID já existir na árvore, ele será atualizado
        """

        if not isinstance(usuario, Usuario):
            raise TypeError("O objeto a ser inserido deve ser um objeto da classe Usuario.")
        
        # A chave é o id_usuario, o valor é o próprio objeto Usuario
        self.arvore_usuarios.inserir(usuario.id_usuario, usuario)
        print(f"Usuário {usuario.nome} (ID: {usuario.id_usuario}) inserido/atualizado.")

    def buscar_usuario(self, id_usuario):
        """
        Busca e retorna um objeto Usuario pelo seu id_usuario
        Retorna None se o usuário não for encontrado
        """

        if not isinstance(id_usuario, int):
            raise TypeError("O ID do usuário deve ser um número inteiro.")
            
        usuario_encontrado = self.arvore_usuarios.buscar(id_usuario)
        if usuario_encontrado:
            print(f"Usuário com ID {id_usuario} encontrado: {usuario_encontrado.nome}")
        else:
            print(f"Usuário com ID {id_usuario} não encontrado.")
        return usuario_encontrado

    def remover_usuario(self, id_usuario):
        """
        Remove um Usuario da árvore puxando pelo seu id_usuario
        """

        if not isinstance(id_usuario, int):
            raise TypeError("O ID do usuário a ser removido deve ser um número inteiro.")
        
        if self.buscar_usuario(id_usuario):
            self.arvore_usuarios.remover(id_usuario)
            print(f"Usuário com ID {id_usuario} removido com sucesso.")
        else:
            print(f"Não foi possível remover: Usuário com ID {id_usuario} não encontrado.")

    # Método para listar todos os usuários em ordem de ID
    def listar_usuarios_em_ordem(self):
        """
        Lista todos os usuários na árvore em ordem crescente de ID.
        """

        print("\n--- Usuários na árvore (ordenados por ID) ---")
        usuarios = self.arvore_usuarios.percurso_em_ordem()
        if not usuarios:
            print("Nenhum usuário na árvore.")
        for user in usuarios:
            print(user)
