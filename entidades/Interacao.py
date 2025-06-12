from datetime import datetime # importa o módulo datetime

class Interacao:
    TIPOS_INTERACAO_VALIDOS = {'view_start', 'like', 'share', 'comment'} # cria um conjunto de strings contendo os valores permitidos para o atributo tipo_interacao

    def __init__(self, conteudo_associado, id_usuario, timestamp_interacao, 
                 plataforma_interacao, tipo_interacao, 
                 watch_duration_seconds=0, comment_text="", interacao_id=None):
        self.__interacao_id = interacao_id # é iniciado com None como valor padrão
        self.__conteudo_associado = conteudo_associado
        self.__id_usuario = int(id_usuario)
        self.__timestamp_interacao = self._converter_timestamp(timestamp_interacao)
        self.__plataforma_interacao = plataforma_interacao
        self.tipo_interacao = tipo_interacao  # validador via property
        self.watch_duration_seconds = watch_duration_seconds  # idem
        self.comment_text = comment_text or ""

    def _converter_timestamp(self, ts): # método protegido, para ser usado apenas dentro dessa classe Interacao
        if isinstance(ts, datetime):
            return ts # se o valor já for do formato datetime, só retorna
        return datetime.fromisoformat(ts) # se não for, faz a conversão para um objeto de formato datetime

    @property # getter do atributo privado tipo_interacao
    def tipo_interacao(self):
        return self.__tipo_interacao

    @tipo_interacao.setter
    def tipo_interacao(self, valor):
        if valor not in self.TIPOS_INTERACAO_VALIDOS: # checagem se o tipo_interacao pertence ao conjunto definido de valores válidos
            raise ValueError(f"Tipo de interação inválido: {valor}") # levanta o erro de valor se não pertencer
        self.__tipo_interacao = valor # se pertencer, insere no atributo

    @property # getter do atributo privado watch_duration_seconds
    def watch_duration_seconds(self):
        return self.__watch_duration_seconds

    @watch_duration_seconds.setter
    def watch_duration_seconds(self, valor):
        self.__watch_duration_seconds = max(0, int(valor))
            # define o atributo com o valor inserido se ele for positivo, ou 0 caso contrário

    @property # getter do atributo privado comment_text
    def comment_text(self):
        return self.__comment_text

    @comment_text.setter
    def comment_text(self, texto):
        if texto is None:
            texto = "" # define o atributo com uma string vazia caso ele esteja como None por algum motivo
        self.__comment_text = str(texto).strip() # retira os espaços das pontas da string, independente de seu conteúdo, antes de atribuir

    def __str__(self): # método pra exibição simples dos atributos da classe
        return f"Interacao({self.__tipo_interacao} por usuário: {self.__id_usuario})"

    def __repr__(self): # método pra exibição mais técnica dos atributos da classe
        return f"<Interacao tipo = {self.__tipo_interacao} usuario = {self.__id_usuario}>"
