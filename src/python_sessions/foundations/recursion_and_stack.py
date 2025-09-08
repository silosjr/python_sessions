"""
Um módulo dedicado ao estudo da recursão, conceito fundamental e poderoso 
na ciência da computação.

A recursão ocorre quando uma função chama a si mesma para resolver um problema.
Uma função recursiva bem projetada possui dois componente essenciais:
1.  O caso base: Uma condição que interrompe a recursão, retornando um resultado
    direto. Sem um caso base, a função chamaria a si mesma infinitamente.
2.  O caso recursivo: A parte da função que se chama novamente, mas com argumentos
    que se aproximam progressivamente do caso base.

Cada chamada de função consome memória na pilha de chamadas (`callstack`).
Se a recursão for muito profunda (ou infinita), ela pode esgotar essa memória, 
resultando em um erro conhecido como estouro de pilha (`stackoverflow`), que em
Python é representado pela exceção `RecursionError`.
"""
from __future__ import annotations

__author__ = 'Enock Silos'
__version__ = '1.0.0' 
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

def recurse(first_value: int, second_value: int) -> int  :
    """
    Executa um cálculo recursivo simples.

    Esta função demonstra o padrão recursivo fundamental. Ela decrementa o 
    primeiro valo e o adiciona ao segundo a cada chamada, até que o primeiro
    valor atinja o caso base (zero).

    O fluxo de retorno é crucial: quando o caso base é atingido, o resultado
    é retornado para a chamada anterior, que por sua vez o retorna para sua
    chamada anterior, e assim por diante, até que o valor final chegue à 
    chamada original.

    Args:
        first_value (int): O contador que se aproxima do caso base (0).
        second_value (int): O acumulador que armazena a soma.

    Returns:
        int: O valor final do acumulador quando o caso base é alcançado.
    """
    if first_value == 0:
        return second_value
    else:
        return recurse(first_value - 1, first_value + second_value)

def prompt_recursion() -> None:
    """
    Orquestra a interação com o usuário para a demonstração da recursão.

    Esta função solicita os valores iniciais ao usuário e invoca a função
    recursiva dentro de um bloco `try/except` para lidar de forma segura
    com potenciais erros de `RecursionError`, que ocorrem se a profundidade
    da recursão exceder o limite do interpretador Python.

    Side Effects:
        - Lê dados de entrada padrão (input).
        - Imprime dados de saída padrão (print).
    """
    print('\n--- Demonstração de Recursão ---')
    first_value = int(input('Digite o valor inicial do contador (ex: 10): '))
    second_value = int(input('Digite o valor inicial do acumulador (ex: 0): '))

    try:
        result = recurse(first_value, second_value)
        print(f'\nResultado do cálculo recursivo: {result}')
    except RecursionError:
        print(
             '\nErro: RecursionError! O valor inicial do contador é muito alto'
        )
        print(
        'Como medida de segurança, o interpretador interrompeu o programa para'
        'evitar um estouro da pilha de chamadas (`stack overflow`).'
        )

def main() -> None:
    """
    O ponto de entrada principal para a execução do scrip.
    """
    prompt_recursion()

if __name__ == '__main__':
    main()