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

### 1.9.0 (2025-08-05)

- Adicionado: O programa agora controla a data de aniversário e o e-mail de cada contato, com validação de entrada opcional em edições.

### 1.10.0 (2025-08-05)

- Adicionado: O programa agora permite registrar múltiplos telefones para cada contato, associando um tipo (ex: 'celular', 'residencial') a cada número.

## [1.10.0] - 2025-08-06

### Adicionado

- Implementada a capacidade de adicionar múltiplos telefones a um único contato.
- Adicionada a classificação de telefones por tipo (Residencial, Celular, etc.).

### Modificado

- Refatorada a estrutura de dados de contato para armazenar telefones em um dicionário (`Dict[str, str]`) em vez de uma string única.
- Atualizadas as funções `add_contact`, `update_contact` e `show_data` para serem compatíveis com a nova estrutura de dados de telefones.
- Aprimorada a função `ask_phones` para permitir a edição de um dicionário de telefones existente, tornando a atualização de contatos mais intuitiva.

## [1.0.1] - 2025-08-06

### Changed

- Melhorada a experiência do jogador com a adição de um cronômetro para medir a duração de cada partida.

## [1.0.0] - (Data da versão anterior)

### Added

- Versão inicial do jogo da forca.
- Lógica para carregar palavras de `words.txt`.
- Desenho do enforcado em ASCII art.

## [1.11.0] - 2025-08-08

### Changed

- **Refatoração do Sistema de Persistência:** O sistema de salvamento de arquivos foi completamente alterado do formato de texto simples (`.txt`) para o formato JSON (`.json`).
- **Estrutura de Dados Interna:** A estrutura de dados para cada contato foi alterada de uma lista para um dicionário, tornando o código mais legível e robusto.

### Added

- **Validação de Erros Aprimorada:** O carregamento de arquivos agora trata casos de arquivo corrompido ou com formato JSON inválido.
