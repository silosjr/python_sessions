"""
Módulo para a implementação de uma Fila de Serviço genérica e thread-safe.

Este módulo provê a classe `ServiceQueue`, uma estrutura de dados projetada
para operações em ambientes de missão crítica. Garante não apenas determinismo
e extensibilidade, mas também segurança em ambientes concorrentes (thread-safety)
através de um mecanismo de bloqueio reentrante (RLock).
"""

from __future__ import annotations
import hashlib
from threading import RLock
from typing import (
    TypeVar
)
from .policies import ( 
    FifoPolicy,
    QueuePolicy
)

__author__ = 'Enock Silos'
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

T = TypeVar('T')

class ServiceQueue[T]:
    """
    Representa uma fila de serviços FIFO (First-in, First-out) thread-safe.

    Esta estrutura de dados encapsula a lógica para enfileirar, desenfileirar e
    observar itens, garantindo a ordem de chegada e provendo mecanismos para
    auditoria e extensibilidade.

    A classe é projetada para ser `thread-safe`, utilizando um mecanismo de
    bloqueio reentrante (RLock) para garantir que todas as operações que acessam o
    estado interno sejam atômicas. Isso a torna segura para uso em ambientes
    de alta concorrência, onde múltiplas threads podem tentar acessar a mesma
    instância de fila simultaneamente.

    Attributes:
        _items (list[T]): Estrutura de dados interna para armazenar os elementos
                          da fila. O uso do underscore indica que é um atributo
                          privado para a lógica interna da classe.
        _policy (QueuePolicy[T]): O objeto de política que dita a lógica.
        _lock (threading.RLock): O objeto de bloqueio reentrante para sincronização.
    """

    def __init__(self, policy: QueuePolicy[T] | None = None) -> None:
        """
        Inicializa uma nova instância de ServiceQueue.

        Além da lista de itens e da política, este construtor inicializa um
        Lock Reentrante (`threading.RLock`). A escolha por um RLock em vez de
        um Lock padrão é deliberada para prevenir deadlocks em cenários onde
        métodos sincronizados da classe (como `dequeue`) precisam chamar
        outros métodos sincronizados (como `is_empty` ou `size`) na mesma
        thread. O RLock permite que a mesma thread adquira o bloqueio
        múltiplas vezes sem causar um impasse.

        Args:
            policy (QueuePolicy[T] | None, optional): A política de enfileiramento a 
                                                      ser usada. Se None, a política 
                                                      FifoPolicy será usada como padrão.
                                                      Defaults to None.

        """
        self._items: list[T] = []
        if policy is None:
            self._policy: QueuePolicy[T] = FifoPolicy()
        else:
            self._policy: QueuePolicy[T] = policy
        self._lock = RLock()

    def enqueue(self, item: T) -> None:
        """
        Adiciona um item ao final da fila após validação pela política.

        Esta operação adquire o bloqueio interno da fila antes de realizar a
        validação e a inserção do item, e o libera imediatamente após. Isso
        garante que a operação de enfileiramento seja atômica e não possa ser
        interrompida ou corrompida por outra thread.

        Args:
            item (T): O elemento a ser adicionado à fila.

        Raises:
            ValueError: Se o item for considerado inválido pela política.
        """
        with self._lock:
            self._policy.validate_item(item)
            self._items.append(item)

    @property
    def size(self) -> int:
        """
        Retorna o número atual de itens na fila. de forma thread-safe.

        A contagem de itens é uma operação atômica. O bloqueio é adquirido
        para garantir que o tamanho retornado corresponda a um estado
        consistente da fila, não sendo afetado por modificações concorrentes.

        Returns:
            int: A quantidade de itens na fila.
        """
        with self._lock:
            return len(self._items)

    @property
    def is_empty(self) -> bool:
        """
        Verifica se a fila está vazia de forma thead-safe.

        Esta propriedade é inerentemente thread-safe, pois delega sua lógica
        para a propriedade `.size`, que já implementa o bloquei de
        sincronização para garantir uma leitura consistente.

        Returns:
            bool: True se a fila estiver vazia, False, caso contrário.
        """
        return self.size == 0

    def dequeue(self) -> T:
        """
        Remove e retorna o próximo item da fila de forma atômica e thread-safe.

        Esta operação é atômica. O bloqueio da fila é mantido durante a
        verificação de vacuidade, a seleção do índice pela política e a
        remoção do item. Isso previne condições de corrida onde múltiplas
        threads poderiam tentar remover itens de uma fila quase vazia.

        Raises:
            IndexError: Se a fila estiver vazia no momento da chamada.

        Returns:
            T: O primeiro item da fila, determinado pela política.
        """
        with self._lock:
            if self.is_empty:
                raise IndexError(' Falha ao remover: a fila está vazia.')

            index_to_remove = self._policy.get_next_index(self._items)
            return self._items.pop(index_to_remove)

    def peek(self) -> T:
        """
        Retorna o próximo item da fila (sem removê-lo) de forma thead-safe.

        A observação do próximo item é atômica. O bloqueio garante que o item
        retornado seja consistente e não seja removido por outra thread durante
        a operação de leitura.

        Raises:
            IndexError: Se a fila estiver vazia no momento da chamada.

        Returns:
            T: O primeiro item da fila, determinado pela política.
        """
        with self._lock:
            if self.is_empty:
                raise IndexError(' Não é possível observar uma fila vazia.')
            
            index_to_peek = self._policy.get_next_index(self._items)
            return self._items[index_to_peek]

    def snapshot(self) -> list[T]:
        """
        Retorna uma cópia imutável do estado atual da fila de forma atômica e thread-safe.

        A criação do snapshot é uma operação atômica. O estado da fila é
        bloqueado para garantir que a cópia retornada seja uma representação
        fiel e consistente de um ponto específico no tempo, livre de
        'leituras sujas' (dirty reads) de threads concorrentes..

        Returns:
            list[T]: Uma cópia da lista de itens na fila.
        """
        with self._lock:
            return self._items.copy()

    @property
    def integrity_hash(self) -> str:
        """
        Calcula um hash SHA-256 do estado atual da fila de forma thread-safe.

        O hash serve como uma "impressão digital" única do estado da fila,
        permitindo a verificação de integridade em logs e snapshots. O
        cálculo do hash é atômico. O bloquei é adquirido antes da leitura
        do estado, garantindo que o hash corresponda a um estado consistente
        e não a um estado intermediário durante uma modificação concorrente.

        Returns:
            str: A representação hexadecimal do hash SHA-256 do estado.
        """
        with self._lock:
            state_string = ''.join(map(repr, self._items))

            state_bytes = state_string.encode('utf-8')

            return hashlib.sha256(state_bytes).hexdigest()

