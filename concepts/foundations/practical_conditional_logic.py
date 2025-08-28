"""
practical_conditional_logic.py

Este módulo serve como um compêndio prático para o estudo de estruturas de
controle condicional em Python. Através de uma série de exemplos aplicados,
o módulo demonstra como as declarações `if`, `elif` e `else` são utilizadas
para governar o fluxo de execução de um programa, permitindo que ele tome
decisões e execute blocos de código distintos com base na avaliação de
expressões booleanas.

Cada função encapsula um problema do mundo real, ilustrando um caso de uso
específico da lógica condicional. O objetivo é solidificar a compreensão
teórica do controle de fluxo, conectando-a a cenários tangíveis e práticos,
um pilar fundamental na transição do conhecimento acadêmico para a
proficiência em engenharia de software.
"""
from __future__ import annotations
import random
import locale
from typing import Final, List, Union, Optional
import sys
import os

# Bloco de configuração de path para permitir importações inter-módulos
# em um ambiente de desenvolvimento local.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_root)

from concepts.algorithms.comparison_algorithms import find_min_and_max_from_list

__author__ = 'Enock Silos'
__version__ = '1.2.0'
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

MAXIMUM_VELOCITY_CONSTRAINT: Final[float] = 80.0
PENALTY_CALCULATION_FACTOR: Final[int] = 5

def get_valid_integer_from_user(prompt_message: str) -> Optional[int]:
    """
    Obtém uma entrada numérica inteira e validada pelo usuário.

    Esta função auxiliar (`helper function`) encapsula o processo completo de
    solicitação, validação e conversão de uma entrada do usuário para o tipo
    inteiro. Ela opera dentro de um laço de repetição (`while`) para garantir
    a robustez, persistindo na solicitação até que uma entrada válida seja
    fornecida ou que o usuário opte por cancelar a operação.

    A função implementa um contrato de retorno dual: devolve um objeto do tipo
    `int` em caso de sucesso na conversão, ou o valor `None` para sinalizar
    explicitamente que a operação foi interrompida pelo usuário. Este padrão
    permite que a função que a chama trate a desistência de forma graciosa, sem
    a necessidade de levantar exceções para um comportamento esperado.

    Args:
        prompt_message (str): A mensagem a ser exibida ao usuário para
                              solicitar a entrada de dados.

    Returns:
        Optional[int]: O número inteiro fornecido pelo usuário, ou `None` se
                       a operação for cancelada.

    Side Effects:
        - Lê dados a entrada padrão (`input`).
        - Imprime mensagens de erro e status na saída padrão (`print`).
    """
    while True:
        try:
            user_input = input(prompt_message)

            if user_input.lower() == 's':
                print('\nO usuário cancelou a operação.')
                return None 
            
            converted_number = int(user_input)
            return converted_number

        except ValueError:
            print('ERRO: Entrada inválida. Por favor, digite apenas números inteiros.')
            continue
        except Exception as e:
            print(f'Ocorreu um erro ao tentar processar a operação: {e}')
            break 

def compare_two_numbers() -> None:
    """
    Orquestra a comparação de dois números inteiros fornecidos pelo usuário.

    Este procedimento serve como demonstração didática da estrutura de 
    controle condicional `if/elif/else` e do princípio da Separação de
    Responsabilidades. A função atua como a camada de orquestração, 
    delegando a tarefa complexa de obter e validar a entrada do usuário
    à função auxiliar `get_valid_integer_from_user`.

    A função gerencia o fluxo da aplicação, verificando se a função 
    auxiliar retornou um sinal de cancelamento (`None`) e encerrando 
    a sua própria execução de forma graciosa. Caso ambas as entradas 
    sejam válidas, ela procede à avaliação lógica utilizando operadores
    relacionais para determinar e exibir a relação de magnitude entre
    os dois números.

    Side Effects:
        - Imprime o resultado da comparação e mensagens de status na 
          saída padrão (`print`).
    """
    print('\n--- DEMONSTRAÇÃO DE COMPARAÇÃO NUMÉRICA ---')

    num1 = get_valid_integer_from_user('Digite um número inteiro: ')
    if num1 is None:
        return 
    
    num2 = get_valid_integer_from_user('Digite o segundo número inteiro: ')
    if num2 is None:
        return 
    
    if num1 < num2:
        result_message = f'{num1} é MENOR que {num2}'
    elif num1 > num2:
        result_message = f'{num1} é MAIOR que {num2}'
    else:
        result_message = f'Os números são IGUAIS ({num1} = {num2})'

    print(f'\nResultado da comparação: {result_message}\n')

def demonstrate_classification_of_numbers_by_range() -> None:
    """
    Demonstra a classificação de um número em faixas de valores dinâmicos.

    Este procedimento serve como um exemplo didático avançado da estrutura de
    controle `if/elif/else` e da sintaxe de comparações encadeadas em Python
    (ex: `min <= valor < max`). A função eleva o conceito de classificação
    ao utiliza limites de faixa gerados de forma pseudoaleatória,
    garantido que cada execução apresente um novo desafio lógico.

    A função adota o princípio de Separação de Responsabilidades ao delegar
    a complexa tarefa de obter e validar a entrada do usuário à função 
    auxiliar `get_valid_integer_from_user`. Ela gerencia o fluxo da 
    aplicação, tratando o caso de cancelamento pelo usuário de forma graciosa
    e, em caso de sucesso, executa a lógica de classificação e apresenta o 
    resultado de forma clara e contextualizada.

    Side Effects:
        - Imprime o resultado da classificação e mensagens de status na saída
          padrão (`print`).
        - Altera o estado do gerador de números pseudoaleatórios do módulo 
          `random`
    """
    print('\n--- DEMONSTRAÇÃO DE CLASSIFICAÇÃO EM FAIXAS DINÂMICAS ---')

    reference_value_1 = random.randint(-10, 10)
    reference_value_2 = random.randint(20, 40)

    print(f'As faixas de referência para esta execução são: < {reference_value_1} e >= {reference_value_2}')

    number_to_classify = get_valid_integer_from_user('Digite um número inteiro para ser classificado: ')

    if number_to_classify is None:
        return 
    
    if number_to_classify < reference_value_1:
        result_message = f'O número {number_to_classify} é MENOR que a primeira faixa ({reference_value_1}).'
    elif reference_value_1 <= number_to_classify < reference_value_2:
        result_message = f'O número {number_to_classify} está NO INTERVALO entre ({reference_value_1}) e ({reference_value_2}).'
    else:
        result_message = f'O número digitado {number_to_classify} é MAIOR OU IGUAL que a segunda faixa {reference_value_2}'

    print(f'\nResultado da Classificação: {result_message}\n')

def calculate_speeding_fine() -> None:
    """
    Simula a operação de um radar de velocidade e calcula uma multa se aplicável.

    Este procedimento demonstra uma estrutura de controle condicional `if/else`.
    O fluxo de execução é bifurcado com base na avaliação de uma expressão
    booleana: a velocidade aferida é maior que o limite permitido?

    A função utiliza o módulo `random` para simular a medição de velocidade,
    criando um cenário dinâmico. A interação com o usuário é substituída por
    uma simulação, elevando o nível de abstração do exemplo. A formatação
    monetária é gerenciada pelo módulo `locale` para apresentação adequada.

    Side Effects:
        - Imprime dados na saída padrão (`print`), simulando a interface de
          um sistema de radar.
        - Utiliza o estado global do gerador de números aleatórios.
    """
    measured_speed: float = random.uniform(50.0, 240.0)
    print(f'''
          \t--- RADAR KM 129 - RODOVIA DOS BANDEIRANTES ---\n
          --- VELOCIDADE MÁXIMA PERMITIDA NO TRECHO: {MAXIMUM_VELOCITY_CONSTRAINT:.0f} KM/H ---\n
          --- STATUS: Realizando leitura de velocidade dos veículos...\n
          ''')
    if measured_speed > MAXIMUM_VELOCITY_CONSTRAINT:
        fine_value: float = PENALTY_CALCULATION_FACTOR * (measured_speed - MAXIMUM_VELOCITY_CONSTRAINT)
        formatted_fine: str = locale.currency(fine_value, grouping=True)
        print(f'''
                  ---------------------------------------------------------------
                  ATENÇÃO: Veículo ultrapassou limite de velocidade permitido.
                  VELOCIDADE CAPTURADA: {measured_speed:.1f} Km/h
                  O motorista será multado
                  VALOR DA MULTA = {formatted_fine}
                  ---------------------------------------------------------------
                  ''')
    else:
        print(f'''
                  -----------------------------------------------------
                  Você passou pelo radar a {measured_speed:.1f} km/h\n
                  Dirija com cuidado. Tenha uma boa viagem!
                  -----------------------------------------------------
                  ''')

def get_min_max_from_user_input() -> None:
    """
    Coleta interativamente uma lista de números do usuário e exibe os extremos.

    Esta função demonstra um padrão de design comum de separação de
    responsabilidades (Separation of Concerns). Ela é responsável apenas pela
    interface com o usuário (I/O) e pela validação da entrada, orquestrando
    um loop `while` para a coleta de dados. A lógica de processamento
    principal (encontrar o mínimo e o máximo) é delegada a uma função pura
    importada de outro módulo (`find_min_and_max_from_list`).

    A função implementa uma lógica de conversão de tipo inteligente, tentando
    converter a entrada para `int` e, em caso de falha, para `float`,
    preservando assim o tipo de dado original sempre que possível.

    Side Effects:
        - Lê dados da entrada padrão (`input`).
        - Imprime dados na saída padrão (`print`).
    """
    print('''\n
    Vamos encontrar o menor e o maior valor numérico a partir de números que você informar.
    Para o uso coreto desta função você deverá informar apenas valores numéricos.
    ''')
    input_list: List[Union[int, float]] = []
    while True:
        try:
            user_input = input('Digite um número (ou "Q" para sair): ')
            if user_input.lower() == 'q':
                break

            try:
                input_list.append(int(user_input))
                print(f'    Lista Atual: {input_list!r}')
            except ValueError:
                input_list.append(float(user_input))
                print(f'    Lista Atual: {input_list!r}')

        except ValueError:
            print('''
                  Digite uma entrada válida. Exemplo: 23
                                                 Exemplo: 4.75
                  Ou digite "Q" para SAIR:
                  ''')

    if input_list:
        min_val, max_val = find_min_and_max_from_list(input_list)
        print(f'''
                  O maior valor digitado foi {max_val}
                  O menor valor digitado foi {min_val}
        ''')
    else:
        print('\n    Nenhum número foi inserido.\n')

if __name__ == '__main__':
    """
    Ponto de entrada (entry point) para a execução direta do script.

    Este bloco é executado somente quando o arquivo é invocado como o programa
    principal. Sua principal responsabilidade é configurar o ambiente de
    execução (como o `locale` para formatação de moeda) e orquestrar a
    chamada das funções de demonstração contidas no módulo.
    """
    try:
        locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
    except locale.Error:
        print("Aviso: Locale 'pt_BR.UTF-8' não foi encontrado. Usando formatação padrão.")

    calculate_speeding_fine()
    get_min_max_from_user_input()
    compare_two_numbers()
    demonstrate_classification_of_numbers_by_range()