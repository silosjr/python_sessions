# Changelog

Todas as alterações notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em Keep a Changelog,
e este projeto adere ao Versionamento Semântico.

[Não lançado]
Adicionado
(Adicione aqui as novas funcionalidades em desenvolvimento)

[1.11.0] - 2025-09-07
Adicionado
Implementação do "Explorador de Grelhas Matemáticas" no módulo iterative_process_examples.py, uma ferramenta interativa de linha de comando para gerar e visualizar matrizes de resultados de operações matemáticas.

A nova funcionalidade inclui uma função de ordem superior para o cálculo da grelha e um procedimento de renderização de tabelas com ajuste dinâmico de colunas para otimizar a visualização dos dados.

Alterado
Refatorada a estrutura condicional if/elif para seleção de operações, substituindo-a por um dicionário de mapeamento (OPERATIONS_MAP) para maior clareza e escalabilidade do código.

Extraída a lógica de coleta de dados do utilizador para uma função dedicada (get_grid_intervals_from_user), centralizando a validação de entradas e melhorando a modularidade.

[1.10.0] - 2025-09-06
Added
iterative_process_examples.py:

Adicionada a função calculate_change_breakdown, uma implementação de padrão acadêmico do Algoritmo Guloso (Greedy Algorithm) para a resolução do Problema do Troco (Change-Making Problem).

O algoritmo foi projetado para operar com inteiros (centavos) para garantir a precisão matemática absoluta, uma prática de excelência em software financeiro.

Adicionada a função de interface demonstrate_change_making_algorithm, que orquestra a interação com o usuário e apresenta a decomposição do valor numa tabela de extrato formatada com caracteres de desenho de caixa de linha dupla, para uma apresentação de dados de nível profissional.

Adicionadas constantes de regras de negócio (BRAZILIAN_CURRENCY_DENOMINATIONS) para desacoplar os dados da lógica do algoritmo.

[1.9.0] - 2025-09-05
Added
iterative_process_examples.py:

Adicionada uma simulação completa de um sistema de Ponto de Venda (PDV) interativo, a demonstrate_interactive_pos_session.

O sistema foi arquitetado em três camadas (Dados, Lógica, Interface) para demonstrar o princípio da Separação de Responsabilidades.

Implementado o motor de lógica pura update_shopping_cart, que gerencia o estado do carrinho de forma imutável, seguindo o padrão de design 'state reducer'.

Adicionadas as funções de apresentação display_product_catalog e display_cart_status para renderizar os dados em tabelas formatadas de padrão profissional.

Adicionada a função de cálculo pura calculate_cart_total para encapsular a lógica de negócio de totalização da compra.

[1.11.0] - 2025-09-02
Added
Novo Módulo: statistical_analysis_engine.py: Foi criado um novo módulo de algoritmos, concepts/algorithms/statistical_analysis_engine.py, para abrigar uma nova ferramenta de análise estatística descritiva de alto padrão. Esta adição representa um avanço significativo na arquitetura do projeto, introduzindo um sistema de componentes desacoplados.

Arquitetura de Três Camadas: A nova funcionalidade foi projetada seguindo o princípio da Separação de Responsabilidades, com três componentes distintos:

Coleta de Dados Pura (collect_numeric_data_with_sentinel): Uma função de interface robusta e reutilizável, responsável exclusivamente pela aquisição de uma amostra de dados numéricos do usuário, utilizando um valor de sentinela para a conclusão e tratando cancelamentos de forma inequívoca.

Motor de Cálculo (generate_statistical_report): Uma função de cálculo pura e de ordem superior, que recebe a amostra de dados e um dicionário de operações, aplicando cada cálculo de forma agnóstica.

Orquestração e Apresentação (demonstrate_statistical_analysis_with_sentinel): A função de interface final que orquestra o fluxo, integrando a coleta e o processamento, e exibe os resultados num relatório tabular profissional.

Ferramentas Estatísticas Extensíveis: Foi introduzida a constante STATISTICAL_OPERATIONS, um dicionário que mapeia os nomes das métricas (Soma, Média, etc.) às suas respectivas funções de cálculo (sum, lambda, etc.). Esta abordagem declarativa torna o motor de análise infinitamente extensível a novas métricas sem a necessidade de alterar a lógica de processamento principal.

Changed
Refatoração e Migração de Lógica: A funcionalidade de cálculo de estatísticas agregadas, que existia de forma monolítica no módulo iterative_process_examples.py, foi removida e substituída por esta nova arquitetura superior, eliminando redundância e elevando o padrão de design do projeto.

[1.11.0] - 2025-09-01
Added
Simulador de Amortização de Empréstimo Pessoal: Foi adicionada uma nova e robusta calculadora financeira ao módulo. Esta funcionalidade modela o processo de amortização de uma dívida, proporcionando um exemplo didático de um sistema financeiro que decai com o tempo.

Integração com API do Banco Central: O simulador foi projetado para operar com dados do mundo real, conectando-se à API do Banco Central do Brasil (BCB) através da função fetch_bcb_economic_indicator para obter a taxa de juros média e atual do mercado para empréstimos pessoais não consignados.

Motor de Cálculo Financeiramente Preciso: Foi implementada a função pura calculate_loan_amortization_schedule, que contém o algoritmo de amortização. Este motor realiza a validação de negócio crítica para detetar cenários de "espiral de dívida" e inclui a lógica para o ajuste preciso da última parcela, garantindo a exatidão financeira da simulação.

Interface de Usuário Profissional: Foi criada a função prompt_loan_amortization_simulation para orquestrar a interação com o usuário. A função apresenta um extrato de amortização completo, formatado numa tabela profissional que detalha, mês a mês, a alocação do pagamento entre juros e principal, e a evolução do saldo devedor.

[1.10.0] - 2025-09-01
Changed
Aprimoramento do Simulador Financeiro: A função calculate_simple_savings_projection foi refatorada para aceitar um novo parâmetro opcional, monthly_deposit. Esta alteração transforma a ferramenta de um simples simulador de juros compostos num motor de cálculo para planos de acumulação de capital, com ou sem aportes mensais. A lógica interna foi ajustada para incorporar o depósito ao saldo antes do cálculo do rendimento, garantindo a precisão financeira.

Aprimoramento da Interface de Simulação: A função prompt_simple_savings_simulation foi atualizada para incluir um diálogo com o usuário sobre a inclusão de depósitos mensais. A tabela de resultados agora apresenta uma nova coluna para o "Depósito Mensal", e toda a informação exibida é extraída diretamente da estrutura de dados retornada pelo motor de cálculo, respeitando o princípio da Fonte Única da Verdade.

[1.5.0] - 2025-09-01
Added
Função Auxiliar de Decisão (get_valid_answer_from_user): Adicionada uma nova função auxiliar reutilizável ao módulo practical_conditional_logic.py. Esta ferramenta é projetada para obter uma resposta binária (Sim/Não) do usuário de forma robusta e consistente com a interface do projeto, retornando um valor booleano (True/False) ou None em caso de cancelamento.

[1.9.0] - 2025-09-01
Added
Simulador Financeiro Dinâmico (calculate_simple_savings_projection): Adicionada uma calculadora de projeção de rendimentos para a Caderneta de Poupança. Esta funcionalidade representa um avanço arquitetural significativo, movendo o módulo de calculadoras estáticas para simulações dinâmicas baseadas em dados económicos reais.

Integração com API do Banco Central (fetch_bcb_economic_indicator): Implementada uma nova função auxiliar robusta para consumir a API de Séries Temporais (SGS) do Banco Central do Brasil. Esta função serve como uma ponte segura e resiliente para a obtenção de indicadores económicos em tempo real, exemplificando padrões profissionais de requisições web (requests), tratamento de exceções de rede e análise de dados JSON.

Modelagem de Regras de Negócio Oficiais: O cálculo do rendimento da poupança agora implementa a regra de negócio oficial do Brasil, que é dependente do valor da taxa Selic. As constantes que definem esta regra (SELIC_THRESHOLD_FOR_SAVINGS_YIELD_RULE, etc.) foram externalizadas, promovendo a manutenibilidade e a clareza do código.

Interface de Simulação (prompt_simple_savings_simulation): Criada a função de interface com o usuário para a nova simulação, que orquestra a coleta de dados, a chamada ao motor de cálculo e a apresentação de um extrato mensal detalhado e profissionalmente formatado.

[1.8.0] - 2025-08-31
Added
Demonstração de Sessão de Quiz (demonstrate_quiz_session): Adicionada uma nova função ao módulo iterative_process_examples.py. Esta função refatora um snippet de quiz em um motor de quiz genérico, ensinando o princípio da Separação de Responsabilidades ao modelar as perguntas e respostas como uma estrutura de dados externa (QUIZ_DATA). A implementação também demonstra o gerenciamento de estado em laços, o uso de enumerate para numeração, e técnicas de formatação para uma interface de usuário robusta e gramaticalmente correta.

[1.7.0] - 2025-08-31
Added
Demonstração de Divisão via Subtração (demonstrate_division_with_subtraction): Adicionada uma nova função ao módulo iterative_process_examples.py. Esta função demonstra, de forma didática, como a operação de divisão inteira (quociente e resto) pode ser simulada através da subtração repetida.

Função de Cálculo Pura (divide_by_subtraction): Implementada uma função auxiliar que isola a lógica de cálculo, servindo como um exemplo claro do princípio de Separação de Responsabilidades e um par conceitual para a função de multiplicação via adição.

[1.6.0] - 2025-08-30
Added
Demonstração de Multiplicação via Adição (demonstrate_multiplication_with_addition): Adicionada uma nova função ao módulo iterative_process_examples.py. Esta função demonstra, de forma didática, como a operação de multiplicação pode ser simulada através da adição repetida.

Função de Cálculo Pura (multiply_by_addition): Implementada uma função auxiliar que isola a lógica de cálculo, servindo como um exemplo claro do princípio de Separação de Responsabilidades e de um algoritmo de acumulação.

[1.5.0] - 2025-08-29
Added
Demonstração de Tabuada Customizável (demonstrate_custom_multiplication_table): Adicionada uma nova função ao módulo iterative_process_examples.py. Esta função demonstra a geração de uma tabuada de multiplicação com base, início e fim definidos pelo usuário.

Ensino de Formatação Dinâmica: A nova função implementa um padrão profissional de formatação de saída, calculando dinamicamente a largura das colunas para garantir um alinhamento perfeito, servindo como um exemplo avançado do uso de f-strings.

[1.4.0] - 2025-08-29
Changed
Generalização da Função de Filtragem: A função demonstrate_generation_of_filtered_numbers foi significativamente refatorada e renomeada para demonstrate_custom_filtering.

Added
Suporte para Filtragem Customizável: A função demonstrate_custom_filtering agora opera como uma Função de Ordem Superior, aceitando um predicado (Callable) como argumento. Isto permite a geração de sequências numéricas com qualquer regra de filtragem, como demonstrado na função main com o uso de funções lambda para gerar números ímpares e múltiplos de 3.

[1.3.0] - 2025-08-29
Added
Demonstração de Geração de Sequência Filtrada (demonstrate_generation_of_filtered_numbers): Adicionada uma nova função ao módulo iterative_process_examples.py. Esta função serve como um exemplo didático da combinação de um processo iterativo com uma lógica de decisão para filtrar dados.

Ensino de List Comprehension com Filtro: A nova função foi implementada utilizando uma List Comprehension com uma cláusula if, ensinando uma técnica "Pythonica" avançada para a criação de listas baseadas em condições.

Changed
A função main() em iterative_process_examples.py foi atualizada para incluir a chamada à nova demonstração.

[1.2.0] - 2025-08-29
Added
Demonstração de Contagem Regressiva (demonstrate_iterative_countdown): Adicionada uma nova função ao módulo iterative_process_examples.py. Esta função serve como um exemplo didático de um processo iterativo decrescente, utilizando a função range() com um passo negativo.

Par Pedagógico Iteração vs. Recursão: A nova função foi projetada para ser um contraponto direto à função recursiva countdown, enriquecendo o valor didático do projeto ao permitir a comparação entre as duas abordagens para resolver o mesmo problema.

Changed
A função main() em iterative_process_examples.py foi atualizada para incluir a chamada à nova demonstração.

[1.1.0] - 2025-08-29
Added
Novo Módulo (iterative_process_examples.py): Criado um novo módulo na pasta concepts/foundations para abrigar exemplos didáticos focados em processos iterativos e laços de repetição.

Demonstração de Contagem Simples (demonstrate_simple_counting): Adicionada a primeira função ao novo módulo. Esta função refatora um snippet de contagem simples, transformando-o em uma demonstração interativa e robusta que ensina a coleta de dados, validação e o uso de padrões de formatação como List Comprehension e .join().

Reutilização de Código: A nova função importa e reutiliza a ferramenta get_valid_integer_from_user do módulo de lógica condicional, demonstrando a modularidade do projeto.

[1.4.0] - 2025-08-28
Added
Demonstração de Status Acadêmico (determine_academic_status): Adicionada uma nova função ao módulo practical_conditional_logic.py para demonstrar uma cadeia if/elif/else na classificação da média de um aluno.

Função Auxiliar de Entrada para float (get_valid_float_from_user): Criada uma nova função auxiliar reutilizável para a solicitação e validação de números de ponto flutuante, expandindo a "caixa de ferramentas" de entrada do módulo.

Validação de Domínio: A função determine_academic_status agora inclui uma validação de domínio para garantir que a média inserida pelo usuário esteja dentro do intervalo válido (0-10).

Changed
A função main() em practical_conditional_logic.py foi atualizada para incluir a chamada à nova demonstração de status acadêmico.

[1.3.0] - 2025-08-28
Added
Demonstração de Saudação Contextual (demonstrate_time_of_day_greeting): Adicionada uma nova função ao módulo practical_conditional_logic.py para demonstrar uma cadeia if/elif/else que seleciona uma saudação apropriada com base na hora atual do sistema.

Uso do Módulo datetime: A nova demonstração foi implementada utilizando o módulo datetime para obter a hora do sistema de forma robusta, seguindo o princípio de "Fonte Única da Verdade" para derivar os dados para a lógica e para a apresentação.

Changed
A função main() em practical_conditional_logic.py foi atualizada para incluir a chamada à nova demonstração de saudação.

[1.2.0] - 2025-08-28
Added
Demonstração de Classificação por Faixas (demonstrate_classification_of_numbers_by_range): Adicionada uma nova função ao módulo practical_conditional_logic.py para demonstrar a estrutura if/elif/else na classificação de um número em faixas de valores.

Uso de Faixas Dinâmicas: A nova demonstração utiliza o módulo random para gerar os limites das faixas a cada execução, tornando o exemplo mais interativo e didático.

Comparações Encadeadas: O código exemplifica o uso da sintaxe de comparações encadeadas (min <= valor < max), uma prática recomendada em Python para verificar se um valor se encontra num intervalo.

Changed
A função main() em practical_conditional_logic.py foi atualizada para incluir a chamada à nova demonstração de classificação.

[1.1.0] - 2025-08-26
Added
Demonstração de Comparação Numérica (compare_two_numbers): Adicionada uma nova função ao módulo practical_conditional_logic.py para demonstrar de forma interativa a estrutura de controle if/elif/else, comparando dois números inteiros fornecidos pelo usuário.

Função Auxiliar de Entrada (get_valid_integer_from_user): Criada uma função auxiliar reutilizável para encapsular a lógica de solicitação e validação de entrada de números inteiros. Esta função implementa um tratamento de erros robusto e permite que o usuário cancele a operação de forma graciosa, retornando Optional[int].

Changed
Arquitetura de Código: A função compare_two_numbers foi refatorada para utilizar a nova função auxiliar, promovendo o princípio DRY (Don't Repeat Yourself) e melhorando a legibilidade e a manutenibilidade do código.

A função main() em practical_conditional_logic.py foi atualizada para incluir a chamada à nova demonstração de comparação.

[1.9.0] - 2025-08-26
Added
Simulador de Fatura de Energia Elétrica: Adicionada uma nova e complexa calculadora ao módulo practical_calculators.py para simular a faturação de energia elétrica com base em tarifas progressivas.

Função de Cálculo Pura (calculate_electricity_bill_details): Implementada para encapsular a lógica de negócio de tarifação por faixas (tiered billing). A função é robusta, com validação de ValueError e KeyError.

Função de Simulação (run_electricity_bill_simulation): Criada para orquestrar uma simulação não-interativa, demonstrando um cenário de uso realista e apresentando uma fatura profissionalmente formatada.

Modelagem de Dados para Tarifas (ELECTRICITY_TARIFFS_CONFIG): As complexas regras de negócio das tarifas de energia foram desacopladas da lógica e modeladas como um dicionário de dicionários, garantindo alta manutenibilidade e escalabilidade.

Changed
A função main() em practical_calculators.py foi atualizada para incluir a chamada ao novo simulador de fatura de energia.

[1.8.0] - 2025-08-25
Added
Simulador de Financiamento Imobiliário: Adicionada uma nova calculadora ao módulo practical_calculators.py para analisar a viabilidade de um financiamento.

Função de Análise Pura (analyze_loan_viability): Implementada para encapsular a lógica de negócio do cálculo da prestação mensal e da verificação contra a taxa máxima de comprometimento de renda. A função retorna um dicionário estruturado com o dossiê completo da análise.

Função de Interface (prompt_loan_viability_analyzer): Criada para gerir a interação com o utilizador, com tratamento robusto de erros e uma apresentação de resultados formatada profissionalmente.

Constante de Regra de Negócio (MAX_INCOME_COMMITMENT_RATE): Adicionada para isolar a taxa de 30% de comprometimento de renda, melhorando a manutenibilidade.

Changed
A função main() em practical_calculators.py foi atualizada para incluir a chamada ao novo simulador de financiamento.

[1.7.0] - 2025-08-25
Added
Calculadora Aritmética Básica: Adicionada uma nova calculadora ao módulo practical_calculators.py para realizar as quatro operações aritméticas fundamentais.

Função de Cálculo Pura (perform_arithmetic_operation): Implementada com um padrão de mapeamento (dispatch dictionary) usando o módulo operator, substituindo if/elif/else para maior clareza e escalabilidade. A função inclui validação robusta para operadores inválidos e divisão por zero, levantando exceções específicas.

Função de Interface (prompt_basic_calculator): Criada para gerenciar a interação com o usuário, com um tratamento de exceções unificado que captura ValueError e ZeroDivisionError, garantindo que o programa não encerre inesperadamente e forneça feedback claro.

Changed
A função main() em practical_calculators.py foi atualizada para incluir a chamada à nova calculadora aritmética.

[1.6.0] - 2025-08-25
Added
Calculadora de Conta de Celular: Adicionada uma nova funcionalidade ao módulo practical_calculators.py para simular o cálculo de uma fatura de telefonia móvel.

Função de Simulação (run_phone_bill_simulation): Implementada uma função de interface não-interativa que simula um cenário de uso real, selecionando um plano e um consumo de minutos de forma aleatória para gerar um extrato detalhado.

Função de Cálculo Pura (calculate_phone_bill_details): Criada uma função de lógica de negócio que recebe um plano e um consumo, retornando um dicionário estruturado com o detalhamento completo da fatura (custo base, minutos excedentes, custo extra e total).

Modelagem de Dados para Planos (MOBILE_PHONE_PLANS): As regras de negócio dos planos de celular foram desacopladas da lógica e modeladas como uma constante estruturada (dicionário de dicionários), melhorando a manutenibilidade e escalabilidade do código.

Changed
A função main() em practical_calculators.py foi atualizada para incluir a chamada à nova simulação de fatura de celular.

Editado - 2025-08-24
(README.md): Alterações que representam a estrutura hierárquica atual do repositório.

Editado - 2025-08-23
(README.md): Alterações que representam a estrutura hierárquica atual do repositório.

[1.0.0] - 2025-08-24
Adicionado
(concepts/foundations): Inserção de `practical_conditional_logic.py`.

[1.0.0]
Adicionado
(concepts/algorithms): Inserção de `comparison_algorithms.py`

[1.5.0]
Refatorado
(concepts/foundations): Refatoração e inclusão de novas funções à `practical_calculators.py`.

[1.0.0] - 2025-08-23
Adicionado
(diagrams): Inserção de script `stack_trace_analysis.md`.

[1.0.0] - 2025-08-23
Adicionado
(concepts/foundations): Inserção de script `function_return_values_and_design.py`.

[1.0.0] - 2025-08-23
Adicionado
(concepts/algorithms): Inserção de script `practical_recursive_examples.py`.

Editado  - 2025-08-22
(README.md): Alterações que representam a atual estrutura hierárquica do repositório.

[1.3.0] - 2025-08-22
Adicionado
(concepts/foundations): Inserção de script `practical_calculators` com refatoração em funções que oferecem respaldo para uso de constante ao invés de variáveis.

[1.1.0] - 2025-08-22
Editado
(concepts/foundations): Inserção das funções `demonstrate_operator_precedence()`, `demonstrate_assignment_and_types()` e `demonstrate_boolean_logic()` ao script `expressions_and_statements`.

[1.0.0] - 2025-08-22
Adicionado
(concepts/foundations): Inserções dos scripts `epoch_time_converter.py`, `conditional_logic.py` e `recursion_and_stack`, adaptação da estrutura hierárquica do README.md que corresponda às atualizações e adição de `run_sessions` à seção `.gitignore`.

[1.0.0] - 2025-08-21
Adicionado
(concepts/foundations): Inserção de script `functions_design_and_composition.py` e alteração do README.md para
corresponder às alterações.

[1.0.0] - 2025-08-20
Adicionado
(concepts/foundations): Inserção de script `functions_composition_and_flow.py` e alteração do README.md para corresponder às mudanças.

[1.0.0] - 2025-08-19
Adicionado
(concepts/foundations): Inserção de script `control_flow_and_recursion.

[1.0.0] - 2025-08-19
Adicionado
(diagrams/recursive_stack_diagram.puml): Inserção de diagrama de pilha para função `countdown()` de `control_flow_and_recursion`.
(README.md): Alteração da estrutura hierárquica de modo a corresponder às novas inserções.

[1.0.0] - 2025-08-18
Adicionado
(concepts/foudantions): Inserção de script `expressions_and_statements.py` e atualização da estrutura hierárquica no README.md após inclusão de novo script.

[1.0.0] - 2025-08-18
Adicionado
(concepts/foundations): Inserção de script `unit_conversion_calculator.py`, indicação de status de versão em `syntax_and_operators` e atualização da estrutura hierárquica no README.md após inclusão de novo script.

[1.0.0] - 2025-08-18
Adicionado
(concepts/foundations): Criação de subpasta e inserção do script `syntax_and_operators.py`.
Alterado
(README.md): inclusão no `README.md` de nova estrutura de pastas.

[1.0.0] - 2025-08-18
Alterado
(concepts/algorithms): Descarte do script original binary_search.py e criação de um novo sob mesma nomenclatura com abordagem voltada para experiência de tentativa de acertos por parte da máquina, deixando o controle de dicas em mãos do usuário.

[3.0.0] - 2025-08-17
Adicionado
(projects/poker_hand_analyzer): Adicionado um novo projeto completo para análise e simulação de mãos de Pôquer, incluindo a classe PokerHand com lógica de classificação detalhada.

(utils/project_setup.py): Criado um novo módulo de utilidade para configurar o sys.path de forma robusta, garantindo que as importações relativas funcionem em diferentes ambientes de execução.

Alterado
(concepts/card_game_inheritance.py): O método deal_hands na classe Deck foi refatorado para ser uma "fábrica" flexível, aceitando um parâmetro hand_class para instanciar diferentes tipos de mãos (ex: Hand, PokerHand).

[2.3.0] - 2025-08-17
Adicionado
(concepts/object_oriented_programming): A classe Deck no script card_game_inheritance.py foi aprimorada com o novo método deal_hands.

[2.2.1] - 2025-08-16
Corrigido
(concepts/natural_language_processing): A lógica de caminho de arquivo em markov_analyzer.py foi refatorada para usar pathlib.

## [2.3.0] - 2025-08-17

### Novidades Adicionadas

- **(concepts/object_oriented_programming)**: A classe `Deck` no script `card_game_inheritance.py` foi aprimorada com o novo método `deal_hands`, que simula a distribuição de cartas para múltiplas mãos.

## [1.1.0] - 2025-08-16

### Alterado

- Estrutura do projeto reorganizada:
  - Alterações registradas na estrutura hierárquica do README.md.
  - Criada a subpasta `algorithms` dentro da pasta `concepts`.
  - Adicionado o script `binary_search.py` dentro de `concepts/algorithms`.
- Objetivo:
  - Melhorar a organização dos módulos didáticos, separando algoritmos individuais por tema.

## [1.0.0] - 2025-08-16

### Adicionado

- Módulo de **Busca Binária Genérica** com tipagem segura (`TypeVar` + `Protocol`).
- Função `binary_search(sequence: List[T], item: T) -> int | None`:
  - Localiza o índice de um elemento em sequências ordenadas.
  - Retorna `None` se o elemento não estiver presente.
- Protocolo `Comparable` para garantir que os elementos suportem `<`, `>`, `==`.
- Exemplo de execução interativa no bloco `__main__`.
- Compatível com qualquer tipo comparável (`int`, `float`, `str`, etc.) em Python 3.10+.

## [1.0.1] - 2025-08-16

## Adicionado (versão 1.0.1)

- **Script Python (`uml_model.py`)**:
  - Implementada a estrutura básica para modelagem de objetos orientados a classes em Python.
  - Adicionadas as classes:
    - `PythonObject`: Superclasse abstrata para elementos representáveis em UML.
    - `ClassDef`: Representa uma definição de classe Python com métodos associados.
    - `Method`: Representa um método vinculado a uma instância de `ClassDef`.
  - Uso de docstrings exaustivas e type hints para fins educacionais.
  - Definido propósito didático para uso em análise ou geração de diagramas UML.
  - Metadados do módulo incluídos: autor, versão, e status de desenvolvimento.

- **Diagrama UML PlantUML (`class_relation_diagram.puml`)**:
  - Criado o diagrama UML que representa as relações de herança e composição entre as classes:
    - `ClassDef` e `Method` herdam de `PythonObject`.
    - `ClassDef` contém múltiplos `Method` (composição).
  - Comentários explicativos sobre os elementos UML utilizados.
  - Alinhamento com o modelo Python implementado no módulo `uml_model.py`.

[2.2.1] - 2025-08-16
Corrigido
(concepts/natural_language_processing): A lógica de caminho de arquivo em markov_analyzer.py foi refatorada para usar pathlib, tornando a localização do arquivo de texto padrão (emma.txt) robusta e independente do diretório de execução do script.

[2.2.0] - 2025-08-15
Added

Funções auxiliares find_defining_class e print_attributes para introspecção e depuração.

Arquivo CHANGELOG.md para documentar as alterações.

Changed
O script find_defining_class foi movido para o módulo utils/debug_tools.py para melhor organização e reutilização do código.

A versão do script debug_tools.py foi sincronizada para 2.2.0 para refletir a versão do projeto principal.

[2.2.0] - 2025-08-15
Adicionado
(concepts/object_oriented_programming): Adicionado o script card_game_inheritance.py, um estudo de caso sobre Herança em POO, com as classes Card, Deck e Hand.

[2.1.0] - 2025-08-15
Alterado
(concepts): Aprimorada a organização da biblioteca de conceitos com a criação da subpasta /object_oriented_programming para agrupar todos os scripts relacionados à POO.

(concepts): Movidos os scripts custom_time.py, geometric_analysis.py, time_encapsulation.py e kangaroo_puzzle.py para a nova subpasta de POO.

[2.0.0] - 2025-08-14
Alterado
Estrutura do Repositório: O projeto foi completamente reestruturado em uma arquitetura de pastas (/projects, /concepts, /utils) para separar aplicações, exemplos de conceitos e ferramentas reutilizáveis. Esta é uma mudança fundamental na organização do projeto.

(concepts/custom_time.py): A classe Time foi extensivamente refatorada para um modelo orientado a objetos, com a lógica de funções externas movida para métodos de instância (**init**, **str**, **add**, **radd**, to_seconds, etc.).

(concepts/geometric_analysis.py): A classe Point foi aprimorada com o método **add**, que agora suporta despacho por tipo para somar com outros objetos Point ou com tuplas.

Adicionado
(utils/debug_tools.py): Criado o primeiro módulo de utilidades, contendo a função print_attributes para inspeção genérica de objetos.

Removido
(projects/bmi): Removido o script duplicado bmi_calculator.py para manter uma única fonte de verdade no projeto (bmi.py).

Diversas funções globais (time_to_integer, print_time, is_after, etc.) foram removidas e sua lógica foi incorporada como métodos nas classes correspondentes.

[1.0.0] - 2025-08-12
Esta versão representa o estado do projeto antes da grande reestruturação. O histórico detalhado foi arquivado.

Adicionado
Versão inicial dos projetos contacts, hangman, bmi, e dos scripts de conceitos custom_time e geometric_analysis.
