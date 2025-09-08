"""
Módulo para Análise de Desempenho e Conversão de Unidades.

Este módulo apresenta uma abordagem sistemática para a resolução de problemas
de cálculo que envolvem múltiplas unidades de medida. O princípio fundamental
demonstrado é a decomposição de um problema complexo em um conjunto de funções
"puras", coesas e reutilizáveis, cada uma com uma responsabilidade única e bem
definida.

A metodologia empregada consiste em:
1.  Estabelecer uma base de unidades fundamentais (segundos para tempo, milhas
    para distância).
2.  Criar um conjunto de ferramentas de conversão para mapear as unidades de
    entrada para esta base comum.
3.  Desenvolver funções de cálculo que operam exclusivamente sobre estas
    unidades fundamentais, simplificando a lógica matemática.
4.  Converter os resultados finais de volta para as unidades desejadas para
    apresentação.

Esta abordagem arquitetônica não apenas garante a precisão dos cálculos, mas
também resulta em um código mais legível, testável e de fácil manutenção.
"""
from __future__ import annotations
from typing import Tuple 

__author__ = 'Enock Silos'
__version__ = '0.3.0'
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

def convert_to_seconds(minutes: float | int, seconds: float | int) -> float | int:
    """
    Converte uma duração temporal para a unidade fundamental de segundos.

    Args:
        minutes (float | int): A componente de minutos da duração.
        seconds (float | int): A componente de segundos da duração.

    Returns:
        float | int: A duração total expressa em segundos.
    """
    return minutes * 60 + seconds 

def convert_km_to_miles(kilometers: float | int) -> float:
    """
    Converte uma distância de quilômetros para milhas.

    Args:
        kilometers (float | int): A distância em quilômetros.

    Returns:
        float: A distância equivalente em milhas.
    """
    MILES_PER_KILOMETER = 1 / 1.61
    return kilometers * MILES_PER_KILOMETER

def seconds_to_hours(seconds: int | float) -> float:
    """
    Converte uma duração em segundos para a unidade de horas.

    Args:
        seconds (float |int): A duração total em segundos.

    Returns:
        float: A duração equivalente em horas, como um número de ponto flutuante.
    """
    return seconds / 3600

def get_pace_per_mile(total_seconds: float, total_miles: float) -> Tuple[int, float]:
    """
    Calcula o passo médio (pace), uma medida de tempo por uma unidade de distância.

    O `pace` é uma métrica fundamental em análises de corrida, representando
    o tempo necessário para percorrer uma unidade de distância (neste caso, uma milha).
    A função retorna o resultado em formato legível de minutos e segundos.

    Args:
        total_seconds (float): A duração total da atividade em segundos.
        total_miles (float): A distância total da atividade em milhas.

    Returns:
        Tuple[int, float]: Uma tupla representando o passo médio no formato
                           (minutos, segundos) por milha.
    """
    if total_miles == 0:
        return (0, 0.0)
    
    seconds_per_mile = total_seconds / total_miles
    minutes, seconds = divmod(seconds_per_mile, 60)
    return (int(minutes), seconds)

def get_average_speed_mph(total_miles: float, total_seconds: float) -> float:
    """
    Calcula a velocidade média em milhas por hora (mph).

    A velocidade é uma medida de distância por unidade de tempo. Esta função
    calcula esta métrica, garantindo que as unidades de entrada sejam
    consistentes para produzir um resultado em mph.

    Args:
        total_miles (float): A distância total da atividade em milhas.
        total_seconds (float): A duração total da atividade em segundos.

    Returns:
        float: A velocidade média em milhas por hora
    """
    if total_seconds == 0:
        return 0.0
    total_hours = seconds_to_hours(total_seconds)
    return total_miles / total_hours

if __name__ == '__main__':
    # Definição das constantes do problema a ser analisado
    RACE_DISTANCE_KM = 10
    RACE_TIME_MINUTES = 42
    RACE_TIME_SECONDS = 42

    print('--- Análise de Desempenho de uma Corrida ---')
    print(f'Dados de Entrada: Distância de {RACE_DISTANCE_KM} km em {RACE_TIME_MINUTES}m {RACE_TIME_SECONDS}s\n')

    total_seconds = convert_to_seconds(RACE_TIME_MINUTES, RACE_TIME_SECONDS)
    total_miles = convert_km_to_miles(RACE_DISTANCE_KM)

    print('--- Unidades Normalizadas ---')
    print(f'Duração total em segundos: {total_seconds:.2f} s')
    print(f'Distância total em milhas: {total_miles:.2f} mi\n')

    pace_minutes, pace_seconds = get_pace_per_mile(total_seconds, total_miles)
    average_speed = get_average_speed_mph(total_miles, total_seconds)

    print('--- Resultados da Análise ---')
    print(f'Passo Médio (pace): {pace_minutes} minutos e {pace_seconds:.2f} segundos por milha.')
    print(f'Velocidade Média: {average_speed:.2f} milhas por hora.\n')

      
    

