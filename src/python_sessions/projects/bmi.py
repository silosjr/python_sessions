"""
Calculadora de Índice de Massa Corpórea (IMC) - Versão Modular.

Este script oferece uma implementação robusta e modular para calcular o IMC
de um usuário. Foi projetado não apenas para ser funcional, mas também para servir
como um exemplo didático de boas práticas de programação em Python, incluindo
separação de responsabilidades, tratamento de erros e clareza de código.

-------------------------------------------------------------------------------

Estrutura do Módulo:
    O programa é dividido em quatro funções principais, cada uma com uma
    responsabilidade única, orquestradas pela função `main`.

    - get_user_data():
        Responsável por toda a interação com o usuário para coletar e validar
        o peso e a altura, garantindo que os dados estejam prontos para o cálculo.

    - calculate_bmi(weight, height):
        Uma função de cálculo "pura" e "silenciosa". Sua única tarefa é receber
        os dados já validados e retornar o resultado do IMC ou `None` em
        caso de falha, sem interagir com o usuário.

    - evaluate_bmi(bmi):
        Responsável por interpretar o valor numérico do IMC e traduzi-lo
        em uma categoria compreensível para o usuário final.

    - main():
        A função que gerencia o fluxo de execução do programa.
        Ela chama as outras funções na ordem correta, passando os dados
        necessários e tratando os possíveis estados de falha.

-------------------------------------------------------------------------------

Princípios de Design e Boas Práticas Aplicadas:

    - Modularidade e Separação de Responsabilidades:
        Cada função tem um propósito claro e bem definido, tornando o código
        mais fácil de ler, testar e manter. A lógica de obtenção de dados,
        cálculo e apresentação são totalmente desacopladas.

    - Robustez e Programação Defensiva:
        O script é resiliente a erros do usuário. Ele lida com entradas
        inválidas (letras em vez de números, via `ValueError`), valores fora
        dos limites esperados (peso ou altura absurdos) e cancelamentos
        (via `KeyboardInterrupt`), sem quebrar.

    - Fluxo de Controle Explícito:
        O uso de `None` como um valor de retorno para sinalizar falhas
        (em `get_user_data` e `calculate_bmi`) permite que a função `main`
        tome decisões informadas sobre como proceder, em vez de deixar
        uma função de baixo nível encerrar o programa abruptamente.

    - Clareza e Legibilidade:
        O uso de nomes de variáveis e funções descritivos, anotações de tipo
        (`Type Hints`) e `docstrings` detalhadas tornam o código
        autodocumentado e mais fácil de entender.

-------------------------------------------------------------------------------

Como Usar:
    Execute o script a partir de um terminal. O programa solicitará
    interativamente que você insira seu peso em quilogramas (kg) e sua
    altura em centímetros (cm).

    Exemplo de execução:
        $ python nome_do_script.py
"""
__author__ = 'Enock Silos'
__version__ = '0.3.0'
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

def calculate_bmi(weight: float, height: float) -> float | None:
    """
    Calcula o Índice de Massa Corpórea (IMC) de forma segura.

    Esta é uma função "pura" e "silenciosa". Ela não interage com o
    usuário. Sua única responsabilidade é calcular.

    Args:
        weight (float): O peso em quilogramas.
        height (float): A altura em metros.
    
    Returns:
        float: O valor do IMC, ou None, caso haja qualquer falha no seu cálculo.
    """
    bmi = None 
    try:
        if height > 0:
            bmi = weight / (height ** 2) 
    except Exception:
        pass 
    return bmi

def evaluate_bmi(bmi: float) -> None:
    """
    Categoriza o valor do IMC à uma condição de saúde.

    Args:
        bmi (float): O valor do IMC calculado.

    Side Effects:
        Imprime o valor do IMC e sua categoria correspondente.
    """
    print(f'\n\t\t---> Seu IMC: {bmi:.2f} <---\n')
    if bmi < 18.5:
        print("\t\tResultado: Abaixo do peso ideal")
    elif 18.5 <= bmi < 25:
        print("\t\tResultado: Peso está dentro do normal")        
    elif 25 <= bmi < 30:
        print("\t\tResultado: Sobrepeso")
    elif 30 <= bmi < 35:
        print("\t\tResultado: Obesidade grau 1")
    elif 35 <= bmi < 40:
        print("\t\tResultado: Obesidade grau 2")
    else:
        print("\t\tResultado: Obesidade grau 3")

    print('\n\t\t--- FIM DO PROGRAMA ---\n')

def get_user_data() -> tuple[float, float] | None :
    """
    Coleta e valida os dados de peso e altura do usuário, permitidno
    tentativas repetidas até que os dados sejam válidos.

    Returns:
        tuple: Uma tupla (peso, altura_em_metros) se os dados forem válidos,
        ou None se o usuário cancelar a operação.
    """
    while True:
        try:
            weight = float(input('\n\tSeu peso em kg (Exemplo: 75.5): '))
            if 0 < weight <= 300:
                print(f'\n\t\t--- Seu peso: {weight}kg ---')
                height_cm = float(input('\n\tAltura sem vírgula (Exemplo: 170) cm: '))
                if 0 < height_cm <= 225:
                    print(f'\n\t\t--- Sua altura: {height_cm:.0f}cm ---')
                    return weight, height_cm / 100
                else:
                    print('\n\t\tERRO: Valor máximo é 225')
            else:
                print('\n\t\tERRO: Valor máximo é 300')
        except ValueError:
            print('\n\t\tERRO: Você deve digitar um número válido.')
        except KeyboardInterrupt:
            print('\n\tOperação cancelada pelo usuário.')
            return None 

def main():
    """
    Ponto de entrada do script. `main` "orquestra" todo o funcionamento do programa a 
    partir da execução sequencial das funções que resultam no cálculo do IMC, a partir
    da interação do usuário com a entrada dos dados solicitados.
    """
    print('\n\t\t --- Cálculo do IMC ---\n')

    user_data = get_user_data()
    
    if user_data is not None:
        weight, height = user_data
    
    bmi = calculate_bmi(weight, height)
    if bmi is not None:
        evaluate_bmi(bmi)
    else:
        print('\nNão foi possível calcular o IMC. Ocorreu um erro interno.\n')
    
if __name__ == '__main__':
    main()