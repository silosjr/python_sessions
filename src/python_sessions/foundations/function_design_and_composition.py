"""
Uma exploração sobre abstração procedural e composição funcional em Python.

Este módulo serve como uma demonstração prática de princípios fundamentais de
engenharia de software, realizados através da linguagem de programação Python.
Ele ilustra como tarefas procedurais complexas podem ser sistematicamente
decompostas em funções mais simples, reutilizáveis e parametrizadas. Os
conceitos centrais aqui explorados são cruciais para o desenvolvimento de
sistemas de software escaláveis, manuteníveis e compreensíveis.

Conceitos Fundamentais Demonstrados:
------------------------------------
1.  **Decomposição Funcional**: A estratégia primária empregada é a
    decomposição de um problema complexo — como a renderização de uma grade —
    em uma hierarquia de funções mais simples e de responsabilidade única.
    Cada função encapsula uma parte específica da lógica (ex: desenhar uma
    viga horizontal, desenhar postes verticais), que pode ser desenvolvida,
    testada e compreendida de forma independente.

2.  **Generalização por Meio da Parametrização**: O módulo demonstra a
    evolução de funções estáticas de propósito específico para utilitários
    dinâmicos de propósito geral. Ao introduzir parâmetros (ex: `total_width`,
    `grid_size`), as funções são abstraídas de "números mágicos" e constantes,
    aumentando assim sua aplicabilidade e reusabilidade em uma gama maior de
    domínios de problemas.

3.  **Funções de Ordem Superior (Higher-Order Functions)**: O script explora
    o conceito de funções como cidadãs de primeira classe. Funções como
    `do_twice` e `do_four` aceitam outras funções como argumentos (tipos
    `Callable`), fornecendo um mecanismo poderoso para abstrair o fluxo de
    controle e padrões de repetição. Este é um conceito fundamental em
    paradigmas de programação funcional.

4.  **Aderência ao Princípio DRY (Don't Repeat Yourself)**: Através do uso
    de laços e funções de ordem superior, a implementação final elimina
    sistematicamente a redundância de código presente nas versões iniciais.
    Isso não apenas reduz as linhas de código, mas, mais importante, minimiza
    a superfície para erros potenciais e simplifica a manutenção futura.

5.  **Expressões Idiomáticas (Pythonic) e Legibilidade**: O processo de
    refatoração enfatiza a clareza e o uso de expressões idiomáticas do Python.
    Isso inclui a adoção de nomes descritivos para variáveis e funções, a
    aplicação rigorosa de dicas de tipo (type hints) conforme a PEP 484 para
    análise estática e clareza, e a utilização de métodos nativos (`str.rjust`)
    onde eles oferecem uma alternativa mais concisa e eficiente à
    implementação manual.

Este módulo destina-se a ser tanto um utilitário funcional quanto uma
ferramenta pedagógica, adequado para o estudo por novatos em ciência da
computação e como referência para praticantes experientes sobre os princípios
de código limpo e design robusto.
"""

from __future__ import annotations
from typing import Any, Callable

__author__ = 'Enock Silos'
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'


def right_justify(text: str, total_width: int) -> None:
    """
    Imprime uma string justificada à direita dentro de uma largura total.

    Esta função implementa a lógica de justificação manualmente, calculando
    o preenchimento de espaços necessário e concatenando-o com o texto.

    Args:
        text (str): A string a ser justificada
        total_width (int): A largura total de caracteres da linha de saída final.
                           A string será preenchida com espaços à sua esquerda para
                           se ajustar a esta largura.
    """
    padding_length = total_width - len(text)

    if padding_length < 0:
        padding_length = 0

    padding = ' ' * padding_length
    final_text = padding + text 
    print(final_text)

def right_justify_pythonic(text: str, total_width: int) -> None:
    """
    Imprime uma string justificada à direita (implementação idiomática).
    
    Esta função utiliza o método nativo `str.rjust()`, que é a forma
    padrão e mais eficiente de realizar a justificação à direita em Python.

    Args:
        text (str): A string a ser justificada.
        total_width (int): A largura total de caracteres da linha de saída final.
    """
    print(text.rjust(total_width))

def do_twice(func: Callable[[Any], None], arg: Any) -> None:
    """
    Executa uma determinada função duas vezes com o mesmo argumento.

    Args:
        func (Callable[[Any], None]): Um chamável (função ou método) que aceita um único argumento
                                      e não retorna nada (None).
        arg (Any): O argumento a ser passado para `func` em cada execução.
    """
    func(arg)
    func(arg)

def do_four(func: Callable[[Any], None], arg: Any) -> None:
    """
    Executa uma determinada função quatro vezes com o mesmo argumento.

    Args:
        func (Callable[[Any], None]): Um chamável (função ou método) que aceita um único argumento
                                      e não retorna nada (None).
        arg (Any): O argumento a ser passado para `func` em cada execução.
    """
    do_twice(func, arg)  
    do_twice(func, arg)  

def draw_beam_segments(grid_size: int) -> None:
    """
    Imprime os segmentos repetitivos da viga horizontal de uma grade.

    Args:
        grid_size (int): O número de células da grade, que dita quantos
                         segmentos imprimir.
    """
    print(((' '+'-') * 4 + ' '+'+') * grid_size, end='')
    
def draw_full_beam(grid_size: int) -> None:
    """
    Imprime uma viga horizontal completa para uma grade.

    Args:
        grid_size (int): O número de células que a viga deve abranger.
    """
    print('+', end='')
    draw_beam_segments(grid_size)
    print()

def draw_posts(grid_size: int) -> None:
    """
    Imprime uma única fileira de postes verticais para uma grade.

    Args:
        grid_size (int): O número de células, que dita o número de postes.
    """
    print('|', end='')
    print((' ' * 9 +'|') * grid_size)

def draw_grid(grid_size: int) -> None:
    """
    Imprime uma grade completa de um tamanho especificado (N x N).

    Args:
        grid_size (int): A dimensão da grade (ex: 2 para uma grade 2x2).
    """
    for _ in range(grid_size):
        draw_full_beam(grid_size)
        do_four(draw_posts, grid_size)

    draw_full_beam(grid_size)

def main() -> None:
    """
    Função de execução principal para demonstrar as capacidades do módulo.
    """
    print('--- Demonstração de Justificação de String ---')
    print('Versão Manual:')
    right_justify('monty', 70)
    print("Versão 'Pythonic' (com .rjust):")
    right_justify_pythonic('monty', 70)
    print('\n' + '=' * 40 + '\n')

    print('--- Demonstração de Funções de Ordem Superior ---')
    do_four(print, 'spam')
    print('\n' + '=' * 40 + '\n')

    print('--- Demonstração de Desenho de Grade Procedural ---')
    print('>>> Desenhando uma grade 2x2:')
    draw_grid(2)
    print('\n>>> Desenhando uma grade 4x4:')
    draw_grid(4)

if __name__ == '__main__':
    main()