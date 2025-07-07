import csv
from datetime import datetime

# Importa as estruturas de dados
from estruturas_dados.fila import Fila
from estruturas_dados.arvore_binaria_busca import ArvoreBinariaBusca

# Importa o novo algoritmo de ordenação
from algoritmos.ordenacao import quick_sort

# Importa as classes de entidade
from entidades.Plataforma import Plataforma
from entidades.Conteudo import Conteudo
from entidades.Usuario import Usuario
from entidades.Interacao import Interacao

class SistemaAnaliseEngajamento:
    def __init__(self):
        self.fila_interacoes_brutas = Fila()
        self._arvore_conteudos = ArvoreBinariaBusca()
        self._arvore_usuarios = ArvoreBinariaBusca()
        self._plataformas_registradas = {}
        self._proximo_id_plataforma = 1

    def carregar_interacoes_csv(self, caminho_arquivo: str):
        # Complexidade de Tempo: O(M), onde M é o número de linhas no CSV.
        try:
            with open(caminho_arquivo, mode='r', encoding='utf-8') as f:
                leitor_csv = csv.DictReader(f)
                for linha in leitor_csv:
                    self.fila_interacoes_brutas.enfileirar(linha)
            print(f"Dados do arquivo '{caminho_arquivo}' carregados na fila com sucesso.")
        except FileNotFoundError:
            print(f"Erro: Arquivo não encontrado em '{caminho_arquivo}'.")

    def processar_interacoes_da_fila(self):
         # Complexidade de Tempo: O(M * (log N + log U)), onde M é o número de interações,
         # N é o número de conteúdos únicos e U é o número de usuários únicos (assumindo árvores balanceadas).
        print("Iniciando processamento das interações da fila...")
        contador_erros = 0
        while not self.fila_interacoes_brutas.esta_vazia():
            dados_interacao = self.fila_interacoes_brutas.desenfileirar()
            try:
                #Nomes das colunas
                plataforma = self.obter_plataforma(dados_interacao['plataforma'])
                id_conteudo = int(dados_interacao['id_conteudo'])
                
                conteudo = self._arvore_conteudos.buscar(id_conteudo)
                if not conteudo:
                    conteudo = Conteudo(id_conteudo, dados_interacao['nome_conteudo'])
                    self._arvore_conteudos.inserir(id_conteudo, conteudo)
                
                id_usuario = int(dados_interacao['id_usuario'])
                usuario = self._arvore_usuarios.buscar(id_usuario)
                if not usuario:
                    usuario = Usuario(id_usuario)
                    self._arvore_usuarios.inserir(id_usuario, usuario)
                
                # Tratamento do formato da data/hora
                timestamp = datetime.strptime(dados_interacao['timestamp_interacao'], "%Y-%m-%d %H:%M:%S")

                # Tratamento de duração vazia
                duracao_segundos = int(dados_interacao['watch_duration_seconds'] or 0)

                interacao = Interacao(
                    conteudo_associado=conteudo,
                    plataforma_interacao=plataforma,
                    id_usuario=id_usuario,
                    timestamp_interacao=timestamp,
                    tipo_interacao=dados_interacao['tipo_interacao'],
                    watch_duration_seconds=duracao_segundos,
                    comment_text=dados_interacao['comment_text']
                )
                
                conteudo.adicionar_interacao(interacao)
                usuario.registrar_interacao(interacao)

            except (ValueError, KeyError) as e:
                if contador_erros < 5:
                    print(f"AVISO: Linha ignorada devido a erro. Causa: {e}. Dados: {dados_interacao}")
                contador_erros += 1
        
        if contador_erros > 0:
            print(f"\nProcessamento da fila concluído. Total de {contador_erros} linhas com erros foram ignoradas.")
        else:
            print("Processamento da fila concluído com sucesso.")

    def obter_plataforma(self, nome_plataforma: str) -> Plataforma:
        return self._plataformas_registradas.get(nome_plataforma) or self.cadastrar_plataforma(nome_plataforma)

    def cadastrar_plataforma(self, nome_plataforma: str) -> Plataforma:
        if nome_plataforma not in self._plataformas_registradas:
            nova_plataforma = Plataforma(nome_plataforma, self._proximo_id_plataforma)
            self._plataformas_registradas[nome_plataforma] = nova_plataforma
            self._proximo_id_plataforma += 1
        return self._plataformas_registradas[nome_plataforma]

    def _gerar_relatorio_ordenado(self, titulo: str, lista_objetos: list, metrica_chave, top_n: int):
        # Complexidade de Tempo: Dominada pelo quick_sort, O(N log N) onde N é len(lista_objetos).
        print(titulo)
        if not lista_objetos:
            print("Nenhum dado para exibir.")
            return
        
        ordenados = quick_sort(lista_objetos, chave=metrica_chave, decrescente=True)
        
        for i, obj in enumerate(ordenados[:top_n]):
            valor_metrica = metrica_chave(obj)
            
            # Verifica o tipo do objeto para obter o nome correto e de forma segura.
            if isinstance(obj, Conteudo):
                nome_obj = obj.nome_conteudo
            elif isinstance(obj, Plataforma):
                nome_obj = obj.nome_plataforma
            elif isinstance(obj, Usuario):
                nome_obj = f"Usuário ID: {obj.id_usuario}"
            else:
                nome_obj = "Objeto Desconhecido" # Garante que não haverá erros
            
            print(f"{i+1}. {nome_obj} | Métrica: {valor_metrica}")

    def gerar_todos_os_relatorios(self, top_n=5):
        print("\n" + "="*50)
        print("RELATÓRIOS DE ENGAJAMENTO DE MÍDIAS GLOBO - FASE 3")
        print("="*50)

        # 1. Ranking de conteúdos mais consumidos
        conteudos = self._arvore_conteudos.percurso_em_ordem()
        self._gerar_relatorio_ordenado(
            f"\n--- Top {top_n} Conteúdos por Tempo de Consumo (segundos) ---",
            conteudos,
            lambda c: c.calcular_tempo_total_consumo(),
            top_n
        )

        # 2. Usuários com maior tempo total de consumo
        usuarios = self._arvore_usuarios.percurso_em_ordem()
        self._gerar_relatorio_ordenado(
            f"\n--- Top {top_n} Usuários por Tempo de Consumo (segundos) ---",
            usuarios,
            lambda u: u.calcular_tempo_total_consumo_plataforma(None), # None para todas as plataformas
            top_n
        )
        
        # 3. Plataforma com maior engajamento
        plataformas = list(self._plataformas_registradas.values())
        engajamento_por_plataforma = {p.nome_plataforma: 0 for p in plataformas}

        usuarios = self._arvore_usuarios.percurso_em_ordem()
        for usuario in usuarios:
            for interacao in usuario._interacoes_realizadas:
                if interacao.tipo_interacao in ['like', 'share', 'comment']:
                    # CORREÇÃO APLICADA AQUI
                    nome_da_plataforma = interacao.plataforma_interacao.nome_plataforma
                    if nome_da_plataforma in engajamento_por_plataforma:
                        engajamento_por_plataforma[nome_da_plataforma] += 1

        self._gerar_relatorio_ordenado(
            f"\n--- Top {top_n} Plataformas por Engajamento (likes+shares+comments) ---",
            plataformas,
            lambda p: engajamento_por_plataforma.get(p.nome_plataforma, 0),
            top_n
        )

        # 4. Conteúdos mais comentados
        self._gerar_relatorio_ordenado(
            f"\n--- Top {top_n} Conteúdos por Número de Comentários ---",
            conteudos,
            lambda c: len(c.listar_comentarios()),
            top_n
        )

        # 5. Total de interações por tipo de conteúdo
        self._gerar_relatorio_ordenado(
            f"\n--- Top {top_n} Conteúdos por Total de Interações ---",
            conteudos,
            lambda c: len(c._interacoes),
            top_n
        )

        # 6. Tempo médio de consumo para cada plataforma
        print(f"\n--- Tempo Médio de Consumo por Plataforma ---")
        for plataforma in plataformas:
            total_duracao = 0
            interacoes_com_duracao = 0
            for u in usuarios:
                for interacao in u._interacoes_realizadas:
                    if interacao.plataforma_interacao == plataforma and interacao.watch_duration_seconds > 0:
                        total_duracao += interacao.watch_duration_seconds
                        interacoes_com_duracao += 1
            
            media = total_duracao / interacoes_com_duracao if interacoes_com_duracao > 0 else 0
            print(f"- {plataforma.nome_plataforma}: {media:.2f} segundos")
