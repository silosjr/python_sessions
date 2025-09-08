"""
Módulo de Demonstração do Algoritmo de Busca Binária

Este módulo fornece uma implementação didática e interativa do algoritmo de
busca binária. O sistema, atuando como um agente de busca, tenta determinar
um valor numérico secreto dentro de um intervalo pré-definido. A convergência
para o valor correto é guiada por um oráculo externo (o operador humano), que
fornece feedback a cada iteração.

Metodologia:
O algoritmo opera sob o princípio de divisão e conquista. A cada passo, o
espaço de busca, definido por um limite inferior (low) e superior (high), é
dividido ao meio. O valor central é proposto como um palpite. Com base no
feedback do oráculo ('maior', 'menor' ou 'correto'), metade do espaço de busca
é descartada, reduzindo exponencialmente o número de candidatos.

Complexidade e Pior Cenário:
A complexidade de tempo do algoritmo é logarítmica, O(log N), onde N é o
número de elementos no intervalo. Para um intervalo de N=128 elementos,
o número máximo de iterações (palpites) requerido por esta implementação é
dado pela fórmula floor(log2(N)) + 1, resultando em 8 iterações no pior caso
(e.g., quando o valor secreto é o último elemento do intervalo).

Uso:
Para executar a demonstração, o script pode ser invocado diretamente através
de um interpretador Python.
"""

from __future__ import annotations
import time 

__author__ = 'Enock Silos'
__version__ = '0.3.0'
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

def binary_search() -> None:
    """
    Executa uma sessão interativa para demonstrar a busca binária.

    Esta função encapsula a lógica completa do algoritmo. Ela inicializa o
    estado da busca (limites, contador de tentativas) e entra em um laço
    iterativo. Em cada iteração, calcula-se um novo palpite, que é apresentado
    ao operador. A resposta do operador é então utilizada para ajustar os
    limites do próximo espaço de busca.

    O processo termina quando o valor é encontrado ou quando o espaço de
    busca se esgota (indicando `feedback` inconsistente do operador).

    Side Effects:
        - Imprime informações de estado e prompts no console (`stdout`).
        - Lê dados da entrada padrão do usuário (`stdin`).
    """
    MINIMUM = 1
    MAXIMUM = 128 

    print('\n\t      --- BENVINDO(A)! ---\n')
    time.sleep(1.5)
    print(' Hoje você irá entender como funciona o algoritmo da Busca Binária.\n')
    time.sleep(1.5)
    print(f'\tPense em um número entre {MINIMUM} e {MAXIMUM}. Memorize-o.\n')
    time.sleep(2.0)

    low = MINIMUM
    high = MAXIMUM
    tries = 0
    got_it = False

    while low <= high:
        tries += 1
        guess = (low + high) // 2

        print(f'\tMeu {tries}º palpite é {guess}')
        time.sleep(1.5)

        answer = input('''
                    Acertei o número que você pensou? (S)
                    É maior? (+)
                    É menor? (-)\n
                    ou `Q` para SAIR:
                    ''')
        
        if answer.lower() == 'q':
            return
        elif answer.lower() == 's':
            print(f'''\tÓtimo! O computador acertou o número em {tries} tentativa(s).
                    \tO número era {guess}''')
            got_it = True
            break 
        elif answer == '+':
            low = guess + 1
        elif answer == '-':
            high = guess - 1
        else:
            print('Por favor, digite APENAS `S` `+` ou `-`\n')
            tries -= 1

    if not got_it:
        print('''
            ATENÇÃO: Suas dicas foram inconsistentes. O número não pôde ser encontrado\n
            \tO programa será encerrado.\n''')
        
if __name__ == '__main__':
    binary_search()
    
    

