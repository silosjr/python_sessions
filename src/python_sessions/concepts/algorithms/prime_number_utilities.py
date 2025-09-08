"""

"""

from __future__ import annotations
from math import sqrt
from typing import Iterator, Optional
from python_sessions.utils.input_handlers import get_valid_integer_from_user

__author__ = 'Enock Silos'
__version__ = '1.0.0' 
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

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
        raw_input = input(prompt_message)
        if raw_input.lower() == 'q':
            return None 
        try:
            return int(raw_input)
        except ValueError:
            print(' ERRO: Entrada inválida. Por favor, digite apenas números inteiros.')
            continue
        except Exception as e:
            print(f' Ocorreu um erro ao tentar processar a operação: {e}')
            break 


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

def run_prime_checker_ui() -> None:
    """
    
    """
    prompt_message = (
        ' Digite um número inteiro para verificar sua primalidade ("Q" para encerrar): '
                     )
    while True:
        candidate_prime_input = get_valid_integer_from_user(prompt_message)
        if candidate_prime_input is None:
            return
        if is_prime(candidate_prime_input):
            print(f'\n {candidate_prime_input} é um número primo.')
        else:
            print(f' {candidate_prime_input} não é um número primo.')
        print('-' * 20)

if __name__ == '__main__':
    run_prime_checker_ui()
