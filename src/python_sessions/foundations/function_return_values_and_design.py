"""
Este script serve como um estudo prático e didático sobre o design e a implementação
de funções com valores de retorno em Python. O código explora a transição de funções 
sem valor de retorno (que executam funções, mas não retornam valores) para funções com resultado, que
são fundamentais para a computação e a composição de algoritmos.

O módulo aborda os seguintes tópicos de forma sequencial e autoexplicativa:
1.  Valores de Retorno: A sintaxe e a semântica de instrução `return`.
2.  Desenvolvimento Incremental: Uma metodologia para construir e depurar funções 
    complexas em pequenos passos verificáveis, utilizando código de "andaime" (scaffoding).
3.  Composição de Funções: A prática de combinar funções simples para resolver problemas
    mais complexos, tratando saídas de funções como entrada para outras.
4.  Funções booleanas: Funções que retornam `True` ou `False`, encapsulando testes lógicos
    para melhorar a legibilidade do código.
5.  Recursividade: A técnica na qual uma função chama a si mesma para resolver um problema,
    ilustrada com o exemplo clássico do fatorial.
6.  Verificação de Tipos e Padrão Guardião: Práticas de programação defensiva para garantir
    que as funções recebam argumentos válidos (pré-condições) antes de executar sua lógica
    principal.

Cada função é anotada com Type Hints (PEP 484) e segue as convenções de estilo do PEP 8, 
alinhando-se com a filosofia do repositório `python_sessions` de produzir código claro, 
profissional e educativo.
"""

from __future__ import annotations
from math import pi, sqrt
from typing import Union

__author__ = 'Enock Silos'
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

def calculate_circle_area(radius: float) -> float:
    """
    Calcula a área de um círculo com base no raio fornecido.

    Esta função exemplifica o conceito mais fundamental de um valor de retorno.
    Ela recebe um único argumento, executa um cálculo matemático e retorna o 
    resultado, que pode ser atribuído a uma variável ou usado em outra expressão.

    Args:
        radius (float): O raio do círculo. Deve ser um valor numérico não negativo.

    Returns:
        float: A área calculada do círculo (π * raio²).
    """
    area: float = pi * radius**2
    return area

def get_absolute_value(x: Union[int, float]) -> Union[int, float]:
    """
    Retorna o valor absoluto de um número.

    Esta função demonstra o uso de múltiplas instruções `return`dentro de diferentes
    ramos de uma estrutura condicional. A execução da função termina assim que a 
    primeira instrução `return` é encontrada.

    Args:
        x (Union[int, float]): O número (inteiro ou ponto flutuante) para o qual o 
                               valor será calculado.

    Returns:
        Union[int, float]: O valor absoluto de 'x', que será sempre não negativo.
    """
    if x < 0:
        return -x 
    else:
        return x 

def calculate_distance(
                       x1: float, y1: float,
                       x2: float, y2: float
                       ) -> float:
    """
    Calcula a distância euclidiana entre dois pontos em um plano 2D.

    Esta função foi construída utilizando a metodologia de desenvolvimento incremental.
    As variáveis temporárias `dx`, `dy` e `dsquared` foram usadas para facilitar a 
    depuração passo a passo. O código de 'andaime' (scaffolding), que consiste em instruções
    `print`, foi comentado para manter um registro didático do processo de construção.

    Args:
        x1 (float): A coordenada x do primeiro ponto.
        y1 (float): A coordenada y do primeiro ponto.
        x2 (float): A coordenada x do segundo ponto.
        y2 (float): A coordenada y do segundo ponto.

    Returns:
        float: A distância euclidiana entre (x1, y1) e (x2, y2).
    """
    dx = x2 - x1
    dy = y2 - y1 
    dsquared = (dx + dy) ** 2
    result = sqrt(dsquared)

#     print(f'''
#                 - Diferença entre os eixos `x` = {dx}
#                 - Diferença entre os eixos `y` = {dy}
#                 - Soma dos quadrados das diferenças dos eixos `x` e `y` = {dsquared}
#                 - Raiz Quadrada da Soma dos Quadrados das diferenças dos eixos `x` e `y` = {result}
# ''')

    return result 

def calculate_circle_area_from_points(
                                      xc: float,
                                      yc: float,
                                      xp: float,
                                      yp: float
                                     ) -> float: 
    """
    Calcula a área de um círculo dadas as coordenadas de seu centro e de um ponto
    em seu perímetro.

    Esta função é um exemplo primário de composição. Ela não implementa uma nova 
    lógica de cálculo, mas orquestra o trabalho de outras duas funções previamente
    definidas (`calculate_distance` e `calculate_circle_area`) para resolver um 
    problema mais complexo.

    Args:
        xc (float): A coordenada x do centro do círculo.
        yc (float): A coordenada y do centro do círculo.
        xp (float): A coordenada x de um ponto no perímetro.
        yp (float): A coordenada y de um ponto no perímetro.

    Returns:
        float: A área do círculo definido pelos pontos fornecidos.
    """

    return calculate_circle_area(calculate_distance(xp, xc, yp, yc))

def is_divisible(x: int, y: int) -> bool:
    """
    Verifica se um inteiro `x` é perfeitamente divisível por um inteiro `y`.

    Esta é uma função booleana. Ela encapsula um teste lógico e retorna diretamente
    o resultado da expressão booleana `x % y == 0`. Funções como esta tornam o código
    mais legível ao dar um nome semântico a uma condição.

    Args:
        x (int): O dividendo.
        y (int): O divisor.

    Returns:
        bool: `True` se `x` for divisível por `y`, `False`, caso contrário.

    Side Effects:
        - Pode levantar uma exceção `ZeroDivisionError` se `y` for 0.
    """
    if y == 0:
        raise ZeroDivisionError('Não é possível realizar uma divisão por zero.')
    
    return x % y == 0 

def calculate_factorial(n: int) -> Union[int, None]:
    """
    Calcula o fatorial de um inteiro não negativo usando recursividade.

    Esta função demonstra três conceitos:
    1.  Padrão Guardião: As duas primeiras condicionais atuam como 'guardiãs', 
        validando as pré-condições do argumento (`n` deve ser um inteiro não
        negativo) e retornando `None` se forem violados.
    2.  Caso Base: A condição `n == 0` que termina a recursão.
    3.  Passo Recursivo: A chamada de função a si mesma com um argumento modificado
        (`n - 1`) que se aproxima do caso base.

    Args:
        n (int): O número para o qual o fatorial será calculado.

    Returns:
        Union[int, None]: O valor do fatorial de `n`, ou `None` se a entrada for 
                          inválida (não inteira ou negativa).

    Side Effects:
        - Imprime uma mensagem de erro no console se a entrada for inválida.
    """
    if not isinstance(n, int):
        print(f'    ERRO: Fatorial é definido apenas para números inteiros. Valor recebido: {n}')
        return None
    
    if n < 0:
        print('     Não é possível calcular o fatorial de um número negativo.')
        return None 
    
    if n == 0:
        return 1 
    else:
        return calculate_factorial(n - 1) * n 
    
if __name__ == '__main__':

    print('--- Demonstração das Funções do Módulo ---')

    print('\n1.     Calculando a área de um círculo com raio 5:')
    area_exemplo = calculate_circle_area(5.0)
    print(f'    Resultado: {area_exemplo:.4f}')

    print('\n2.     Calculando o valor absoluto de -10 e 7:')
    abs_neg = get_absolute_value(-10)
    abs_pos = get_absolute_value(7)
    print(f'    | -10 | = {abs_neg}')
    print(f'    | 7   | = {abs_pos}')

    print('\n3.     Calculando a distância entre os pontos (1, 2) e (4, 6):')
    distancia_exemplo = calculate_distance(1, 2, 4, 6)
    print(f'    Resultado: {distancia_exemplo}')

    print('\n4.     Calculando a área do círculo com centro (0, 0) e ponto (3, 4) no perímetro:')
    area_composta = calculate_circle_area_from_points(0, 0, 3, 4)
    print(f'    (O raio é a distância entre os pontos, que é 5)')
    print(f'    Resultado: {area_composta:.4f}')

    print('\n5.     Verificando Divisibilidade:')
    print(f'    É 10 divisível por 2? -> {is_divisible(10, 2)}')
    print(f'    É 10 divisível por 3? -> {is_divisible(10, 3)}')

    print('\n6.     Calculando o fatorial:')
    print(f'    5! = {calculate_factorial(5)}')
    print(f'    0! = {calculate_factorial(0)}')
    print(f'    Tentando com entrada inválida (-2):')
    print(f'    -2! = {calculate_factorial(-2)}')
    print(f'    Testando com entrada inválida (3.5):')
    print(f'    3.5! = {calculate_factorial(3.5)}\n')