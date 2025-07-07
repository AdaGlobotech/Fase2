### CLASSE BASE CONTEÚDO
from entidades import Interacao


class Conteudo:
   
    def __init__(self, id_conteudo: int, nome_conteudo: str):
        self._id_conteudo = id_conteudo
        self._nome_conteudo = nome_conteudo
        self._interacoes: list['Interacao'] = []

    @property
    def id_conteudo(self) -> int:
        return self._id_conteudo
    
    @property
    def nome_conteudo(self) -> str:
        return self._nome_conteudo
    
    @id_conteudo.setter
    def id_conteudo(self, id):
        if not isinstance(id, int): # checa se o valor inserido para id_conteudo é do tipo int
            raise TypeError("O id_conteudo deve ser um valor inteiro") # levanta TypeError se não for do tipo desejado
        self.__id_conteudo = id # se não der erro é porque o valor inserido é int, então pode ser inserido no atributo

    @nome_conteudo.setter
    def nome_conteudo(self, nome):
        if not isinstance(nome, str): # checa se o valor inserido para nome_conteudo é do tipo str
            raise TypeError("O nome_conteudo deve ser uma string.") # levanta TypeError se não for do tipo desejado
        self.__nome_conteudo = nome # se não der erro é porque o valor inserido é str, então pode ser inserido no atributo
    
    def adicionar_interacao(self, interacao: 'Interacao'):
        """
        Adiciona uma interação à lista de interações deste conteúdo.
        """
        self._interacoes.append(interacao)

    def ver_interacoes(self): # visualizador das interações
        return self.__interacoes

    def calcular_total_interacoes_engajamento(self) -> int:
        """
        Calcula o total de 'like', 'share', 'comment'.
        """
        return sum(1 for i in self._interacoes if i.tipo_interacao in ['like', 'share', 'comment'])

    
    def calcular_contagem_por_tipo_interacao(self):
        contadores = self.calcular_total_interacoes_engajamento() # puxa os valores devolvidos pela função que conta as interações
        interacoes = ['like', 'share', 'comment'] # lista contendo os nomes das interações de interesse
        dicionario = dict(zip(interacoes, contadores)) # cria um dicionário a partir da junção dos nomes e seus valores correspondentes

        return dicionario
    
    def calcular_tempo_total_consumo(self) -> int:
        """
        Soma watch_duration_seconds das interações.
        """
        return sum(i.watch_duration_seconds for i in self._interacoes)
    
    def calcular_media_tempo_consumo(self):
        lista_watch_duration_positivos = [] # lista para guardar só os valores watch_duration_seconds > 0, que serão usados no cálculo da média

        for objeto in self.__interacoes: # percorre os objetos que compõem a lista de interações
            if objeto.watch_duration_seconds > 0:
                lista_watch_duration_positivos.append(objeto.watch_duration_seconds)

        media = sum(lista_watch_duration_positivos) / len(lista_watch_duration_positivos) # calcula a média a partir dos valores de watch_duration_seconds

        return media
    
    def listar_comentarios(self) -> list[str]:
        """
        Retorna uma lista dos textos dos comentários.
        """
        return [i.comment_text for i in self._interacoes if i.tipo_interacao == 'comment' and i.comment_text]
    
    
    def __str__(self): 
        return f'Conteúdo: {self.nome_conteudo} | ID: {self.id_conteudo}'
    
    def __repr__(self):
        return f"Conteudo(id={self.id_conteudo}, nome='{self.nome_conteudo}')"

### SUBCLASSE VIDEO
class Video (Conteudo):
    def __init__(self, id_conteudo_video, nome_conteudo_video, duracao_total_video_seg):
        super().__init__(id_conteudo_video, nome_conteudo_video) # traz o método construtor da superclasse Conteudo
        self.__duracao_total_video_seg = duracao_total_video_seg # acessa o setter que faz a validação e coloca valor no atributo

    @property # getter do atributo privado duracao_total_video_seg
    def duracao_total_video_seg(self):
        return self.__duracao_total_video_seg
    
    @duracao_total_video_seg.setter
    def duracao_total_video_seg(self, valor):
        if not isinstance(valor, int): # checa se o valor inserido para duracao_total_video_seg é do tipo int
            raise TypeError("A duracao_total_video_seg deve ser um valor inteiro") # levanta TypeError se não for do tipo desejado
        self.__duracao_total_video_seg = valor # se o valor passar na validação, é colocado no atributo privado
    
    def calcular_percentual_medio_assistido(self):
        tempo_medio_consumo = self.calcular_media_tempo_consumo() # puxa a média de tempo de consumo pelo método correspondente contido na classe Conteudo

        if self.__duracao_total_video_seg == 0:
            return 0 # resultado pedido no enunciado se o total for 0
        
        percentual_medio_assistido = (tempo_medio_consumo / self.__duracao_total_video_seg) * 100 # calcula a % a partir da média e do atributo duracao_total_video_seg

        return percentual_medio_assistido
    
### SUBCLASSE PODCAST
class Podcast (Conteudo):
    def __init__(self, id_conteudo_podcast, nome_conteudo_podcast, duracao_total_episodio_seg = None):
        super().__init__(id_conteudo_podcast, nome_conteudo_podcast) 
        self.duracao_total_episodio_seg = duracao_total_episodio_seg # o atributo é iniciado com o valor padrão None, sendo opcional inserir valor nele

    @property # getter do atributo privado duracao_total_episodio_seg
    def duracao_total_episodio_seg(self):
        return self.__duracao_total_episodio_seg
    
    @duracao_total_episodio_seg.setter
    def duracao_total_episodio_seg(self, valor):
        self.__duracao_total_episodio_seg = valor

### SUBCLASSE ARTIGO
class Artigo (Conteudo):
    def __init__(self, id_conteudo_artigo, nome_conteudo_artigo, tempo_leitura_estimado_seg):
        super().__init__(id_conteudo_artigo, nome_conteudo_artigo) 
        self.__tempo_leitura_estimado_seg = tempo_leitura_estimado_seg

    @property # getter do atributo privado tempo_leitura_estimado_seg
    def tempo_leitura_estimado_seg(self):
        return self.__tempo_leitura_estimado_seg
    
    @tempo_leitura_estimado_seg.setter
    def tempo_leitura_estimado_seg(self, valor):
        if not isinstance(valor, int): # checa se o valor inserido para tempo_leitura_estimado_seg é do tipo int
            raise TypeError("O tempo_leitura_estimado_seg deve ser um valor inteiro.") # levanta TypeError se não for do tipo desejado
        self.__tempo_leitura_estimado_seg = valor