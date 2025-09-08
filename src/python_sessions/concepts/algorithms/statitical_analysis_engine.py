"""
Este módulo fornece um conjunto de ferramentas de alto nível para a 
realização de análises estatísticas descritivas sobre conjuntos de dados
numéricos. A arquitetura implantada exemplifica o princípio da Separação
de Responsabilidades (Separation of Concerns), decompondo o problema em três
componentes distintos e coesos: uma camada de aquisição de dados, um motor de
cálculo puro e uma camada de orquestração e apresentação.

O motor de cálculo é agnóstico em relação aos dados e às operações,
utilizando o paradigma de Funções de Ordem Superior para ampliar um conjunto
arbitrário de funções estatísticas a um vetor de dados de entrada. Esta
abordagem, fundamentada em conceitos de programação funcional, resulta em um
sistema extensível, em que novas métricas de tendência central ou de dispersão
podem ser incorporadas sem a necessidade de modificar o algoritmo de 
processamento principal.
"""

from __future__ import annotations
from typing import Optional, List, Dict, Any, Callable

__author__ = 'Enock Silos'
__version__ = '0.3.0'
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

STATISTICAL_OPERATIONS: Dict[str, Any]  = {
    'Soma': sum,
    'Média': lambda data: sum(data) / len(data) if data else 0.0 
}

def generate_statistical_report(
    data: List[int],
    operations: Dict[str, Callable[[List[int]], float]]
) -> Dict[str, float]:
    """
    Executa um conjunto de operações estatísticas sobre uma amostra de dados.

    Esta função representa um motor de cálculo puro e agnóstico. A sua única
    responsabilidade é receber um vetor de dados (`data`) e um dicionário de
    operações (`operations`) e aplicar cada função de cálculo aos dados.

    A assinatura desta função é um exemplo de Função de Ordem Superior,
    um conceito fundamental da programação funcional. O parâmetro `operations`
    utiliza o tipo `Callable` para definir um contrato rigoroso: ele só aceita
    funções que, por sua vez, aceitam uma lista de inteiros e devolvem um 
    número de ponto flutuante.

    Esta arquitetura desacoplada permite que o motor de análise seja
    infinitamente extensível. Novas métricas estatísticas podem ser adicionadas
    ao dicionário de operações sem que nenhuma linha de código deste motor
    precise ser alterada.

    Args:
        data (List[int]): A amostra de dados numéricos a ser analisada.
        operations (Dict[str, Callable[[List[int]], float]]): Um dicionãrio
            em que as chaves são os nomes das métricas estatísticas e os valores
            são as funções `Callable` que as implementam.

    Returns:
        Dict[str, float]: Um dicionário contendo o relatório final, em que cada
                          chave é o nome de uma métrica e cada valor é o seu
                          resultado calculado.
    """
    report = {}

    for stat_name, operation in operations.items():
        result = operation(data)
        report[stat_name] = result

    return report

def collect_numeric_data_with_sentinel() -> Optional[List[int]]:
    """
    Coleta uma série de dados numéricos inteiros a partir da entrada do usuário.

    Este procedimento implementa um laço de repetição indefinido (`while True`)
    para a aquisição sequencial de dados, um padrão canônico para o processamento
    de amostras de tamanho não predeterminado. A iteração é terminada pela 
    inserção de um valor de sentinela (`Q`), que sinaliza a conclusão bem-sucedida
    da entrada de dados.

    A função é robusta a erros de entrada, utilizando um bloco `try/except`
    para validar apenas valores inteiros que sejam convertidos e adicionados
    ao conjunto de dados. Em caso de interrupção forçada pelo usuário
    (`KeyboardInterrupt`), a função comunica a falha ao retornar `None`,
    distinguindo inequivocamente um cancelamento de uma coleta bem-sucedida
    de uma amostra vazia.

    Returns:
        Optional[List[int]]: Uma lista contendo a amostra de dados numéricos
                             inseridos pelo usuário, ou `None` se a operação
                             foi explicitamente cancelada.
    """
    user_input_values = []

    while True:
        try:
            user_input = input('Digite um número inteiro ("Q" → SAIR): ')
            if user_input.lower() == 'q':
                break

            converted_input = int(user_input)
            user_input_values.append(converted_input)
        except ValueError:
            print('ERRO: A entrada dever ser um valor numérico inteiro.')
            continue
        except KeyboardInterrupt:
            return

    # print(f'DEBUG: {user_input_values}')
    return user_input_values 

def demonstrate_aggregated_stats_with_sentinel() -> None:
    """
    Orquestra e demonstra o fluxo completo de uma análise estatística.

    Esta função atua como a camada de orquestração ("manager"), integrando os
    componentes de coleta de dados e de processamento. A sua responsabilidade
    é gerir o diálogo com o usuário, invocar as ferramentas de backend e,
    finalmente, apresentar o relatório final em uma formatação tabular e 
    profissional.

    O procedimento segue um fluxo de trabalho de três etapas:
    1.  Invoca `collect_numeric_data_with_sentinel` para a aquisição da amostra.
    2.  Entrega a amostra coletada e a "caixa de ferramentas" de operações
        (`STATISTICAL_OPERATIONS`) ao motor `generate_statistical_report`.
    3.  Recebe o dicionário de resultados e itera sobre ele para construir e
        exibir um relatórip formatado para o usuário final.
    """
    print('\n─ ─ ─ MOTOR DE ANÁLISE ESTATÍSTICA DESCRITIVA ─ ─ ─\n')
    numeric_data = collect_numeric_data_with_sentinel()
    if numeric_data is None:
        print('\nOperação cancelada pelo usuário.')
        return

    final_report = generate_statistical_report(numeric_data, STATISTICAL_OPERATIONS)

    print('\n─ ─ ─ Relatório Estatístico Final ─ ─ ─')

    if not numeric_data:
        print('Nenhuma amostra foi inserida para análise.')
        return 

    title_stat_name_column = 'MÉTRICA ESTATÍSTICA'
    title_stat_value_column = 'VALOR CALCULADO'

    col_stat_name_width = 25
    col_stat_value_width = 20

    top_border = f"┌{'─' * (col_stat_name_width + 2)}┬{'─' * (col_stat_value_width + 2)}┐"
    header_line = f"│ {title_stat_name_column:^{col_stat_name_width}} │ {title_stat_value_column:^{col_stat_value_width}} │"
    middle_border = f"├{'─' * (col_stat_name_width + 2)}┼{'─' * (col_stat_value_width + 2)}┤"
    bottom_border = f"└{'─' * (col_stat_name_width + 2)}┴{'─' * (col_stat_value_width + 2)}┘"

    print(top_border)
    print(header_line)
    print(middle_border)

    for stat_name, stat_value in final_report.items():
        if isinstance(stat_value, int):
            formatted_value = f'{stat_value}'
        else:
            formatted_value = f'{stat_value:.2f}'

        data_row = f'│ {stat_name:<{col_stat_name_width}} │ {formatted_value:>{col_stat_value_width}} │'
        print(data_row)

    print(bottom_border)

def main() -> None:
    """
    Ponto de entrada principal para a execução do módulo.
    """
    demonstrate_aggregated_stats_with_sentinel()

if __name__ == '__main__':
    main()
