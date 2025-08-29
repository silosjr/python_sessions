"""
iterative_process_examples.py    
"""

from __future__ import annotations
from typing import List 
from practical_conditional_logic import get_valid_integer_from_user

__author__ = 'Enock Silos'
__version__ = '1.2.0' 
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

def demonstrate_generation_of_filtered_numbers() -> None:
    """
    Demonstra a geração de uma sequência numérica filtrada por uma condição.

    Este procedimento serve como um exemplo didático para a combinação de um
    processo iterativo com uma lógica de decisão (filtragem), um padrão
    fundamental em processamento de dados. A função encapsula um fluxo 
    completo: coleta de dados, validação robusta e a geração da sequência
    final, culminando em uma apresentação de dados formatada.

    A implementação utiliza uma abordagem declarativa e "Pythonica" através de
    uma List Comprehension com uma cláusula `if`. Esta técnica permite a
    construção de uma lista de resultados de forma concisa e eficiente, 
    expressando a intenção de "gerar uma lista de números que satisfaçam
    uma condição" em uma única linha concise e legível de código.

    A função também pratica a programação defensiva, validando a entrada do
    usuário para garantir que o limite da sequência seja um número positivo,
    evitando comportamentos inesperados ou ilógicos.

    Side Effects:
        - Imprime a sequência gerada e mensagens de status na saída 
          padrão (`print`).
        - Realiza chamadas de I/O para obter os dados do usuário.
    """
    print('\n--- DEMONSTRAÇÃO DE GERAÇÃO DE NÚMEROS FILTRADOS ---\n')

    upper_limit = get_valid_integer_from_user('Digite o limite numérico para a sequência a ser gerada: ')

    if upper_limit is None:
          return

    if upper_limit <= 0:
          print('ERRO: O valor limite deve ser um número positivo e maior que 0. Encerrando o programa')
          return
    
    odd_numbers: List[str] = [str(i) for i in range(1, upper_limit + 1) if i % 2 != 0]

    formatted_list = ' -> '.join(odd_numbers)
    print(f'\nSequência de Números Ímpares Gerada até {upper_limit}: \n{formatted_list}\n --- FIM DA SEQUÊNCIA ---')



def main() -> None:
    # demonstrate_simple_counting()
    # demonstrate_iterative_countdown()
    demonstrate_generation_of_filtered_numbers()


if __name__ == '__main__':
    main()