"""
Módulo de Ferramentas de Depuração.

Este módulo contém funções de utilidade genéricas para ajudar na depuração
e introspecção de objetos durante o desenvolvimento de software em Python.
"""
from __future__ import annotations
from typing import Any, Optional

__author__ = 'Enock Silos'
__version__ = '0.3.0'
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Production'

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

def find_defining_class(obj: object, method_name: str) -> Optional[type]:
    """
    Encontra e retorna a classe que define um método específico.

    Esta função de instrospecção percorre a Ordem de Resolução de Métodos (MRO)
    de um objeto para encontrar onde um método foi originalmente definido.

    Args:
        obj (object): Qualquer objeto Python a ser inspecionado.
        method_name (str): O nome do método a ser procurado na hierarquia.

    Returns:
        Optional[type]: A classe que define o método, ou None se não for encontrada.
    """
    for cls in type(obj).mro():
        if method_name in cls.__dict__:
            return cls 
    return None 

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

    # Demonstração de `find_defining_class` com um exemplo de tecnologia.
    class Server:
        def start(self):
            return "Server is starting..."
    
    class WebServer(Server):
        def start(self):
            return "Web server is starting..."
    
    web_server = WebServer()

    defining_class = find_defining_class(web_server, 'start')
    
    if defining_class:
        print(f"O método 'start' do objeto '{web_server.__class__.__name__}' é definido na classe: {defining_class.__name__}")
    else:
        print("Não foi possível encontrar a classe que define o método 'start'.")