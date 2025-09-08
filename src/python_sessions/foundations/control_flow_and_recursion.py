"""
Módulo Didático sobre Fluxo de Controle E Recursividade

Este script serve como um estudo de caso prático sobre os mecanismos
fundamentais que governam o fluxo de execução em Python: as expressões
booleanas, as estruturas condicionais e a recursividade.
"""

from __future__ import annotations
import random 
from typing import Optional

__author__ = 'Enock Silos'
__version__ = '0.3.0'
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

def is_even(number: int) -> bool:
    """
    Verifica se um número inteiro é par.
    A função utiliza o operador módulo (`%`), que retorna o resto de uma 
    divisão. Um número é considerado par se, e somente se, o resto da sua
    divisão por 2 for igual a 0. A função retorna diretamente o resultado
    desta expressão booleana.

    Args:
        number (int): O número inteiro a ser verificado. 

    Returns:
        bool: True, se o número for par, False caso contrário.
    """
    return number % 2 == 0

def compare_numbers(x: int | float, y: int | float) -> str:
    """
    Compara dois números e retorna a sua relação em formato de uma expressão matemática.

    Esta função "pura encapsula a lógica de comparação, retornando um
    resultado conciso em vez de imprimir diretamente. Ela utiliza uma
    cadeia `if/elif/else` para cobrir todas as três possibilidades de
    relação entre dois números.

    Args:
        x (int | float): O primeiro número para a comparação.
        y (int | float): O segundo número para a comparação.

    Returns:
        str: Uma string com uso dos operadores relacionais (`<`, `>`, `==`).
    """
    if x == y:
        return f'{x} == {y}'
    elif x > y:
        return f'{x} > {y}'
    else:
        return f'{x} < {y}'

def countdown(n: int) -> None:
    """
    Executa uma contagem regressiva recursiva a partir de n.

    Esta função demonstra o conceito de recursividade para realizar uma ação
    (imprimir na tela) sem retornar um valor.

    Args:
        n (int): O número inicial para a contagem regressiva.
    """
    
    if n <= 0:
        print('Fogo!')
    else:
        print(n)
        countdown(n - 1)

def calculate_factorial(n: int) -> Optional[int]:
    """
    Calcula o fatorial de um número inteiro não negativo de forma recursiva.

    Esta função demonstra a recursividade para calcular e retornar um valor.
    Ela inclui "cláusulas de guarda" para garantir que a entrada seja válida
    (um inteiro não negativo), tornando-a uma ferramenta robusta.
    
    - Caso Base (n == 0): Retorna 1, por definição matemática.
    - Caso Recursivo (else): Retorna n multiplicado pelo fatorial de (n-1).

    Args:
        n (int): O número para o qual o fatorial será calculado. 

    Raises:
        TypeError: Se a entrada não for um número inteiro.

    Returns:
        Optional[int]: O valor do fatorial como um inteiro, ou None se a
                       entrada for um número negativo.
    """
    if not isinstance(n, int):
        raise TypeError('O argumento deve ser um número inteiro')
    
    if n < 0:
        return None  
    
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

if __name__ == '__main__':
    
    print('--- Fase 1. Demonstração de Condicionais ---\n')
    # Teste para `is_even()`
    number = random.randint(0, 100)

    if is_even(number):
        print(f'\t{number} é par\n')
    else:
        print(f'\t{number} é ímpar\n')

    # Teste para `compare_numbers()`
    n1, n2 = random.randint(0, 100), random.randint(0, 100)

    comparison_result = compare_numbers(n1, n2)
    print(f'\n\t{comparison_result}\n')

    print('--- Fase 2. Demonstração de Recursividade ---\n')
    print('\tContagem Regressiva a partir de 3:\n')
    countdown(3)

    print('\n\tCálculo de Fatorial de 4:\n')
    factorial_result = calculate_factorial(4)
    print(f'\tO fatorial de 4 é {factorial_result}\n')

    print('\tTestando o tratamento de erros da função de fatorial:')
    print(f'\n\tTentando calcular o fatorial de -3: {calculate_factorial(-3)}')

    try:
        calculate_factorial(3.5)
    except TypeError as e:
        print(f'Tentando calcular o fatoria de 3.5: ERRO -> {e}')

        """
    Diagrama de Pilha para countdown(3):

    +-------------------+
    | __main__          |
    |-------------------|
    | chama countdown(3)|
    +-------------------+
            |
            v
    +-------------------+
    | countdown(n=3)    | print(3)
    |-------------------|
    | chama countdown(2)|
    +-------------------+
            |
            v
    +-------------------+
    | countdown(n=2)    | print(2)
    |-------------------|
    | chama countdown(1)|
    +-------------------+
            |
            v
    +-------------------+
    | countdown(n=1)    | print(1)
    |-------------------|
    | chama countdown(0)|
    +-------------------+
            |
            v
    +-------------------+
    | countdown(n=0)    | print('Fogo!')
    |-------------------|
    | retorna           |
    +-------------------+
            ^
            |
    +-------------------+
    | ...retorna        |
    +-------------------+
    """