
'''
Função que Atualiza um Salário Após um Aumento Percentual

Este script demonstra como usar funções e formatação profissional de números para calcular o aumento de um salário.
O foco principal é apresentar uma solução bem-estruturada, que pode ser facilmente adaptada para outros cenários de
cálculo. A lógica do programa é dividida em duas partes principais:

1 - Função `calculate_new_salary()`: Uma função dedicada a receber um salário e uma porcentagem, retornando o valor 
    atualizado. Essa prática de encapsulamento de lógica é fundamental para a criação de código reutilizável e de 
    fácil manutenção.

2 - Bloco de Execução: O bloco `if __name__ == '__main__':` define a área principal de execução do script. Nele, 
    demonstramos a chamada da função e a exibição dos resultados. A importação** da biblioteca 'locale' é utilizada
    para garantir que a saída de moeda siga o padrão brasileiro, uma prática de alta qualidade para formatação de dados.
'''
__author__ = 'Autor: Enock Silos'
__version__ = '1.0.0' 
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

import locale as loc

def calculate_new_salary(initial_salary, percentage_increase):
    '''
    Calcula o novo salário após um aumento percentual.

    Esta função recebe um salário inicial e uma porcentagem de aumento,
    calcula o novo salário e retorna o valor final.

    Args:
        initial_salary (float): O salário inicial, em formato decimal.
        percentage_increase (int): O percentual de aumento, em formato inteiro.

    Returns:
        float: O valor do novo salário após o aumento, em formato decimal.
    '''
    value_increase = initial_salary * (percentage_increase / 100)
    new_salary = initial_salary + value_increase
    return new_salary

if __name__ == '__main__':
    # Define as configurações regionais para o Brasil
    loc.setlocale(loc.LC_MONETARY, 'pt_BR.UTF-8')
    # Declaração de variáveis 
    salário_inicial = 1975.0
    aumento_percentual = 15
    # Chamada da função para obter o resultado
    salário_final = calculate_new_salary(salário_inicial, aumento_percentual)
    # Calcula o valor do aumento para o print
    valor_aumento = salário_inicial * (aumento_percentual / 100)
    # Imprime os resultados com formatação de moeda 
    print('\n--- Aumento de Salário ---\n')
    print(f'Salário inicial: {loc.currency(salário_inicial, grouping=True)}') 
    print(f'Aumento: {aumento_percentual}%') 
    print(f'Valor acrescentado: {loc.currency(valor_aumento, grouping=True)}') 
    print(f'Valor atualizado: {loc.currency(salário_final, grouping=True)}\n')

    