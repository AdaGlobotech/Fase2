from entidades import Plataforma, Usuario, Interacao, Video, Podcast, Artigo
    # importa todos os módulos criados anteriormente

import csv # importa o módulo necessário pra carregar os dados csv

class SistemaAnaliseEngajamento:

    def __init__(self):
        self.__plataformas_registradas = {} # inicia o dicionário vazio
        self.__conteudos_registrados = {} # inicia o dicionário vazio
        self.__usuarios_registrados = {} # inicia o dicionário vazio
        self.__proximo_id_plataforma = 1 # inicializa como 1 pois será o primeiro ID registrado de plataforma

    def cadastrar_plataforma(self, nome_plataforma: str) -> Plataforma:
        # método para criar objetos do tipo plataforma e adicioná-los ao dicionário de plataformas_registradas
        if nome_plataforma not in self.__plataformas_registradas:
            # checa se a plataforma dada ainda não foi registrada
            plataforma = Plataforma(id_plataforma=self.__proximo_id_plataforma, nome_plataforma=nome_plataforma)
                # cria um objeto da classe Plataforma com o id_plataforma em seu valor atual e o nome 
            self.__plataformas_registradas[nome_plataforma] = plataforma
                # adiciona ao dicionário de plataformas_registradas o objeto, com sua chave sendo o nome da plataforma
            self.__proximo_id_plataforma += 1
                # atualiza o id_plataforma para cadastrar a próxima plataforma
        return self.__plataformas_registradas[nome_plataforma]
                # retorna o objeto criado da classe Plataforma

    def obter_plataforma(self, nome_plataforma: str) -> Plataforma:
        return self.__plataformas_registradas.get(nome_plataforma) or self.cadastrar_plataforma(nome_plataforma)
            # devolve o objeto Plataforma com o nome dado
            # ou aplica o método cadastrar_plataforma feito anteriormente para cadastrá-lo se ele ainda não existir

    def listar_plataformas(self) -> list:
        return list(self.__plataformas_registradas.values())
            # retorna uma lista com todos os objetos Plataforma cadastrados

    def _carregar_interacoes_csv(self, caminho_arquivo: str) -> list:
        # método privado que retorna uma lista de dicionários, em que cada um representa uma linha do CSV,
        # com as chaves sendo os nomes das colunas
        with open(caminho_arquivo, newline='', encoding='utf-8') as csvfile: # abre o arquivo csv
            leitor = csv.DictReader(csvfile) # transforma em dicionários o que foi lido do csv
            return list(leitor) # retorna a lista de dicionários

    def processar_interacoes_do_csv(self, caminho_arquivo):
        registros = self._carregar_interacoes_csv(caminho_arquivo)
            # guarda em registros a lista de dicionários com os dados
        for reg in registros: # para cada dicionário (cada linha dos dados)
            try:
                id_conteudo = int(reg["id_conteudo"])
                nome_conteudo = reg["nome_conteudo"]
                id_usuario = int(reg["id_usuario"])
                timestamp = reg["timestamp_interacao"]
                nome_plataforma = reg["plataforma"]
                tipo_interacao = reg["tipo_interacao"]
                duracao = int(reg.get("watch_duration_seconds", 0) or 0)
                comentario = reg.get("comment_text", "")
                    # guarda em variáveis os valores de cada coluna dos dados

                plataforma = self.obter_plataforma(nome_plataforma)
                    # chama o módulo que retorna ou cria um objeto Plataforma

                # Suporte genérico para conteúdo: assume Video como padrão
                if id_conteudo not in self.__conteudos_registrados:
                    self.__conteudos_registrados[id_conteudo] = Video(id_conteudo, nome_conteudo, duracao_total_video_seg=3600)
                    # foi estabelecido o padrão de conteúdo como Video e um valor padrão de duração

                conteudo = self.__conteudos_registrados[id_conteudo]

                if id_usuario not in self.__usuarios_registrados:
                    self.__usuarios_registrados[id_usuario] = Usuario(id_usuario)

                usuario = self.__usuarios_registrados[id_usuario]

                interacao = Interacao(
                    conteudo_associado=conteudo,
                    id_usuario=id_usuario,
                    timestamp_interacao=timestamp,
                    plataforma_interacao=plataforma,
                    tipo_interacao=tipo_interacao,
                    watch_duration_seconds=duracao,
                    comment_text=comentario
                )

                conteudo.adicionar_interacao(interacao)
                usuario.registrar_interacao(interacao)

            except ValueError as e:
                print(f"[ERRO] Ignorando linha com erro: {e}")
                    # segue o programa caso haja ValueError em algum 

    def gerar_relatorio_engajamento_conteudos(self, top_n: int = None):
        conteudos = list(self.__conteudos_registrados.values())
        conteudos.sort(key=lambda c: c.calcular_tempo_total_consumo(), reverse=True)
        for conteudo in conteudos[:top_n]:
            tempo_total = conteudo.calcular_tempo_total_consumo()
            media_tempo = conteudo.calcular_media_tempo_consumo()
            num_comentarios = len(conteudo.listar_comentarios())
            print(f"{conteudo}: Tempo Total = {tempo_total}s, Média Tempo = {media_tempo:.1f}s, Comentários = {num_comentarios}")
            
    def gerar_relatorio_atividade_usuarios(self, top_n: int = None):
        usuarios = list(self.__usuarios_registrados.values())
        usuarios.sort(key=lambda u: sum(i.watch_duration_seconds for i in u._Usuario__interacoes_realizadas), reverse=True)
        for usuario in usuarios[:top_n]:
            print(f"Usuário {usuario.id_usuario}: {len(usuario._Usuario__interacoes_realizadas)} interações")

    def identificar_top_conteudos(self, metrica: str, n: int):
        chave_funcoes = {
            'tempo_total_consumo': lambda c: c.calcular_tempo_total_consumo(),
            'media_consumo': lambda c: c.calcular_media_tempo_consumo(),
            'comentarios': lambda c: len(c.listar_comentarios())
        }
        if metrica not in chave_funcoes:
            raise ValueError("Métrica inválida")
        conteudos = list(self.__conteudos_registrados.values())
        conteudos.sort(key=chave_funcoes[metrica], reverse=True)
        for conteudo in conteudos[:n]:
            print(f"{conteudo} -> {metrica}: {chave_funcoes[metrica](conteudo)}")
