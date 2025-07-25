class Plataforma:
    def __init__(self, nome_plataforma, id_plataforma = None):
        # Se o nome for vazio ou só espaço em branco, já é levantado erro e o programa é interrompido
        if not nome_plataforma or not nome_plataforma.strip():
            raise ValueError("O nome da plataforma não pode estar vazio.")

        # Guarda o nome limpo (sem espaços antes ou depois)
        self.__nome_plataforma = nome_plataforma.strip()

        # O ID da plataforma é opcional, pode ser gerado depois pelo sistema
        self.__id_plataforma = id_plataforma

    # A partir daqui, estou usando property pra acessar os atributos de forma segura
    @property # getter do atributo privado id_plataforma
    def id_plataforma(self):
        return self.__id_plataforma

    @id_plataforma.setter
    def id_plataforma(self, valor):
        # Por enquanto não será colocada nenhuma validação no ID
        self.__id_plataforma = valor

    @property # getter do atributo privado nome_plataforma
    def nome_plataforma(self):
        return self.__nome_plataforma

    @nome_plataforma.setter
    def nome_plataforma(self, valor):
        # Toda vez que alguém tentar mudar o nome, também será verificado se está válido
        if not valor or not valor.strip():
            raise ValueError("O nome da plataforma não pode estar vazio.")
        self.__nome_plataforma = valor.strip()

    # Esse método serve pra quando se usar print(plataforma)
    # Vai aparecer só o nome da plataforma, sem os detalhes técnicos
    def __str__(self):
        return self.__nome_plataforma

    # Aqui é uma versão mais técnica, útil pra debug ou no terminal
    def __repr__(self):
        return f"Plataforma(nome='{self.__nome_plataforma}')"

    # Permite que a gente compare duas plataformas com ==
    # Por padrão, o nome é comparado
    def __eq__(self, other):
        if isinstance(other, Plataforma):
            return self.nome_plataforma.lower() == other.nome_plataforma.lower() #mantém a comparação em minúsculas
        return False

    # Com esse método, dá pra usar Plataforma como chave em dicionário ou dentro de um set
    def __hash__(self):
        return hash(self.nome_plataforma.lower()) #mantém o hash do nome em minúsculas
        # Isso garante que "Globoplay" e "globoplay" sejam considerados iguais
        # e tenham o mesmo hash, facilitando a comparação e armazenamento.