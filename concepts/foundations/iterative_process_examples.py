"""
iterative_process_examples.py    
"""

from __future__ import annotations
from typing import List, Callable, Tuple 
from practical_conditional_logic import get_valid_integer_from_user

__author__ = 'Enock Silos'
__version__ = '1.8.0' 
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

QUIZ_DATA = [
     {'question_text': 'What?', 'correct_answer': 'b'},
     {'question_text': 'How?', 'correct_answer': 'a'},
     {'question_text': 'Why?', 'correct_answer': 'd'}
]

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

def multiply_by_addition(number_to_add: int, times_to_add: int) -> int:
    """
    Simula a operação de multiplicação através de um processo de adição iterativa.

    Este procedimento computacional demonstra, a partir de princípios elementares,
    como uma operação aritmética de ordem superior (multiplicação) pode ser 
    decomposta em uma sequência de operações fundamentais (adição). A função
    serve como um exemplo canônico de um algoritmo de acumulação.

    A lógica opera sobre um acumulador, inicializado com o elemento neutro da
    adição (zero), e itera um número de vezes definido por `times_to_add`. A 
    cada iteração, o `number_to_add` é somado ao valor corrente do acumulador.
    O resultado final é o produto dos dois operandos de entrada.

    Args:
        number_to_add (int): O número a ser repetidamente somado (o multiplicando).
        times_to_add (int): O número de vezes que a adição será executada (o
        multiplicador).

    Returns:
        int: O resultado final da operação, equivalente a `number_to_add` * `times_to_add`.
    """
    accumulator = 0
         
    for _ in range(times_to_add):
         accumulator += number_to_add
         
    return accumulator

def demonstrate_multiplication_with_addition() -> None:
    """
    Orquestra uma demonstração interativa da simulação da multiplicação.

    Esta função serve como a camada de interface para o algoritmo puro
    `multiply_by_addition`. Ela encapsula todo o fluxo de interação com o
    usuário, incluindo a solicitação de dados, a validação de cancelamento e
    a apresentação final do resultado.

    A implementação exemplifica o princípio da Separação de Responsabilidades
    (Separation of Concerns), onde a lógica de negócio (o cálculo em si) é
    isolada da lógica de apresentação (I/O), resultando em um código mais
    modular, testável e de fácil manutenção.

    Side Effects:
        - Realiza chamadas de I/O para obter os dados do usuário (`input`).
        - Imprime o resultado formatado e mensagens de status na saída 
          padrão (`print`).
    """
    print('\n--- DEMONSTRAÇÃO: MULTIPLICAÇÃO VIA ADIÇÃO ---\n')

    first_number = get_valid_integer_from_user('Digite o multiplicando ("S" SAIR):')
    if first_number is None:
         return 
    
    second_number = get_valid_integer_from_user('Digite o multiplicador ("S" SAIR):')
    if second_number is None:
         return 

    result = multiply_by_addition(first_number, second_number)
    print(f'\n{first_number} x {second_number} = {result}')

def divide_by_subtraction(dividend: int, divisor: int) -> Tuple[int, int]:
    """
    Simula a operação de divisão inteira através de um processo de subtração iterativa.

    Este procedimento computacional demonstra, a partir de princípios elementares, como
    a operação da divisão inteira, que resulta em um quociente e um resto, pode ser 
    decomposta em uma sequência de subtrações. A função serve como um exemplo canônico
    de um algoritmo de redução e contagem.

    A lógica opera sobre uma variável que representa o dividendo corrente, subtraindo 
    iterativamente o divisor desta enquanto o resultado se mantiver não-negativo. Um 
    contador é incrementado a cada subtração bem-sucedida. Ao término do laço, o valor
    final do contador representa o quociente, e o valor remanescente no dividendo 
    corrente constitui o resto.

    Args:
        dividend (int): O número a ser dividido.
        divisor (int): O número pelo qual se divide.

    Returns:
        Tuple[int, int]: Uma tupla contendo dois inteiros, representando respectivamente
                         o quociente e o resto da divisão.
    """
    quotient_counter = 0
    current_dividend = dividend

    while current_dividend >= divisor:
          current_dividend -= divisor 
          quotient_counter += 1

    return quotient_counter, current_dividend

def demonstrate_division_with_subtraction() -> None:
    """
    Orquestra uma demonstração interativa da simulação de divisão inteira.

    Esta função serve como a camada de interface para o algoritmo puro
    `divide_by_subtraction`. Ela encapsula todo o fluxo de interação com
    o usuário incluindo a solicitação de dados (dividendo e divisor), a
    validação de entradas e casos de borda (como a divisão por zero), e 
    a apresentação final do resultado de forma didática.

    A implementação exemplifica o princípio de Separação de Responsabilidades,
    onde a lógica de negócio (o cálculo em si) é isolada da lógica de 
    apresentação (I/O). A mensagem de saída é construída para não apenas mostrar
    o resultado, mas para explicar o processo algorítmico subjacente, reforçando
    o valor pedagógicoda demonstração.

    Side Effects:
        - Realiza chamadas de I/O para obter os dados do usuário (`input`).
        - Imprime o resultado formatado e mensagens de status na saída 
          padrão (`print`).
    """
    print('\n--- DEMONSTRAÇÃO DA DIVISÃO COM USO DA SUBTRAÇÃO ---\n')

    dividend = get_valid_integer_from_user('Digite um número para o dividendo ("S" SAIR): ')
    if dividend is None:
        return  

    divisor = get_valid_integer_from_user('Digite um número para o divisor ("S" SAIR): ')
    if divisor is None:
        return 
    
    if divisor == 0:
        print('Não é possível dividir por zero. Encerrando.')
        return
    
    quotient, remainder = divide_by_subtraction(dividend, divisor)

    print(f'''
             Análise do Processo: O divisor ({divisor}) foi subtraído do dividendo ({dividend})
             com sucesso por {quotient} vezes (o quociente), resultando em um valor final de 
             {remainder} ( o resto).   
          \n''')

def demonstrate_quiz_session() -> None:
    """
    Orquestra uma demonstração de uma sessão de quiz interativo.

    Este procedimento computacional exemplifica a implementação de um motor
    de quiz genérico, um padrão arquitetural fundamental que promove a 
    Separação de Responsabilidades (Separation of Concerns). A lógica do quiz
    - o conjunto de perguntas e suas respectivas respostas corretas - é
    abstraída em uma estrutura de dados externa (`QUIZ_DATA`), permitindo que
    a função opere como um executor agnóstico ao conteúdo específico.

    O algoritmo demonstra um processo iterativo com estado, onde um laço 
    percorre a estrutura de dados do quiz. A cada iteração, o estado da 
    sessão (a pontuação do usuário) é atualizado com base na avaliação da
    resposta fornecida. A função `enumerate` é utilizada para a geração
    dinâmica e correta da numeração das questões.

    A implementação também foca na experiência do usuário (UX), fornecendo
    feedback imediato após cada resposta. Adicionalmente, emprega uma 
    expressão condicional aninhada em uma f-string para garantir a 
    correção gramatical na apresentação da pontuação final (singular vs.
    plural), um exemplo de refinamento de interface.

    Side Effects:
        - Realiza chamadas de I/O para obter as respostas do usuário (`input`).
        - Imprime as questões, o feedback e o resultado final na saída padrão
          (`print`).

    """
    points = 0
    print('\n--- DEMONSTRAÇÃO DE SESSÃO DE QUIZ INTERATIVO ---\n')
    for question_number, question_data in enumerate(QUIZ_DATA):
        print(f'Questão {question_number + 1}: {question_data['question_text']}')

        user_answer: str = input('Sua Resposta: ')
        if user_answer.lower() == question_data['correct_answer']:
            print('✅ Resposta Correta!')
            points += 1
        else:
             print(f'❌ Resposta Incorreta. A resposta correta era: {question_data['correct_answer']}')
    
    print('\n' + '-' * 30)
    print(f'Pontuação Final: {points} {'ponto' if points == 1 else 'pontos'}')
    print('--- FIM DA SESSÃO ---\n')

def main() -> None:
    demonstrate_simple_counting()
    demonstrate_iterative_countdown()
    demonstrate_custom_filtering('Números Ímpares', lambda n: n % 2 != 0)
    demonstrate_custom_filtering('Múltiplos de 3', lambda n: n % 3 == 0)
    demonstrate_custom_multiplication_table()
    demonstrate_multiplication_with_addition()   
    demonstrate_division_with_subtraction() 
    demonstrate_quiz_session()

if __name__ == '__main__':
    main()