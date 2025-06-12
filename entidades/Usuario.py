from collections import Counter

class Usuario:
    def __init__(self, id_usuario):
        self.__id_usuario = int(id_usuario)
        self.__interacoes_realizadas = []

    @property # getter do atributo privado id_usuario
    def id_usuario(self):
        return self.__id_usuario

    @property # getter do atributo privado interacoes_realizadas
    def interacoes_realizadas(self):
        return list(self.__interacoes_realizadas)

    def registrar_interacao(self, interacao):
        self.__interacoes_realizadas.append(interacao)
            # incrementa a lista de interações feitas por esse usuário com um objeto da classe Interacao

    def obter_interacoes_por_tipo(self, tipo_desejado):
        return [i for i in self.__interacoes_realizadas if i.tipo_interacao == tipo_desejado]
            # list comprehension que devolve uma lista filtrando os objetos Interacao cujo tipo_interacao é do tipo desejado

    def obter_conteudos_unicos_consumidos(self):
        return set(i._Interacao__conteudo_associado for i in self.__interacoes_realizadas)
            # para cada objeto Interacao dentro da lista de interacoes_realizadas por esse usuário,
            # resgata o conteudo_associado a ele, e cria um set com todos eles,
            # o que pela definição do set já cria um conjunto de elementos únicos

    def calcular_tempo_total_consumo_plataforma(self, plataforma):
        return sum(i.watch_duration_seconds for i in self.__interacoes_realizadas
                   if i._Interacao__plataforma_interacao == plataforma)
            # percorre a lista de interacoes_realizadas por esse usuário,
            # junta em uma tupla o valor de watch_duration_seconds daquela interação caso seja da plataforma desejada,
            # e devolve a soma desse valores

    def plataformas_mais_frequentes(self, top_n=3):
        contagem = Counter(i._Interacao__plataforma_interacao for i in self.__interacoes_realizadas)
            # o método Counter do módulo collections cria um 
            # dicionário contendo cada plataforma das interações realizadas pelo usuário,
            # e quantas interações foram feitas para cada uma delas

        return [plataforma for plataforma, _ in contagem.most_common(top_n)]
            # retorna uma lista com as top_n (que por padrão vale 3) plataformas com as maiores frequências

    def __str__(self): # método pra exibição simples dos atributos da classe
        return f"Usuário {self.__id_usuario}"

    def __repr__(self): # método pra exibição mais técnica dos atributos da classe
        return f"<Usuario id={self.__id_usuario}, Interações:{self.__interacoes_realizadas}>"
