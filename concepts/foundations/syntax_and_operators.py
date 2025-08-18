"""
Este script didático explora os fundamentos da sintaxe e dos operadores
em Python, baseado nos exercíos propostos no livro `Pense em Python`.

O objetivo é demonstrar e explicar os erros de sintaxe mais comuns de
forma controlada, permitindo que um iniciante entenda as mensagens de 
erro do Python em um ambiente seguro.
"""
from __future__ import annotations
from typing import Any 

__author__ = 'Enock Silos'
__version__ = '1.0.0' 
__email__ = 'init.caucasian722@passfwd.com'
__status__ = ''

def test_code_snippet(description: str, code_snippet: str) -> None:
    """
    Executa um trecho de código como string e relata o resultado.

    Esta função atua como `laboratório seguro` para testar código que
    pode gerar erros. Ela usa um bloco `try/except` para capturar qualquer
    exceção, imprimindo a mensagem de erro sem interromper o programa.

    Args:
        description (str): Uma descrição clara do que está sendo testado.
        code_snippet (str): O trecho de código a ser executado, como uma string.
    """
    print(f'\n\t--- Teste: {description} ---\n')
    print(f'\tCódigo a ser executado: {code_snippet}\n')
    try:
        # `exec()` executa uma string como se fosse código Python
        exec(code_snippet)
    except Exception as e:
        print(f'Resultado -> ERRO: {type(e).__name__}: {e}\n') 
    else:
        print('Nenhum erro foi detectado ao realizar a operação.\n')
        print('-' * 50)

def main():
    """
    Função principal que executa as demonstrações dos cenários
    das ocorrências de erros.
    """
    # Omissão de parênteses em uma instrução `print`
    test_code_snippet(
        'Omitindo parênteses em print',
        "print('Olá Mundo'"
    )
    # Omissão de aspas em string
    test_code_snippet(
        'Omitindo uma aspa em string',
        "print('Olá Mundo)"
    )
    # Uso de operadores de sinal
    test_code_snippet(
        'Usando um sinal `+` antes de um número',
        'print(+2)'
    )
    test_code_snippet(
        "Usando dois sinais `+` entre números",
        'print(2++2)'
    )
    # Uso de zeros à esquerda
    test_code_snippet(
        "Tentando usar um zero à esquerda em um número (notação octal antiga)",
        'print(02)'
    )
    # Dois valores sem operador
    test_code_snippet(
        'Dois valores sem operador entre eles',
        'print(4  5)'
    )

if __name__ == '__main__':
    main()

