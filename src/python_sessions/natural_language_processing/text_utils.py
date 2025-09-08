"""
Módulo de Ferramentas Auxiliares para processamento de texto.

Este módulo contém funções utilitárias que podem ser usadas para limpar
e manipular arquivos de texto, especialmente aqueles provenientes de
fontes como o Projeto Gutenberg.
"""

from __future__ import annotations
from typing import TextIO, Tuple, TypeVar

__author__ = 'Enock Silos'
__version__ = '0.3.0'
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Production'

# T é uma variável de tipo genérico, permitindo que a função shift
# funcione com tuplas de qualquer tipo (str, int, etc.)
T = TypeVar('T')

def skip_gutenberg_header(file_pointer: TextIO) -> None:
    """
    Avança um objeto de arquivo até o final do cabeçalho do Projeto Gutemberg.

    Args:
        file_pointer (TextIO): O objeto de arquivo (stream) de texto aberto.
    """
    for line in file_pointer:
        if line.startswith('******The Project Gutenberg Etext of Emma'):
            break

def shift(prefix: Tuple[T, ...], word: T) -> Tuple[T, ...]:
    """
    Desloca uma tupla, removendo o primeiro elemento e adicionando um novo ao final.

    Esta função "pura" não modifica a tupla original, mas retorna uma nova.

    Args:
        prefix (Tuple[T, ...]): A tupla de entrada (ex: ('a', 'rose')).
        word (T): O novo elemento a ser adicionado ao final.

    Returns:
        Tuple[T, ...]: Uma nova tupla com os elementos deslocados (ex: 'rose', 'is').
    """
    return prefix[1:] + (word,)

if __name__ == '__main__':
    # Exemplo de uso da função shift com uma tupla.
    # No contexto de Markov, esta função poderia ser usada para
    # "mover" o foco de uma palavra para a próxima.
    print("Demonstrando a função shift:")
    my_tuple = (['Python', 'C'], ['MySQL'], ['SQL', 'Git'])
    shifted_tuple = shift(my_tuple, 'GitHub')
    print(f"Tupla original: {my_tuple}")
    print(f"Tupla deslocada: {shifted_tuple}")

