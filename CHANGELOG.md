# Changelog

Todas as alterações notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em Keep a Changelog,
e este projeto adere ao Versionamento Semântico.

[Não lançado]
Adicionado
(Adicione aqui as novas funcionalidades em desenvolvimento)

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
