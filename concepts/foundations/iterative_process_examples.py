"""
iterative_process_examples.py    
"""

from __future__ import annotations
from typing import List, Callable
from practical_conditional_logic import get_valid_integer_from_user

__author__ = 'Enock Silos'
__version__ = '1.5.0' 
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

def demonstrate_simple_counting() -> None:
    """
    Demonstra um processo de contagem interativa com limites definidos pelo usuário.

    Este procedimento serve como um exemplo didático fundamental para o conceito
    de iteração controlada. A função encapsula um fluxo completo: coleta de 
    dados, validação robusta e execução do processo iterativo, culminando em
    uma apresentação de dados formatada de maneira profissional.

    A implementação adota o princípio da Separação de Responsabilidades ao
    delegar a tarefa de obter e validar a entrada do usuário à função auxiliar
    `get_valid_integer_from_user`. A função principal gerencia a lógica de 
    negócio, validando a consistência dos dados de entrada (o número inicial
    deve ser menor ou igual ao final) antes de prosseguir.

    O núcleo da lógica de contagem foi implementado utilizando um padrão 
    declarativo e "Pythonico", que emprega a função `range()` e uma `List
    Comprehension` para gerar a sequência de números de uma só vez. A
    apresentação final utiliza o método de string `.join()` para formatar
    a saída, uma técnica que demonstra a separação entre a coleta de dados e a
    sua posterior formatação.

    Side Effects:
        - Imprime o resultado da contagem e mensagens de status na saída
          padrão (`print`).
        - Realiza chamadas de I/O para obter os dados do usuário.
    """
    print('\n--- DEMONSTRAÇÃO DE CONTAGEM SIMPLES ---')

    start_number = get_valid_integer_from_user('Digite um número inicial para a contagem ("S" -> SAIR): ')

    if start_number is None:
        return
    
    end_number = get_valid_integer_from_user('Digite um número final para a contagem ("S" -> SAIR): ')
    
    if end_number is None:
            return
    
    if start_number <= end_number:
        numbers_to_print: List[str] = [str(i) for i in range(start_number, end_number + 1)]

        formatted_list: str = ' -> '.join(numbers_to_print)
        print(f'\nContagem: {formatted_list}')
        print('--- FIM DA CONTAGEM ---\n')
    else:
        print('ERRO: O número inicial deve ser menor do que o número final.')
        return 

def demonstrate_iterative_countdown() -> None:
    """
    Demonstra um processo de contagem regressiva utilizando uma abordagem declarativa.

    Este procedimento serve como um exemplo didático para o conceito de iteração 
    controlada em ordem decrescente. Em vez de um laço iterativo explícito
    (como `while`ou `for`), esta implementação utiliza uma List Comprehension
    combinada com a função `range()` e um passo (step) negativo. Esta é uma 
    técnica "Pythonica" avançada que expressa a intenção do código de forma 
    mais concisa e declarativa.

    Pedagogicamente, esta função serve como um contraponto direto à sua
    contraparte recursiva (`countdown`em `control_flow_and_recursion.py`),
    permitindo ao usuário comparar e constrastar as duas principais
    abordagens para resolver problemas que envolvem repetição.

    A função encapsula um fluxo completo: coleta de dados, validação robusta
    e execução do processo iterativo, culminando em uma apresentação de dados
    formatada.

    Side Effects:   
        - Imprime o resultado da contagem e mensagens de status na saída
          padrão (`print`).
        - Realiza chamada de I/O para obter dados do usuário.
    """
    print('\n--- DEMONSTRAÇÃO DE CONTAGEM REGRESSIVA ITERATIVA ---')

    start_number = get_valid_integer_from_user('Digite um número inicial para a contagem regressiva ("S" SAIR): ')

    if start_number is None:
          return
     
    end_number = get_valid_integer_from_user('Digite um número final para a contagem regressiva ("S" SAIR): ')

    if end_number is None:
          return 
     
    if start_number >= end_number:
        numbers_to_print: List[str] = [str(i) for i in range(start_number, end_number - 1, -1)]
        formatted_list = ' -> '.join(numbers_to_print)        
        print(f'\nContagem Regressiva: {formatted_list}')
        print('--- FIM DA CONTAGEM ---\n')
    else:
          print('ERRO: O número inicial deve ser maior ou igual do que o número final.')
          return 

def demonstrate_custom_filtering(sequence_description: str, filter_rule: Callable[[int], bool]) -> None:
    """
    Demonstra a geração de uma sequência numérica filtrada por uma regra customizável.

    Este procedimento exemplifica o conceito de Função de Ordem Superior
    (High-Order Function), um pilar da programação funcional. A função aceita
    não apenas dados (o limite da sequência), mas também lógica na forma de um
    predicado (`filter_rule`). Este predicado é uma função `Callable`que recebe
    um inteiro e retorna um booleano, determinando se o número deve ou não ser
    incluído na sequência resultante.

    Esta abordagem de design abstrai a lógica de filtragem, transformando a
    função em uma ferramenta genérica e reutilizável, capaz de gerar qualquer
    tipo de sequência filtrada (números ímpares, múltipos de um valo, etc.)
    sem que a sua implementação interna precise ser alterada.

    A implementação utiliza uma List Comprehension, passando cada elemento da
    sequência gerada pelo `range()` através da `filter_rule` fornecida,
    numa demonstração de código declarativo, conciso e "Pythonico".

    Args:
        sequence_description (str): Uma descrição textual da sequência que está
                                    a ser gerada (ex: "Números Ímpares),
                                    utilizada para a apresentação dos resultados.
        filter_rule (Callable[[int], bool]): A função predicado que será executada
                                             para cada número. Deve retornar `True`
                                             para os números a serem incluídos e 
                                             `False` caso contrário.

    Side Effects:
        - Imprime a sequência gerada e mensagens de status na saída 
          padrão (`print`).
        - Realiza chamadas de I/O para obter os dados do usuário.
    """
    print('\n--- DEMONSTRAÇÃO DE GERAÇÃO DE NÚMEROS FILTRADOS ---\n')

    upper_limit = get_valid_integer_from_user('Digite o limite numérico máximo para a sequência a ser gerada: ')

    if upper_limit is None:
          return

    if upper_limit <= 0:
          print('ERRO: O valor limite deve ser um número positivo e maior que 0. Encerrando o programa')
          return
    
    filtered_number_strings: List[str] = [str(i) for i in range(1, upper_limit + 1) if filter_rule(i)]

    formatted_list = ' -> '.join(filtered_number_strings)
    print(f'\n>>> Sequência Gerada para a condição fornecida: {sequence_description}: \n{formatted_list} ', end='')
    print('FIM DA SEQUÊNCIA ')

def demonstrate_custom_multiplication_table() -> None:
    """
    Demonstra a geração de uma tabuada de multiplicação com intervalo customizável.

    Este procedimento serve como um exemplo didático avançado de um processo
    iterativo. A função não apenas executa uma repetição controlada, mas também
    implementa um padrão de design profissional para a apresentação de dados 
    tabulados: o cálculo dinâmico de largura de coluna.

    A lógica de iteração é realizada utilizando um laço `for` em conjunto com a 
    função `range()`, a abordagem canônica e "Pythonica" para percorrer
    sequências numéricas definidas.

    O principal valor pedagógico reside na lógica de formatação. Antes da
    iteração, a função pré-calcula a largura máxima necessária para cada
    coluna, inspecionando os valores de entrada. Esta largura é então
    utilizada em f-strings para garantir um alinhamento perfeito de saída,
    independentemente da magnitude dos números fornecidos pelo usuário.
    Esta técnica é um exemplo prático de programação adaptativa e robusta.

    A função também encapsula um fluxo completo de iteração, incluindo a
    coleta de múltiplos dados, validação de consistência lógica (o início
    do intervalo não pode ser maior que o fim) e o tratamento de erros.

    Side Effects:
        - Imprime a tabuada gerada e mensagens de status na saída 
          padrão (`print`).
        - Realiza chamadas de I/O para obter os dados do usuário.
    """
    print('\n--- DEMONSTRAÇÃO DE TABUADA CUSTOMIZADA DE MULTIPLICAÇÃO ---\n')

    table_number = get_valid_integer_from_user('Informe o número da tabuada a ser gerada: ')

    if table_number is None:
         return 
    
    if table_number <= 0:
         print('ATENÇÃO: O número para a tabuada deve ser não-negativo e diferente de zero. Encerrando.')
         return 
    
    start_range = get_valid_integer_from_user('Digite o número inicial do intervalo: ')

    if start_range is None:
         return
    
    end_range = get_valid_integer_from_user('Digite o número final do intervalo: ')
    print()

    if end_range is None:
         return 
    
    if start_range > end_range:
         print('ATENÇÃO: O valor para o número inicial não pode ser maior que o valor número final do intervalo. Encerrando.')
         return 
    
    max_table_number_width = len(str(table_number))
    max_result_width = len(str(table_number * end_range))
    max_width_start_range = len(str(start_range))
    max_width_end_range = len(str(end_range))
    max_result_multiplier = max(max_width_start_range, max_width_end_range)

    for n in range(start_range, end_range + 1):
         print(f'{table_number:>{max_table_number_width}} x {n:>{max_result_multiplier}} = {n * table_number:>{max_result_width}}\n')

def main() -> None:
    demonstrate_simple_counting()
    demonstrate_iterative_countdown()
    demonstrate_custom_filtering('Números Ímpares', lambda n: n % 2 != 0)
    demonstrate_custom_filtering('Múltiplos de 3', lambda n: n % 3 == 0)
    demonstrate_custom_multiplication_table()
    
if __name__ == '__main__':
    main()