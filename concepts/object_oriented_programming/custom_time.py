"""
Este script define a classe `Time` e suas funcionalidades para manipulação
e formatação de horários, demonstrando conceitos avançados de POO em Python,
como sobrecarga de operadores e despacho por tipo..
"""

from __future__ import annotations

__author__ = 'Enock Silos'
__version__ = '3.2.0' 
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

class Time:
    """
    Representa a hora do dia de forma autosuficiente.

    Esta classe encapsula os dados (hora, minuto, segundo) e os comportamentos
    (conversão, soma, incremento, comparação) relacionados a um ponto no tempo.

    Atributos:
        - hour (int): A hora (0-23).
        - minute (int): O minuto (0-59).
        - second (int): O segundo (0-59).
    """
    hour: int = 0
    minute: int = 0 
    second: int = 0

    def __init__(self, hour: int = 0, minute: int = 0, second: int = 0) -> None:
        """Inicializa uma nova instância da classe `Time`.

        Este método construtor atribui os valores iniciais de hora, minuto
        e segundo ao objeto no momento de sua criação.

        Args:
            hour (int, optional): O valor inicial para a hora. Padrão é 0.
            minute (int, optional): O valor inicial para o minuto. Padrão é 0.
            second (int, optional): O valor inicial para o segundo. Padrão é 0.
        """
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self) -> str:
        """
        Retorna a representação em string do objeto (`hh:mm:ss`).

        Returns:
            str: A hora no formato hh:mm:ss
        """
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def to_seconds(self) -> int:
        """
        Converte o tempo deste objeto para o número total de segundos.

        Este método calcula o valor total em segundos com base nos atributos
        `hour`, `minute` e `second` da própria instância.

        Returns:
            int: O número total de segundos equivalentes ao tempo do objeto.
        """
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds
    
    def __lt__(self, other: Time) -> bool:
        """
        Compara este tempo (self) com outro (other).

        Este método especial sobrecarrega o operador `<`, permitindo identificar
        se este objeto `Time` é menor que `other`.

        Args:
            other (Time): O outro objeto `Time`a ser comparado com este.

        Returns:
            bool: True se `self` for menor que `other`, False, caso contrário.
        """
        return self.to_seconds() < other.to_seconds()
    
    @classmethod
    def from_seconds(cls, total_seconds: int) -> 'Time':
        """
        Cria uma instância de `Time` a partir de um número total de segundos.

        Este método de classe atua como uma "fábrica" alternativa, reconstruindo
        um objeto `Time` a partir de um único inteiro.

        Args:
            total_seconds (int): O número total de segundos a ser convertido.

        Returns:
            Time: Um novo objeto `Time`. Note que o atributo da hora pode ser
                  maior que 23 se os segundos representarem mais de um dia.
        """
        new_time = cls()
        minutes, new_time.second = divmod(total_seconds, 60)
        new_time.hour, new_time.minute = divmod(minutes, 60)
        return new_time 
    
      
    def __add__(self, other: 'Time' | int) -> 'Time':
        """
        Soma este objeto `self` com outro objeto `Time` usando o operador `+`
        ou com um inteiro (segundos).

        Este método utiliza despacho por tipo para se comportar de forma diferente
        dependendo do tipo do operando `other`.

        Args:
            other (Time | int): O outro objeto `Time` ou o número de segundos a somar.

        Returns: 
            Time: Um novo objeto `Time` com o resultado da soma.

        Raises:
            TypeError: Se `other` não for do tipo `Time` ou `int`.
        """
        if isinstance(other, Time):
            seconds = self.to_seconds() + other.to_seconds()
            return Time.from_seconds(seconds)
        elif isinstance(other, int):
            total_new_seconds = self.to_seconds() + other
            return Time.from_seconds(total_new_seconds)
        else:
            raise TypeError(f"Operação '+' não suportada entre 'Time' e '{type(other).__name__}'.")
        
    def __radd__(self, other: int) -> 'Time':
        """
        Permite a soma com o objeto `Time` no lado direito (ex: 10 + `Time`).

        Este método é chamado como um "fallback" pelo Python quando uma operação
        como `int` e `Time` é tentada. Ele garante que a soma seja comutativa.

        Args:
            other (int): O inteiro (segundos) no lado esquerdo do operador `+`.

        Returns:
            Time: O resultado da soma, delegando para o método __add__.
        """
        return self.__add__(other)
        
    def increment(self, seconds: int) -> None:
        """
        Incrementa o tempo do objeto por uma dada quantidade de segundos.

        Este método é "impuro" pois modifica diretamente (muta) os atributos
        da própria instância do objeto. Ele utiliza a lógica de conversão
        para segundos para garantir um cálculo robusto.

        Args:
            seconds (int): O número de segundos a serem adicionados.
        """
        total_seconds = self.to_seconds() + seconds
        new_time = Time.from_seconds(total_seconds) 
        self.hour = new_time.hour
        self.minute = new_time.minute 
        self.second = new_time.second

    def add_seconds(self, seconds: int) -> Time:
        """
        Cria e retorna um novo objeto `Time` incrementado por segundos.

        Este método "puro" não modifica a instância original (`self`).

        Args:
            seconds (int): O número de segundos a serem adicionados ao objeto.

        Returns: 
            Time: Um novo objeto `Time` com o tempo incrementado.
        """
        total_new_seconds = self.to_seconds() + seconds
        return Time.from_seconds(total_new_seconds)
        
    def is_after(self, other: Time) -> bool:
        """
        Verifica se um horário é cronologicamente depois de outro (`other`).

        Este método resolve o problema sem usar a instrução `if`.

        Args:
            other (Time): O segundo objeto a ser comparado.

        Returns:
            bool: True se o primeiro objeto é cronologicamente depois do outro
                  (`other`), caso contrário, False.
        """
        return self.to_seconds() > other.to_seconds()

if __name__ == '__main__':
    # Criando instâncias da classe Time com o novo construtor __init__
    start_time = Time(9, 45)
    duration = Time(1, 35)

    print("--- Demonstração da Classe Time Refatorada ---")
    
    # Testando o método __str__
    print(f"Hora de início: {start_time}")
    print(f"Duração: {duration}")

    # Testando o método "puro" __add__()
    end_time = start_time + duration
    print(f"Hora de término (usando +): {end_time}\n")

    t1 = Time(9, 45)
    t2 = Time(1, 35)
    print('--- Demonstração do Despacho por Tipo em __add__ e __radd__ ---')
    # Teste 1: Time + Time
    sum_time = t1 + t2 
    print(f'{t1} + {t2} = {sum_time}')
    # Teste 2: Time + int (chama __add__)
    sum_seconds_left = t1 + 3600
    print(f'{t1} + 3600 segundos = {sum_seconds_left}')
    # Teste 3: int + Time (chama __radd__)
    sum_seconds_right = 3600 + t1 
    print(f'3600 segundos + {t1} = {sum_seconds_right}')
    # Teste 4: Tentativa de erro
    try:
        resultado_erro = t1 + 'texto'
    except TypeError as e:
        print(f'\nTentativa de somar com um tipo inválido gerou o erro esperado:')
        print(e,'\n')
    
    # Testando o método "puro" add_seconds()
    end_time_plus_30s = end_time.add_seconds(30)
    print(f"Término + 30 segundos (puro): {end_time_plus_30s}")
    print(f"Objeto original não foi modificado: {end_time}")

    # Testando o método "impuro" increment()
    print("\n--- Testando o método de mutação 'increment' ---")
    print(f"Hora de início (antes): {start_time}")
    start_time.increment(500) # Modifica o objeto start_time
    print(f"Hora de início (depois de incrementar 500s): {start_time}")
    
    # Testando o método is_after()
    print(f"\nA nova hora de início é depois da duração? {start_time.is_after(duration)}\n")





