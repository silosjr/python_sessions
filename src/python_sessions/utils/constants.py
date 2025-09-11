"""
Módulo central para constantes de aplicação.

Este módulo serve como a Fonte Única da Verdade (SSoT) para valores
literais e de configuração que são partilhados por múltiplos componentes
do pacote `python_sessions`. Centralizar estas constantes aqui garante
consistência e facilita a manutenção e reconfiguração do sistema.

Constantes disponíveis::

    PADDING_WIDTH: int = 4
    CALCULATION_IN_PROGRESS_MESSAGE: str =
        ' Cálculo em execução. Sistema ocupado, aguarde conclusão.'
    DEFAULT_SAMPLE_SIZE: int = 7
    ZERO_DIVISION_ERROR_MESSAGE: str =
        ' ERRO CRÍTICO: Divisor igual a zero detectado. Execução terminada.'
    SELECTED_OPTION_INPUT: str = ' ~ Sua opção → '
    ERROR_INVALID_MENU_OPTION: str =
        ' ERRO: Por favor insira uma das opções válidas do menu.'
    USER_CANCELLED_OPERATION_MESSAGE: str =
        ' Operação cancelada pelo usuário. Nenhuma alteração foi realizada.'
    SESSION_TERMINATED_MESSAGE: str = '\\n [SESSÃO ENCERRADA]\\n'
"""
from __future__ import annotations

__author__ = 'Enock Silos'
__version__ = '0.3.0'
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

PADDING_WIDTH: int = 4
CALCULATION_IN_PROGRESS_MESSAGE: str = ' Cálculo em execução. Sistema ocupado, aguarde conclusão.'
DEFAULT_SAMPLE_SIZE = 7
ZERO_DIVISION_ERROR_MESSAGE: str = ' ERRO CRÍTICO: Divisor igual a zero detectado. Execução terminada.'
SELECTED_OPTION_INPUT: str = ' ~ Sua opção → '
ERROR_INVALID_MENU_OPTION: str = ' ERRO: Por favor insira uma das opções válidas do menu.'
USER_CANCELLED_OPERATION_MESSAGE: str = ' Operação cancelada pelo usuário. Nenhuma alteração foi realizada.'
SESSION_TERMINATED_MESSAGE: str = '\n [SESSÃO ENCERRADA]\n'
