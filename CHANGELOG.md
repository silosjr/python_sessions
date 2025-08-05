# Changelog

Todas as alterações notáveis deste projeto serão documentadas neste arquivo.

## [1.0.0] - 2025-08-03

### Added

-   Primeiro script didático: `percentage_and_formatting.py`.
-   Documentação do projeto no `README.md` com estrutura e detalhes da Sessão 1.
-   Arquivo `.gitignore` para ignorar arquivos de sistema e de cache.
-   Informações de autoria (`__author__`, `__version__`, etc.) no script.

### Changed

-   Refatoração da função `calculate_new_salary` para uma lógica matemática mais concisa.

### Fixed

-   Inconsistência na nomenclatura de variáveis no bloco de execução para aderir aos padrões em inglês e snake_case.
-   Erro de digitação no nome da variável `final_salary`.

### 1.1.0 (2025-08-05)
- Adicionado: O menu principal agora exibe o número total de contatos na agenda.

### 1.1.1 (2025-08-05)
- Corrigido: O separador de contatos foi alterado para `∴` para evitar falhas ao lidar com nomes ou telefones que contenham caracteres especiais.

### 1.2.0 (2025-08-05)
- Adicionado: A função de listagem de contatos agora exibe a posição de cada contato na agenda.

### 1.3.0 (2025-08-05)
- Adicionado: O menu principal agora inclui a opção de ordenar a lista de contatos por nome em ordem alfabética.

### 1.4.0 (2025-08-05)
- Adicionado: As funções de alterar e apagar contatos agora solicitam uma confirmação do usuário antes de efetuar a operação.

### 1.5.0 (2025-08-05)
- Adicionado: Implementada uma variável de controle para verificar alterações não salvas antes de ler ou gravar um arquivo, prevenindo a perda de dados.

### 1.6.0 (2025-08-05)
- Adicionado: O programa agora carrega automaticamente a última agenda usada ao ser iniciado.

### 1.7.0 (2025-08-05)
- Adicionado: As funções `ask_name` e `ask_phone` agora aceitam um parâmetro opcional para exibir um valor padrão, melhorando a experiência do usuário na edição de contatos.

### 1.8.0 (2025-08-05)
- Adicionado: O programa agora verifica a repetição de nomes ao adicionar ou alterar contatos, garantindo a unicidade dos registros.