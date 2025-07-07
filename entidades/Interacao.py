from datetime import datetime

from entidades import Conteudo
from entidades.Plataforma import Plataforma 

class Interacao:
    TIPOS_INTERACAO_VALIDOS = {'view_start', 'like', 'share', 'comment'} # cria um conjunto de strings contendo os valores permitidos para o atributo tipo_interacao

    def __init__(self, conteudo_associado: 'Conteudo', plataforma_interacao: 'Plataforma', id_usuario: int, timestamp_interacao: datetime, tipo_interacao: str, watch_duration_seconds: int, comment_text: str):
        
        self.conteudo_associado = conteudo_associado
        self._plataforma_interacao = plataforma_interacao
        self._id_usuario = id_usuario
        self._timestamp_interacao = timestamp_interacao
        
        if tipo_interacao not in self.TIPOS_INTERACAO_VALIDOS:
            raise ValueError(f"Tipo de interação inválido: {tipo_interacao}")
        self._tipo_interacao = tipo_interacao
        
        self._watch_duration_seconds = max(0, watch_duration_seconds)
        self.comment_text = comment_text.strip() if comment_text else ""

    def _converter_timestamp(self, ts): # método protegido, para ser usado apenas dentro dessa classe Interacao
        if isinstance(ts, datetime):
            return ts # se o valor já for do formato datetime, só retorna
        return datetime.fromisoformat(ts) # se não for, faz a conversão para um objeto de formato datetime

    @property
    def plataforma_interacao(self) -> 'Plataforma':
        return self._plataforma_interacao

    @property # getter do atributo privado tipo_interacao
    def tipo_interacao(self) -> str:
        return self._tipo_interacao

    @tipo_interacao.setter
    def tipo_interacao(self, valor):
        if valor not in self.TIPOS_INTERACAO_VALIDOS: # checagem se o tipo_interacao pertence ao conjunto definido de valores válidos
            raise ValueError(f"Tipo de interação inválido: {valor}") # levanta o erro de valor se não pertencer
        self._tipo_interacao = valor # se pertencer, insere no atributo

     # getter do atributo privado watch_duration_seconds
    @property
    def watch_duration_seconds(self) -> int:
        return self._watch_duration_seconds

    @watch_duration_seconds.setter
    def watch_duration_seconds(self, valor):
        self._watch_duration_seconds = max(0, int(valor))
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

    def __repr__(self) -> str:
        return f"Interacao(tipo='{self.tipo_interacao}', usuario='{self._id_usuario}')"
