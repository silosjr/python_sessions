Changelog
Todas as alterações notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em Keep a Changelog,
e este projeto adere ao Versionamento Semântico.

[Não lançado]
Adicionado
(Adicione aqui as novas funcionalidades em desenvolvimento)

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