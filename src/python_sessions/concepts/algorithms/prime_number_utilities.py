"""
Módulo de Ferramentas de Aritmética de Primos com interface de Linha de Comando.

Este módulo fornece um conjunto coeso de funcionalidades para a análise e
geração de números primos, encapsulado em uma interface de usuário interativa
(CLI). A arquitetura do módulo adere estritamente ao Princípio de 
Responsabilidade Única (SRP), decompondo a aplicação em componentes lógicos,
de apresentação e controle.

Funcionalidades Principais:
-   `is_prime`: Uma função pura e otimizada para a verificação de primalidade.
-   `generate_primes`: Um gerador de avaliação preguiçosa para a produção
     eficiente de uma sequência infinita de primos.
-   `main`: Orquestra uma interface de menu (REPL) que permite ao usuário
     interagir com as funcionalidades acima.

O design do módulo serve como um caso de estudo para a construção de 
ferramentas de linha de comando modulares e robustas em Python, priorizando
a clareza arquitetônica e a experiência do usuário.
"""

from __future__ import annotations
from math import sqrt
from typing import Iterator, Optional
from itertools import islice
from python_sessions.utils.input_handlers import (
    get_valid_integer_from_user,
    cli_pause
)

__author__ = 'Enock Silos'
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Production'

PADDING_WIDTH = 4
COLUMNS_PER_LINE = 15

def is_prime(number: int) -> bool:
    """
    Determina a primalidade de um inteiro através de um algoritmo otimizado.

    Na teoria dos números, um número primo é definido como um número natural
    maior que 1 que não possui divisores positivos além de 1 e ele mesmo.
    Esta função implementa o método de divisão por tentativa (trial division)
    incorporando um conjunto de otimizações matemáticas para avaliar de forma
    eficiente a primalidade do inteiro fornecido.

    A lógica de avaliação segue uma sequência hierárquica de exclusão:
    1.  Casos triviais: Números menores ou iguais a 1 são, por definição,
        excluídos do conjunto dos números primos.
    2.  Caso especial do par: O número 2 é tratado como um caso especial,
        sendo o único número primo par.
    3.  Exclusão dos pares: Todos os outros números pares são compostos,
        visto que são divisíveis por 2, e são imediatamente descartados.

    O núcleo do algoritmo reside no laço `while`, que itera sobre potenciais
    divisores. A variável `divisor` representa um candidato a fator do `number`.
    A iteração prossegue sob duas otimizações cruciais:

    a) Limite do Espaço de Busca: A iteração de `divisor` ocorre apenas até
       a raiz qudrada de `number`. Este limite baseia-se no teorema 
       fundamental de que, se um número `n` é composto (i.e., n = a * b),
       então pelo menos um de seus fatores (`a` ou `b`) deve ser menor ou
       igual a `sqrt`. Testar divisores além deste ponto é computacionalmente
       redundante.

    b) Incremento de Divisores Ímpares: Após a exclusão inicial de todos os 
       números pares, os únicos candidatos a divisores primos restantes são
       ímpares. O `divisot` é inicializado em 3 e incrementado em +2 em 
       cada iteração (3, 5, 7,...), o que efetivamente reduz pela metade o
       número de testes de divisão necessários dentro do espaço de busca já
       otimizado.

    Se nenhum divisor for encontrado até o limite da raiz quadrada, o número
    é conclusivamente determinado como primo.

    Args:
        number (int): O inteiro a ser avaliado para primalidade.

    Returns:
        bool: Retorna `True` se `number` for um número primo, e `False`
              caso contrário.
    """
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    divisor = 3
    while divisor <= int(sqrt(number)):
        if number % divisor == 0:
            return False
        divisor += 2
    return True

def generate_primes() -> Iterator[int]:
    """
    Gera uma sequência infinita de números primos utilizando avaliação preguiçosa.

    Esta função é implementada como um gerador Python, o que significa que ela
    produz números primos sob demanda, sem computá-los todos de uma vez ou
    armazená-los em memória. Esta abordagem é conhecida como avaliação 
    preguiçosa (lazy evaluation).

    O mecanismo opera através de um laço infinito (`while True`) que testa 
    sequencialmente cada inteiro (`candidate_number`), começando pelo 2. A
    lógica de verificação de primalidade é delegada à `is_prime()`.

    A palavra-chave `yield` é o coração do gerador: ele pausa o estado da
    função, entrega o número primo encontrado e só retorna a execução a partir
    daquele ponto quando o próximo valor for solicitado pelo consumidor do
    iterador. Este design é altamente eficiente em termos de memória e ideal
    para tarefas que requerem um número grande ou indefinido de primos.

    Exemplos de Uso:
        Para obter os primeiros 10 números primos de forma segura a partir
        deste gerador infinito, pode-se usar `itertools.islice`:

        >>> from itertools import islice
        >>> first_ten_primes = list(islice(generate_primes(), 10))
        >>> print(first_ten_primes)
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    Yields:
        Iterator[int]: Um iterador que produz indefinidamente o próximo número
                       primo na sequência como um inteiro
    """
    candidate_number = 2
    while True:
        if is_prime(candidate_number):
            yield candidate_number
        candidate_number += 1

def _display_menu() -> None:
    """
    Renderiza o menu principal da aplicação na saída padrão.

    Esta função é responsável exclusivamente pela apresentação da interface
    do menu, garantindo uma formatação visual consistente e alinhada.
    """
    menu_prime_number_utils = [
    ' ANALISADOR DE PRIMOS: Verificação e Geração',
    ' Escolha uma das opções abaixo:',
    ' [1] - Verificar a primalidade de um número',
    ' [2] - Gerar os "N" primeiros primos',
    ' [Q] - Encerra a sessão'
    ]

    content_width = max(len(line) for line in menu_prime_number_utils)
    internal_width = content_width + PADDING_WIDTH

    top_border = f'╔{'═' * (internal_width)}╗'
    middle_border = f'╠{'═' * (internal_width)}╣'
    bottom_border = f'╚{'═' * (internal_width)}╝'

    title = menu_prime_number_utils[0]
    header_line = f'║{title:^{internal_width}}║'

    print(top_border)
    print(header_line)
    print(middle_border)

    for line in menu_prime_number_utils[1:]:
        padded_line = f'  {line}'
        print(f'║{padded_line:<{internal_width}}║')
        
    print(bottom_border)

def _handle_user_choice(selected_option: str) -> None:
    """
    Atua como um 'dispatcher', executando a função apropriada.

    Com base na escolha do utilizador, esta função delega a execução para
    a função de manipulação de negócio correspondente.

    Args:
        selected_option (str): A opção inserida pelo usuário no menu.
    """
    if selected_option == '1':
        _handle_prime_check()
    elif selected_option == '2':
        _handle_prime_generation()
    else:
        print('\n ERRO: Por favor, informe uma das opções válidas do menu.')

def _handle_prime_check() -> None:
    """
    Orquestra o fluxo de trabalho para verificar a primalidade de um número.

    Esta função encapsula a lógica para a opção [1] do menu:
    solicita um número ao utilizador, invoca as função `is_prime` e
    apresenta o resultado formatado.
    """
    prompt = ' Por favor, informe um número inteiro para verificar sua primalidade:\n ❭❭❭ '
    number_to_check = get_valid_integer_from_user(prompt)
    if number_to_check is None:
        return None
    if is_prime(number_to_check):
        print(f'\n {number_to_check} é um número primo.')
    else:
        print(f'\n {number_to_check} não é um número primo.')

def _handle_prime_generation() -> None:
    """
    Orquestra o fluxo para gerar os N primeiros números primos.

    Encapsula a lógica de negócio para a ação [2] do menu: solicita ao
    usuário a quantidade de primos, valida a entrada, consome o gerador
    `generate_primes` de forma segura e exibe o resultado numa grelha formatada.
    """
    prompt = ' Por favor, informe a quantidade de números primos a ser gerada: \n ❭❭❭ '
    n = get_valid_integer_from_user(prompt)
    if n is None:
        return None
    if n <= 0:
        print('\n ERRO: Por favor, informe apenas números inteiros positivos.')
        return None
    print(' Entrada aceita. Cálculo iniciado.')

    first_primes = list(islice(generate_primes(), n))

    column_counter = 0
    
    for prime in first_primes:
        print(prime, end=' ')
        column_counter += 1
        if column_counter == COLUMNS_PER_LINE:
            print()
            column_counter = 0
    print()
    return

def main() -> None:
    """
    Função principal que orquestra a interface de linha de comando (REPL).

    Esta função é o ponto de entrada da aplicação. Ela implementa o ciclo
    de Leitura-Avaliação-Impressão-Repetição (Read-Eval-Print-Loop), orquestrando as
    chamadas às funções de exibição, entrada e manipulação da escolha do 
    usuário, até que a sessão seja encerrada.
    """
    while True:
        _display_menu()
        selected_option = input(' ❭❭❭ ')

        if selected_option.lower() == 'q':
            print('\n Sessão Encerrada.')
            break

        _handle_user_choice(selected_option)
        
        if selected_option in ('1', '2'):
            cli_pause()

if __name__ == '__main__':
    main()
