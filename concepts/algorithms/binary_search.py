"""
Módulo didático que implementa o algoritmo de busca binária com tipagem genérica,
garantindo segurança em tempo de verificação por meio da linguagem de tipos do Python.

Este script tem como principal objetivo demonstrar, de forma segura e moderna,
como aplicar a busca binária sobre sequências ordenadas de qualquer tipo de dado
que suporte comparação relacional (isto é, que possa ser comparado com os operadores
<, > e ==).

-------------------------------------------------------------------------------
 Sobre a busca binária:

A busca binária é um algoritmo eficiente para localizar elementos em listas ordenadas.
Seu funcionamento baseia-se na divisão sucessiva do intervalo de busca pela metade,
comparando o elemento central com o alvo desejado. Caso o elemento central seja igual
ao alvo, a busca é encerrada com sucesso. Caso contrário, descarta-se metade da sequência
e repete-se o processo. Sua complexidade é O(log n), sendo amplamente utilizada em
estruturas de dados e algoritmos clássicos.

-------------------------------------------------------------------------------
 Tipagem genérica com segurança: TypeVar + Protocol

Para garantir que os elementos da lista possam ser corretamente comparados ao item buscado,
sem depender de verificações em tempo de execução, o script faz uso de dois recursos poderosos
da biblioteca de tipagem do Python:

1. `Protocol` (do módulo `typing`): 
   Utilizado aqui para definir uma interface estrutural chamada `Comparable`, a qual descreve 
   o comportamento esperado de um tipo "comparável". A classe `Comparable` define três métodos:
   
   - `__lt__(self, other)`: operador de menor (<)
   - `__gt__(self, other)`: operador de maior (>)
   - `__eq__(self, other)`: operador de igualdade (==)

   Ao utilizar esse protocolo, estamos dizendo que qualquer tipo que implemente esses três métodos
   é considerado "comparável" — mesmo que ele não herde explicitamente de `Comparable`. Isso é 
   conhecido como tipagem estrutural ou duck typing estático.

2. `TypeVar` com `bound=Comparable`:
   O uso de `T = TypeVar('T', bound=Comparable)` define um tipo genérico `T`, que pode representar
   qualquer tipo, desde que obedeça à estrutura definida em `Comparable`. Essa ligação entre
   o tipo genérico e o protocolo garante que o algoritmo funcione corretamente com inteiros,
   strings, floats, ou quaisquer outros objetos que possam ser comparados por `<`, `>`, `==`.

3. `@runtime_checkable`:
   Decorador aplicado à classe `Comparable` que permite, opcionalmente, realizar verificações
   de conformidade com o protocolo em tempo de execução usando `isinstance()` ou `issubclass()`.
   Embora essa verificação não seja obrigatória neste script, ela torna o protocolo mais flexível
   e auditável, especialmente em testes ou frameworks.

-------------------------------------------------------------------------------
 Conclusão:

Este módulo é apropriado para fins educacionais e práticos, destacando a importância de:
- Algoritmos eficientes como a busca binária
- Tipagem segura em linguagens dinâmicas
- Princípios modernos de design com Python 3.10+
"""

from __future__ import annotations
from typing import TypeVar, Protocol, List, Any, runtime_checkable 

__author__ = 'Enock Silos'
__version__ = '1.1.0' 
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

@runtime_checkable
class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...

T = TypeVar('T', bound=Comparable)

def binary_search(sequence: List[T], item: T) -> int | None:
    """
    Executa o algoritmo de busca binária sobre uma sequência ordenada, a fim de localizar a posição
    (índice) de um determinado elemento alvo.

    A busca binária pressupõe que a sequência esteja ordenada em ordem crescente, e que os elementos 
    sejam comparáveis entre si por operadores relacionais.

    Args:
        sequence (List[T]): Lista ordenada de elementos comparáveis.
        item (T): Elemento a ser localizado na sequência.

    Returns:
        int | None: Índice do elemento se encontrado; caso contrário, None.
    """
    low = 0
    high = len(sequence) - 1

    while low <= high:
        middle = (low + high) // 2
        guess = sequence[middle]
        
        if guess == item:
            return middle
        if guess > item:
            high = middle - 1
        else:
            low = middle + 1

    return None

if __name__ == '__main__':

    my_array = [1, 3, 5, 7, 8, 9, 23, 67, 788]

    for value in [40, 8]:
        result = binary_search(my_array, value)
        if result is not None:
            print(f"Elemento {value} encontrado no índice {result}.")
        else:
            print(f"Elemento {value} não encontrado.")