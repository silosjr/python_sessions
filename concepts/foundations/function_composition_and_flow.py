"""
Módulo Didático sobre a Definição, Composição e Fluxo de Funções.

Este script serve como um estudo de caso prático sobre os conceitos
fundamentais que governam a criação e a utilização de funções em Python.
O seu objetivo é transformar os blocos de construção teóricos da programação
estruturada em ferramentas práticas e autoexplicativas.

O módulo explora progressivamente:
1.  A utilização de funções nativas para conversão de tipos e o tratamento
    robusto de erros de conversão.
2.  A importação e utilização de funções de módulos externos, como o `math`.
3.  A definição de novas funções (`def`), distinguindo entre funções "nulas"
    (que realizam uma ação) e "funções com resultado" (que retornam um valor).
4.  O conceito de composição, sob o qual as funções são usadas como blocos de 
    construção para criar comportamentos mais complexos.
5.  O escopo de variáveis e o fluxo de execução durante chamadas de função.
"""

from __future__ import annotations
from typing import Any, Optional
import math 
import random 

__author__ = 'Enock Silos'
__version__ = '1.0.0' 
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

def analyze_value(value: Any) -> None:
    """
    Analisa um valor e testa a sua conversibilidade para tipos fundamentais.

    Esta função atua como um "laboratório seguro", demonstrando como as 
    funções de conversão de tipo (`int()`, `float()`, `str()` e `complex()`)
    se comportam com diferentes entradas. Cada tentativa de conversão é
    encapsulada em um bloco `try/except/else` para relatar o sucesso ou a 
    falha de forma controlada, sem interromper o programa.

    Args:
        value (Any): O valor de qualquer tipo a ser analizado.
    """
    print(f'\n\t--- Análise do Valor: {value} (Tipo: {type(value).__name__}) --- \n')
    
    try:
        converted_int = int(value)
    except (Exception, ValueError) as e:
        print(f'🚫 Não foi possível converter {value} do tipo {type(value)} para `int``\n❗ Motivo: {e}\n')
    else:
        print(f'✅ Foi possível converter {value} para o `int` {converted_int}\n')

    try:
        converted_float = float(value)
    except (Exception, ValueError) as e:
        print(f'🚫 Não foi possível converter {value} do tipo {type(value)} para um `float`\n❗ Motivo: {e}\n')
    else:
        print(f'✅ Foi possível converter {value} do tipo {type(value)} no `float` {converted_float}\n')

    try:
        converted_str = str(value)
    except (Exception, ValueError) as e:
            print(f'🚫 Não foi possível converter {value} do tipo {type(value)} para o tipo `str`\n❗ Motivo: {e}\n')
    else:
        print(f"✅ Foi possível converter {value} do tipo {type(value)} na `string` '{converted_str}'\n")
        
    try:
        converted_complex = complex(value)
    except (Exception, ValueError) as e:
        print(f'🚫 Não foi possível realizar a conversão de um tipo: {type(value)} para outro tipo.\n❗ Motivo: {e}\n')
    else:
        print(f'✅ Foi possível converter {value} do tipo {type(value)} no `complex` {converted_complex}\n')
    
    print('-' * 75)

def calculate_signal_to_noise_ratio(signal_power: float, noise_power: float) -> Optional[float]:
    """
    Calcula a Relação Sinal-Ruído (SNR) em decibéis (dB).

    Esta função demonstra a utilização de ferramentas de um módulo externo (`math`)
    para realizar cálculos científicos. Inclui uma cláusula de guarda para
    evitar erros matemáticos (divisão por zero ou log de número não positivo).

    Args:
        signal_power (float): A potência do sinal.
        noise_power (float): A potência do ruído

    Returns:
        Optional[float]: O valor da SNR em decibéis, ou None se a entrada for inválida.
    """
    if signal_power <= 0 or noise_power <= 0:
        return None
    
    ratio = signal_power / noise_power
    decibels = 10 * math.log10(ratio) 
    return decibels

def display_twice(message: str) -> None:
    """
    Função "nula" que realiza uma ação: imprimir uma mensagem duas vezes.

    Args:
        message (str): A mensagem a ser impressa no console.
    """
    print(message)
    print(message)

def compose_message(part1: str, part2: str) -> str:
    """
    Função "com resultado" que concatena duas strings e retorna a nova string.

    Esta função demonstra o conceito de variável local (`composed_message`) e 
    a separação entre a lógica de cálculo e a apresentação do resultado.

    Args:
        part1 (str): A primeira parte da mensagem que será concatenada.
        part2 (str): A segunda parte da mensagem que será concatenada.

    Returns:
        str: A união das duas strings resultando em uma única string.
    """
    composed_message = part1 + part2
    return composed_message

if __name__ == '__main__':

    print('--- Fase 1: Explorando Funções de Conversão de Tipo ---\n')
    analyze_value('123')
    analyze_value(98.6)
    analyze_value(0)
    analyze_value('Olá, Mundo')
    analyze_value([1, 2, 3])

    print('\n--- Fase 2: Definindo e Compondo Novas Funções ---\n')
    
    # 1. Demonstração do uso de um módulo externo
    print('1. Cálculo da Relação Sinal-Ruído (SNR):')
    snr = calculate_signal_to_noise_ratio(signal_power=100, noise_power=10)
    if snr is not None:
        print(f'   Resultado: {snr:.2f} dB\n')

    # 2. Demonstração da composição de funções
    print('2. Demonstração de Composição e Fluxo de Execução:\n')
    
    # Criamos duas partes de uma mensagem
    prefixo = 'Explícito é melhor do que '
    sufixo = 'implícito.'
    
    # Usamos a nossa função "com resultado" para compor a mensagem final
    mensagem_completa = compose_message(prefixo, sufixo)
    
    # Usamos a nossa função "nula" para exibir o resultado
    print('   A função `compose_message` criou a mensagem:')
    print(f"   '{mensagem_completa}'")
    print('\n   A função `display_twice` agora a exibirá duas vezes:\n')
    display_twice(mensagem_completa)
    print()