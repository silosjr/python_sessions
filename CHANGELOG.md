# Changelog

Todas as alterações notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em Keep a Changelog,
e este projeto adere ao Versionamento Semântico.

[Não lançado]
Adicionado
(Adicione aqui as novas funcionalidades em desenvolvimento)

Editado  - 2025-08-22
(README.md): Alterações que se representam a atual estrutura hierárquica do repositório.

[1.3.0] -2025-08-22
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
