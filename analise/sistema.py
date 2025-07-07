from entidades import Plataforma, Usuario, Interacao, Video, Podcast, Artigo
from estruturas_dados import Fila, ArvoreBinariaBusca
import csv
from collections import defaultdict

# Algoritmos de ordenação utilizados:
# - Quick Sort: eficiente para listas grandes, complexidade média O(n log n)
# - Insertion Sort: eficiente para listas pequenas, complexidade O(n^2), não utilizado neste módulo pois os dados são consideráveis

def _quick_sort(lista, key=lambda x: x):
    if len(lista) <= 1:
        return lista[:]
    pivo = key(lista[0])
    menores = [x for x in lista[1:] if key(x) <= pivo]
    maiores = [x for x in lista[1:] if key(x) > pivo]
    return _quick_sort(menores, key) + [lista[0]] + _quick_sort(maiores, key)

def _insertion_sort(lista, key=lambda x: x):
    resultado = lista[:]
    for i in range(1, len(resultado)):
        atual = resultado[i]
        j = i - 1
        while j >= 0 and key(resultado[j]) > key(atual):
            resultado[j + 1] = resultado[j]
            j -= 1
        resultado[j + 1] = atual
    return resultado

class SistemaAnaliseEngajamento:
    def __init__(self):
        self.__plataformas_registradas = {}
        self.__arvore_conteudos = ArvoreBinariaBusca()
        self.__arvore_usuarios = ArvoreBinariaBusca()
        self.__proximo_id_plataforma = 1
        self.__fila_interacoes_brutas = Fila()

    # Gera ranking dos conteúdos mais assistidos, ordenando pelo tempo total de consumo
    # Utiliza Quick Sort para eficiência com grandes volumes de dados
    def gerar_ranking_conteudos_mais_consumidos(self, top_n: int = 5):
        conteudos = self.__arvore_conteudos.percurso_em_ordem()
        ordenados = _quick_sort(conteudos, key=lambda c: c.calcular_tempo_total_consumo())[::-1]
        for c in ordenados[:top_n]:
            print(f"{c.nome_conteudo}: {c.calcular_tempo_total_consumo()}s")

    # Gera ranking de usuários com maior tempo de consumo
    # Utiliza Quick Sort com função de soma de durações
    def gerar_usuarios_maior_consumo(self, top_n: int = 5):
        usuarios = self.__arvore_usuarios.percurso_em_ordem()
        ordenados = _quick_sort(
            usuarios,
            key=lambda u: sum(i.watch_duration_seconds for i in u.interacoes_realizadas)
        )[::-1]
        for u in ordenados[:top_n]:
            total = sum(i.watch_duration_seconds for i in u.interacoes_realizadas)
            print(f"Usuário {u.id_usuario}: {total}s")

    # Identifica a plataforma com maior engajamento (like, share, comment)
    # Usa sorted embutido para dicionário pequeno, pois o número de plataformas é reduzido
    def gerar_plataforma_maior_engajamento(self):
        contagem = defaultdict(int)
        for u in self.__arvore_usuarios.percurso_em_ordem():
            for i in u.interacoes_realizadas:
                if i.tipo_interacao in ('like', 'share', 'comment'):
                    contagem[i._Interacao__plataforma_interacao.nome_plataforma] += 1
        ordenado = sorted(contagem.items(), key=lambda x: x[1], reverse=True)
        for nome, qtd in ordenado:
            print(f"{nome}: {qtd} interações")

    # Lista os conteúdos com maior número de comentários registrados
    # Ordena por tamanho da lista de comentários usando Quick Sort
    def gerar_conteudos_mais_comentados(self, top_n: int = 5):
        conteudos = self.__arvore_conteudos.percurso_em_ordem()
        ordenados = _quick_sort(conteudos, key=lambda c: len(c.listar_comentarios()))[::-1]
        for c in ordenados[:top_n]:
            print(f"{c.nome_conteudo}: {len(c.listar_comentarios())} comentários")

    # Apresenta o total de interações por tipo para cada conteúdo
    def gerar_total_interacoes_por_tipo_conteudo(self):
        conteudos = self.__arvore_conteudos.percurso_em_ordem()
        for c in conteudos:
            tipos = c.calcular_contagem_por_tipo_interacao()
            print(f"{c.nome_conteudo} - {tipos}")

    # Calcula o tempo médio de consumo para cada plataforma
    def gerar_tempo_medio_consumo_por_plataforma(self):
        total_duracao = defaultdict(list)
        for u in self.__arvore_usuarios.percurso_em_ordem():
            for i in u.interacoes_realizadas:
                total_duracao[i._Interacao__plataforma_interacao.nome_plataforma].append(i.watch_duration_seconds)
        for plataforma, tempos in total_duracao.items():
            media = sum(tempos) / len(tempos) if tempos else 0
            print(f"{plataforma}: {media:.2f}s")

    # Lista a quantidade total de comentários feitos em cada conteúdo
    def gerar_qtd_comentarios_por_conteudo(self):
        conteudos = self.__arvore_conteudos.percurso_em_ordem()
        for c in conteudos:
            qtd = len(c.listar_comentarios())
            print(f"{c.nome_conteudo}: {qtd} comentários")
