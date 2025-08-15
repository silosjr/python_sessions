"""
Módulo de Ferramentas de Depuração.

Este módulo contém funções de utilidade genéricas para ajudar na depuração
e introspecção de objetos durante o desenvolvimento de software em Python.
"""

__author__ = 'Enock Silos'
__version__ = '1.0.0' 
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Production'

from typing import Any

def print_attributes(obj: Any) -> None:
    """
    Imprime os atributos e valores de um objeto para fins de depuração.

    Esta função de utilidade inspeciona qualquer objeto Python, iterando
    sobre seus atributos e imprimindo cada nome de atributo seguido de seu valor
    correspondente na tela. É uma ferramenta útil para entender o estado interno
    de um objeto durante o desenvolvimento.

    Args:
        obj (Any): O objeto a ser inspecionado.

    Side Effects:
        Imprime os pares atributo-valor do objeto no console.
    """
    for attr_name in vars(obj):
        attr_value = getattr(obj, attr_name)
        print(f'    - {attr_name}: {attr_value}')
    print('-' * 20)

if __name__ == '__main__':
    # Para demonstrar, precisamos de uma classe de exemplo.
    # Em um projeto real, importaríamos uma classe como a `Point`
    class DemoPoint:
        def __init__(self, x: float, y: float) -> None:
            self.x = x
            self.y = y

    ponto_exemplo = DemoPoint(10, 20)

    print('Demonstrando o uso de `print_attributes` com um objeto DemoPoint:')
    print_attributes(ponto_exemplo)

    lista_exemplo = [1, 2, 3]
    # A função não funciona bem com tipos nativos como listas que não têm
    # um `__dict__` (onde `vars()` procura), o que é uma limitação a ser 
    # notada.
    print('\nTentando inspecionar uma lista (pode não produzir saída):')
    try:
        print_attributes(lista_exemplo)
    except TypeError as e:
        print(f'Não foi possível inspecionar a lista: {e}\n')  