"""
Este script didático explora a aplicação prática da recursividade para resolver
problemas clássicos da ciência da computação. Cada função implementa uma 
solução recursiva para um desafio específico, demonstrando como a decomposição
de um problema em problemas menores e semelhantes pode levar a soluções elegantes
e poderosas.

Os algoritmos abordados incluem:
-   Verificação de Palíndromos: Determinar se uma string é lida da mesma forma nos
    dois sentidos.
-   Potenciação: Verificar se um número é uma potência de outro.
-   Máximo Divisor Comum (MDC): Encontrar o maior divisor comum entre dois números 
    usando o algoritmo de Euclides.

O código segue as diretrizes da PEP 8 e utiliza Type Hints (PEP 484) para garantir
clareza, robustez e manutenibilidade.

-----------------------------------------------------------------------------------
                            UMA BREVE INTUIÇÃO MATEMÁTICA
-----------------------------------------------------------------------------------
Antes de mergulhar no código, é fundamental entender a lógica por trás de cada
algoritmo.

1.  Palíndromo:
    A ideia recursiva é simples: uma palavra só pode ser um palíndromo se suas 'pontas'
    (a primeira e última letras) forem iguais. Se forem, nós as descartamos e resolvemos
    um problema menor: a palavra do meio também é um palíndromo? Repetimos isso até que
    não sobre nada ou que sobre uma única letra, que são, por definição, palíndromos.

2.  Potência de um Número:
    A pergunta "27 é uma potência de 3?" é o mesmo que perguntar "podemos chegar a 27 
    multiplicando 3 por si mesmo um número (n) inteiro de vezes?". A abordagem recursiva
    inverte isso: podemos "desmontar" 27 dividindo-o por 3 repetidamente até chegarmos 
    em 1? Se 27 for divisível por 3, sobram 9. Se 9 for divisível por 3, sobram 3. Se 3
    for divisível por 3 chegamos a 1. Chegar em 1 significa sucesso.

3.  Máximo Divisor Comum (MDC) - O algoritmo de Euclides:
    Imagine que queremos ladrilhar uma sala de 24x18 metros com o maior ladrilho quadrado
    possível. O tamanho desse ladrilho é o MDC(24, 18).
    ✔️ Passo 1: Colocamos um ladrilho 18x18 metros. Sobra um retângulo de 6x18.
    ✔️ Passo 2: O problema agora é menor: ladrilhar a área de 18x6. A genialidade de Euclides
                 foi provar que MDC(24, 18) = MDC(18, 6).
    ✔️ Passo 3: Tentamos ladrilhar a área de 18x6 com ladrilhos de 6x6. Cabem exatamente 3, 
                 e não sobra nada (resto = 0).
    ✔️ Conclusão: O último divisor que usamos (6) é o MDC.
    A regra matemática é MDC(a, b) = MDC(b, resto de a/b). O processo para quando o resto é 0.
"""

from __future__ import annotations

__author__ = 'Enock Silos'
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

def first(word: str) -> str:
    """
    Retorna o primeiro caractere de uma string.
    """
    return word[0]
    
def last(word: str) -> str:
    """
    Retorna o último caractere de uma string.
    """
    return word[-1]

def middle(word: str) -> str:
    """
    Retorna a string sem o primeiro e sem o último caractere.
    """
    return word[1:-1]

def is_palindrome(word: str) -> bool:
    """
    Verifica recursivamente se uma palavra é um palíndromo.

    Um palíndromo é uma palavra que se lê da mesma forma nos dois sentidos.
    Esta função implementa a definição recursiva:
    1.  Casos-Base: Uma string vazia ou com uma única letra é um palíndromo.
    2.  Passo Recursivo: Uma string é um palíndromo se sua primeira e última
        letras são iguais e a sub-string do meio também é um palíndromo.

    Args:
        word (str): A palavra a ser verificada.

    Returns:
        bool: `True` se a palavra for um palíndromo, `False`, caso contrário.
    """
    if len(word) <= 1:
        return True
    
    return first(word) == last(word) and is_palindrome(middle(word))

def is_power_of(number: int, base: int) -> bool:
    """
    Verifica recursivamente se `number` é uma potência de `base`.

    A função responde à pergunta: "Existe um expoente inteiro n>= 0
    tal que base^n = number?".
    1.  Caso-Base: Se `number` for 1, ele é a potência zero da base
        (base^0 = 1), então retornamos `True`.
    2.  Passo Recursivo: Se `number` for divisível pela `base`, resolvemos
        um problema menor: `number / base` também é uma potência de `base`?
    3.  Caso de Falha: Se `number` não for divisível pela `base`, ou se a 
        base for 1 e o número não (para evitar loop infinito), não é uma
        potência.

    Args:
        number (int): O número a ser verificado.
        base (int): A base da potência.

    Returns:
        bool: `True` se `number` for uma potência de `base`, `False`, caso contrário.
    """
    if base <= 1:
        return number == 1

    if number == 1:
        return True 
    else:
        if number % base == 0:
            return is_power_of((number // base), base)
        return False 

def calculate_gcd(a: int, b: int) -> int:
    """
    Calcula o Máximo Divisor Comum (MDC) de dois inteiros usando o algoritmo recursivo
    de Euclides.

    A lógica se baseia no princípio de que o MDC de dois números não muda se o maior
    número for substituído pela sua diferença com o menor, ou, de forma mais eficiente,
    pelo resto de sua divisão.
    1.  Caso-Base: MDC(a, 0) = a. Quando o segundo número se torna 0, o primeiro é a 
        resposta.
    2.  Passo Recursivo: MDC(a, b) é o mesmo que MDC(b, a % b).

    Args:
        a (int): O primeiro número inteiro.
        b (int): O segundo número inteiro.

    Returns:
        int: O maior inteiro que divide `a` e `b` sem deixar resto.
    """
    if b == 0:
        return a 
    else:
        return calculate_gcd(b, a % b)
    
if __name__ == '__main__':

    print("--- Demonstração de Algoritmos Recursivos Práticos ---")

    print("\n1. Verificando Palíndromos:")
    print(f"   'reviver' é um palíndromo? -> {is_palindrome('reviver')}")
    print(f"   'osso' é um palíndromo? -> {is_palindrome('osso')}")
    print(f"   'python' é um palíndromo? -> {is_palindrome('python')}")

    print("\n2. Verificando se um número é potência de outro:")
    print(f"   27 é uma potência de 3? -> {is_power_of(27, 3)}")
    print(f"   16 é uma potência de 2? -> {is_power_of(16, 2)}")
    print(f"   12 é uma potência de 3? -> {is_power_of(12, 3)}")
    print(f"   1 é uma potência de 5? -> {is_power_of(1, 5)}")

    print("\n3. Calculando o Máximo Divisor Comum (MDC):")
    print(f"   MDC(24, 18) -> {calculate_gcd(24, 18)}")
    print(f"   MDC(48, 180) -> {calculate_gcd(48, 180)}")
    print(f"   MDC(101, 103) (primos entre si) -> {calculate_gcd(101, 103)}")
    


    
     





