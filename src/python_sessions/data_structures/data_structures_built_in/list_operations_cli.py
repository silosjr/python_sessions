"""
Módulo de interface de Linha de Comando (CLI) para Operações com Listas.

Este módulo implementa a camada de interação com o operador para as
funcionalidades de operações com listas. Sua única responsabilidade é
gerenciar o ciclo de vida da aplicação (REPL), a apresentação da UI, a
aquisição e validação da entrada do operador, e a orquestração das
chamadas aos componentes de lógica de negócio puros, que são importados
do módulo `list_operations_showcase`. A arquitetura adere estritamente ao
Princípio da Responsabilidade Única.
"""

from __future__ import annotations
from typing import (
    List
)
from python_sessions.utils.input_handlers import (
    get_valid_integer_from_user,
    get_valid_float_from_user,
    cli_pause
)
from python_sessions.utils.constants import (
    USER_CANCELLED_OPERATION_MESSAGE,
    PADDING_WIDTH,
    ERROR_INVALID_MENU_OPTION,
    SELECTED_OPTION_INPUT,
    SESSION_TERMINATED_MESSAGE
)
from python_sessions.data_structures.data_structures_built_in.list_operations_showcase import (
    calculate_average,
    partition_by_predicate
)
__author__ = 'Enock Silos'
__version__ = '0.3.0'
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

def _handle_average_calculation() -> None:
    """
    Orquestra o fluxo de UI para a coleta e cálculo da média.

    Atua como o manipulador de interface para a funcionalidade de cálculo
    de média. É responsável por todas as interações com o operador,
    incluindo a solicitação de parâmetros, a validação de entradas no
    contexto da UI, a invocação da lógica de negócio (`calculate_average`)
    e a formatação da saída. O tratamento de cancelamento pelo usuário é
    gerenciado nesta camada para garantir feedback operacional explícito.
    """
    prompt = ' Informe a quantidade de amostras a ser coletada (inteiro > 0) ou ("Q" para encerrar): '
    sample_size = get_valid_integer_from_user(prompt)
    if sample_size is None:
        print(USER_CANCELLED_OPERATION_MESSAGE)
        return

    if sample_size <= 0:
        print('\n ERRO: A quantidade de amostras deve ser um valor inteiro positivo. Encerrando.\n')
        return

    samples = []

    for i in range(1, sample_size + 1):
        prompt = f' Valor da amostra {i} / {sample_size} ("Q" para encerrar) → '
        sample_value = get_valid_float_from_user(prompt)
        if sample_value is None:
            print(USER_CANCELLED_OPERATION_MESSAGE)
            return
        
        samples.append(sample_value)

    average = calculate_average(samples)
    print(f'\n A média de {len(samples)} amostras coletadas é [ {average:.2f} ]')

def _handle_partition_operation() -> None:
    """
    Gerencia o fluxo de UI para a operação de particionamento de dados.

    Esta função serve como a camada de interface para a funcionalidade de
    particionamento de dados. Ela orquestra a aquisição de um conjunto de
    dados numéricos do operador, define o predicado de classificação
    (neste caso, `n > 0`), invoca o motor de particionamento genérico
    `partition_by_predicate`, e apresenta os dois conjuntos de dados
    resultantes de forma explícita e formatada.
    """
    collected_data: List[int] = []
    prompt = ' Digite um número inteiro ("Q" para encerrar) ou (0 (zero) para iniciar o processamento): '
    while True:
        integer_input = get_valid_integer_from_user(prompt)
        if integer_input is None:
            print(USER_CANCELLED_OPERATION_MESSAGE)
            return
        
        if integer_input == 0:
            break

        collected_data.append(integer_input)

    predicate = lambda n: n > 0
        
    positives, non_positives = partition_by_predicate(collected_data, predicate)
    print(f' Partição 1 (Predicado: n > 0) → {positives}')
    print(f' Partição 2 (Predicado: n <= 0) → {non_positives}')

def _display_menu() -> None:
    """
    Renderiza o menu principal da aplicação na saída padrão.

    Esta função é um componente de apresentação, responsável exclusivamente
    pela exibição do menu de opções disponíveis para o operador. A formatação
    é padronizada para garantir uma interface de usuário consistente.
    """
    operations_menu = [
        ' MENU DE CÁLCULOS ESTATÍSTICOS',
        ' Por favor, selecione a operação a ser executada:',
        ' [1] - Cálculo da Média',
        ' [2] - Particionamento de Dados',
        ' [Q] - Encerrar sessão'
    ]
    content_width = max(len(line) for line in operations_menu)
    internal_width = content_width + PADDING_WIDTH

    top_border = f'╔{'═' * (internal_width)}╗'
    middle_border = f'╠{'═' * (internal_width)}╣'
    bottom_border = f'╚{'═' * (internal_width)}╝'

    title = operations_menu[0]
    header_line = f'║{title:^{internal_width}}║'

    print(top_border)
    print(header_line)
    print(middle_border)

    for line in operations_menu[1:]:
        padded_line = f'  {line}'
        print(f'║{padded_line:<{internal_width}}║')

    print(bottom_border)

def _handle_user_choice(selected_option: str) -> None:
    """
    Atua como despachante de comandos da interface de usuário.

    Esta função interpreta a seleção do operador e delega o fluxo de controle
    para o manipulador de UI apropriado. Atua como um ponto de roteamento
    central, desacoplando o laço principal da implementação específica de
    cada funcionalidade.

    Args:
        selected_option (str): A opção fornecida pelo usuário, captura
                               pelo laço principal.
    """
    if selected_option == '1':
        _handle_average_calculation()
    elif selected_option == '2':
        _handle_partition_operation()
    else:
        print(ERROR_INVALID_MENU_OPTION)

def main() -> None:
    """
    Função principal que orquestra o ciclo de vida da aplicação (REPL).

    Ponto de entrada do programa. Implementa um laço de Leitura-Avaliação-
    Impressão (Read-Eval-Print Loop) que gerencia o estado da sessão do
    operador. É responsável por exibir o menu, capturar a entrada do
    usuário e despachar a ação correspondente, tratando também da condição
    de terminação do programa.
    """
    while True:
        _display_menu()
        selected_option = input(SELECTED_OPTION_INPUT)

        if selected_option.lower() == 'q':
            print(SESSION_TERMINATED_MESSAGE)
            break

        _handle_user_choice(selected_option)

        if selected_option in ('1', '2'):
            cli_pause()

if __name__ == '__main__':
    main()