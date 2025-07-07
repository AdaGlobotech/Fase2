
# 📊 Análise de Engajamento de Mídias Globo – Projeto Unificado - Fase 3: Análise de Engajamento de Mídias Globo com Estruturas de Dados

Este projeto foi desenvolvido como parte da Fase 3 do bootcamp Ada+Globotech, com foco em aplicar os princípios de **Estruturas de Dados** para analisar o engajamento de usuários com conteúdos da Globo em diferentes plataformas.


## Equipe 5✨

-  Bernardo Soutelo
-  Felipe Sales
-  Iane Gomes
-  Ren Wrobleski

## 🎯 Objetivo

- Fila para carga de dados;
- Árvore binária de busca para armazenamento eficiente;
- Algoritmos de ordenação (QuickSort foi o escolhido);
- Refatoração do codigo da etapa anterior
- Relatórios baseados nessas estruturas.

## 🧱 Estrutura do Projeto

```bash
fase3/
├── main.py                      
├── interacoes_globo.csv         # CSV com dados de teste com mais entradas e usuarios repetidos
├── interacoes_globo_antigo.csv  # CSV com dados sem adições
├── teste_fila_arvore.py
├── entidades/                   # Classes de domínio
│   ├── conteudo.py              
│   ├── interacao.py             
│   ├── plataforma.py            
│   └── usuario.py  
├── estruturas_dados/
│   ├── fila.py
│   ├── arvore_binaria_busca.py
├── algoritmos/
│   ├── ordenadores.py  
├── testes_unitarios_etapa2/
    ├── teste_conteudo_integracao_usuario.py 
    ├── teste_plataforma_conteudo_integracao.py  
    ├── teste_usuario_integracao.py             
└── analise/
    └── sistema.py               # Classe SistemaAnaliseEngajamento
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

## 📚 Aprendizados

Este projeto reforçou o uso de:

- Uso prático de filas e árvores binárias;
- Cálculo de métricas com base em interações;
- Aplicação de algoritmos clássicos de ordenação;
- Organização modular e reutilização de entidades da etapa anterior.

---
