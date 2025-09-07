"""
Um módulo didático que explora a implementação de processos iterativos
através de exemplos práticos e do mundo real.

Este script serve como um compêndio para o estudo de laços de repetição
(`while`, `for`), gerenciamento de estado e a separação de responsabilidades
entre a lógica de cálculo e a interface com o usuário. Cada função principal
(`demonstrate...`) encapsula um problema discreto, utilizando funções
auxiliares para garantir a robustez, a clareza e a reutilização do código.

O módulo evolui de simples contagens para simulações complexas, como um
motor de ponto de venda (PDV), ensinando não apenas a sintaxe de Python,
mas também os padrões de design de software que sustentam aplicações 
profissionais e escaláveis.

Este módulo foi expandido para incluir uma suíte de funções que implementam
um explorador interativo de grelhas matemáticas. Esta nova funcionalidade é
arquitetada em torno de uma função de ordem superior que gera uma matriz de
resultados ao aplicar uma operação binária arbitrária sobre o produto de dois
intervalos numéricos definidos pelo utilizador. O sistema é complementado por
uma interface de linha de comando para a parametrização da operação e dos
operandos, e por um procedimento de visualização que renderiza a matriz resultante
numa tabela de texto com larguras de coluna ajustadas dinamicamente para uma
apresentação otimizada dos dados.
"""

from __future__ import annotations
from typing import List, Callable, Tuple, Dict, Union, Iterable, Optional
import locale
from wcwidth import wcswidth
import operator 
from practical_conditional_logic import get_valid_integer_from_user
from practical_conditional_logic import get_valid_answer_from_user
from practical_conditional_logic import get_valid_float_from_user

__author__ = 'Enock Silos'
__version__ = '1.10.0'
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

QUIZ_DATA = [
     {'question_text': 'What?', 'correct_answer': 'b'},
     {'question_text': 'How?', 'correct_answer': 'a'},
     {'question_text': 'Why?', 'correct_answer': 'd'}
]

PRODUCT_CATALOG: Dict[str, Dict[str, Union[str, float]]] = {
    'CAM-MSC-BR-M': {
        'name': 'Camiseta Masculina Branca - Tamanho M',
        'price': 169.90
        },
    'TEN-FEM-PT-38': {
        'name': 'Tênis Feminino Preto - Tamanho 38',
        'price': 299.99
        },
    'CEL-SAM-A52-BL': {
        'name': 'Celular Samsung A52 - Azul',
        'price': 1099.99
    },
    'FON-BLU-JBL-VP': {
        'name': 'Fone Bluetooth JBL - Vermelho e Preto',
        'price': 379.90
    },
    'NOT-DEL-I5-16GB': {
        'name': 'Notebook Dell i5 - 16GB RAM',
        'price': 5999.99
    },
    'VES-GAM-PRE-XXL': {
        'name': 'Vestido Gama Preto - Tamanho XXL',
        'price': 579.90
    },
    'BOL-COU-MR-PEQ': {
        'name': 'Bolsa Couro Marrom - Pequena',
        'price': 799.99
    },
    'REL-CAS-GSH-NEG': {
        'name': 'Relógio Casio G-Shock - Preto',
        'price': 899.00
    },
    'TV-SAM-55-UHD': {
        'name': "Smart TV Samsung 55''",
        'price': 4099.99
    },
    'LIV-FIC-1984-ORW': {
        'name': 'Livro Ficção "1984" - George Orwel',
        'price': 59.90
    }
}

BRAZILIAN_CURRENCY_DENOMINATIONS: List[int] = [
    20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1
]
CENTS_PER_REAL: int = 100
BANKNOTE_THRESHOLD_IN_CENTS: int = 100
PADDING_WIDTH = 4
OPERATIONS_MAP: Dict[str, Callable] = {
    '1': operator.add,
    '2': operator.sub,
    '3': operator.mul,
    '4': operator.truediv
}
INTERVAL_BOUND_VIOLATION_ERROR_MESSAGE = (
' ERRO: O limite inferior especificado para o intervalo deve ser menor ou igual ao limite superior. '
' Por favor, verifique os valores informados para garantir conformidade com as restrições do intervalo.'
)

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
    o valor pedagógico da demonstração.

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

def update_shopping_cart(cart: Dict[str, int], action: Dict[str, Union[str, int]]) -> Dict[str, int]:
    """
    Processa uma ação e devolve o novo estado do carrinho de compras.

    Esta função representao o motor de lógica central (backend) do sistema de Ponto
    de Venda (PDV) Sua principal responsabilidade corporativa é garantir a
    integridade transacional do carrinho, processando ações atômicas como a 
    adição ou remoção de itens. Do ponto de vista acadêmico, esta é uma
    função pura que implementa o padrão de design 'state reducer', um pilar 
    de arquiteturas de gerenciamento de estado previsíveis.

    A função opera sob o princípio da imutabilidade: ela nunca modifica o
    dicionário `cart` original. Em vez disso, cria uma cópia e aplica as 
    modificações, retornando um novo objeto de estado. Esta abordagem previne
    efeitos colaterais (side effects) e torna o fluxo de dados do sistema
    explícito e fácil de depurar, um requisito crítico para sistemas
    financeiros e de inventário.

    Args:
        cart (Dict[str, int]): O dicionário que representa o estado atual do
                               carrinho de compras. As chaves são os SKUs dos
                               produtos e os valore são suas quantidades.
        action (Dict[str, Union[str, int]]): Um dicionário que descreve a 
                                             operação a ser executada
                                             seguindo o 'Command Pattern'.

    Returns:
        Dict[str, int]: Uma nova versão do dicionário do carrinho, refletindo
                        o estado após a aplicação da ação.
    """
    updated_cart = cart.copy()
    action_type = action.get('type')

    if action_type == 'ADD_ITEM':
        product_sku = action.get('sku')
        quantity_to_add = action.get('quantity', 1)
        if isinstance(quantity_to_add, int) and quantity_to_add > 0:
            updated_cart[product_sku] = updated_cart.get(product_sku, 0) + quantity_to_add
    
    elif action_type == 'REMOVE_ITEM':
        product_sku = action.get('sku')
        quantity_to_remove = action.get('quantity', 1)
        if isinstance(quantity_to_remove, int) and product_sku in updated_cart:
            new_quantity = updated_cart[product_sku] - quantity_to_remove
            if new_quantity > 0:
                updated_cart[product_sku] = new_quantity
            else:
                del updated_cart[product_sku]

    return updated_cart

def display_product_catalog() -> None:
    """
    Exibe o catálogo de produtos em uma tabela formatada.
    """
    sku_column_title = 'CÓDIGO SKU DO PRODUTO'
    name_column_title = 'NOME DO PRODUTO'
    price_column_title = 'PREÇO'

    col_sku_width = 25
    col_name_width = 45
    col_price_width = 20

    top_border = f'╔{'═' * (col_sku_width + 2)}╦{'═' * (col_name_width + 2)}╦{'═' * (col_price_width + 2)}╗'
    header_line = f'║ {sku_column_title:^{col_sku_width}} ║ {name_column_title:^{col_name_width}} ║ {price_column_title:^{col_price_width}} ║'
    middle_border = f'╠{'═' * (col_sku_width  + 2)}╬{'═' * (col_name_width + 2)}╬{'═' * (col_price_width + 2)}╣'
    bottom_border = f'╚{'═' * (col_sku_width + 2)}╩{'═' * (col_name_width + 2)}╩{'═' * (col_price_width + 2)}╝'

    print(top_border)
    print(header_line)
    print(middle_border)

    for sku, details in PRODUCT_CATALOG.items():
        product_name = details['name']
        product_price = details['price']
        data_row = (f'║ {sku:<{col_sku_width}} ║ {product_name:<{col_name_width}} ║ {locale.currency(product_price, grouping=True):>{col_price_width}} ║')
        print(data_row)

    print(bottom_border)

def display_cart_status(cart: Dict[str, int], cart_total: float) -> None:
    """
    Exibe o estado atual do carrinho de compras e o seu total.

    Esta função atua como a camada de apresentação ('view') para a sessão de PDV.
    A sua única responsabilidade corporativa é renderizar os dados de uma venda 
    em andamento em um formato de extrato claro e profissional para o operador.

    Do ponto de vista acadêmico, este é um procedimento 'impuro' cuja única 
    finalidade são os efeitos colaterais (I/O), imprimindo uma representação
    visual do estado da aplicação sem conter nenhuma lógica de negócio.

    Args:
        cart (Dict[str, int]): _description_
        cart_total (float): _description_
    """
    title_sku_col = 'CÓDIGO (SKU)'
    title_name_col = 'NOME DO PRODUTO'
    title_quantity_col = 'QUANTIDADE'
    title_unit_price_col = 'PREÇO UNITÁRIO'
    title_subtotal_col = 'SUBTOTAL'
    title_total_col = 'VALOR TOTAL'

    width_sku_col = 20
    width_name_col = 45
    width_quantity_col = 15
    width_unit_price_col = 20
    width_subtotal_col = 20

    header_line = (
        f'║ {title_sku_col:<{width_sku_col}} ║ '
        f'{title_name_col:<{width_name_col}} ║ '
        f'{title_quantity_col:^{width_quantity_col}} ║ '
        f'{title_unit_price_col:>{width_unit_price_col}} ║ '
        f'{title_subtotal_col:>{width_subtotal_col}} ║'
    )

    top_border = (
        f'╔{"═" * (width_sku_col + 2)}╦'
        f'{"═" * (width_name_col + 2)}╦'
        f'{"═" * (width_quantity_col + 2)}╦'
        f'{"═" * (width_unit_price_col + 2)}╦'
        f'{"═" * (width_subtotal_col + 2)}╗'
    )

    middle_border = (
        f'╠{"═" * (width_sku_col + 2)}╬'
        f'{"═" * (width_name_col + 2)}╬'
        f'{"═" * (width_quantity_col + 2)}╬'
        f'{"═" * (width_unit_price_col + 2)}╬'
        f'{"═" * (width_subtotal_col + 2)}╣'
    )

    bottom_border = (
        f'╚{"═" * (width_sku_col + 2)}╩'
        f'{"═" * (width_name_col + 2)}╩'
        f'{"═" * (width_quantity_col + 2)}╩'
        f'{"═" * (width_unit_price_col + 2)}╩'
        f'{"═" * (width_subtotal_col + 2)}╝'
    )

    print(top_border)
    print(header_line)
    print(middle_border)

    for sku, quantity in cart.items():
        details = PRODUCT_CATALOG[sku]
        name = details['name']
        price = details['price']
        subtotal = price * quantity

        row = (
            f'║ {sku:<{width_sku_col}} ║ '
            f'{name:<{width_name_col}} ║ '
            f'{quantity:^{width_quantity_col}} ║ '
            f'{locale.currency(price, grouping=True):>{width_unit_price_col}} ║ '
            f'{locale.currency(subtotal, grouping=True):>{width_subtotal_col}} ║'
        )
        print(row)

    print(bottom_border)

    total_box_padding = (
        (width_sku_col + 2) +
        (width_name_col + 2) +
        (width_quantity_col + 2) +
        3
    )

    total_box_top = (
        f'{" " * total_box_padding}'
        f'╔{"═" * (width_unit_price_col + 2)}╦{"═" * (width_subtotal_col + 2)}╗'
    )

    total_box_content = (
        f'{" " * total_box_padding}'
        f'║ {title_total_col:>{width_unit_price_col}} ║ {locale.currency(cart_total, grouping=True):>{width_subtotal_col}} ║'
    )

    total_box_bottom = (
        f'{" " * total_box_padding}'
        f'╚{"═" * (width_unit_price_col + 2)}╩{"═" * (width_subtotal_col + 2)}╝'
    )

    print(total_box_top)
    print(total_box_content)
    print(total_box_bottom)

def calculate_cart_total(cart: Dict[str, int]) -> float:
    """
    Calcula o valor monetário total de um carrinho de compras.

    Esta função de utilidade encapsula a lógica de negócio para a totalização
    de uma venda. Do ponto de vista corporativo, ela garante que o cálculo do
    preço final seja consistente e centralizado, consultando o `PRODUCT_CATALOG`
    como a única fonte da verdade para os preços, um requisito para a 
    conformidade de auditoria.

    Academicamente, esta é uma função de agregação pura que executa uma
    operação de 'map-reduce': primeiro, ela 'mapeia' cada item do carrinho
    (SKU e quantidade) para o seu valor de subtotal e, em seguida, 'reduz'
    esses subtotais a um único valor final através da soma.

    Args:
        cart (Dict[str, int]): O dicionário do carrinho de compras.

    Returns:
        float: O valor total da compra.
    """
    total_amount = 0.0

    for sku, quantity in cart.items():
        price = PRODUCT_CATALOG.get(sku, {}).get('price', 0.0)
        total_amount += price * quantity

    return total_amount

def demonstrate_interactive_pos_session() -> None:
    """
    Orquetra uma sessão de caixa interativa para um sistema de Ponto de Venda.

    Esta função serve como o controlador da inteface de usuário (UI) para a
    simulação. No contexto corporativo, ela representa o 'posto de caixa',
    gerenciando o ciclo de vida de uma transação, desde o seu início até à
    sua finalização. A sua responsabilidade é traduzir as entradas do 
    operador em comandos estruturados e orquestrar a interação entre as
    camadas de lógica e apresentação.

    Academicamente, esta função implementa um laço de eventos (event loop) que
    gerencia o estado de aplicação (`cart`). A cada iteração, ela lê um
    evento do usuário, despacha-o para o motor de lógica (`update_shopping_cart`)
    para obter o novo estado, e, quando solicitado, delega a renderização do
    estado atual para as funções de apresentação.
    """
    cart = {}

    while True:
        print(
            '\n\tMENU DE OPERAÇÕES DO CAIXA:\n'
            '\tPOR FAVOR, ESCOLHA UMA AÇÃO:\n'
            '\t"A" -> ADICIONAR UM ITEM\n'
            '\t"D" -> REMOVER UM ITEM\n'
            '\t"V" -> VISUALIZAR O CARRINHO\n'
            '\t"E" -> FINALIZAR A TRANSAÇÃO\n'
            '\t"Q" -> CANCELAR A SESSÃO\n'
            )
        try:
            selected_action = input('\tSUA OPÇÃO -> ')

            if selected_action.lower() == 'q':
                print('\nSessão do caixa encerrada.')
                return

            elif selected_action.lower() == 'a':
                display_product_catalog()
                selected_sku = input('\nAdicione o código SKU do produto: ').upper()
                if selected_sku not in PRODUCT_CATALOG:
                    print(f'ERRO: Código SKU {selected_sku} não encontrado. Tente novamente.')
                    continue 
                
                selected_quantity = get_valid_integer_from_user('Quantidade ("Q" -> SAIR) = ')
                if selected_quantity is not None:
                    add_item_action = {
                                    'type': 'ADD_ITEM',
                                    'sku': selected_sku,
                                    'quantity': selected_quantity
                                      }
                    cart = update_shopping_cart(cart, add_item_action)
                    print(f"\nItem '{PRODUCT_CATALOG[selected_sku['name']]}' adicionado com sucesso.")
                else:
                    print('\nERRO: CÓDIGO SKU não encontrado no catálogo')
                    continue

            elif selected_action.lower() == 'v':
                if not cart:
                    print('\nO carrinho de compras está vazio.')
                    continue

                cart_total = calculate_cart_total(cart)
                display_cart_status(cart, cart_total)

            elif selected_action.lower() == 'd':
                if not cart:
                    print('\nO carrinho de compras está vazio.')
                    continue
                
                current_cart_total = calculate_cart_total(cart)
                display_cart_status(cart, current_cart_total)

                sku_to_remove = input('\nInforme o código SKU do produto a remover: ').upper()
                
                if sku_to_remove not in cart:
                    print(f'ERRO: Produto com SKU {sku_to_remove} não encontrado no carrinho. Tente novamente.')
                    continue

                quantity_in_cart = cart.get(sku_to_remove)
                prompt = (
                    f'Existem {quantity_in_cart} unidades deste item. '
                    f'Quantas deseja remover? ("Q" -> SAIR):'
                )
                quantity_to_remove = get_valid_integer_from_user(prompt)

                if quantity_to_remove is None:
                    continue 

                if not 0 < quantity_to_remove <= quantity_in_cart:
                    print(f'ERRO: A quantidade a remover deve ser entre 1 e {quantity_in_cart}.')
                    continue

                remove_item_action = {
                    'type': 'REMOVE_ITEM',
                    'sku': sku_to_remove,
                    'quantity_to_remove': quantity_to_remove
                }
                cart = update_shopping_cart(cart, remove_item_action)
                print(f"\nItem '{PRODUCT_CATALOG[sku_to_remove]['name']}' atualizado com sucesso.")
            
            elif selected_action.lower() == 'e':
                if not cart:
                    print('\nO carrinho está vazio. Nenhuma transação a ser finalizada.')
                    continue 

                final_total = calculate_cart_total(cart)
                display_cart_status(cart, final_total)

                customer_purchase_confirmation = get_valid_answer_from_user(
                    '\nConfirma o encerramento da compra?'
                    '\n"Y" => SIM'
                    '\n"N" => NÃO\n'
                )
                if customer_purchase_confirmation is None:
                    continue
                
                if customer_purchase_confirmation:
                    print('❰ TRANSAÇÃO FINALIZADA COM SUCESSO ❱\n')
                    break 
                else:
                    print('\nFinalização da venda cancelada. A sessão continua ativa.')
                    continue
        except ValueError:
            print('\nERRO: Escolha uma opção válida do MENU.')
            continue

def calculate_change_breakdown(total_amount_in_cents: int) -> Dict[int, int]:
    """
    Decompõe um valor monetário no número mínimo de cédulas e moedas.

    Esta função implementa um Algoritmo Guloso (Greedy Algorithm) para a
    resolução do Problema do Troco (Change-Making Problem), um problema
    clássico de otimização combinatória. A implementação é especificamente
    projetada para o sistema monetário brasileiro, cujas denominações 
    formam um sistema canônico, garantindo que a abordagem gulosa sempre
    convirja para a solução ótima (o menor número total de cédulas/moedas).

    O algoritmo opera exclusivamente com os valores inteiros representando
    centavos para garantir a precisão matemátia absoluta, evitando as 
    inconsistências inerentes à aritmética de ponto flutuante em contextos
    financeiros. O processo iterativo percorre as denominações monetárias,
    previamente ordenadas de forma descendente, e, para cada uma, calcula
    quantas vezes ela pode ser subtraída do montante restante.

    Args:
        total_amount_in_cents (int): Valor total em centavos a ser processado.

    Returns:
        Dict[int, int]: Um dicionário que mapeia cada denominação utilizada
                        (em centavos) à sua respectiva quantidade no troco.

    Raises:
        ValueError: Se o `total_amount_in_cents` fornecido for negativo. 
    """
    if total_amount_in_cents < 0:
        raise ValueError('O valor a ser decomposto não pode ser negativo.')

    change_breakdown_report = {}
    remaining_amount_to_decompose = total_amount_in_cents

    for denomination_value in BRAZILIAN_CURRENCY_DENOMINATIONS:
        count_for_denomination = remaining_amount_to_decompose // denomination_value
        if count_for_denomination > 0:
            change_breakdown_report[denomination_value] = count_for_denomination
            remaining_amount_to_decompose -= count_for_denomination * denomination_value

    return change_breakdown_report

def demonstrate_change_making_algorithm() -> None:
    """
    Orquestra a demonstração do Algoritmo Guloso para o Problema do Troco.

    Esta função serve como a camada de interface (UI) e orquestração para a
    demonstração do algoritmo de decomposição de troco. A sua arquitetura
    segue o princípio da Separação de Responsabilidades: a sua única
    responsabilidade é gerir o diálogo com o usuário, coletar e validar a
    entrada, invocar o motor de cálculo puro (`calculate_change_breakdown`) e
    apresentar os resultados de forma clara e profissional.

    A função inicia por solicitar um valor monetário, que é então validado
    para garantir que se encontra no domínio do problema (não-negativo). Em
    seguida, o valor é convertido para uma representação de centavos para
    assegurar a precisão matemática, antes de ser passado para o motor de 
    cálculo. O resultado, um dicionário de dados puros, é então formatado
    em uma tabela de extrato, traduzindo os dados numéricos em uma apresentação
    legível e profissional, que distingue entre cédulas e moedas e respeita
    as convenções gramaticais.

    Side Effects:
        - Realiza chamadas de I/O para obter os dados do usuário (`input`).
        - Imprime o relatório de troco e mensagens de status na saída
          padrão ( `print`).
    """
    print("\n\t❰❰❰ DEMONSTRAÇÃO DO GREEDY ALGORITHM (ALGORITMO GULOSO) ❱❱❱\n")

    prompt = ' Digite um valor monetário para ser decomposto ("Q" -> SAIR): R$'
    total_amount_in_reais = get_valid_float_from_user(prompt)

    if total_amount_in_reais is None:
        return
    
    if total_amount_in_reais < 0.0:
        print('\n ERRO: Informe um valor positivo.\n')
        return
    
    amount_in_cents = int(total_amount_in_reais * CENTS_PER_REAL)

    change_breakdown = calculate_change_breakdown(amount_in_cents)
    
    print(f'\n\t\t❰❰❰ DECOMPOSIÇÃO DE {locale.currency(total_amount_in_reais, grouping=True)} ❱❱❱\n')

    if not change_breakdown:
        print(' Nenhuma cédula ou moeda necessária.')

    title_quantity = 'QUANTIDADE'
    title_unit = 'UNIDADE'
    title_value = 'VALOR (R$)'

    width_quantity = 15
    width_unit = 25
    width_value = 25

    top_border = f'╔{'═' * (width_quantity + 2)}╦{'═' * (width_unit + 2)}╦{'═' * (width_value + 2)}╗'
    header = f'║ {title_quantity:^{width_quantity}} ║ {title_unit:^{width_unit}} ║ {title_value:^{width_value}} ║'
    middle_border = f'╠{'═' * (width_quantity + 2)}╬{'═' * (width_unit + 2)}╬{'═' * (width_value + 2)}╣'
    bottom_border = f'╚{'═' * (width_quantity + 2)}╩{'═' * (width_unit + 2)}╩{'═' * (width_value + 2)}╝'

    print(top_border)
    print(header)
    print(middle_border)

    for denomination_in_cents, count in change_breakdown.items():
        if denomination_in_cents >= BANKNOTE_THRESHOLD_IN_CENTS:
            base_unit_name = 'cédula'
            value_in_reais = denomination_in_cents // CENTS_PER_REAL
            formatted_value = f"R$ {value_in_reais},00"
        else:
            base_unit_name = 'moeda'
            value_in_reais = denomination_in_cents / CENTS_PER_REAL
            formatted_value = locale.currency(value_in_reais, grouping=True)

        unit_label = f'{base_unit_name}{'s' if count != 1 else ''} de'

        data_row = f'║ {count:<{width_quantity}} ║ {unit_label:<{width_unit}} ║ {formatted_value:>{width_value}} ║'
        print(data_row)

    print(f'{bottom_border}\n')

def generate_mathematical_grid(
    operation: Callable[[float, float], float],
    row_operands: Iterable[float],
    column_operands: Iterable[float]
) -> List[List[float]]:
    """
    Constrói uma matriz aplicando uma operação a pares de elementos de dois iteráveis.

    Esta é uma função de ordem superior que opera sobre os princípios do
    produto cartesiano. Para cada elemento no iterável `row_operands`, a função
    aplica a `operation` binária a este elemento em conjunto com cada elemento
    de `column_operands`, sequencialmente. O resultado é uma matriz (lista de
    listas) onde cada célula (i, j) corresponde ao resultado de
    operation(row_operands[i], column_operands[j]).

    Args:
        operation (Callable[[float, float], float]): Uma função binária que
            aceita dois operandos numéricos (float) e retorna um único
            resultado numérico (float).
        row_operands (Iterable[float]): Um iterável de valores numéricos que
            servirão como o primeiro operando em cada aplicação da `operation`.
        column_operands (Iterable[float]): Um iterável de valores numéricos que
            servirão como o segundo operando em cada aplicação da `operation`.

    Returns:
        List[List[float]]: Uma matriz bidimensional contendo os resultados 
                           computados da operação.
    """
    result_grid = []
    for row_val in row_operands:
        computed_row = [operation(row_val, col_val) for col_val in column_operands]
        result_grid.append(computed_row)
    return result_grid

def display_grid_as_table(
    grid_data: List[List[float]],
    row_labels: List[str],
    column_labels: List[str]
) -> None:
    """
    Renderiza uma matriz de dados bidimensional como uma tabela formatada em texto.

    Este procedimento de visualização emprega uma arquitetura de largura de
    coluna dinâmica. Previamente à renderização, a função inspeciona a 
    totalidade dos dados de entrada - incluindo rótulos de linha, rótulos de
    coluna e os dados da própria matriz - para determinar a largura ótima para
    cada coluna. Este cálculo garante uma apresentação perfeitamente alinhada e
    sem truncamento, independentemente da magnitude dos valores. Os valores
    numéricos são formatados para exibição com duas casas decimais.

    Args:
        grid_data (List[List[float]]): A matriz de dados numéricos a ser
                                       exibida, representada como uma lista
                                       de listas.
        row_labels (List[str]): Uma lista de strings que serve como
                                identificadores para cada linha da matriz.
        column_labels (List[str]): Uma lista de strings que serve como o
                                   cabeçalho para cada coluna da matriz.
    """
    if not grid_data or not grid_data[0]:
        print(' Aviso: Não há dados para exibir na grelha.')
        return

    grid_data_str = [[f'{cell:.2f}'for cell in row] for row in grid_data]
    num_data_columns = len(grid_data_str[0])

    first_column_width = len(max(row_labels, key=len))

    column_widths = []
    for col_index in range(num_data_columns):
        items_in_this_column = [column_labels[col_index]]
        for row in grid_data_str:
            items_in_this_column.append(row[col_index])

        longest_item = max(items_in_this_column, key=len)
        width = len(longest_item)
        column_widths.append(width)

    all_widths = [first_column_width] + column_widths

    all_header_labels = [''] + column_labels
    header_parts = [f' {label:^{width}} ' for label, width in zip(all_header_labels, all_widths)]
    header_line = f'║{'║'.join(header_parts)}║'

    border_parts = ['═' * (width + 2) for width in all_widths]
    top_border = f'╔{'╦'.join(border_parts)}╗'
    middle_border = f'╠{'╬'.join(border_parts)}╣'
    bottom_border = f'╚{'╩'.join(border_parts)}╝'

    print(top_border)
    print(header_line)
    print(middle_border)

    for row_label, row_data in zip(row_labels, grid_data_str):
        first_cell = f' {row_label:<{first_column_width}} '
        data_cell_parts = [f' {cell:>{width}} ' for cell, width in zip(row_data, column_widths)]
        data_line = f'║{first_cell}║{'║'.join(data_cell_parts)}║'
        print(data_line)

    print(bottom_border)

def demonstrate_math_grid_explorer() -> None:
    """
    Encapsula e executa o ciclo de vida da aplicação interativa
    'Explorador de Grelhas Matemáticas'.

    Esta função serve como o ponto de entrada principal, orquestrando a
    interação com o utilizador. Define as funções auxiliares aninhadas para
    lógica específica de interface e gere o ciclo de enventos principais (main loop),
    que consiste em:
    1.  Apresentar um menu de operações matemáticas.
    2.  Capturar a seleção do utilizador.
    3.  Coletar e validar os parâmetros de intervalo para a grelha.
    4.  Invocar as funções de núcleo para computar os dados e os rótulos.
    5.  Exibir a grelha resultante como uma tabela formatada.
    O ciclo termina quando o utilizador solicita a saída ou ocorre um erro
    não tratado.
    """
    def get_grid_intervals_from_user() -> Optional[Dict[str, int]]:
        """
        Conduz a interface para a coleta dos limites dos intervalos da grelha.

        A função solicita sequencialmente ao utilizador os limites inferior e
        superior para os intervalos de linhas e colunas. Cada entrada é
        validada para ser um número inteiro através da função externa
        `get_valid_integer_from_user`. Adicionalmente, valida se o limite
        inferior de cada intervalo não é superior ao seu respectivo limite
        superior.

        Returns:
            Optional[Dict[str, int]]: Um dicionário contendo os quatro limites
                (`row_start`, `row_end`, `col_start`, `col_end`) em caso de sucesso,
                ou None se o utilizador anular a operação em qualquer etapa da
                inserção de dados.
        """
        prompt_message_row_start = (
            ' Por favor, insira o valor correspondente ao limite inferior do intervalo de linhas ("Q" para encerrar): '
            )
        row_start = get_valid_integer_from_user(prompt_message_row_start)
        if row_start is None:
            return
        prompt_message_row_end = (
            ' Por favor, insira o valor correspondente ao limite superior do intervalo de linhas ("Q" para encerrar): '
            )
        row_end = get_valid_integer_from_user(prompt_message_row_end)
        if row_end is None:
            return
        prompt_message_col_start = (
            ' Por favor, insira o valor correspondente ao limite inferior do intervalo de colunas ("Q" para encerrar): '
            )
        col_start = get_valid_integer_from_user(prompt_message_col_start)
        if col_start is None:
            return
        prompt_message_col_end = (
            ' Por favor insira o valor correspondente ao limite superior para o intervalo de colunas ("Q" para encerrar): '
            )
        col_end = get_valid_integer_from_user(prompt_message_col_end)
        if col_end is None:
            return

        if not row_start <= row_end or not col_start <= col_end:
            print(INTERVAL_BOUND_VIOLATION_ERROR_MESSAGE)
            return

        return {
            'row_start': row_start, 'row_end': row_end,
            'col_start': col_start, 'col_end': col_end
               }

    def generate_labels(start: int, end: int) -> List[str]:
            """
            Gera uma sequência de rótulos textuais a partir de um intervalo numérico.

            Args:
                start (int): O limite inferior, inclusivo, do intervalo.
                end (int): O limite superior, inclusivo, do intervalo.

            Returns:
                List[str]: Uma lista de strings, onde cada elemento corresponde a um
                           número no intervalo especificado.
            """
            return list(map(str, range(start, end + 1)))

    while True:
        try:
            menu_lines = [
                'OPERAÇÕES MATEMÁTICAS',
                ' Por favor, selecione uma operação matemática para executar: ',
                ' [1] Adição ➕',
                ' [2] Subtração ➖',
                ' [3] Multiplicação ✖️',
                ' [4] Divisão ➗',
                ' [Q] Sair 🚪🏃',
                ' Insira o valor que corresponda à sua escolha'
                         ]

            content_width = max(wcswidth(line) for line in menu_lines)
            frame_width = content_width + PADDING_WIDTH

            top_border = f'╔{'═' * (frame_width)}╗'
            title = menu_lines[0]
            title_width = wcswidth(title)
            padding_total = frame_width - title_width
            padding_left = padding_total // 2
            padding_right = padding_total - padding_left
            header_line = f'║{' ' * padding_left}{title}{' ' * padding_right}║'

            middle_border = f'╠{'═' * (frame_width)}╣'
            bottom_border = f'╚{'═' * (frame_width)}╝'

            print(top_border)
            print(header_line)
            print(middle_border)

            for line in menu_lines[1:]:
                visual_width = wcswidth(line)
                padding_needed = frame_width - visual_width
                padding = ' ' * max(0, padding_needed)
                print(f'║{line}{padding}║')
            
            print(bottom_border)
            selected_option = input('❭❭❭')
            
            if selected_option.lower() == 'q':
                print(' Sessão Encerrada.')
                break

            elif selected_option in OPERATIONS_MAP:
                intervals = get_grid_intervals_from_user()
                if intervals is None:
                    continue
                
                row_start = intervals['row_start']
                row_end = intervals['row_end']
                col_start = intervals['col_start']
                col_end = intervals['col_end']

                operation_function = OPERATIONS_MAP[selected_option]
                if selected_option == '4' and col_start <= 0 <= col_end:
                    print(' ERRO: Impossível dividir por zero.')
                    continue

                grid_data = generate_mathematical_grid(
                            operation_function,
                            range(row_start, row_end + 1),
                            range(col_start, col_end + 1)
                                                      )
                row_labels = generate_labels(row_start, row_end)
                column_labels = generate_labels(col_start, col_end)
                display_grid_as_table(grid_data, row_labels, column_labels)
                break
        except Exception as e:
            print(
                f' Ocorreu um erro inesperado ao tentar realizar a operação'
                f' Detalhes: {e}'
                ' Encerrando a operação.')
            break

def main() -> None:
    """
    Ponto de entrada principal para a execução do script.

    Esta função serve como o orquestrador central, invocando as principais
    funções de demonstração do módulo numa sequência predefinida. A sua
    existência, em conjunto com o bloco `if __name__ == '__main__':`,
    representa um padrão de design canônico em Python que garante que a
    lógica de execução só seja disparada quando o arquivo é executado
    diretamente, e não quando é importado como um módulo por outro script.

    Side Effects:
        - Invoca outras funções que realizam operações de I/O (Entrada/Saída),
          resultando em texto exibido no console e na solicitação de dados
          ao usuário.
    """
    try:
        locale.setlocale(locale.LC_MONETARY, 'pt_BR.utf-8')
    except locale.Error:
        print("Aviso: `locale 'pt_BR.UTF-8' não encontradop. Usando formatação padrão.\n")
    # demonstrate_simple_counting()
    # demonstrate_iterative_countdown()
    # demonstrate_custom_filtering('Números Ímpares', lambda n: n % 2 != 0)
    # demonstrate_custom_filtering('Múltiplos de 3', lambda n: n % 3 == 0)
    # demonstrate_custom_multiplication_table()
    # demonstrate_multiplication_with_addition()
    # demonstrate_division_with_subtraction()
    # demonstrate_quiz_session()
    # demonstrate_interactive_pos_session()
    # demonstrate_change_making_algorithm
    demonstrate_math_grid_explorer()

if __name__ == '__main__':
    main()