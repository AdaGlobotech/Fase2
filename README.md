
# 📊 Análise de Engajamento de Mídias Globo – Projeto Unificado - Fase 3: Análise de Engajamento de Mídias Globo com Estruturas de Dados

Este projeto foi desenvolvido como parte da Fase 3 do bootcamp Ada+Globotech, com foco em aplicar os princípios de **Estruturas de Dados** para analisar o engajamento de usuários com conteúdos da Globo em diferentes plataformas.


## Equipe 5✨

-  Bernardo Soutelo
-  Felipe Sales
-  Iane Gomes
-  Ren Wrobleski

## 🎯 Objetivos da Fase 3
- Utilizar uma **fila** para carregamento inicial das interações.
- Armazenar conteúdos e usuários em **árvores binárias de busca**.
- Aplicar **QuickSort** na geração dos rankings e relatórios.
- Refatorar a etapa anterior para utilizar essas estruturas de forma eficiente.

## 🧱 Estrutura do Projeto

```bash
fase3/

## 🧱 Estrutura do Repositório
```text
Fase3/
├── main.py
├── interacoes_globo.csv         # Dataset com novas interações (inclui usuários repetidos)
├── interacoes_globo_antigo.csv  # Versão original do dataset
├── teste_fila_arvore.py         # Demonstrações de Fila, Árvore e QuickSort
├── entidades/                   # Classes de domínio
│   ├── Conteudo.py
│   ├── Interacao.py
│   ├── Plataforma.py
│   └── Usuario.py
├── estruturas_dados/            # Implementações de Fila e Árvore
│   ├── fila.py
│   └── arvore_binaria_busca.py
├── algoritmos/
│   └── ordenacao.py             # Implementação do QuickSort
├── testes_unitarios_etapa2/     # Scripts de testes manuais
│   ├── teste_conteudo_integracao_usuario.py
│   ├── teste_plataforma_conteudo_interacao.py
│   └── teste_usuario_integracao.py
└── analise/
    └── sistema.py               # SistemaAnaliseEngajamento
```

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/AdaGlobotech/Fase2.git
   cd Fase2
   ```

2. Instale o Python (recomendado 3.10+)

3. Execute o sistema:
   ```bash
   python main.py
   ```

O sistema irá:

Carregar o dataset em uma fila.
Processar as interações, preenchendo as árvores de conteúdos e usuários.
Gerar relatórios no terminal com os resultados mais relevantes (top conteúdos, usuários, plataformas e outras métricas).



## 🧪 Testes

O projeto inclui **testes manuais** para validar:

- Funcionamento da (`Fila`);
- Funcionamento da (`Arvore Binaria`);
- Funcionamento do (`QuickSort`);
- Registro e contagem de interações (`Usuario`);
- Cálculo de tempo total e média de consumo (`Conteudo`);
- Comentários por conteúdo (`Interacao`);
- Validação de tipos permitidos (`Interacao.TIPOS_INTERACAO_VALIDOS`);
- Ordenação por métricas no sistema de análise.

O arquivo teste_fila_arvore.py demonstra o funcionamento das estruturas de dados e do QuickSort.

## 📚 Aprendizados

Este projeto reforçou o uso de:

- Uso prático de filas e árvores binárias;
- Cálculo de métricas com base em interações;
- Aplicação de algoritmos clássicos de ordenação;
- Organização modular e reutilização de entidades da etapa anterior.

---
