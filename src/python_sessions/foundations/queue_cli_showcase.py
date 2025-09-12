"""
Módulo de demonstração e validação para o componente ServiceQueue.

Este script serve como um exemplo prático e um cenário de validação para a
classe ServiceQueue. Ele ilustra como a mesma classe pode exibir comportamentos
distintos (como FIFO e LIFO) através da injeção de diferentes objetos de política,
demonstrando o Padrão de Projeto Strategy em ação.
"""

from __future__ import annotations
from python_sessions.data_structures.custom_data_structures.service_queue import (
    ServiceQueue
)
from python_sessions.data_structures.custom_data_structures.policies import (
    LifoPolicy
)

__author__ = 'Enock Silos'
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

def run_fifo_demo() -> None:
    """
    Demonstra o comportamento de uma fila com a política FIFO.
    """
    print(' [FIFO] First-in, First-out: Execução Sequencial Iniciada.')
    fifo_queue = ServiceQueue[int]()
    print(' FIFO pronta. Estado: Operacional.')
    print('\n [FIFO] Operação: Enfileirando 3 itens (10, 20, 30)')
    fifo_queue.enqueue(10)
    fifo_queue.enqueue(20)
    fifo_queue.enqueue(30)
    print(f' [FIFO] Novo Estado: {fifo_queue.snapshot()}')
    print('\n [FIFO] Operação: Processando a fila...')

    while not fifo_queue.is_empty:
        removed_item = fifo_queue.dequeue()
        print(f' [FIFO] Item processado: [ {removed_item} ]')

    print(f' [FIFO] Estado Final: {fifo_queue.snapshot()}')

def run_lifo_demo() -> None:
    """
    Demonstra o comportamento de uma fila com a política LIFO.
    """
    print(' [LIFO] Last-in, First-out: Execução Sequencial Iniciada.')
    lifo_queue = ServiceQueue[int](policy=LifoPolicy())
    print(' LIFO pronta. Estado: Operacional.')
    print('\n [LIFO] Operação: Enfileirando 3 itens (10, 20, 30)')
    lifo_queue.enqueue(10)
    lifo_queue.enqueue(20)
    lifo_queue.enqueue(30)
    print(f' [LIFO] Novo Estado: {lifo_queue.snapshot()}')
    print('\n [LIFO] Operação: Processando a fila...')

    while not lifo_queue.is_empty:
        removed_item = lifo_queue.dequeue()
        print(f' [LIFO] Item processado: [ {removed_item} ]')

    print(f' [LIFO] Estado Final: {lifo_queue.snapshot()}')

def main() -> None:
    """
    Ponto de entrada que orquestra a execução das demonstrações de fila.
    """
    run_fifo_demo()
    print('\n' * 2)
    run_lifo_demo()

if __name__ == '__main__':
    main()

