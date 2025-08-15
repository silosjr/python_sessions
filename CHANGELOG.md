Changelog
Todas as alterações notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em Keep a Changelog,
e este projeto adere ao Versionamento Semântico.

[Não lançado]
Adicionado
(Adicione aqui as novas funcionalidades em desenvolvimento)
[2.2.0] - 2025-08-15
Added

Funções auxiliares find_defining_class e print_attributes para introspecção e depuração.

Arquivo CHANGELOG.md para documentar as alterações.

Código de teste no bloco if __name__ == '__main__' para provar a herança do método sort na classe Hand.

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

(concepts/custom_time.py): A classe Time foi extensivamente refatorada para um modelo orientado a objetos, com a lógica de funções externas movida para métodos de instância (__init__, __str__, __add__, __radd__, to_seconds, etc.).

(concepts/geometric_analysis.py): A classe Point foi aprimorada com o método __add__, que agora suporta despacho por tipo para somar com outros objetos Point ou com tuplas.

Adicionado
(utils/debug_tools.py): Criado o primeiro módulo de utilidades, contendo a função print_attributes para inspeção genérica de objetos.

Removido
(projects/bmi): Removido o script duplicado bmi_calculator.py para manter uma única fonte de verdade no projeto (bmi.py).

Diversas funções globais (time_to_integer, print_time, is_after, etc.) foram removidas e sua lógica foi incorporada como métodos nas classes correspondentes.

[1.0.0] - 2025-08-12
Esta versão representa o estado do projeto antes da grande reestruturação. O histórico detalhado foi arquivado.

Adicionado
Versão inicial dos projetos contacts, hangman, bmi, e dos scripts de conceitos custom_time e geometric_analysis.