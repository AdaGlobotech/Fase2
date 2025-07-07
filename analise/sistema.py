from entidades import Plataforma, Usuario, Interacao, Video, Podcast, Artigo
from estruturas_dados import Fila, ArvoreBinariaBusca
import csv

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

    def cadastrar_plataforma(self, nome_plataforma: str) -> Plataforma:
        if nome_plataforma not in self.__plataformas_registradas:
            plataforma = Plataforma(
                id_plataforma=self.__proximo_id_plataforma,
                nome_plataforma=nome_plataforma
            )
            self.__plataformas_registradas[nome_plataforma] = plataforma
            self.__proximo_id_plataforma += 1
        return self.__plataformas_registradas[nome_plataforma]

    def obter_plataforma(self, nome_plataforma: str) -> Plataforma:
        return self.__plataformas_registradas.get(nome_plataforma) or \
            self.cadastrar_plataforma(nome_plataforma)

    def listar_plataformas(self) -> list:
        return list(self.__plataformas_registradas.values())

    def _carregar_interacoes_csv(self, caminho_arquivo: str) -> None:
        with open(caminho_arquivo, newline='', encoding="utf-8") as csvfile:
            leitor = csv.DictReader(csvfile)
            for linha in leitor:
                self.__fila_interacoes_brutas.enfileirar(linha)

    def processar_interacoes_do_csv(self, caminho_arquivo: str) -> None:
        self._carregar_interacoes_csv(caminho_arquivo)
        while not self.__fila_interacoes_brutas.esta_vazia():
            reg = self.__fila_interacoes_brutas.desenfileirar()
            try:
                id_conteudo = int(reg["id_conteudo"])
                nome_conteudo = reg["nome_conteudo"]
                id_usuario = int(reg["id_usuario"])
                timestamp = reg["timestamp_interacao"]
                nome_plataforma = reg["plataforma"]
                tipo_interacao = reg["tipo_interacao"]
                duracao = int(reg.get("watch_duration_seconds", 0) or 0)
                comentario = reg.get("comment_text", "")

                plataforma = self.obter_plataforma(nome_plataforma)

                conteudo = self.__arvore_conteudos.buscar(id_conteudo)
                if conteudo is None:
                    conteudo = Video(id_conteudo, nome_conteudo, duracao_total_video_seg=3600)
                    self.__arvore_conteudos.inserir(id_conteudo, conteudo)

                usuario = self.__arvore_usuarios.buscar(id_usuario)
                if usuario is None:
                    usuario = Usuario(id_usuario)
                    self.__arvore_usuarios.inserir(id_usuario, usuario)

                interacao = Interacao(
                    conteudo_associado=conteudo,
                    id_usuario=id_usuario,
                    timestamp_interacao=timestamp,
                    plataforma_interacao=plataforma,
                    tipo_interacao=tipo_interacao,
                    watch_duration_seconds=duracao,
                    comment_text=comentario,
                )

                conteudo.adicionar_interacao(interacao)
                usuario.registrar_interacao(interacao)

            except ValueError as e:
                print(f"[ERRO] Ignorando linha com erro: {e}")

    def gerar_relatorio_engajamento_conteudos(self, top_n: int | None = None) -> None:
        conteudos = self.__arvore_conteudos.percurso_em_ordem()
        conteudos = _quick_sort(conteudos, key=lambda c: c.calcular_tempo_total_consumo())[::-1]
        for conteudo in conteudos[:top_n]:
            tempo_total = conteudo.calcular_tempo_total_consumo()
            media_tempo = conteudo.calcular_media_tempo_consumo()
            num_comentarios = len(conteudo.listar_comentarios())
            print(
                f"{conteudo}: Tempo Total = {tempo_total}s, "
                f"Média Tempo = {media_tempo:.1f}s, Comentários = {num_comentarios}"
            )

    def gerar_relatorio_atividade_usuarios(self, top_n: int | None = None) -> None:
        usuarios = self.__arvore_usuarios.percurso_em_ordem()
        usuarios = _quick_sort(
            usuarios,
            key=lambda u: sum(i.watch_duration_seconds for i in u._Usuario__interacoes_realizadas)
        )[::-1]
        for usuario in usuarios[:top_n]:
            print(
                f"Usuário {usuario.id_usuario}: "
                f"{len(usuario._Usuario__interacoes_realizadas)} interações"
            )

    def identificar_top_conteudos(self, metrica: str, n: int) -> None:
        chave_funcoes = {
            "tempo_total_consumo": lambda c: c.calcular_tempo_total_consumo(),
            "media_consumo": lambda c: c.calcular_media_tempo_consumo(),
            "comentarios": lambda c: len(c.listar_comentarios()),
        }
        if metrica not in chave_funcoes:
            raise ValueError("Métrica inválida")

        conteudos = self.__arvore_conteudos.percurso_em_ordem()
        conteudos = _quick_sort(conteudos, key=chave_funcoes[metrica])[::-1]
        for conteudo in conteudos[:n]:
            print(f"{conteudo} -> {metrica}: {chave_funcoes[metrica](conteudo)}")
