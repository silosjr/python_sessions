"""
Um módulo que forncece uma coleção de calculadoras utilitárias interativas.

Este script serve como um exemplo prático de como os conceitos fundamentais
de programação (variáveis, entrada/saída, tratamento de exceções) são aplicados
para construir ferramentas que resolvem problemas específicos do mundo real.

Cada função encapsula a lógica para uma única tarefa, interagindo com o usuário
através da interface de linha de comando (CLI) para obter dados e apresentar
resultados de forma robusta e clara. O uso de constantes para valores que 
representam regras de negócio fixas, como taxas ou fatores de conversão, torna
o código mais legível e fácil de manter.
"""
from __future__ import annotations
import locale 

__author__ = 'Enock Silos'
__version__ = '1.3.0' 
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

PERCENTAGE_INCREASE: float = 15
CAR_RENTAL_PER_KM: float = 0.15
CAR_RENTAL_PER_DAY: float = 60.0
MINUTES_LOST_PER_CIGARRETE: int = 10

def calculate_sum_from_user_input() -> None:
    """
    Solicita dois números inteiros ao usuário e exibe a soma.

    Esta função demonstra o processo de I/0 (Entrada/Saída) e o tratamento
    de exceções para garantir que a entrada do usuário seja válida antes 
    do processamento.

    Side Effects:
        - Lê dados da entrada padrão (`input`).
        - Imprime dados na saída padrão (`print`).
    """
    print('--- 1.   Calculadora de Soma ---')
    while True:
        try:
            num1 = int(input('Digite o primeiro número a ser somado: '))
            num2 = int(input('Digite o segundo número a ser somado: '))
            print(f'A soma entre {num1} e {num2} é igual a {num1 + num2}')
            break
        except ValueError:
            print('Digite apenas números inteiros. Exemplo: 75\n') 
        except KeyboardInterrupt:
            print('\nOperação cancelada pelo usuário.\n')
            break 
        except Exception as e:
            print(f'Ocorreu um erro inesperado. O programa será encerrado {e}')
        
def convert_meters_to_millimeters() -> None:
    """
    Converte um valor de metros para milímetros forncido pelo usuário.

    Side Effects:
        - Lê dados de entrada padrão (`input`).
        - Imprime dados na saída padrão (`print`).
    """
    print('---- 2.  Conversor: Metros para Milímetros ---')
    MILLIMETERS_PER_METER = 1000
    while True:
        try:
            meters = float(input('Digite a medida em metros:'))
            millimeters = meters * MILLIMETERS_PER_METER
            print(f'    Resultado: {meters} metro(s) corresponde(m) a {meters * MILLIMETERS_PER_METER:.0f} milímetro(s).\n')
            break
        except ValueError:
            print('     Digite um valor numérico válido. Ex: 172\n')
        except KeyboardInterrupt:
            print('\nOperação cancelada pelo usuário.\n')
            break 
        except Exception as e:
            print(f'Não foi possível concluir a operação. O programa será encerrado {e}')

def calculate_salary_increase(salary: float) -> float :
    '''
    Calcula o novo salário aplicando a taxa de aumento definida no módulo.

    Esta função encapsula a regra de negócio de reajuste salarial, utilizando
    a constante `PERCENTAGE_INCREASE` para garantir consistência.

    Args:
        salary (float): O salário inicial, em formato decimal.

    Returns:
        float: O valor do novo salário após o aumento, em formato decimal.
    '''
    return salary * (1 + PERCENTAGE_INCREASE / 100)

def prompt_salary_increase() -> None:
    """
    Orquestra a interação com o usuário para o cálculo de reajuste salarial
    com base em uma taxa pré-definida e exibe os resultados em uma tabela.

    Side Effects:
        - Lê dados de entrada padrão (`input`).
        - Imprime dados na saída padrão (`print`).
    """
    try:
        locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
    except locale.Error:
        print("Aviso: Locale 'pt_BR.UTF-8' não foi encontrado. Usando formatação padrão.")

    print('\n--- 3.  Calculadora de Reajuste Salarial ---')
    while True:
        try:
            initial_salary = float(input('Informe seu salário atual: R$ '))

            increase_value = initial_salary * (PERCENTAGE_INCREASE / 100)
            final_salary = calculate_salary_increase(initial_salary)

            format_initial = locale.currency(initial_salary, grouping=True)
            format_increase = locale.currency(increase_value, grouping=True)
            format_final = locale.currency(final_salary, grouping=True)

            header = (
                f"{'SALÁRIO INICIAL':<20} | "
                f"{'AUMENTO (%)':^12} | "
                f"{'ACRÉSCIMO':^20} | "
                f"{'NOVO SALÁRIO':>20}"
            )
            separator = '-' * len(header)
            data_row = (
                f"{format_initial:<20} | "
                f"{f'{PERCENTAGE_INCREASE:.1f}%':^12} | "
                f"{format_increase:^20} | "
                f"{format_final:>20}"
            )

            print('\n' + separator)
            print(header)
            print(separator)
            print(data_row)
            print(separator + '\n')
            break

        except ValueError:
            print('\nErro: Digite um valor numérico válido. Exemplo: 4957.50\n')
        except KeyboardInterrupt:
            print('\nOperação cancelada pelo usuário.')
            break
        except Exception as e:
            print(f'Ocorreu um erro inesperado: {e}')
            break

def prompt_product_discount() -> None:
    """
    Calcula e exibe o valor de um desconto e o preço final de um produto.

    Side Effects:
        - Lê dados de entrada padrão (`input`).
        - Imprime dados na saída padrão (`print`).
    """
    print('--- 4.   Calculadora de Descontos ---')
    while True:
        try:
            product_price = float(input('Informe o preço do produto: R$'))
            discount_off = float(input('Informe o valor do desconto (%): '))

            discount_value = product_price * (discount_off / 100)
            final_price = product_price - discount_value 

            print(f'    Resultado: Aplicando {discount_off}%. você economizará {locale.currency(discount_value, grouping=True)}.')
            print(f'    O valor total a ser pago é de {locale.currency(final_price, grouping=True)}.')
            break
        except ValueError:
            print('\n   ERRO: Digite valores numéricos válidos.\n')
        except KeyboardInterrupt:
            print('\n   Operação cancelada pelo usuário.\n')
            break

def prompt_temperature_converter() -> None:
    """
    Converte uma temperatura de graus Celsius para Fahrenheit.

    A fórmula F = (C * 9/5) + 32 é implementada usando constantes nomeadas
    para maior clareza e manutenbilidade do código.

    Side Effects:
        - Lê dados da entrada padrão (`input`).
        - Imprime dados na saída padrão (`print`).
    """
    print('--- 5.   Conversor: Celsius para Fahrenheit ---')
    FAHRENHEIT_FACTOR: float = 9 / 5
    FAHRENHEIT_OFFSET: int = 32
    while True:
        try:
            celsius = float(input('Informe a temperatura em graus Celsius (°C): '))
            fahrenheit = (celsius * FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET
            print(f'   Resultado: {celsius}°C equivalem a {fahrenheit:.1f}°F.\n')
            break
        except ValueError:
            print('\n   Erro: Digite um valor numérico válido.\n')
        except KeyboardInterrupt:
            print('\n   Operação cancelada pelo usuário.\n')
            break

def prompt_car_rental_calculator() -> None:
    """
    Calcula o custo total do aluguel de um carro com base nos dias de uso
    e quilômetros rodados, utilizando taxas pré-definidas.

    Side Effects:
        - Lê dados da entrada padrão (`input`).
        - Imprime dados na saída padrão (`print`).
    """
    print('--- 6.   Calculadora de Aluguel de Veículos ---')
    while True:
        try:
            kms_driven = float(input('Informe a distância percorrida (Km): '))
            days_rented = int(input('Informe o número de dias de aluguel: '))

            total_cost = (kms_driven * CAR_RENTAL_PER_KM) + (days_rented * CAR_RENTAL_PER_DAY)

            print(f'   Custo por {kms_driven} Km: {locale.currency(kms_driven * CAR_RENTAL_PER_KM, grouping=True)}')
            print(f'   Custo por {days_rented} dias: {locale.currency(days_rented * CAR_RENTAL_PER_DAY, grouping=True)}')
            print(f'   Resultado: O valor total a ser pago é de {locale.currency(total_cost, grouping=True)}.\n')
            break
        except ValueError:
            print('\n   ERRO: Digite valores numéricos válidos.\n')
        except KeyboardInterrupt:
            print('\n   Operação cancelada pelo usuário.\n')
            break

def prompt_smoking_impact_calculator() -> None:
    """
    Calcula uma estimativa de dias de vida perdidos com base no histórico
    de tabagismo do usuário.

    Side Effects:
        - Lê dados da entrada padrão (`input`).
        - Imprime dados na saída padrão (`print`).
    """
    print('--- 7.   Calculadora de Impacto do Tabagismo ---')
    DAYS_IN_A_YEAR: int = 365
    MINUTES_IN_A_DAY: int = 1440
    while True:
        try:
            cigarettes_per_day = int(input('Quantos cigarros você fuma por dia? '))
            years_smoking = int(input('Fuma há quantos anos? '))

            total_cigarettes = cigarettes_per_day * years_smoking * DAYS_IN_A_YEAR
            total_minutes_lost = total_cigarettes * MINUTES_LOST_PER_CIGARRETE
            days_lost = total_minutes_lost / MINUTES_IN_A_DAY

            print(f'\n   Em {years_smoking} anos, você fumou aproximadamente {total_cigarettes} cigarros.')
            print(f'   Resultado: Isso representa uma estimativa de {days_lost:.1f} dias de vida perdidos.\n')
            break
        except ValueError:
            print('\n   Erro: Digite valores numéricos inteiros.\n')
        except KeyboardInterrupt:
            print('\n   Operação cancelada pelo usuário.\n')
            break

def main() -> None:
    '''
    Ponto de entrada principal que orquestra a execução sequencial de todas
    as calculadoras práticas do módulo.

    Side Effects:
        - Imprime dados na saída padrão (`print`).
        - Invoca funções que realizam I/O.
    '''
    try:
        locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
    except locale.Error:
        print("Aviso: Locale 'pt_BR.UTF-8' não encontrado. Usando formatação padrão.\n")

    calculate_sum_from_user_input()
    convert_meters_to_millimeters()
    prompt_salary_increase()
    prompt_product_discount()
    prompt_temperature_converter()
    prompt_car_rental_calculator()
    prompt_smoking_impact_calculator()

if __name__ == '__main__':
    main()
