
# 📊 Análise de Engajamento de Mídias Globo – Projeto Orientado a Objetos

Este projeto foi desenvolvido como parte da Fase 2 do bootcamp Ada+Globotech, com foco em aplicar os princípios de **Programação Orientada a Objetos com Python** para analisar o engajamento de usuários com conteúdos da Globo em diferentes plataformas.


## Equipe ✨

-  Bernardo Soutelo
-  Felipe Sales
-  Iane Gomes
-  Ren Wrobleski

## 🎯 Objetivo

Criar um sistema robusto e modular capaz de:

- Carregar interações de um arquivo CSV;
- Organizar os dados em classes como `Plataforma`, `Conteudo`, `Usuario` e `Interacao`;
- Calcular métricas como tempo total de consumo, média por conteúdo e interações por tipo;
- Gerar relatórios ordenados com os conteúdos e usuários mais ativos.

## 🧱 Estrutura do Projeto

```bash
fase2/
├── main.py                      # Executa o sistema
├── interacoes_globo.csv         # CSV com dados de teste com mais entradas e usuarios repetidos
├── interacoes_globo_antigo.csv  # CSV com dados sem adições
├── teste_conteudo_integracao_usuario.py  # Teste unitario de integração, conteudo e usuario
├── teste_plataforma_conteudo_integracao.py  # Teste unitario de plataforma, conteud oe integração
├── teste_usuario_integracao.py  # Teste unitario de integração e usuario
├── entidades/                   # Classes de domínio
│   ├── conteudo.py              # Conteudo, Video, Podcast, Artigo
│   ├── interacao.py             # Classe Interacao
│   ├── plataforma.py            # Classe Plataforma
│   └── usuario.py               # Classe Usuario
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

- Registro e contagem de interações (`Usuario`);
- Cálculo de tempo total e média de consumo (`Conteudo`);
- Comentários por conteúdo (`Interacao`);
- Validação de tipos permitidos (`Interacao.TIPOS_INTERACAO_VALIDOS`);
- Ordenação por métricas no sistema de análise.

> Em versões futuras, os testes manuais poderão ser migrados para `unittest` ou `pytest`.

## 📋 Funcionalidades Implementadas

✅ Cadastro e obtenção automática de plataformas  
✅ Suporte a diferentes tipos de conteúdo (herança/polimorfismo)  
✅ Relatórios ordenados por tempo ou engajamento  
✅ Validações robustas nos atributos das entidades  
✅ Simulação com CSV de +50 registros realistas

## 📚 Aprendizados

Este projeto reforçou o uso de:

- Encapsulamento com `@property` e uso de Decorators;
- Métodos mágicos para representação e comparação;
- Herança e sobreposição de métodos;
- Delegação de responsabilidades entre classes.

---
