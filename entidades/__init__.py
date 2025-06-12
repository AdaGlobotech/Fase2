from .Plataforma import Plataforma
from .Conteudo import Conteudo, Video, Podcast, Artigo # traz as subclasses dependentes de Conteudo
from .Interacao import Interacao
from .Usuario import Usuario

__all__ = [ # definição das classes disponíveis para serem importadas
    "Plataforma",
    "Conteudo",
    "Video",
    "Podcast",
    "Artigo",
    "Interacao",
    "Usuario"
]
