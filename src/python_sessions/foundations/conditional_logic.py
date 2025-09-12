"""
Este módulo é um estudo de caso sobre o uso de estruturas de controle condicional
(blocos `if/else`) para implementar a lógica de decisão em programação.

A lógica condicional é um pilar fundamental da ciência da computação, permitindo 
que um programa execute diferentes blocos de código com base em critérios predefinidos
que são avaliados como verdadeiros (`True`) ou falsos (`False`). Para ilustrar este 
conceito, o script utiliza dois exemplos clássicos da matemática: a verificação de 
uma violação do Último Teorema de Fermat e a validação da desigualdade triangular.
"""
from __future__ import annotations

__author__ = 'Enock Silos'
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

def check_fermat(a: int, b: int, c: int, n: int) -> bool:
    """
    Verifica se os números fornecidos violam o Último Teorema de Fermat.

    O Último Teorema de Fermat afirma que não existem números inteiros
    positivos a, b e c que possam satisfazer a equação aⁿ + bⁿ = cⁿ para
    qualquer valor inteiro de n maior que 2. Esta função testa essa 
    proposição, retornando `True` se uma violação for encontrada (um contra
    exemplo) e `False`, caso contrário.

    Args:
        a (int): O primeiro número inteiro da base.
        b (int): O segundo número inteiro da base.
        c (int): O terceiro número inteiro da base.
        n (int): O expoente inteiro, que deve ser maior que 2.

    Returns:
        bool: `True` se a condição for satisfeita (violando o teorema), `False`,
               caso contrário
    """
    return n > 2 and a**n + b**n == c**n

def prompt_fermat_check() -> None:
    """
    Orquestra a interação com o usuário para a verificação do Teorema de Fermat.

    Esta função lida com a entrada de dados do usuário, invoca a função de lógica
    pura `check_fermat` para realizar o cálculo e, em seguida, interpreta o 
    resultado booleano para apresentar uma mensagem informativa no console.

    Side Effects:
        - Lê dados da entrada padrão (input).
        - Imprime dados na saída padrão (print).
    """
    a = int(input('Digite o valor de a: '))
    b = int(input('Digite o valor de b: '))
    c = int(input('Digite o valor de c: '))
    n = int(input('Digite o valor do expoente n (maior que 2): '))
        
    was_fermat_violation = check_fermat(a, b, c, n)
    if was_fermat_violation:
        print('\nHoly smokes, Fermat was wrong!')
    else:
        print("\nNo, that doesn't work.")
    
def is_triangle(side_1: int, side_2: int, side_3: int) -> bool:
    """
    Determina se três comprimentos de lado podem formar um triângulo válido.

    A função baseia-se no Teorema da Desigualdade Triangular, que postula que
    a soma dos comprimentos de quaisquer dois lados de um triângulo deve ser
    sempre maior que o comprimento do terceiro lado. Todas as três combinações
    devem ser verdadeiras para que um triângulo seja válido.

    Args:
        side_1 (int): O comprimnto do primeiro lado.
        side_2 (int): O comprimento do segundo lado.
        side_3 (int): O comprimento do terceiro lado.

    Returns:
        bool: `True` se os lados podem formar um triangulo, `False`, caso contrário.
    """
    condition_1 = (side_1 + side_2) > side_3
    condition_2 = (side_2 + side_3) > side_1
    condition_3 = (side_1 + side_3) > side_2
    return condition_1 and condition_2 and condition_3

def prompt_triangle_check() -> None:
    """
    Coordena a interação com o usuário para a verificação da desigualdade triangular.

    Esta função solicita ao usuário os comprimentos de três lados, invoca a função de
    lógica pura `is_triangle` e exibe uma mensagem clara indicando se os comprimentos
    fornecidos podem ou não formar um triângulo.

    Side Effects:
        - Lê dados de entrada (input).
        - Imprime dados na saída padrão (print).
    """
    print('\n--- Vefificador de Triângulos ---')
    print('Vamos verificar se você consegue formar um triângulo com 3 medidas.')
    side_1 = int(input('Digite a primeira medida:'))
    side_2 = int(input('Digite a segunda medida:'))
    side_3 = int(input('Digite a terceira medida:'))

    is_valid_triangle = is_triangle(side_1, side_2, side_3)
    if is_valid_triangle:
        print('Yes, you have a triangle.')
    else:
        print("No, you don't have a triangle.")
    
def main() -> None:
    """
    O ponto de entrada principal para a execução do script.
    """
    prompt_fermat_check()
    prompt_triangle_check()

if __name__ == '__main__':
    main()


