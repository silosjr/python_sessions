# python_sessions/concepts/foundations/expressions_and_statements.py

"""
Módulo Didático sobre Expressões, Instruções e Operadores Fundamentais.

Este script serve como laboratório prático para a exploração de conceitos
fundamentais da sintaxe e da lógica de cálculo em Python. O seu desígnio é
demonstrar, de forma controlada e autoexplicativa, tanto a reação do
interpretador a instruções sintaticamente anômalas quanto a aplicação de
operadores aritméticos para a resolução de problemas práticos.
"""
from __future__ import annotations
from syntax_and_operators import test_code_snippet
from unit_conversion_calculator import convert_to_seconds
import math
import locale

__author__ = 'Enock Silos'
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'


def demonstrate_operator_precedence() -> None:
    """
    Ilustra a ordem de avaliação de operadores em uma expressão complexa.

    Em ciência da computação, 'precedência de operadores' define a ordem em
    que as operações são realizadas. O interpretador segue estas regras para
    resolver uma expressão a um valor final único. Esta função detalha o
    processo passo a passo, mostrando como a exponenciação (**) precede a
    multiplicação (*), que por sua vez precede a adição (+), e como
    operadores de mesma precedência são avaliados da esquerda para a direita.
    """
    expression: float = 10 % 3 * 10 ** 2 + 1 - 1 * 4 / 2
    print(f'''
        --- 1. Demonstração: Precedência de Operadores ---

        Expressão Original: 10 % 3 * 10 ** 2 + 1 - 1 * 4 / 2

        Ordem de Avaliação pelo Interpretador:
        1. Exponenciação (maior precedência):
           10 % 3 * 100 + 1 - 1 * 4 / 2

        2. Multiplicação, Divisão e Módulo (da esquerda para a direita):
           (10 % 3) * 100 + 1 - 1 * 4 / 2  -> (1) * 100 + 1 - 1 * 4 / 2
           (1 * 100) + 1 - 1 * 4 / 2      -> 100 + 1 - 1 * 4 / 2
           100 + 1 - (1 * 4) / 2          -> 100 + 1 - (4) / 2
           100 + 1 - (4 / 2)              -> 100 + 1 - 2.0

        3. Adição e Subtração (da esquerda para a direita):
           (100 + 1) - 2.0                -> 101 - 2.0
           (101 - 2.0)                    -> {expression}
    ''')


def demonstrate_assignment_and_types() -> None:
    """
    Demonstra a atribuição de valores a variáveis e a tipagem dinâmica.

    Um 'statement de atribuição' (=) associa um nome (identificador) a um
    valor na memória. Python é uma linguagem de tipagem dinâmica, o que
    significa que o tipo da variável é inferido a partir do valor que lhe é
    atribuído. Esta função exibe diferentes valores e seus tipos
    correspondentes (`str`, `int`, `float`), que são inferidos
    automaticamente pelo interpretador.
    """
    name: str = 'Enock Silos'
    age: int = 40
    weight: float = 74.0
    height: float = 1.72
    print(f'''
        --- 2. Demonstração: Atribuição e Tipos Fundamentais ---

        Nome:      {name:<10} -> {type(name)}
        Idade:     {age:<10}  -> {type(age)}
        Peso:      {weight:<10}  -> {type(weight)}
        Altura:    {height:<10}  -> {type(height)}
    ''')


def demonstrate_boolean_logic() -> None:
    """
    Explora como expressões lógicas e de comparação são avaliadas para um
    resultado booleano (True ou False).

    Operadores de comparação (>=) e lógicos (and) são usados para formular
    condições complexas. O resultado dessas expressões é a base do controle
    de fluxo. A função simula um boletim acadêmico para demonstrar como uma
    condição de aprovação composta é calculada e avaliada.
    """
    PASSING_GRADE: int = 7
    data_structures: float = 6.9
    algorithms: float = 8.5
    operating_systems: float = 9.0
    passed: bool = (algorithms >= PASSING_GRADE and
                    data_structures >= PASSING_GRADE and
                    operating_systems >= PASSING_GRADE)
    print(f'''
        --- 3. Demonstração: Lógica Booleana ---

                      🔹  BOLETIM FINAL  🔹
        ------------------------------------------------
        ℹ️  True = Aprovado
        ℹ️  False = Reprovado
        ------------------------------------------------
            DISCIPLINAS              NOTAS
        ------------------------------------------------
        Estrutura de Dados       {data_structures} ⚠️
        Algoritmos               {algorithms} ✅
        Sistemas Operacionais    {operating_systems} ✅
        ------------------------------------------------
        SITUAÇÃO FINAL = {passed} ❌
''')


def calculate_sphere_volume(radius: float) -> float:
    """
    Calcula o volume de uma esfera com base no seu raio.

    Esta função implementa a fórmula matemática V = (4/3) * π * r³. A utilização
    do módulo `math` para a constante `pi` garante a precisão do cálculo.
    """
    return (4 / 3) * math.pi * (radius ** 3)


def apply_discount(full_price: float, discount_percentage: float) -> float:
    """
    Calcula o valor final de um item após a aplicação de um desconto percentual.

    A lógica subtrai a fração do desconto do valor unitário (100%) para
    encontrar o fator multiplicativo do preço final.
    """
    return full_price * (1 - discount_percentage / 100)


def calculate_shipping(num_itens: int) -> float:
    """
    Calcula o custo total do frete com base numa lógica de preços escalonada.

    A função modela um cenário comercial comum onde o custo de envio para o
    primeiro item é fixo, e um custo adicional menor é aplicado para cada
    item subsequente.
    """
    FIRST_ITEM_COST: float = 3.00
    ADDITIONAL_ITEM_COST: float = 0.75

    if num_itens <= 0:
        return 0.0

    return FIRST_ITEM_COST + (num_itens - 1) * ADDITIONAL_ITEM_COST


def main() -> None:
    """
    Ponto de entrada principal que orquestra as diferentes fases de
    demonstração do script.
    """
    print('\n--- Fase 0: Demonstrações de Conceitos Fundamentais ---')
    demonstrate_operator_precedence()
    demonstrate_assignment_and_types()
    demonstrate_boolean_logic()

    print('\n\n--- Fase 1: Laboratório de Sintaxe (Análise de Erros) ---')
    test_code_snippet(
        'Atribuição com literal à esquerda (ex: 42 = n)',
        'n = 42; 42 = n'
    )
    test_code_snippet(
        'Atribuição Encadeada (ex: x = y = 1)',
        "x = y = 1; print(f'x={x}, y={y}')"
    )
    test_code_snippet(
        'Ponto e Vírgula ao fim da linha (ex: x = 1;)',
        'x = 1;'
    )
    test_code_snippet(
        'Uso de ponto para denotar um tipo `float` (ex: x = 1.)',
        "x = 1.; print(f'O tipo de x é {type(x).__name__}')"
    )
    test_code_snippet(
        'Tentativa de Multiplicação Implícita (ex: xy)',
        'x = 1; y = 3 ; print(xy)'
    )

    print('\n\n--- Fase 2: Aplicação de Expressões (Estudos de Caso) ---')
    # Cálculo do volume de uma esfera com raio 5
    sphere_volume = calculate_sphere_volume(5)
    print(f'\n1. O volume de uma esfera com raio 5 é {sphere_volume:.2f}cm³')

    # Simulação de Custo Comercial
    print('\n2. Simulação de Custo Comercial')
    locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
    RETAIL_PRICE: float = 24.95
    WHOLESALE_DISCOUNT_PERCENTAGE: int = 40
    quantity: int = 60

    final_shipping_value = calculate_shipping(quantity)
    discounted_price = apply_discount(RETAIL_PRICE, WHOLESALE_DISCOUNT_PERCENTAGE)
    total_cost = discounted_price * quantity + final_shipping_value

    print(f'   VALOR VAREJO: {locale.currency(RETAIL_PRICE, grouping=True):>40}')
    print(f'   VALOR ATACADO: {locale.currency(discounted_price, grouping=True):>39}')
    print(f'   VALOR DO FRETE (1 exemplar): {locale.currency(calculate_shipping(1), grouping=True):>24}')
    print(f'   QUANTIDADE SOLICITADA: {quantity:>25} unidades')
    print(f'   TOTAL A SER PAGO: {locale.currency(total_cost, grouping=True):>37}')

    # Cálculo de Logística e Tempo
    print('\n3. Cálculo de Logística e Tempo')
    start_time_seconds = convert_to_seconds(minutes=(6 * 60 + 52), seconds=0)
    slow_pace_duration = convert_to_seconds(8, 15) * 2
    fast_pace_duration = convert_to_seconds(7, 12) * 3
    race_duration_seconds = slow_pace_duration + fast_pace_duration
    arrival_time_seconds = start_time_seconds + race_duration_seconds

    hours, remaining_seconds = divmod(arrival_time_seconds, 3600)
    minutes, seconds = divmod(remaining_seconds, 60)

    print(f'   A hora de chegada calculada é {int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}\n')


if __name__ == '__main__':
    main()
