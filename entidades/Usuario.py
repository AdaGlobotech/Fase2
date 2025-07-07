from collections import Counter

from entidades import Interacao
from entidades.Plataforma import Plataforma

class Usuario:
    def __init__(self, id_usuario):
        self._id_usuario = id_usuario
        self._interacoes_realizadas: list['Interacao'] = []

     # getter do atributo privado id_usuario
    @property
    def id_usuario(self) -> int:
        return self._id_usuario

    @property # getter do atributo privado interacoes_realizadas
    def interacoes_realizadas(self):
        return list(self.__interacoes_realizadas)

    def registrar_interacao(self, interacao: 'Interacao'):
        self._interacoes_realizadas.append(interacao)
            # incrementa a lista de interações feitas por esse usuário com um objeto da classe Interacao

    def obter_interacoes_por_tipo(self, tipo_desejado):
        return [i for i in self.__interacoes_realizadas if i.tipo_interacao == tipo_desejado]
            # list comprehension que devolve uma lista filtrando os objetos Interacao cujo tipo_interacao é do tipo desejado

    def obter_conteudos_unicos_consumidos(self):
        return set(i._Interacao__conteudo_associado for i in self.__interacoes_realizadas)
            # para cada objeto Interacao dentro da lista de interacoes_realizadas por esse usuário,
            # resgata o conteudo_associado a ele, e cria um set com todos eles,
            # o que pela definição do set já cria um conjunto de elementos únicos

    def calcular_tempo_total_consumo_plataforma(self, plataforma: 'Plataforma' = None) -> int:
        """
        Calcula o tempo total de consumo para uma plataforma específica ou para todas.
        """
        tempo_total = 0
        for interacao in self._interacoes_realizadas:
            if plataforma is None or interacao.plataforma_interacao == plataforma:
                tempo_total += interacao.watch_duration_seconds
        return tempo_total


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
        return f"Usuario(id_usuario={self.id_usuario})"
