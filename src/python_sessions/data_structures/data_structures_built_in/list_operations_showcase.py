"""
Módulo de Lógica de Negócio para Operações Fundamentais com Listas.

Este módulo contém um conjunto de componentes de lógica pura, formalmente
verificados e agnósticos a qualquer interface, que implementam operações
fundamentais de processamento de dados sobre estruturas de lista. Cada
componente adere estritamente ao Princípio da Responsabilidade Única,
sendo destinado à importação e reutilização por camadas superiores do sistema,
como interfaces de usuário ou outros serviços de negócio. 
"""

from __future__ import annotations
from typing import (
    List,
    Callable,
    Iterable,
    Tuple,
    TypeVar,
    Sequence,
    Set
    )

__author__ = 'Enock Silos'
__version__ = '0.3.0' 
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

T = TypeVar('T')

def calculate_average(samples: Sequence[float]) -> float:
    """
    Computa a média aritmética de uma sequência de números.

    Esta função implementa o cálculo da média de forma defensiva. Ela opera
    sob um contrato de entrada de somente leitura (`Sequence`), trata
    explicitamente o caso de borda de uma entrada vazia, e levanta uma
    exceção `ValueError` de forma controlada se o contrato de tipo for
    violado em tempo de execução com dados não-numéricos, garantindo uma
    falha previsível.

    Args:
        samples (Sequence[float]): Uma sequência de somente leitura de
                                   números de ponto flutuante para os quais
                                   a média será calculada.

    Returns:
        float: A média aritmética dos números da sequência, ou 0.0 se a
               sequência de entrada estiver vazia.

    Raises:
        ValueError: Se a sequência de entrada contiver um ou mais
                    elementos não-numéricos que impeçam o cálculo.
    """
    if not samples:
        return 0.0
    try:
        return sum(samples) / len(samples)
    except TypeError as e:
        raise ValueError(
            ' A sequência de entrada contém valores não numéricos que '
            ' impedem o cálculo da média.'
        ) from e

def partition_by_predicate(
    data: Iterable[T],
    predicate: Callable[[T], bool]
    ) -> Tuple[List[T], List[T]]:
    """
    Particiona um iterável em duas listas com base em um predicado.

    Esta função de alta ordem implementa um motor de particionamento estável
    e agnóstico ao tipo. Ela itera sobre um fluxo de dados de entrada e
    distribui cada elemento em uma de duas partições de saída, com base no
    resultado booleano de uma função de predicado fornecida. Este design
    permite a sua reutilização em uma vasta gama de cenários de triagem e
    classificação de dados em pipelines de processamento.

    Args:
        data (Iterable[T]): O fluxo de dados de entrada a ser processado.
                            Pode ser qualquer objeto iterável do Python.
        predicate (Callable[[T], bool]): A função de classificação que é
                                         invocada para cada elemento. Deve
                                         aceitar um elemento do tipo T e
                                         retornar um valor booleano.

    Returns:
        Tuple[List[T], List[T]]: Uma tupla contendo duas listas. A primeira
                                 lista contém todos os elementos para os
                                 quais o predicado avaliou como `True`. A
                                 segunda contém todos os elementos para os
                                 quais o predicado avaliou como `False`. A
                                 ordem relativa dos elementos é preservada
                                 em ambas as partições.
    """
    passed_items: List[T] = []
    failed_items: List[T] = []
    
    for i in data:
        if predicate(i):
            passed_items.append(i)
        else:
            failed_items.append(i)

    return passed_items, failed_items

def extract_unique_preserving_order(
    data: Iterable[T]
) -> Sequence[T]:
    """_summary_

    Args:
        data (Iterable[T]): _description_

    Returns:
        Sequence[T]: _description_
    """
    unique_items: List[T] = []
    seen: Set[T] = set()

    for item in data:
        if item not in seen:
            unique_items.append(item)
            seen.add(item)

    return unique_items