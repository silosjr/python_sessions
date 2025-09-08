"""
Um script didático dedicado à exposição do conceito de `Unix Time`, também
conhecido como 'Tempo de Época' (Epoch Time).

Este módulo provÊ uma demonstração prática de como adquirir o número total de
segundos decorridos desde a Época Unix (00:00:00 UTC de 1 de janeiro de 1970)
e converter  este vasto número inteiro em um formato legível por humanos,
dividido em dias, horas, minutos e segundos.

O script emprega operações aritméticas fundamentais, especificamente a divisão 
inteira (operador `//`) e o módulo (operador `%`), para realizar a conversão.
Tais operações representam pilares da lógica computacional para a manipulação
de estrutura de dados periódicas e hierárquicas, como o tempo.
"""
from __future__ import annotations
from typing import Tuple
import time

__author__ = 'Enock Silos'
__version__ = '1.0.0' 
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

SECONDS_PER_DAY = 86400
SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

def convert_seconds_to_dhms(total_seconds: float) -> Tuple[int, int, int, int]:
    """
    Converte um carimbo de tempo (`timestamp`) de segundos desde a Época em uma
    tupla estruturada contendo dias, horas, minutos e segundos.

    Esta função é o exemplo de uma função 'pura'. Dado um mesmo `imput`, ela
    sempre produzirá o mesmo `output`, sem causar efeitos colaterais como 
    imprimir dados na tela ou modificar variáveis externas. Funções puras são
    previsíveis, facéis de testar e altamente reutilizáveis.

    O algoritmo emprega uma sequência de cálculos aritméticos para decompor o 
    total de segundos em suas unidades temporais constituintes. A metodologia 
    se baseia na divisão inteira para encontrar o número completo de uma unidade
    e no operador de módulo para determinar o valor restante, que será usando no
    cálculo da próxima unidade menor. Este é um padrão algorítmico muito comum em
    sistemas de tempo. 

    Args:
        total_seconds (float): Um número de ponto flutuante que representa o total
                               de segundos decorridos desde a Época Unix. Tipicamente
                               obtido através de `time.time()`.

    Returns:
        Tuple[int, int, int, int]: Uma tupla contendo quatro números inteiros na ordem:
                                   (dias, horas, minutos, segundos)
                            
    """
    days: int = int(total_seconds // SECONDS_PER_DAY)
    remaining_seconds: float = total_seconds % SECONDS_PER_DAY

    hours: int = int(remaining_seconds // SECONDS_PER_HOUR)
    remaining_seconds %= SECONDS_PER_HOUR

    minutes: int = int(remaining_seconds // SECONDS_PER_MINUTE)  

    seconds: int = int(remaining_seconds % SECONDS_PER_MINUTE)

    return days, hours, minutes, seconds
    
def display_time(days: int, hours: int, minutes: int, seconds: int) -> None:
    """
    Apresenta as unidades de tempo convertidas em uma tabela formatada.

    A única responsabilidade desta função é a formatação da saída. Separar
    o processamento de dados (realizado por `convert_seconds_to_dhms`) da
    apresentação destes dados é um princípio fundamental de design de software
    conhecido como 'Separação de Responsabilidades' (Separation of Concerns).
    Esta prática resulta em um código mais modular, reutilizável e de fácil
    manutenção.

    Args:
        days (int): O número de dias inteiros.
        hours (int): O número de horas inteiras.
        minutes (int): O número de minutos inteiros.
        seconds (int): O número de segundos inteiros.
    """
    print('\n--- Análise de Tempo desde a Época Unix ---\n')
    print(
        'O tempo atual, medido em segundos desde 1º de Janeiro de 1970, '
        'foi convertido para:'
    )
    print('-' * 55)
    print(f"{'Dias':<10} | {'Horas':^10} | {'Minutos':^10} | {'Segundos':>10}")
    print('-' * 55)
    print(f'{days:<10} | {hours:^10} | {minutes:^10} | {seconds:^10}')
    print('-' * 55)

def main() -> None:
    """
    O ponto de entrada principal para execução do script.

    Esta função orquestra a lógica primária do programa: ela obtém o tempo
    atual, invoca a lógica de conversão e, em seguida, chama a função de
    exibição para apresentar os resultados ao usuário.
    """
    current_timestamp: float = time.time()
    days, hours, minutes, seconds = convert_seconds_to_dhms(current_timestamp)
    display_time(days, hours, minutes, seconds)

if __name__ == '__main__':
    main()



