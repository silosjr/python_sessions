"""
Artefato de Verfificação e Validação para `list_operations_showcase`.

Este módulo constitui a suíte de provas formais para os componentes de lógica
de negócio definidos no módulo `list_operations_showcase`. Cada teste unitário
é projetado para validar um aspecto específico do contrato de uma função,
garantindo que o comportamento do sistema seja determinístico e matematicamente
correto sob um conjunto definido de condições operacionais.

A execução bem-sucedida desta suíte é um pré-requisito para a certificação do
módulo-alvo para o status de `Production`.
"""

from __future__ import annotations
import unittest
from typing import (
    Sequence,
    TypeVar,
    List,
    Optional
)
from python_sessions.data_structures.data_structures_built_in.list_operations_showcase import (
    calculate_average,
    partition_by_predicate,
    extract_unique_preserving_order,
    try_pop_last_item
)

__author__ = 'Enock Silos'
__version__ = '0.3.0'
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Verification'

T = TypeVar('T')

class TestCalculateAverage(unittest.TestCase):
    """
    Suíte de provas formais para a função `calculate_average`.

    Esta classe encapsula o conjuntos de todos os testes unitários projetados
    para validar a correção da função `calculate_average`. A suíte abrange o
    caminho nominal, casos de borda e cenários de dados heterogêneos para
    garantir uma cobertura de verificação abrangente.
    """

    def test_nominal_case_positive_floats(self):
        """
        Prova [1]: Valida o cálculo para o caminho nominal.

        Este teste verifica a correção matemática da função sob as condições
        operacionais mais comuns: uma lista de números de ponto flutuante
        positivos. A aprovação deste ensaio é a linha de base para a
        confiança no componente.
        """
        sample_data = [10.0, 20.0, 60.0]
        expected_result = 30.0
        actual_result = calculate_average(sample_data)
        self.assertAlmostEqual(actual_result, expected_result)
    
    def test_edge_case_empty_list(self):
        """
        Prova[2]: Valida o comportamento para o caso de borda de lista vazia.

        Esta prova verifica a robustez da função contra uma entrada de
        `ZeroDivisionError`. O contrato da função especifica que a média de
        um conjunto de dados vazio é 0.0. Este teste garante que essa
        condição de contorno seja gerenciada de forma segura e previsível.
        """
        sample_data = []
        expected_result = 0.0
        actual_result = calculate_average(sample_data)
        self.assertEqual(actual_result, expected_result)

    def test_edge_case_single_element_list(self):
        """
        Prova[3]: Valida o caso de borda de lista com elemento único.

        Esta prova garante que a lógica de divisão e soma se comporta
        corretamente quando o denominador é 1. A média de uma lista com um
        único elemento deve ser o próprio elemento. Este teste valida a
        identidade matemática sob essa condição.
        """
        sample_data = [42.5]
        expected_result = 42.5
        actual_result = calculate_average(sample_data)
        self.assertAlmostEqual(actual_result, expected_result)

    def test_mixed_positive_negative_and_zero_values(self):
        """
        Prova [4]: Valida o cálculo com dados heterogêneos.

        Este teste verifica a robustez matemática da função com um conjunto
        de dados que inclui valores positivos, negativos e o zero. Garante
        que a implementação de `sum()` e a subsequente divisão operam
        corretamente em todo o domínio de números reais, não apenas em um
        subconjunto.
        """
        sample_data = [10.0, -20.0, 0.0, 30.0]
        expected_result = 5.0
        actual_result = calculate_average(sample_data)
        self.assertAlmostEqual(actual_result, expected_result)

    def test_raises_value_error_on_non_numeric_data(self):
        """
        Verifica a robustez defensiva do componente contra dados malformados.

        Esta prova valida o caminho de falha controlada da função. Ela
        garante que, quando o contrato de tipo é violado em tempo de
        execução com uma sequência contendo dados não-numéricos, a função
        levanta a exceção `ValueError` esperada, em conformidade com sua
        especificação de programação defensiva.
        """
        malforned_data = [10.0, 'p', 20.0]
        with self.assertRaises(ValueError):
            calculate_average(malforned_data)

class TestPartitionByPredicate(unittest.TestCase):
    """
    Suíte de provas formais para o motor `partition_by_predicate`.
    """
    
    def test_nominal_case_integer_partition(self):
        """
        Verifica o particionamento de uma sequência heterogênea de inteiros.

        Esta prova do caminho nominal valida que o motor de particionamento
        segrega corretamente os elementos em duas partições com base em um
        predicado matemático simples, confirmando a correção da lógica central.
        """
        sample_data = [-99, 1, 9, 7, 1421, 87, -2, -77]
        expected_result = ([1, 9, 7, 1421, 87], [-99, -2, -77])
        actual_result = partition_by_predicate(sample_data, lambda x: x > 0)
        self.assertEqual(actual_result, expected_result)

    def test_edge_case_empty_iterable(self):
        """
        Verifica a robustez do componente ao processar um iterável vazio.

        Esta prova de caso de borda crítica garante que o motor é null-safe,
        retornando corretamente uma tupla de duas listas vazias sem levantar
        exceções, em conformidade com o seu contrato.
        """
        sample_data = []
        expected_result = ([], [])
        actual_result = partition_by_predicate(sample_data, lambda x: True)
        self.assertEqual(actual_result, expected_result)

    def test_case_all_items_pass_predicate(self):
        """
        Verifica o comportamento para um dataset onde todos os itens satisfazem o predicado.

        Esta prova valida que a partição 'failed' é corretamente retornada
        vazia quando nenhum elemento falha no teste do predicado, garantindo
        o comportamento correto para datasets homogêneos.
        """
        sample_data = [-66, -1, -33]
        expected_result = ([-66, -1, -33], [])
        actual_result = partition_by_predicate(sample_data, lambda x: x < 0)
        self.assertEqual(actual_result, expected_result)

    def test_case_all_items_fail_predicate(self):
        """
        Verifica o comportamento para um dataset onde nenhum item satisfaz o predicado.

        Esta prova, o inverso da anterior, valida que a partição 'passed'
        é retornada vazia quando todo os elementos falham no teste,
        completando a verificação de robustez para datasets homogêneos.
        """
        sample_data = [3, 7, 9]
        expected_result = ([], [3, 7, 9])
        actual_result = partition_by_predicate(sample_data, lambda x: x < 0)
        self.assertEqual(actual_result, expected_result)

class TestExtractUniquePreservingOrder(unittest.TestCase):
    """
    Suíte de V&V para o componente `extract_unique_preserving_order`.

    Esta classe de teste implementa um conjunto de provas formais para
    verificar a corre~]ap, robustez e generalidade do motor de extração
    de elementos únicos, garantindo sua conformidade com o contrato
    funcional sob diversas condições operacionais, conforme o PESSMC 4.3.
    """
    
    def test_nominal_case_width_duplicates(self):
        """
        Verifica a correção do algoritmo no caminho nominal com dados duplicados.

        Esta prova formal valida a capacidade fundamental do componente de
        processar uma sequência heterogênea, remover todos os elementos
        duplicados e preservar a ordem de aparição do primeiro elemento
        da cada conjunto de duplicatas. Este é o principal caso de uso
        operacional da função.
        """
        sample_data: Sequence[int] = [1, 5, 2, 1, 9, 5, 8]
        expected_result: Sequence[int] = [1, 5, 2, 9, 8]
        actual_result = extract_unique_preserving_order(sample_data)
        self.assertEqual(actual_result, expected_result)

    def test_edge_case_empty_iterable(self):
        """
        Verifica a robustez do componente sob a condição de contorno de entrada nula.

        Conforme o PESSMC 4.3.3, um componente de missão crítica deve se
        comportar de forma previsível na ausência de dados. Esta prova
        garante que o componente retorna corretamente uma sequência vazia
        quando a entrada está vazia, prevenindo falhas de `NoneType` ou
        `IndeErro` em pipelines de dados.
        """
        sample_data: Sequence[T] = []
        expected_result: Sequence[T] = []
        actual_result = extract_unique_preserving_order(sample_data)
        self.assertEqual(actual_result, expected_result)

    def test_case_no_duplicates(self):
        """
        Verifica o comportamento idempotente do componente com dados já únicos.

        Esta prova valida que, quando a sequência de entrada já é única,
        a função atua como uma operação de identidade (idempotente),
        retornando a sequência original inalterada. Isso garante que o
        componente não introduz artefatos ou modificações inesperadas
        em conjunto de dados que já cumprem a condição de unicidade.
        """
        sample_data: Sequence[int] = [1, 2, 3, 4, 5]
        expected_result: Sequence[int] = [1, 2, 3, 4, 5]
        actual_result = extract_unique_preserving_order(sample_data)
        self.assertEqual(actual_result, expected_result)

    def test_generic_type_with_strings(self):
        """
        Verifica a conformidade do componente com seu contrato com seu contrato de tipo genérico.

        Esta prova formal valida que a lógica de deduplicação e preservação
        de ordem é universalmente aplicável a qualquer tipo de dado 'hashable',
        utilizando `str` como o caso de teste representativo para tipos não-
        numéricos. O sucesso deste teste certifica a robustez e a generalidade
        do algoritmo para além do domínio numérico, em conformidade com o
        PESSMC 3.2.2.
        """
        sample_data: Sequence[str] = ['a', 'b', 'a', 'c', 'b']
        expected_result: Sequence[str] = ['a', 'b', 'c']
        actual_result = extract_unique_preserving_order(sample_data)
        self.assertEqual(actual_result, expected_result)

class TestTryPopLastItem(unittest.TestCase):
    """
    Suíte de V&V para o componente de operação segura `try_pop_last_item`.

    Esta classe de teste implementa um conjunto de provas formais para
    verificar o comportamento dual do componente `try_pop_last_item`.
    As provas validam não apenas o valor de retorno, mas também o efeito
    colateral esperado (modificação da lista) no caminho de sucesso, e a
    execução da degradação graciosa (retorno de `None`) no caminho de
    falha, garantindo conformidade com o PESSMC 2.1 e 4.3.
    """

    def test_nominal_case_on_non_empty_list(self):
        """
        Verifica a correção do valor de retorno e do efeito colateral no caminho nominal.

        Esta prova valida a operação bem-sucedida do componente
        em uma lista não vazia. A verificação é dupla:
        1. Prova que o valor de retorno é o último elemento da lista original.
        2. Prova que o efeito colateral da operação - a remoção do último
           elemento - modifica a lista de entrada para o estado esperado.
        O sucesso deste teste certifica o comportamento completo da função
        em seu principal caso de uso operacional.
        """
        sample_data: List[int] = [1, 2, 3]
        expected_return_value: int = 3
        expected_list_after_pop: List[int] = [1, 2]

        actual_return_value = try_pop_last_item(sample_data)

        self.assertEqual(actual_return_value, expected_return_value)
        self.assertEqual(sample_data, expected_list_after_pop)

    def test_failure_case_on_empty_list(self):
        """
        Verifica a execução da degradação graciosa em uma lista vazia.

        Esta prova formal valida o comportamento de resiliência do
        componente sob a garantia de contorno de uma entrada nula.
        A verificação garante que a invocação da função em uma lista
        vazia não levanta uma exceção `IndexError`, mas sim retorna `None`,
        cumprindo o contrato `Optional[T]` e demonstrando uma falha
        controlada, conforme exigido pelo PESSMC 2.1. Também se verifica
        que a lista de entrada permanece inalterada.
        """
        sample_data: List[T] = []
        expected_return_value: Optional[T] = None
        expected_list_after_pop: List[T] = []

        actual_return_value = try_pop_last_item(sample_data)

        self.assertEqual(actual_return_value, expected_return_value)
        self.assertEqual(sample_data, expected_list_after_pop)

if __name__ == '__main__':
    unittest.main()