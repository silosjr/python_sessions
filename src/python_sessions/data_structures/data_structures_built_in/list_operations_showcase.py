"""
Módulo de operações com listase sua interface de usuário.

Este módulo fornece um conjunto de componentes de software para a manipulação
da estrutura de dados `list` do Python. A arquitetura adere estritamente ao
Princípio de Responsabilidade Única (SRP), isolando a lógica de negócio pura
em funções determinísticas e agnósticas ao contexto, enquanto a interação com
o operador é gerenciada por uma camada de interface de usuário (UI) dedicada.

O artefato serve como um laboratório prático para conceitos fundamentais de
estruturas de dados, implementado sob os paradigmas de desenvolvimento para
sistemas de missão crítica.
"""

from __future__ import annotations
from typing import List
from python_sessions.utils.constants import (
    PADDING_WIDTH,
    ERROR_INVALID_MENU_OPTION,
    SELECTED_OPTION_INPUT,
    SESSION_TERMINATED_MESSAGE,
    USER_CANCELLED_OPERATION_MESSAGE
)
from python_sessions.utils.input_handlers import (
    get_valid_float_from_user,
    get_valid_integer_from_user,
    cli_pause
)

__author__ = 'Enock Silos'
__version__ = '0.3.0' 
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Developmet'

def calculate_average(samples: List[float]) -> float:
    """
    Computa a média aritmética de uma coleção de amostras.

    Esta função implementa o algoritmo para o cálculo da média aritmética.
    Opera como um componente de lógica pura: é uma função determinística
    cujo resultado depende exclusivamente de seus dados de entrada, sem
    efeitos colaterais ou dependência de estado externo. Seu contrato
    garante robustez em casos de borda, como a entrada de um conjunto de
    dados vazio.

    Args:
        samples (List[float]): Um iterável de números de ponto flutuante
                               cuja média será computada.

    Returns:
        float: A média aritmética das amostras. Retorna 0.0 se a lista de
               amostras de entrada estiver vazia, garantindo um comportamento
               previsível e matematicamente seguro.
    """
    if not samples:
        return 0.0

    return sum(samples) / len(samples)

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

        if selected_option in ('1'):
            cli_pause()

if __name__ == '__main__':
    main()