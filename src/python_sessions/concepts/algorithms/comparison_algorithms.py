"""
comparison_algorithms.py

Este módulo é dedicado à implementação de algoritmos fundamentais de
comparação, servindo como um recurso didático para o estudo de operações
essenciais em ciência da computação. O foco reside na dissecação de lógicas
que, embora frequentemente abstraídas por funções nativas da linguagem,
constituem a base do processamento de dados e da análise computacional.

O principal algoritmo aqui apresentado resolve o problema de encontrar os
valores de extremo (mínimo e máximo) em uma coleção de dados numéricos. A
implementação é feita de forma explícita, utilizando uma única passagem
(single-pass) sobre a estrutura de dados, o que caracteriza uma solução de
complexidade de tempo linear, O(n). Este enfoque não apenas resolve o
problema de forma eficiente, mas também ilustra conceitos cruciais como
iteração, estado (state), inicialização de variáveis de controle e
programação defensiva para o tratamento de casos de borda (edge cases).
"""
from __future__ import annotations
from typing import List, Tuple, Union

__author__ = 'Enock Silos'
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'


def find_min_and_max_from_list(
    numbers: List[Union[int, float]]
) -> Tuple[Union[int, float], Union[int, float]]:
    """
    Determina os valores mínimo e máximo em uma lista de dados numéricos.

    Este algoritmo implementa uma busca por extremos através de uma única
    iteração sobre a lista de entrada. A estratégia consiste em inicializar
    duas variáveis de estado, `min_value` e `max_value`, com o primeiro
    elemento da coleção. Subsequentemente, o algoritmo percorre os elementos
    restantes, comparando cada um com os valores de extremo atuais e
    atualizando-os conforme necessário.

    A complexidade de tempo desta operação é O(n), onde 'n' é o número de
    elementos na lista, pois cada elemento é visitado exatamente uma vez.
    A complexidade de espaço é O(1), visto que a memória utilizada para as
    variáveis de controle não depende do tamanho da entrada.

    Args:
        numbers (List[Union[int, float]]): Uma lista não vazia de números,
            podendo conter uma mistura de inteiros e pontos flutuantes.

    Returns:
        Tuple[Union[int, float], Union[int, float]]: Uma tupla contendo dois
            valores: o primeiro é o elemento de menor valor encontrado na
            lista, e o segundo é o elemento de maior valor. O tipo dos
            elementos retornados (int ou float) é preservado conforme a
            entrada.

    Raises:
        ValueError: Se a lista `numbers` fornecida como argumento estiver
            vazia, uma vez que é impossível determinar valores de extremo
            em uma coleção sem elementos.
    """
    if not numbers:
        raise ValueError('A lista não pode estar vazia.')

    min_value: Union[int, float] = numbers[0]
    max_value: Union[int, float] = numbers[0]

    for value in numbers[1:]:
        if value < min_value:
            min_value = value

        if value > max_value:
            max_value = value

    return min_value, max_value


if __name__ == '__main__':
    """
    Bloco de demonstração para a execução direta do módulo.

    Este segmento é executado apenas quando o script é invocado como o
    programa principal. Ele serve para testar e demonstrar a funcionalidade
    da função `find_min_and_max_from_list`, exibindo um exemplo claro de
    sua aplicação e do resultado esperado.
    """
    sample_list = [-89, 78.5, 3, 988, 46, 5.2, 99, 18]
    min_val, max_val = find_min_and_max_from_list(sample_list)

    title = " Demonstração do Algoritmo de Busca por Extremos "
    width = 70
    
    print("\n" + f"{title:#^{width}}")
    print(f" » Lista de Entrada: {sample_list!r}")
    print(f" ├{'─' * (width - 4)}┤")
    print(f" » Valor Mínimo Encontrado: {min_val}")
    print(f" » Valor Máximo Encontrado: {max_val}")
    print(f" └{'─' * (width - 4)}┘\n")
