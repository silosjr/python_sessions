"""
Este script é a solução para o exercício de refatoração do capítulo sobre
classes e métodos do livro "Pense em Python" de Allen B. Downey.

O objetivo é alterar a representação interna da classe `Time` para usar um
único inteiro (segundos desde a meia-noite), sem alterar a sua interface
pública ou o comportamento do código de teste.
"""

from __future__ import annotations

__author__ = 'Enock Silos'
__version__ = '0.3.0'
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Production'


class Time(object):
    """
    Representa a hora do dia.

    Esta versão da classe utiliza o encapsulamento: internamente, o tempo é
    armazenado como um único inteiro representando o total de segundos desde a
    meia-noite. No entanto, sua interface pública continua a operar em termos 
    de horas, minutos e segundos, abstraindo os detalhes da implementação
       
    Atributos internos:
         _total_seconds (int): O número de segundos desde a meia-noite.
    """
    def __init__(self, hour=0, minute=0, second=0):
        """
        Inicializa um objeto `Time` convertendo `h`, `m` e `s` para segundos totais.

        Args:
            hour (int, optional): A componente da hora. Padrão é 0.
            minute (int, optional): A componente do minuto. Padrão é 0.
            second (int, optional): A componente do segundo. Padrão é 0.
        """
        self._total_seconds = (hour * 60 + minute) * 60 + second 
        
    def __str__(self) -> str:
        """
        Retorna a representação em string do objeto no formato hh:mm:ss.
        """
        minutes, second = divmod(self._total_seconds, 60)
        hour, minute = divmod(minutes, 60)
        return '%.2d:%.2d:%.2d' % (hour, minute, second)

    def print_time(self) -> None:
        """
        Imprime a representação em string do tempo no console.
        """
        print (self)

    def time_to_int(self) -> int:
        """
        Retorna o número de segundos desde a meia-noite.
        """
        return self._total_seconds

    def is_after(self, other: 'Time') -> bool:
        """
        Retorna `True` se este objeto for depois do outro; `False`, caso contrário.
        """
        return self._total_seconds > other._total_seconds

    def __add__(self, other: 'Time' | int) -> 'Time':
        """
        Soma um objeto `Time` com outro `Time` ou com um número (segundos).

        Args:
            other (Time | int): Outro objeto `Time` ou um valor inteiro (segundos).
        
        Returns:
            Time: Um objeto `Time` com o valor incrementado.
        """
        if isinstance(other, Time):
            total_seconds = self._total_seconds + other._total_seconds
        else:
            total_seconds = self._total_seconds + other
            
        return int_to_time(total_seconds)

    def __radd__(self, other: int) -> 'Time':
        """
        Permite a soma com o objeto `Time` no lado direito (ex: 10 + `Time`).

        Args:
            other (int): o valor inteiro do lado esquerdo a ser somado.

        Returns:
            Time: Um objeto `Time` com seu valor incrementado.
        """
        return self.__add__(other)

    def add_time(self, other: 'Time') -> 'Time':
        """
        Soma dois objetos `Time`, retornando um novo objeto `Time`.

        Args:
            other (Time): O segundo objeto `Time` a ser somado.

        Returns:
            Time: Um novo objeto `Time` resultado da soma de dois destes.
        """
        assert self.is_valid() and other.is_valid()
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds: int) -> 'Time':
        """
        Retorna um novo `Time` que é a soma deste tempo e de segundos.

        Args:
            seconds (int): Os segundos que serão acresecentados ao `Time`.

        Returns:
            Time: Um novo `Time` acrescido dos segundos.
        """
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_valid(self) -> bool:
        """
        Verifica se um objeto `Time` satisfaz as invariantes.
        """
        minutes, second = divmod(self._total_seconds, 60)
        hour, minute = divmod(minutes, 60)
        if hour < 0 or minute < 0 or second < 0:
            return False
        if minute >= 60 or second >= 60:
            return False
        return True


def int_to_time(seconds) -> 'Time':
    """
    Cria um novo objeto `Time` a partir de segundos desde a meia-noite.
    """
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    return Time(hour, minute, second)

def main():
    """
    Código de teste para a classe `Time` (não deve ser modificado).
    """
    start = Time(9, 45, 00)
    start.print_time()

    end = start.increment(1337)
    end.print_time()

    print('Is end after start?', end=' ')
    print(end.is_after(start))

    print('Using __str__')
    print(start, end)

    start = Time(9, 45)
    duration = Time(1, 35)
    print(start + duration)
    print(start + 1337)
    print(1337 + start)

    print('Example of polymorphism')
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print(total)


if __name__ == '__main__':
    main()