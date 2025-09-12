"""
Módulo que define as políticas (estratégias) de enfileiramento.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

__author__ = 'Enock Silos'
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

T = TypeVar('T')

class QueuePolicy(ABC, Generic[T]):
    """
    Define o contrato para todoas as políticas da fila (estratégias).

    Uma classe base abstrata que garante que qualquer política de fila implemente
    os métodos necessários para ser usado pela ServiceQueue.
    """

    @abstractmethod
    def get_next_index(self, items:list[T]) -> int:
        """
        Determina o índice do próximo item a ser removido da fila.

        Args:
            items (list[T]): A lista atual de itens na fila.

        Returns:
            int: O índice do item a ser removido.
        """
        pass

    @abstractmethod
    def validate_item(self, item: T) -> None:
        """
        Valida se um item é adequado para esta política.

        Pode levantar uma exceção (ex: ValueError) se o item for inválido.

        Args:
            item (T): O item a ser validado antes de ser adicionado.
        """
        pass

class FifoPolicy(QueuePolicy[T]):
    """
    Implementa a política FIFO (First-in, First-out). 
    """

    def get_next_index(self, item: list[T]) -> int:
        """
        Para FIFO, o próximo item é sempre o do índice 0.
        """
        return 0

    def validate_item(self, item: T) -> None:
        """
        Em uma lista FIFO simples, todos os itens são aceitos.
        """
        pass

class LifoPolicy(QueuePolicy[T]):
    """
    Implementa a política LIFO (Last-in, First-out).
    """

    def get_next_index(self, items: list[T]) -> int:
        """
        Para LIFO, o próximo item é sempre o último da lista.
        """
        return -1

    def validate_item(self, item: T) -> None:
        """
        Em uma fila LIFO simples, todos os itens são aceitos.
        """
        pass

