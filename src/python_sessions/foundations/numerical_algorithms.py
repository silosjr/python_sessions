"""
Módulo para algoritmos numéricos fundamentais e sua interface de CLI.

Este módulo fornece um conjunto de funções puras que implementam algoritmos
numéricos clássicos, juntamente com uma Interface de Linha de Comando (CLI)
interativa para a sua demonstração e utilização. O design adere estritamente
ao Princípio de Responsabilidade Única (SRP), separando a lógica de negócio
pura da camada de interação com o usuário.

A arquitetura da CLI segue um padrão REPL (Read-Eval-Print-Loop), orquestrado
pela função `main`, que delega tarefas a funções auxiliares dedicadas para
exibição do menu, despacho de comandos e manipulação de cada funcionalidade
específica.
"""

from __future__ import annotations
from typing import Optional
from python_sessions.utils.constants import (
    PADDING_WIDTH,
    CALCULATION_IN_PROGRESS_MESSAGE,
    ZERO_DIVISION_ERROR_MESSAGE
)
from python_sessions.utils.input_handlers import (
    cli_pause,
    get_valid_integer_from_user,
    get_valid_float_from_user
)

__author__ = 'Enock Silos'
__version__ = '0.3.0'
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Production'

def newton_square_root(
    number: float,
    tolerance: float = 0.0001
    ) -> float:
    """
    Calcula a raiz quadrada de um número usando o método de Newton.

    Este algoritmo implementa o método de Newton-Raphson, um processo
    iterativo para encontrar aproximações sucessivamente melhores para as
    raízes de uma função. A função é robusta, validando as pré-condições
    para garantir que opera apenas dentro do seu domínio matemático definido
    (números reais não negativos).

    Args:
        number (float): O número não negativo para o qual a raiz quadrada
                        será calculada.
        tolerance (float, optional): A margem de erro aceitável para a
                                     convergência do algoritmo.
                                     Defaults to 0.0001.
    Raises:
        ValueError: Se o `number` fornecido for negativo.

    Returns:
        float: A aproximação da raiz quadrada do `number`.
    """
    if number < 0:
        raise ValueError(
            ' A raiz quadrada não está definida para números negativos no domínio real.'
    )
    
    if number == 0:
        return 0.0

    estimate = number / 2.0
    
    while abs(number - (estimate * estimate)) > tolerance:
        estimate = (estimate + (number / estimate)) / 2.0
        
    return estimate

def remainder_by_subtraction(
    dividend: int,
    divisor: int
    ) -> int:
    """
    Calcula o resto da divisão inteira usando subtrações sucessivas.

    Esta função implementa o algoritmo de divisão euclidiana para inteiros
    não-negativos. O seu contrato é explícito, recusando-se a operar com
    entradas negativas ou um divisor de zero para garantir um comportamento
    previsível e seguro.

    Args:
        dividend (int): O dividendo.
        divisor (int): O divisor.

    Raises:
        ZeroDivisionError: Se o `divisor` for zero.
        ValueError: Se `dividend` ou `divisor` for negativo.

    Returns:
        int: O resto da divisão inteira.
    """
    if divisor == 0:
        raise ZeroDivisionError(ZERO_DIVISION_ERROR_MESSAGE)
    if dividend < 0 or divisor < 0:
        raise ValueError(
            ' ERRO: Apenas valores não negativos são permitidos.'
)

    remainder_candidate = dividend

    while remainder_candidate >= divisor:
        remainder_candidate -= divisor

    return remainder_candidate

def is_numeric_palindrome(number: int) -> bool:
    """
    Verifica se um inteiro não negativo é um palíndromo.

    Um palíndromo numérico é um número que se lê da mesma forma nos dois
    sentidos (e.g, 121, 4554). O algoritmo funciona invertendo os dígitos
    do número e comparando o resultado com o número original. A função
    opera sob um contrato explícito, aceitando apenas inteiros não negativos.

    Args:
        number (int): O inteiro não negativo a ser verificado.

    Raises:
        ValueError: Se `number` for negativo.

    Returns:
        bool: `True` se o número for um palíndromo, `False` caso contrário.
    """
    if number < 0:
        raise ValueError(
            ' O algoritmo de palíndromo numérico suporta apenas inteiros não negativos.'
        )

    original_number = number
    reversed_number = 0
    working_number = number

    while working_number > 0:
        last_digit = working_number % 10
        reversed_number = (reversed_number * 10) + last_digit
        working_number = working_number // 10

    return original_number == reversed_number

def _display_menu() -> None:
    """
    Renderiza e exibe o menu principal da aplicação na saída padrão.
    """
    numeric_algorithms_menu = [
        ' MENU DE ALGORITMOS NUMÉRICOS',
        ' Selecione a operação desejada:',
        ' [1] - Cálculo de raiz quadrada pelo método de Newton-Raphson',
        ' [2] - Cálculo de resto por subtração sucessiva',
        ' [3] - Verificação de palíndromo numérico',
        ' [Q] - Encerrar sessão'
    ]
    content_width = max(len(line) for line in numeric_algorithms_menu)
    internal_width = content_width + PADDING_WIDTH

    top_border = f'╔{'═' * (internal_width)}╗'
    middle_border = f'╠{'═' * (internal_width)}╣'
    bottom_border = f'╚{'═' * (internal_width)}╝'

    title = numeric_algorithms_menu[0]
    header_line = f'║{title:^{internal_width}}║'

    print(top_border)
    print(header_line)
    print(middle_border)

    for line in numeric_algorithms_menu[1:]:
        padded_line = f'  {line}'
        print(f'║{padded_line:<{internal_width}}║')

    print(bottom_border)

def _handle_newton_sqrt() -> None:
    """
    Manipula o fluxo de UI para o cálculo da raiz quadrada.
    """
    prompt = ' Digite o número para cálculo da raiz quadrada ("Q" para encerrar): '
    try:
        input_number = get_valid_float_from_user(prompt)
        if input_number is None:
            return

        print(CALCULATION_IN_PROGRESS_MESSAGE)
        newton_sqrt = newton_square_root(input_number)

        print(f'\n Resultado: √({input_number}) ≈ {newton_sqrt:.6f}')

    except ValueError as e:
        print(f'\n ERRO: {e}')

def _handle_remainder_by_subtraction() -> None:
    """
    Manipula o fluxo de UI para o cálculo do resto da divisão.
    """
    dividend_prompt = ' Escolha um número para o dividendo ("Q" para encerrar): '
    divisor_prompt = ' Escolha um número para o divisor ("Q" para encerrar): '
    try:
        dividend = get_valid_integer_from_user(dividend_prompt)
        if dividend is None:
            return
        divisor = get_valid_integer_from_user(divisor_prompt)
        if divisor is None:
            return

        print(CALCULATION_IN_PROGRESS_MESSAGE)
        remainder = remainder_by_subtraction(dividend, divisor)
        print(f' ETAPA 1/3: Realizando cálculo da divisão ({dividend} ÷ {divisor})')
        print(f' ETAPA 2/3: Resultado da divisão inteira obtido: ({dividend//divisor})')
        print(f' ETAPA 3/3: Conclusão: O resto da divisão obtido pelas subtrações sucessivas é {remainder}')
    except (ValueError, ZeroDivisionError) as e:
        print(f'\n ERRO: {e}')

def _handle_numeric_palindrome() -> None:
    """
    Manipula o fluxo de UI para a verificação de palíndromo numérico.
    """
    prompt = ' Informe um número inteiro não negativo para verificação de palíndromo numérico ("Q" para encerrar): '
    try:
        numeric_input = get_valid_integer_from_user(prompt)
        if numeric_input is None:
            return
        
        print(CALCULATION_IN_PROGRESS_MESSAGE)
        palindrome_result = is_numeric_palindrome(numeric_input)
        
        if palindrome_result:
            print(f' Conclusão: O número {numeric_input} é um palíndromo.')
        else:
            print(f' Conclusão: O número {numeric_input} não é um palíndromo.')
    
    except ValueError as e:
        print(f' ERRO: {e}')
        
def _handle_user_choice(selected_option: str) -> None:
    """
    Atua como despachante, direcionando a execução para a função correta.

    Args:
        selected_option (str): As opções contidas no menu exibido ao usuário.
    """
    if selected_option == '1':
        _handle_newton_sqrt()
    elif selected_option == '2':
        _handle_remainder_by_subtraction()
    elif selected_option == '3':
        _handle_numeric_palindrome()
    else:
        print(' ERRO: Por favor insira uma das opções válidas do menu.')

def main() -> None:
    """
    Função principal que orquestra a interface de linha de comando (REPL).
    """
    while True:
        _display_menu()
        selected_option = input(' ~ Sua opção → ')

        if selected_option.lower() == 'q':
            print('\n Sessão Encerrada.\n')
            break

        _handle_user_choice(selected_option)

        if selected_option in ('1', '2', '3'):
            cli_pause()

if __name__ == '__main__':
    main()