# TODO Projeto da disciplina de grafos

## Código e experimentos

- Entender modelo IGMC
- Entender camada convolucional RGCNConv (?)
- Entender treinamento
- Revisar tudo
- Treinar com flag `debug`
- Avaliar em termos de RMSE
- Gerar visualizações dos grafos (treino ou teste)
- Gerar estatísticas e levantar metadata (via logs):
  - Dataset original:
    - número de avaliações
    - número de usuários
    - número de ítens
    - densidade
    - intervalo numérico de valores das avaliações
  - Demais datasets (processado):
    - Dataset de treinamento:
      - LEVANTAR OS MESMOS DADOS
    - Dataset de teste:
      - LEVANTAR OS MESMOS DADOS
  - Exemplo do dataset (um subgrafo extraído):
    - ...
  - Modelo:
    - número de parâmetros
      - GNN
      - MLP
      - outros que eu esqueci (?)
      - total
    - número de camadas (4?)
  - Treinamento:
    - listar hiperparâmetros:
      - ...
    - gráfico da loss
      - treinamento
      - teste (?)
      - validação (?)
    - gráfico do RMSE
      - apenas teste

## Apresentação

**Deixar código aberto: google colab e vs code.**

Tópicos:

1. Introdução
    - definição de sistema de recomendações
    - filtragem colaborativa
2. Formulação do problema
    - matrix completion
    - grafo bipartido
3. Proposta
    - utilizar uma rede neural para grafos para tentar prever a avaliação que um usuário `u` daria a um item `v`.
4. Elementos básicos de aprendizado profundo
   1. Redes neurais
   2. Função matemática
   3. Não linear
   4. Parâmetros "treináveis"
   5. Função de perda
   6. Backpropagation
   7. Métrica de avaliação
5. IGMC
   1. **Extração de subgrafos:**
      - fazer com imagens
      - lembrar de mostrar extração de subgrafos e rotulamento de nós
   2. **Arquitetura da GNN:**
      - camada convolucional (R-GCN)
      - representação final dos nós
      - camada de pooling (`concat()`)
   3. MLP:
      - equação
   4. Função de custo:
      - equação
      - **CITAR BACKPROP PARA QUEM NÃO SABE REDES NEURAIS**
   5. Adjacent rating regularization (ARR):
      - equação
   6. Função de custo regularizada:
      - equação
6. Experimentos:
   1. Arquitetura superficial do código
      1. Baixa o banco de dados
      2. Faz um pré-processamento nos dados
      3. Cria bancos de dados dinâmico (extrai por demanda)
      4. Cria o modelo do IGMC
      5. Treina
      6. Mostra resultados e logs
   2. Mostrar estatísticas
   3. Mostrar exemplos do banco de dados de teste
   4. Mostrar avaliação da rede
7. FIM


**ORDENAR:**

- Algoritmo de extração de subgrafos:
  - fazer com imagens
- Arquitetura básica do código:
- Arquitetura do IGMC:
  - Camada de convolução espacial para grafos:
    - citar dimensões das camadas escondidas (?)
    - citar decomposição em base para reduzir número de parâmetros (?)
  - MLP:
    - dropout (drop rate = 0.2)