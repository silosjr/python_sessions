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
from typing import List, Dict, Tuple, Any
import random 
import operator
import time 

__author__ = 'Enock Silos'
__version__ = '1.8.0' 
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

PERCENTAGE_INCREASE: float = 15
CAR_RENTAL_PER_KM: float = 0.15
CAR_RENTAL_PER_DAY: float = 60.0
MAX_INCOME_COMMITMENT_RATE: float = 0.30
MINUTES_LOST_PER_CIGARRETE: int = 10
INCOME_TAX_BRACKETS: List[Dict[str, float]] = [
    {'limit': 4664.68, 'rate': 0.275, 'deduction': 908.73},
    {'limit': 3751.05, 'rate': 0.225, 'deduction': 675.49},
    {'limit': 2826.65, 'rate': 0.15, 'deduction': 394.16},
    {'limit': 2259.20, 'rate': 0.075, 'deduction': 182.16},
    {'limit': 0, 'rate': 0.0, 'deduction': 0.0}
]
SALARY_INCREASE_THRESHOLD: float = 6666
SALARY_TIER_1_INCREASE_PERCENTAGE: float = 0.10
SALARY_TIER_2_INCREASE_PERCENTAGE: float = 0.15
LONG_TRIP_THRESHOLD_KM: float = 2000
SHORT_TRIP_PRICE_PER_KM: float = 2.1
LONG_TRIP_PRICE_PER_KM: float = 1.9
MOBILE_PHONE_PLANS: Dict[str, Dict[str, float]] = {
    'small_talk': {'monthly_base_price': 50.0, 'included_minutes_quota': 100.0, 'excess_minute_cost': 0.20},
    'big_talk': {'monthly_base_price': 99.0, 'included_minutes_quota': 500.0, 'excess_minute_cost': 0.15}
}
ELECTRICITY_TARIFFS_CONFIG: Dict[Dict[str, int | float]] = {
    'residential': {'limit': 500, 'base_rate_per_kwh': 0.40, 'over_limit_rate_per_kwh': 0.65},
    'commercial': {'limit': 1000, 'base_rate_per_kwh': 0.55, 'over_limit_rate_per_kwh': 0.60},
    'industrial': {'limit': 5000, 'base_rate_per_kwh': 0.55, 'over_limit_rate_per_kwh': 0.60 }
}
     
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
    print('--- Calculadora de Soma ---')
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

def perform_arithmetic_operation(
                                operand1: int | float, 
                                operand2: int | float, 
                                operation_symbol: str
                                ) -> int | float:    
    """
    Executa uma operação aritmética básica entre dois operandos.

    Esta função pura serve como o motor de cálculo, abstraindo a lógica
    matemática da interface com o usuário. Ela emprega um padrão de design
    de mapeamento (dispatch table) utilizando um dicionário, onde os símbolos
    das operações (chaves) são associados às suas respectivas funções do
    módulo `operator` (valores). Esta abordagem substitui uma cadeia de
    declarações `if/elif/else`, resultando em um código mais limpo,
    escalável e com complexidade de tempo de busca O(1).

    A função é robusta, realizando validações de pré-condição para os
    argumentos. Ela levanta exceções específicas para operadores inválidos
    (`ValueError`) e para a operação matematicamente indefinida de divisão
    por zero (`ZeroDivisionError`), permitindo que a função chamadora trate
    esses erros de forma controlada.

    Args:
        operand1 (Union[int, float]): O primeiro número da operação.
        operand2 (Union[int, float]): O segundo número da operação.
        operation_symbol (str): O símbolo que representa a operação a ser
                                executada ('+', '-', '*', '/').

    Returns:
        Union[int, float]: O resultado numérico da operação aritmética.

    Raises:
        ValueError: Se o `operation_symbol` não for uma das chaves válidas
                    no dicionário de operações.
        ZeroDivisionError: Se a operação for uma divisão (`'/'`) e o
                           `operand2` for zero.
    """
    operations: dict = {
                        '+': operator.add,
                        '-': operator.sub,
                        '*': operator.mul,
                        '/': operator.truediv
    }

    if operation_symbol == '/' and operand2 == 0:
        raise ZeroDivisionError('Não é possível realizar uma divisão por zero.')

    if operation_symbol not in operations:
        raise ValueError('Operador inválido. Use `+`, `-`, `*` ou `/`')
      
    return operations[operation_symbol](operand1, operand2) 

def prompt_basic_calculator() -> None:
    """
    Orquestra a interface de linha de comando para uma calculadora aritmética.

    Este procedimento gerencia o ciclo de vida da interação com o usuário,
    atuando como a camada de apresentação (View Layer). Ele utiliza um laço
    `while` para criar uma sessão persistente que solicita as entradas
    necessárias (dois operandos e um operador) e orquestra a chamada à
    função de cálculo pura (`perform_arithmetic_operation`).

    A função é projetada para ser altamente robusta, utilizando um bloco
    `try...except` unificado para capturar e tratar de forma elegante as
    exceções propagadas pela camada de cálculo, como `ValueError` (para
    entradas numéricas ou operadores inválidos) e `ZeroDivisionError`.
    Isso garante que o programa não encerre abruptamente e forneça feedback
    claro ao usuário, permitindo uma nova tentativa.

    Side Effects:
        - Lê dados da entrada padrão (`input`).
        - Imprime dados na saída padrão (`print`), incluindo prompts,
          resultados e mensagens de erro.
    """
    print('\n--- CALCULADORA DAS OPERAÇÕES BÁSICAS ---\n')
      
    while True:
        try:
            operand1_input = input('Digite o primeiro número (ou "S" para sair): ')
            if operand1_input.lower() == 's':
                print('Operação finalizada.')
                break

            operand1 = float(operand1_input)

            operand2_input = input('Digite o segundo número (ou "S" para sair): ')
            if operand2_input.lower() == 's':
                print('Operação finalizada.')
                break

            operand2 = float(operand2_input)

            op_symbol_input = input("Escolha a operação [+, -, *, /]: ")

            result = perform_arithmetic_operation(operand1, operand2, op_symbol_input)
            print(f'\nRESULTADO: {operand1} {op_symbol_input} {operand2} = {result:.4f}\n')
            break  

        except ValueError as e:
            print(f"\nERRO DE ENTRADA: {e}. Por favor, tente novamente.\n")
            continue  
        except ZeroDivisionError as e:
            print(f"\nERRO MATEMÁTICO: {e}. Por favor, tente novamente.\n")
            continue  
        except KeyboardInterrupt:
            print('\nOperação cancelada pelo usuário.')
            break

def convert_meters_to_millimeters() -> None:
    """
    Converte um valor de metros para milímetros forncido pelo usuário.

    Side Effects:
        - Lê dados de entrada padrão (`input`).
        - Imprime dados na saída padrão (`print`).
    """
    print('---- Conversor: Metros para Milímetros ---')
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

def calculate_tiered_salary_increase(salary: float) -> float:
    """
    Calcula o novo salário aplicando uma taxa de aumento progressiva.

    Esta função implementa uma regra de negócio de reajuste salarial
    baseada em faixas (tiered structure). A lógica de controle condicional
    avalia o salário de entrada em relação a um limiar pré-definido
    (`SALARY_INCREASE_THRESHOLD`) para determinar qual de duas alíquotas de
    aumento deve ser aplicada.

    Este modelo de cálculo é comum em cenários onde se deseja aplicar
    benefícios distintos para diferentes faixas de remuneração,
    diferenciando-se de um reajuste de taxa única. A função permanece pura,
    sem efeitos colaterais (side effects), dependendo apenas de seu
    argumento de entrada e de constantes do módulo para sua execução.

    Args:
        salary (float): O valor do salário inicial, em formato de ponto
                        flutuante.

    Returns:
        float: O valor do novo salário após a aplicação da alíquota de
               aumento correspondente à sua faixa.
    """
    if salary > SALARY_INCREASE_THRESHOLD:
        increase_rate = SALARY_TIER_1_INCREASE_PERCENTAGE
    else:
        increase_rate = SALARY_TIER_2_INCREASE_PERCENTAGE
    
    return salary * (1 + increase_rate)

def prompt_salary_increase() -> None:
    """
    Orquestra uma simulação de reajuste salarial, comparando dois cenários:
    um com taxa de aumento fixa e outro com taxas progressivas.
    
    A função interage com o usuário para obter o salário inicial e apresenta
    os resultados em uma tabela comparativa, facilitando a visualização das
    diferentes regras de negócio.

    Side Effects:
        - Lê dados de entrada padrão (`input`).
        - Imprime dados na saída padrão (`print`).
    """
    print('\n--- Calculadora de Reajuste Salarial ---')
    while True:
        try:
            user_input = input('Informe seu salário atual (ou "S" para sair): R$ ')
            if user_input.lower() == 's':
                print('Operação Finalizada.')
                break 
            
            cleaned_input = user_input.replace('.', '').replace(',', '.')
            initial_salary = float(cleaned_input)

            if initial_salary < 0:
                print('\nERRO: O salário deve ser um valor positivo.')
                continue 

            fixed_final_salary = calculate_salary_increase(initial_salary)
            fixed_increase_value = fixed_final_salary - initial_salary

            tiered_final_salary = calculate_tiered_salary_increase(initial_salary)
            tiered_increase_value = tiered_final_salary - initial_salary

            tiered_effective_rate = (tiered_increase_value / initial_salary) * 100 if initial_salary > 0 else 0

            header = (
                f"|{'CENÁRIO DE AUMENTO':<30} | "
                f"{'ACRÉSCIMO':^20} | "
                f"{'NOVO SALÁRIO':>20} | "
            )

            separator = '-' * len(header)

            row_fixed = (
                f"{f'| Taxa Fixa ({PERCENTAGE_INCREASE:.1f}%)':<30}  | "
                f'{locale.currency(fixed_increase_value, grouping=True):^20} | '
                f'{locale.currency(fixed_final_salary, grouping=True):>20} | '
            )

            row_tiered = (
                f"{f'| Taxa Progressiva ({tiered_effective_rate:.1f}%)':<30}  | "
                f'{locale.currency(tiered_increase_value, grouping=True):^20} | '
                f'{locale.currency(tiered_final_salary, grouping=True):>20} | '
            )

            print('\n' + separator)
            print(header)
            print(separator)
            print(row_fixed)
            print(row_tiered)
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

def analyze_loan_viability(
                            monthly_income: float,
                            property_value: float,
                            loan_term_years: int
                            )-> Dict[str, Any]:
    """
    Analisa a viabilidade de um financiamento imobiliário com base em parâmetros financeiros.

    Esta função pura encapsula a lógica de negócio central para a avaliação de
    um pedido de financiamento. Ela calcula a prestação mensal (amortização
    simples, sem juros) e compara-a com o limite máximo de endividamento do
    proponente, que é determinado pela constante `MAX_INCOME_COMMITMENT_RATE`.

    A função retorna um dicionário estruturado (um "dossiê de análise"),
    contendo não apenas a decisão booleana de aprovação, mas também todos os
    valores intermediários calculados. Esta abordagem de retorno de dados
    ricos permite que a camada de apresentação (a função `prompt_...`) tenha
    toda a informação necessária para construir uma resposta detalhada para
    o utilizador, mantendo esta função livre de efeitos colaterais (side effects)
    como operações de I/O.

    Args:
        property_value (float): O valor total do imóvel a ser financiado.
        monthly_income (float): A renda mensal bruta do proponente.
        loan_term_years (int): O prazo total do financiamento, em anos.

    Returns:
        Dict[str, Any]: Um dicionário contendo o dossiê completo da análise,
                        com chaves para 'is_approved', 'monthly_payment',
                        'max_affordable_payment', e 'total_installments'.
    """
    if loan_term_years <= 0 or property_value < 0 or monthly_income < 0:
        return {
            'is_approved': False,
            'monthly_payment': 0.0,
            'max_affordable_payment': 0.0,
            'total_installments': 0.0
        }
    
    total_installments = loan_term_years * 12
    monthly_payment = property_value / total_installments if total_installments > 0 else float('inf')
    max_affordable_payment = monthly_income * MAX_INCOME_COMMITMENT_RATE
    is_approved = monthly_payment <= max_affordable_payment

    return {
        'is_approved': is_approved,
        'monthly_payment': monthly_payment,
        'max_affordable_payment': max_affordable_payment,
        'total_installments': total_installments
    }

def prompt_loan_viability_analyzer() -> None:
    """
    Orquestra a interface de utilizador para o simulador de financiamento imobiliário.

    Este procedimento atua como a camada de apresentação (View Layer), gerindo
    o ciclo de vida da interação com o utilizador. Utiliza um laço `while` para
    criar uma sessão que solicita as três entradas de dados necessárias: valor
    do imóvel, renda mensal e prazo.

    A função é projetada para ser robusta, empregando um bloco `try...except`
    para capturar `ValueError` de entradas inválidas e `KeyboardInterrupt`
    para um encerramento gracioso. A lógica de negócio é delegada à função
    pura `analyze_loan_viability`. O dicionário retornado é então
    desempacotado e formatado num "dossiê" final bem alinhado e claro,
    proporcionando uma experiência de utilizador profissional.

    Side Effects:
        - Lê dados da entrada padrão (`input`).
        - Imprime dados formatados na saída padrão (`print`).
        - Utiliza `time.sleep` para simular um tempo de processamento.
    """
    print('\n--- SIMULAÇÃO DE FINANCIAMENTO IMOBILIÁRIO ---\n')
    while True:
        try:
            property_value_user_input = input('VALOR DO IMÓVEL ("S" SAIR): R$')

            if property_value_user_input.lower() == 's':
                print('Operação cancelada.\n')
                break

            property_value = float(property_value_user_input)

            monthly_income_user_input = input('RENDA MENSAL ("S" SAIR): R$')

            if monthly_income_user_input.lower() == 's':
                print('Operação cancelada.\n')
                break

            monthly_income = float(monthly_income_user_input)

            loan_term_years_input_user = input('PRAZO PARA PAGAMENTO EM ANOS ("S" SAIR): ')

            if loan_term_years_input_user.lower() == 's':
                print('Operação cancelada.\n')

            separator = '-' * 65
            
            print(separator)
            print('AGUARDE ALGUNS INSTANTES ENQUANTO SUA SIMULAÇÃO É ANALISADA...')
            time.sleep(3)

            loan_term_years = int(loan_term_years_input_user)

            analysis_data = analyze_loan_viability(monthly_income, property_value, loan_term_years)
            
            loan_principal = property_value
            loan_term_months = analysis_data['total_installments']
            monthly_loan_payment = analysis_data['monthly_payment']
            max_monthly_payment_amount = analysis_data['max_monthly_payment']
            eligibility_result = analysis_data['is_approved']

            label_width = 50
            value_width = 15

            print(separator)
            print(f"{'VALOR DO IMÓVEL:':<{label_width}}{locale.currency(loan_principal, grouping=True):>{value_width}}")
            print(f"{'RENDA MENSAL INFORMADA:':<{label_width}}{locale.currency(monthly_income, grouping=True):>{value_width}}")
            print(f"{'PRAZO EM MESES PARA PAGAMENTO:':<{label_width}}{loan_term_months:>{value_width}}")
            print(f"{'PARCELA MENSAL COM SIMULAÇÃO:':<{label_width}}{locale.currency(monthly_loan_payment, grouping=True):>{value_width}}")
            print(f"{'VALOR MÁXIMO DA PARCELA PARA APROVAÇÃO:':<{label_width}}{locale.currency(max_monthly_payment_amount, grouping=True):>{value_width}}")
            status_message = 'FINANCIAMENTO APROVADO' if eligibility_result else 'FINANCIAMENTO NEGADO'
            print(status_message)
            print(separator)
            break 

        except ValueError as e:
            print(f'\nPor favor, informe corretamente os dados solicitados: {e}')
            continue
        except KeyboardInterrupt:
            print('\nOperação cancelada pelo usuário.')
            break 
        except Exception as e:
            print(f'\nTente realizar outra simulação em alguns instantes: {e}')
            break 

def calculate_progressive_tax(salary: float) -> Dict[str, float]:
    """
    Calcula o imposto de renda progressivo com base no salário mensal.

    Este procedimento computacional implementa o algoritmo para o cálculo do
    Imposto de Renda Retido na Fonte (IRRF) no Brasil, conforme a tabela
    progressiva mensal. A função exemplifica um padrão de design de software
    fundamental: a separação entre dados (regras de negócio) e lógica
    (algoritmo).

    As regras tributárias — as faixas de rendimento, alíquotas e parcelas a
    deduzir — são externalizadas na constante `INCOME_TAX_BRACKETS`. Esta
    abstração permite que a função opere de forma agnóstica a estas regras,
    facilitando a manutenção futura do sistema em caso de alterações na
    legislação fiscal.

    O algoritmo executa uma busca linear através das faixas, que devem estar
    previamente ordenadas de forma decrescente por seu limite, para
    identificar o enquadramento correto do salário fornecido. Uma vez
    identificada a faixa, o imposto devido é calculado utilizando a fórmula
    canônica: `(base_de_cálculo * alíquota) - parcela_a_deduzir`.

    Args:
        salary (float): O valor do salário bruto mensal, que serve como
                        base de cálculo para o imposto.

    Returns:
        Dict[str, float]: Um dicionário contendo o extrato detalhado do
                          cálculo, com as seguintes chaves:
                          - 'tax_due': O valor do imposto a ser pago.
                          - 'rate': A alíquota percentual aplicada.
                          - 'deduction': A parcela a deduzir correspondente.

    Raises:
        ValueError: Lançado se o `salary` fornecido for um valor negativo,
                    pois tal entrada é inválida no domínio do problema.
    """
    if salary < 0:
        raise ValueError("O salário não pode ser um valor negativo.")

    if salary == 0:
        return {'tax_due': 0.0, 'rate': 0.0, 'deduction': 0.0}

    for salary_range in INCOME_TAX_BRACKETS:
        if salary > salary_range['limit']:
            tax_due = (salary * salary_range['rate']) - salary_range['deduction']
            return {
                'tax_due': max(0.0, tax_due),
                'rate': salary_range['rate'],
                'deduction': salary_range['deduction']
            }
        
    return {'tax_due': 0.0, 'rate': 0.0, 'deduction': 0.0}
        
def prompt_income_tax_calculator() -> None:
    """
    Orquestra a interação com o usuário para o cálculo de Imposto de Renda.

    Esta função atua como a camada de interface (View Layer) para a
    calculadora de imposto de renda. Sua responsabilidade primária é gerenciar
    o fluxo de I/O (Entrada/Saída) com o usuário através do console,
    garantindo uma experiência robusta e guiada.

    A implementação utiliza um laço de repetição (`while`) para a coleta e
    validação contínua da entrada. A função realiza a validação de tipo,
    assegurando que a entrada possa ser convertida para um tipo numérico, e a
    validação de domínio, verificando que o valor do salário não seja
    negativo. A lógica de negócio principal, o cálculo progressivo do
    imposto, é delegada à função pura `calculate_progressive_tax`, em
    conformidade com o Princípio da Responsabilidade Única. O dicionário
    retornado por esta função é então desempacotado e formatado para uma
    apresentação clara ao usuário, utilizando o módulo `locale` para a
    formatação monetária.

    Side Effects:
        - Lê dados da entrada padrão (`input`) para obter o salário do
          usuário.
        - Imprime dados na saída padrão (`print`) para exibir o resultado,
          mensagens de status e erros de validação.
        - O fluxo de execução pode ser terminado via `KeyboardInterrupt`.
    """
    print('\n --- Calculadora de Imposto de Renda Progressivo ---\n')
    while True:
        try:
            user_input = input('Por favor, informe o valor do seu salário ("S" para SAIR) R$')

            if user_input.lower() == 's':
                print('\tOperação Finalizada.\n')
                break 
            
            gross_salary = float(user_input)

            if gross_salary <= 0:
                print('\tERRO: O salário não pode ser um número negativo.\n')
                continue

            tax_data = calculate_progressive_tax(gross_salary)

            tax_due = tax_data['tax_due']
            rate = tax_data['rate']

            print(f'''
            Salário Bruto:  {locale.currency(gross_salary, grouping=True):>16}
            Alíquota Efetiva:   {rate:.1%}
            Imposto de Renda:   {locale.currency(tax_due, grouping=True):>10}
            {'-' * 40}
''')
            break
        except ValueError:
            print('\tERRO: Por favor, digite um valor numérico válido\n')
        except KeyboardInterrupt:
            print('\nOperação cancelada pelo usuário.\n')
            break 
     
def calculate_trip_price(distance_in_km: float) -> Tuple[float, float]:
    """
    Calcula o preço total de uma viagem e a tarifa por km aplicada.

    Aplica uma tarifa para viagens curtas e outra para viagens longas,
    com base em um limite de distância pré-definido.

    Args:
        distance_in_km (float): A distância da viagem em quilômetros.

    Returns:
        Tuple[float, float]: Uma tupla contendo o preço total da viagem
                             e a tarifa por km que foi utilizada no cálculo.
    """
    if distance_in_km < 0:
        return 0.0, 0.0
    
    if distance_in_km <= LONG_TRIP_THRESHOLD_KM:
        price_per_km = SHORT_TRIP_PRICE_PER_KM
    else:
        price_per_km = LONG_TRIP_PRICE_PER_KM
    
    total_price = distance_in_km * price_per_km
    return total_price, price_per_km

def prompt_trip_price_calculator() -> None:
    """
    Orquestra a interação com o usuário para o cálculo do preço de uma viagem.

    Exibe uma tabela de tarifas, solicita a distância e apresenta um resumo
    claro do custo final e da tarifa aplicada.
    """
    print('\n--- Calculadora de Preço de Viagem ---')

    col_1_width = 35
    col_2_width = 20

    title_1 = 'DESCRIÇÃO DA TARIFA'
    title_2 = 'PREÇO POR KM'

    short_trip_text = f'Viagens até {LONG_TRIP_THRESHOLD_KM:.0f} KM'
    long_trip_text = f'Viagens acima de {LONG_TRIP_THRESHOLD_KM:.0f} KM'

    short_trip_price = locale.currency(SHORT_TRIP_PRICE_PER_KM, grouping=True)
    long_trip_price = locale.currency(LONG_TRIP_PRICE_PER_KM, grouping=True)

    top_border = f"┌{'─' * (col_1_width + 2)}┬{'─' * (col_2_width + 2)}┐"
    header_line = f"│ {title_1:^{col_1_width}} │ {title_2:^{col_2_width}} │"
    middle_border = f"├{'─' * (col_1_width + 2)}┼{'─' * (col_2_width + 2)}┤"
    short_trip_line = f"│ {short_trip_text:<{col_1_width}} │ {short_trip_price:^{col_2_width}} │"
    long_trip_line = f"│ {long_trip_text:<{col_1_width}} │ {long_trip_price:^{col_2_width}} │"
    bottom_border = f"└{'─' * (col_1_width + 2)}┴{'─' * (col_2_width + 2)}┘"

    print(top_border)
    print(header_line)
    print(middle_border)
    print(short_trip_line)
    print(long_trip_line)
    print(bottom_border)

    while True:
        try:
            user_input = input('Informe a distância em KM do destino da sua viagem (ou "S" para sair): ')
        
            if user_input.lower() == 's':
                print('\nOperação finalizada.')
                break

            cleaned_input = user_input.replace('.', '').replace(',', '.')
            distance_in_km = float(user_input)

            if distance_in_km < 0:
                print('ERRO: A distância não pode ser um valor negativo.\n')
                continue 

            total_price, used_rate = calculate_trip_price(distance_in_km)

            print('\n--- CÁLCULO DO SEU BILHETE ---')
            print(f"{'Distância Informada:':<22} {distance_in_km:,.2f} KM")
            print(f"{'Tarifa Aplicada:':<22} {locale.currency(used_rate, grouping=True)} / KM")
            print(f"{'Valor Total:':<22} {locale.currency(total_price, grouping=True)}")
            print('-' * 40 + '\n')
            break

        except ValueError:
            print('\nERRO: Digite um valor numérico válido para a distância.\n')
        except KeyboardInterrupt:
            print('\nOperação cancelada pelo usuário.')
            break

def calculate_phone_bill_details(plan_name: str, minutes_used: float) -> Dict[str, Any]:
    """
    Calcula o extrato detalhado de uma conta de celular com base no plano e consumo.

    Consulta as regras de negócio definidas na constante `MOBILE_PHONE_PLANS`
    para determinar o preço base, minutos excedentes, custo extra e custo total.

    Args:
        plan_name (str): O nome do plano a ser calculado (deve ser uma chave
                         válida em `MOBILE_PHONE_PLANS`).
        minutes_used (float): O total de minutos consumidos pelo usuário.

    Returns:
        Dict[str, Any]: Um dicionário contedo o extrato detalhado da conta, 
                        com chaves para `base_price`, `extra_minutes_charged`,
                        `extra_cost` e `total_cost`.
    """
    plan_details = MOBILE_PHONE_PLANS[plan_name]

    extra_minutes_charged = max(minutes_used - plan_details['included_minutes_quota'], 0)

    extra_cost = extra_minutes_charged * plan_details['excess_minute_cost']
    total_cost = plan_details['monthly_base_price'] + extra_cost
    
    return {
        'base_price': plan_details['monthly_base_price'],
        'excess_minutes': extra_minutes_charged,
        'extra_cost': extra_cost,
        'total_cost': total_cost
    }

def run_phone_bill_simultation() -> None:
    """
     Orquestra uma simulação de fatura de telefonia móvel e exibe um extrato.

    Este procedimento demonstra a aplicação de regras de negócio complexas
    em um cenário simulado. A função opera de forma não interativa, utilizando
    geração de dados programática para selecionar um plano de serviço e
    simular um volume de consumo de minutos.

    Adotando o princípio da Separação de Responsabilidades, esta função
    atua como a camada de apresentação (View Layer). Ela invoca a função
    de cálculo pura (`calculate_phone_bill_details`) para obter um extrato
    de dados estruturado (um dicionário) e, em seguida, assume a
    responsabilidade de formatar e renderizar esses dados em uma fatura
    legível para o usuário final. A apresentação é condicional, detalhando
    custos excedentes apenas quando estes são aplicáveis, mimetizando o
    comportamento de sistemas de faturamento do mundo real.

    Side Effects:
        - Imprime dados formatados na saída padrão (`print`), constituindo a
          interface de usuário da simulação.
        - Altera o estado do gerador de números pseudoaleatórios global do
          módulo `random` ao invocar `random.choice` e `random.uniform`.
    """
    print('\n--- EXTRATO DETALHADO DE SUA FATURA MONTY ---\n ')

    candidate_plans = random.choice(list(MOBILE_PHONE_PLANS.keys()))
    total_minutes_used = random.uniform(0.0, 800.0)

    bill_details = calculate_phone_bill_details(candidate_plans, total_minutes_used)

    total_cost = bill_details['total_cost']
    base_price = bill_details['base_price']
    extra_minutes_charged = bill_details['excess_minutes']
    extra_cost = bill_details['extra_cost']

    label_width = 20
    value_width = 15

    print(f"{'PLANO CONTRATADO:':<{label_width}} {candidate_plans}")
    print(f"{'CUSTO BASE:':<{label_width}} {locale.currency(base_price, grouping=True):>{value_width}}")
    print(f"{'MINUTOS CONSUMIDOS:':<{label_width}} {total_minutes_used:.0f} min.")

    if extra_cost > 0:

        print(f"{'MINUTOS EXCEDENTES:':<{label_width}} {extra_minutes_charged:.0f} min.")
        print(f"{'CUSTO EXTRA:':<{label_width}} {locale.currency(extra_cost, grouping=True):>{value_width}}")

    print('-' * 40)

    print(f"{'VALOR TOTAL A PAGAR:':<{label_width}} {locale.currency(total_cost, grouping=True):>{value_width}}\n")

def calculate_electricity_bill_details(
                    installation_type: str,
                    kwh_consumption: int
                    )-> Dict[str, Any]:
    """
    Calcula o extrato detalhado de uma fatura de energia elétrica.

    Esta função pura serve como o motor de cálculo para a fatura
    dos serviços de energia, implementando uma lógica de tarifação
    progressiva (tiered). As regras do negócio, incluindo os limites
    e as alíquotas para cada categoria de instalação, são desacopladas
    da lógica e armazenadas na constante de dados `ELECTRICITY_TARIFFS_CONFIG`.

    A função realiza validações de pré-condição para garantir a integridade
    dos dados de entrada, levantando `ValueError para consumo negativo ou
    tipos de instalação desconhecidos. O algoritmo então determina a quantidade
    excedente, aplicando os respectivos custos para calcular o valor tota.

    Args:
        installation_type (str): A categoria da instalação (ex: `residential),
                                 que deve corresponder a uma chave válida em 
                                 `ELECTRICITY_TARIFFS_CONFIG`.
        kwh_consumption (int): O consumo total de energia no período, em quilowatts-
                               hora.

    Raises:
        ValueError: Se `kwh_consumption` for negativo.
        ValueError: Se `installation_type` não for encontrado na configuração de
                    tarifas.

    Returns:
        Dict[str, Any]: Um dicionário estruturado contendo o dossiê completo da 
                        fatura, incluindo as tarifas aplicadas, o detalhe do 
                        consumo e o valor total a pagar.
    """
    if kwh_consumption < 0:
        raise ValueError('Consumo de energia (kwh) não pode ser negativo.')
    
    try:
        tariff_details = ELECTRICITY_TARIFFS_CONFIG[installation_type]
    except KeyError:
        raise ValueError(f'Tipo de instalação inválido: {installation_type}')

    
    limit = tariff_details['limit']
    excess_rate = tariff_details['over_limit_rate_per_kwh']
    base_rate = tariff_details['base_rate_per_kwh']

    extra_kwh = 0 if kwh_consumption <= limit else kwh_consumption - limit 
    base_kwh = min(kwh_consumption, limit)
    
    base_cost = base_kwh * base_rate
    extra_cost = extra_kwh * excess_rate

    total_cost = base_cost + extra_cost

    return {
        'consumer_category': installation_type,
        'tariff_base_rate_per_kwh': tariff_details['base_rate_per_kwh'],
        'tariff_excess_rate_per_kwh': tariff_details['over_limit_rate_per_kwh'],
        'total_energy_consumed': kwh_consumption,
        'excess_energy_consumed_kwh': extra_kwh,
        'total_billing_amount': total_cost
            }

def run_electricity_bill_simulation() -> None:
    """
    Orquestra uma simulação de fatura de energia elétrica e exibe o extrato.

    Este procedimento atual como a camada de apresentação (View Layer), 
    demonstrando a aplicação da lógica de faturamento em um cenário 
    não-interativo do mundo real. A função utiliza o módulo `random` para 
    simular um cliente, selecionando aleatoriamente uma categoria de consumo
    e um volume de energia consumida.

    Seguindo o princípio da Separação de Responsabilidades, a lógica de cálculo
    é delegada à função pura `calculate_electricity_bill_details`.
    O dicionário retornado é então desempacotado e formatado numa fatura detalhada
    e profissionalmente alinhada, que apresenta os custos de forma condicional,
    exibindo o consumo excedente apenas quando aplicável.

    Side Effects:
        - Imprime dados formatados na saída padrão (`print`).
        - Altera o estado do gerador de números pseudoaleatórios do módulo `random`.
    """
    print('\n--- FATURA DA PRESTAÇÃO DE SERVIÇOS DE ENERGIA ELÉTRICA ---')

    candidate_categories = random.choice(list(ELECTRICITY_TARIFFS_CONFIG.keys()))
    total_consumed_kwh = random.randint(150, 10000)

    bill_details = calculate_electricity_bill_details(candidate_categories, total_consumed_kwh)

    installation_type = bill_details['consumer_category']
    base_rate_per_kwh = bill_details['tariff_base_rate_per_kwh']
    excess_cost_rate_per_kwh = bill_details['tariff_excess_rate_per_kwh']
    total_consumption = bill_details['total_energy_consumed']
    extra_kwh = bill_details['excess_energy_consumed_kwh']
    total_cost = bill_details['total_billing_amount']

    separator = '-' * 70
    label_width = 50
    value_width = 15

    print(separator)

    print(f"{'CATEGORIA DE CONSUMO:':<{label_width}}{installation_type:>{value_width}}")
    print(f"{'TARIFA PADRÃO (kWh):':<{label_width}}{locale.currency(base_rate_per_kwh, grouping=True):>{value_width}}")
    print(f"{'TARIFA EXCEDENTE (kWh):':<{label_width}}{locale.currency(excess_cost_rate_per_kwh, grouping=True):>{value_width}}")
    print(separator)
    print(f"{'CONSUMO NO PERÍODO:':<{label_width}}{f'{total_consumption:.0f} kWh':>{value_width}}")
    
    if extra_kwh > 0:
        print(f"{'CONSUMO EXCEDENTE:':<{label_width}}{f'{extra_kwh:.0f} kWh':>{value_width}}")
    
    print(separator)
    print(f"{'VALOR TOTAL A PAGAR:':<{label_width}}{locale.currency(total_cost, grouping=True):>{value_width}}")
    print(separator)

def prompt_product_discount() -> None:
    """
    Calcula e exibe o valor de um desconto e o preço final de um produto.

    Side Effects:
        - Lê dados de entrada padrão (`input`).
        - Imprime dados na saída padrão (`print`).
    """
    print('--- Calculadora de Descontos ---')
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
    print('--- Conversor: Celsius para Fahrenheit ---')
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
    print('--- Calculadora de Aluguel de Veículos ---')
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
    print('--- Calculadora de Impacto do Tabagismo ---')
    
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
    """
    Ponto de entrada principal que orquestra a execução sequencial de todas
    as calculadoras práticas do módulo.

    Side Effects:
        - Imprime dados na saída padrão (`print`).
        - Invoca funções que realizam I/O.
    """
    try:
        locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
    except locale.Error:
        print("Aviso: Locale 'pt_BR.UTF-8' não encontrado. Usando formatação padrão.\n")

    calculate_sum_from_user_input()
    prompt_basic_calculator()
    convert_meters_to_millimeters()
    prompt_salary_increase()
    prompt_loan_viability_analyzer()
    prompt_income_tax_calculator()
    prompt_trip_price_calculator()
    run_phone_bill_simultation()
    run_electricity_bill_simulation()
    prompt_product_discount()
    prompt_temperature_converter()
    prompt_car_rental_calculator()
    prompt_smoking_impact_calculator()

if __name__ == '__main__':
    main()