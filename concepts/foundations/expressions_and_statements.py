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
__version__ = '1.0.0' 
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

def calculate_sphere_volume(radius: float) -> float:
    """
    Calcula o volume de uma esfera com base no seu raio.

    Esta função implementa a fórmula matemática V = (4/3) * π * r³. A utilização
    do módulo `math` para a constante `pi` garante a precisão do cálculo.

    Args:
        radius (float): O raio da esfera, como um número de ponto flutuante.

    Returns:
        float: O volume calculado da esfera.
    """
    return (4 / 3) * math.pi * (radius ** 3)

def apply_discount(full_price: float, discount_percentage: float) -> float:
    """
    Calcula o valor final de um item após a aplicação de um desconto percentual.

    A lógica subtrai a fração do desconto do valor unitário (100%) para 
    encontrar o fator multiplicativo do preço final.

    Args:
        full_price (float): O preço original do item.
        discount_percentage (float): A porcentagem de desconto a ser aplicada (ex: 40 para 40%).

    Returns:
        float: O preço final do item após o desconto
    """
    return full_price * (1 - discount_percentage / 100)
    
def calculate_shipping(num_itens: int) -> float:
    """
    Calcula o custo total do frete com base numa lógica de preços escalonada.

    A função modela um cenário comercial comum onde o custo de envio para o 
    primeiro item é fixo, e um custo adicional menor é aplicado para cada
    item subsequente. A função trata o caso de zero itens de forma robusta.

    Args:
        num_items (int): O número total de itens a serem enviados.

    Returns:
        float: O custo total do frete.
    """
    FIRST_ITEM_COST = 3.00
    ADDITIONAL_ITEM_COST = 0.75

    if num_itens <= 0:
        return 0.0 
    
    return FIRST_ITEM_COST + (num_itens - 1) * ADDITIONAL_ITEM_COST
    
if __name__ == '__main__':

    print('\t--- Fase 1: Laboratório de Sintaxe ---\n')
    # Testando Atribuição Posicional Incorreta
    test_code_snippet(
    'Atribuição com literal à esquerda (ex: 42 = n)',
    'n = 42; 42 = n'
    )
    # Testando a Atribuição Encadeada
    test_code_snippet(
    'Atribuição Encadeada (ex: x = y = 1)',
    "x = y = 1; print(f'x={x}, y={y}')"
    )
    # Testando uso do ponto e vírgula ao fim da linha
    test_code_snippet(
    'Ponto e Vírgula ao fim da linha (ex: x = 1;)',
    'x = 1;'
    )
    # Testando uso do ponto ao fim da linha
    test_code_snippet(
    'Uso de ponto para denotar um tipo `float` (ex: x = 1.)',
    "x = 1.; print(f'O tipo de x é {type(x).__name__}')"
    )
    # Testando exibir variáveis não-declaradas
    test_code_snippet(
    'Tentativa de Multiplicação Implícita (ex: xy)',
    'x = 1; y = 3 ; print(xy)')

    print('\n\tFase 2: Calculadora de Expressões ---\n')
    # Cálculo do volume de uma esfera com raio 5
    sphere_volume = calculate_sphere_volume(5)
    print(f'1.  O volume de uma esfera com raio 5 é {sphere_volume:.2f}cm³\n')

    print('2.   Simulação de Custo Comercial\n')
    # Adaptação para região específica, com formato padronizado
    locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
    RETAIL_PRICE = 24.95
    WHOLESALE_DISCOUNT_PERCENTAGE = 40

    unit_shipping_price = 3.00
    bulk_shipping_price = 0.75
    quantity = 60

    final_shipping_value = calculate_shipping(quantity)

    print(f'VALOR VAREJO : {locale.currency(RETAIL_PRICE, grouping=True):>34}')
    print(f'VALOR ATACADO: {locale.currency(apply_discount(RETAIL_PRICE, WHOLESALE_DISCOUNT_PERCENTAGE), grouping=True):>34}')
    print(f'VALOR DO FRETE PARA UM EXEMPLAR: {locale.currency(calculate_shipping(1), grouping=True):>15}')
    print(f'VALOR DO FRETE PARA EXEMPLAR ADICIONAL: {locale.currency(bulk_shipping_price, grouping=True):>8}')
    print(f'QUANTIDADE SOLICITADA: {quantity:>20} unidades')
    print(f'TOTAL A SER PAGO: {locale.currency(apply_discount(RETAIL_PRICE, WHOLESALE_DISCOUNT_PERCENTAGE) * quantity + final_shipping_value, grouping=True):>32}\n')

    print('3.   Cálculo de Logística e Tempo')
    # Horário de Partida
    start_time_seconds = convert_to_seconds(minutes=(6 * 60 + 52), seconds=0)

    # Duração da corrida em segundos
    slow_pace_duration = convert_to_seconds(8, 15) * 2
    fast_pace_duration = convert_to_seconds(7, 12) * 3
    race_duration_seconds = slow_pace_duration + fast_pace_duration

    # Hora de chegada em segundos desde a meia-noite
    arrival_time_seconds = start_time_seconds + race_duration_seconds

    # Convertendo o total de segundos de volta para o formato hh:mm:ss
    hours, remaining_seconds = divmod(arrival_time_seconds, 3600)
    minutes, seconds = divmod(remaining_seconds, 60)

    print(f'\n4.    A hora de chegada calculada é {int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}\n')




    
