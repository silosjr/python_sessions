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
import datetime 

# Bloco de configuração de path para permitir importações inter-módulos
# em um ambiente de desenvolvimento local.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_root)

from concepts.algorithms.comparison_algorithms import find_min_and_max_from_list

__author__ = 'Enock Silos'
__version__ = '0.3.0'
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

MAXIMUM_VELOCITY_CONSTRAINT: Final[float] = 80.0
PENALTY_CALCULATION_FACTOR: Final[int] = 5

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

def get_time_of_day_greeting() -> None:
    """
    Demonstra uma saudação contextual baseada na hora atual do sistema.

    Este procedimento serve como um exemplo didático da estrutura de controle
    `if/elif/else` para a tomada de decisão baseada em faixas numéricas. A 
    função opera de forma não interativa, obtendo a hora atual diretamente 
    do sistema operacional, o que a torna uma simulação robusta e autônoma.

    A implementação adota o princípio da "Fonte Única da Verdade" (Single
    Source of Truth) ao obter a data e a hora completas uma única vez através
    do módulo `datetime`. A partir deste único objeto, os dados necessários
    tanto para a lógica de controle (a hora como um inteiro) quanto para a 
    apresentação (a hora formatada como texto) são derivados. Esta abordagem
    garante a consistência dos dados e a clareza do código.

    Side Effects:
        - Imprime a saudação resultante e a hora atual na saída padrão (`print`).
        - Realiza uma chamada de sistema para obter a hora local.
    """
    print('\n--- DEMONSTRAÇÃO DE SAUDAÇÃO CONTEXTUAL ---')

    now_date_time = datetime.datetime.now()
    hour = now_date_time.hour
    now = now_date_time.strftime('%H:%M:%S')

    if hour < 12:
        greeting = 'Bom dia!'
    elif 12 <= hour < 18:
        greeting = 'Boa tarde!'
    else:
        greeting = 'Boa noite!'

    print(f'{greeting} A hora atual é: {now}')

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

def determine_academic_status() -> None:
    """
    Demonstra a classificação do status acadêmico de um aluno com base na média.

    Este procedimento serve como exemplo didático da estrutura de controle
    `if/elif/else` para classificar um valor numérico em faixas mutuamente
    exclusivas. As regras de negócio (as notas de corte para aprovação e 
    recuperação) são definidas como constantes locais para maior clareza e 
    manutenibilidade.

    A função adota o princípio de Separação de Responsabilidades ao delegar
    a tarefa de obter e validar a entrada do usuário (a média) à função
    auxiliar `get_valid_float_from_user`. Além da validação de tipo, a função
    implementa uma validação de domínio, garantindo que a média inserida 
    esteja dentro de um intervalo academicamente plausível (0 a 10).

    Side Effects:
        - Imprime o resultado da classificação e mensagens de status na saída
          padrão (`print`).
    """
    print('\n--- DEMONSTRAÇÃO DE STATUS ACADÊMICO ---\n')

    PASSING_GRADE_THRESHOLD = 7.0 
    RECOVERY_GRADE_THRESHOLD = 4.0

    student_average = get_valid_float_from_user('Digite a média final do aluno ("S" SAIR): ')

    if student_average is None:
        return
    
    if not (0.0 <= student_average <= 10.0):
        print(f'ERRO: A média {student_average} é inválida. Digite apenas valores entre 0.0 e 10.0')
        return 

    if student_average >= PASSING_GRADE_THRESHOLD:
        academic_status = 'APROVADO'
    elif RECOVERY_GRADE_THRESHOLD <= student_average < PASSING_GRADE_THRESHOLD:
        academic_status = 'EM RECUPERAÇÃO'
    else:
        academic_status = 'REPROVADO'

    print(f'Média Final = {student_average:.2f} *** STATUS => {academic_status}\n')
 
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

    # calculate_speeding_fine()
    # get_min_max_from_user_input()
    # compare_two_numbers()
    # get_time_of_day_greeting()
    # demonstrate_classification_of_numbers_by_range()
    # determine_academic_status()