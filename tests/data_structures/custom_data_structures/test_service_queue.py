"""
Módulo de verificação formal para o componente ServiceQueue.

Esta suíte de testes, utilizando o framework `unittest`, tem como objetivo
provar o comportamento e as garantias do componente ServiceQueue em
diversos cenários críticos. A cobertura de testes abrange:

1.  **Contrato Funcional Básico:** Validação das operações primárias como
    inicialização, `enqueue`, `dequeue` e `peek`.
2.  **Condições de Borda:** Verificação do comportamento seguro e previsível
    em cenários-limite, como operações em uma fila vazia (`IndexError`).
3.  **Extensibilidade de Políticas:** Prova de que o Padrão Strategy foi
    implementado corretamente, testando o comportamento polimórfico com
    as políticas FIFO e LIFO.
4.  **Segurança de Concorrência:** Validação da `thread-safety` do
    componente através de um teste de estresse que simula acesso concorrente
    por múltiplas threads, prevenindo condições de corrida.
"""

from __future__ import annotations
import unittest
import threading
from python_sessions.data_structures.custom_data_structures.service_queue import (
    ServiceQueue
)
from python_sessions.data_structures.custom_data_structures.policies import (
    FifoPolicy,
    LifoPolicy
)
__author__ = 'Enock Silos'
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Verification'

class TestServiceQueue(unittest.TestCase):
    """
    Suíte de testes formais para o componente ServiceQueue.

    Verifica o contrato funcional, condições de borda, extensibilidade de
    políticas e segurança em ambientes concorrentes (thread-safety).
    """

    def test_initialization_creates_empty_queue(self):
        """
        Verifica se a fila é inicializada vazia e com a política correta.
        """
        sut = ServiceQueue[int]()

        self.assertEqual(sut.size, 0)
        self.assertTrue(sut.is_empty)
        self.assertIsInstance(sut._policy, FifoPolicy)

    def test_enqueue_adds_item_to_queue(self):
        """
        Verifica se enqueue adiciona um item, alterando o tamanho da fila.
        """
        sut = ServiceQueue[int]()
        item_to_add = 42

        sut.enqueue(item_to_add)

        self.assertEqual(sut.size, 1)
        self.assertFalse(sut.is_empty)

    def test_dequeue_returns_and_removes_correct_item_on_fifo(self):
        """
        Verifica se dequeue em uma fila FIFO retorna o item mais antigo e o
        remove da fila.
        """
        sut = ServiceQueue[str]()
        sut.enqueue('primeiro')
        sut.enqueue('segundo')

        removed_item = sut.dequeue()

        self.assertEqual(removed_item, 'primeiro')
        self.assertEqual(sut.size, 1)
        self.assertEqual(sut.peek(), 'segundo')

    def test_dequeue_on_empty_queue_raises_index_error(self):
        """
        Verifica se dequeue em uma fila vazia levanta um IndexError.
        """
        sut = ServiceQueue[int]()

        with self.assertRaises(IndexError):
            sut.dequeue()

    def test_peek_on_empty_queue_raises_index_error(self):
        """
        Verifica se peek em uma fila vazia levanta um IndexError.
        """
        sut = ServiceQueue[int]()

        with self.assertRaises(IndexError):
            sut.peek()

    def test_dequeue_with_lifo_policy_returns_newest_item(self):
        """
        Verifica se, com uma LifoPolicy, dequeue retorna o item mais recente.
        """
        sut = ServiceQueue[str](policy=LifoPolicy())
        sut.enqueue('primeiro')
        sut.enqueue('segundo')
        sut.enqueue('terceiro')

        removed_item = sut.dequeue()

        self.assertEqual(removed_item, 'terceiro')
        self.assertEqual(sut.size, 2)
        self.assertEqual(sut.peek(), 'segundo')

    def test_queue_is_thread_safe_under_concurrent_enqueues(self):
        """
        Verifica se a fila mantém a integridade sob acesso concorrente.

        Cria múltiplas threads, cada uma enfileirando um número de itens
        simultaneamente na mesma fila. O teste passa se o tamanho final da
        fila for a soma de todos os itens enfileirados.
        """
        sut = ServiceQueue[int]()
        num_threads = 10
        items_per_thread = 100
        expected_size = num_threads * items_per_thread

        def worker():
            for i in range(items_per_thread):
                sut.enqueue(i)

        threads = [threading.Thread(target=worker) for _ in range(num_threads)]
        
        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        self.assertEqual(sut.size, expected_size)