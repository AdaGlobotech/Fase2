# main.py
from analise import SistemaAnaliseEngajamento


#CAMINHO_CSV = "interacoes_globo_antigo.csv"
CAMINHO_CSV = "interacoes_globo.csv"

def main():
    print("=" * 60)
    print("Bem-vindo à análise de engajamento das mídias Globo 📺")
    print("Este sistema vai te mostrar os conteúdos e usuários mais ativos!")
    print("=" * 60)
    # 1. Criar uma instância do sistema de análise
    sistema = SistemaAnaliseEngajamento()
    print("\n[INFO] Lendo os dados do arquivo de interações...")
    # 2. Carregar os dados do CSV para a fila
    sistema.carregar_interacoes_csv(CAMINHO_CSV)

    # 3. Processar todas as interações da fila, populando as árvores
    sistema.processar_interacoes_da_fila()

    # 4. Gerar e apresentar todos os relatórios consolidados
    sistema.gerar_todos_os_relatorios(top_n=5)

if __name__ == "__main__":
    main()
