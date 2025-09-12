"""
Módulo de Lógica de Negócio para Operações Fundamentais com Sequências.

Este módulo contém um conjunto de componentes de lógica pura, formalmente
verificados e agnósticos a qualquer interface, que implementam operações
fundamentais de processamento de dados sobre estruturas sequenciais. Cada
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
    Set,
    Optional
    )

__author__ = 'Enock Silos'
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Production'

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
    
    if not all(isinstance(x, (int, float)) for x in samples):
        raise ValueError(
            ' A sequência de entrada contém valores não-numéricos.'
        )

    return sum(samples) / len(samples)

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
    """
    Extrai os elementos únicos de uma sequência, preservando a ordem original de aparição.

    Este componente implementa um algoritmo de deduplicação com preservação
    de ordem, garantindo duas propriedades fundamentais na sequência de
    saída: a unicidade dos elementos e a manutenção da ordem relativa de
    sua primeira aparição na sequência de entrada.

    A implementação é otimizada para complexidade de tempo linear(O(n))
    através do uso de um conjunto (`set`) auxiliar para o rastreamento de
    elementos já processados, o que permite uma verificação de pertencimento
    em tempo médio constante (O(1)). Esta característica de alto desempenho
    torna o componente adequado para o processamento de grandes volumes de
    dados, como os encontrados em pipelines de telemetria ou análise de
    eventos científicos.

    O design é genericamente tipado (TypeVAr) para operar sobre qualquer
    iterável de elementos que sejam `hashable`.

    Args:
        data (Iterable[T]): A sequência de entrada a ser processada. Pode ser
                            qualquer iterável cujos elementos sejam de um
                            tipo `hashable` (ex: int, str, tuple).

    Returns:
        Sequence[T]: Uma nova sequência contendo os elementos únicos da
                     entrada, na ordem de sua primeira aparição.

    Raises:
        TypeError: Se os elementos contidos no iterável de entrada `data`
                   não forem `hashable`.
    """
    unique_items: List[T] = []
    seen: Set[T] = set()

    try:
        for item in data:
            if item not in seen:
                unique_items.append(item)
                seen.add(item)
    except TypeError as e:
        raise ValueError(
            '\n ERRO: um elemento não `hashable` foi encontrado na sequência de entrada'
            ) from e

    return unique_items

def try_pop_last_item(items: List[T]) -> Optional[T]:
    """
    Executa uma ação `pop` segura e resiliente em uma lista mutável.

    Este componente atua como um invólucro de alta integridade (`resilient
    wrapper`) sobre o método `list.pop()`nativo. Sua função primária é
    prevenir a terminação não controlada do sistema devida a uma exceção
    `IndexError` ao operar sobre uma coleção vazia.

    Em conformidade com o PESSMC 2.1, ele implementa o princípio de
    Degradação Graciosa: em vez de levantar uma exceção, a função sinaliza
    a falha de forma determinística retornando `None`. A função possui um
    efeito colateral documentado: ela modifica a lista de entrada `items`
    no caminho de sucesso.

    Args:
        items (List[T]): A lista mutável da qual o último elemento será
                         removido. Esta lista será modificada no local
                         (in-place) se a operação for bem-sucedida.

    Returns:
        Optional[T]: O último elemento (de tipo `T`) se a lista não estiver
                     vazia; caso contrário, `None`.
    """
    try:
        return items.pop()
    except IndexError:
        return None