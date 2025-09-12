"""
Módulo de Configuração de Projeto.

Este módulo contém ferramentas para garantir que os scripts dentro de um
projeto complexo possam se importar uns aos outros de forma robusta,
independentemente de como ou de onde são executados.
"""

from __future__ import annotations
import sys
from pathlib import Path

__author__ = 'Enock Silos'
__status__ = 'Production'

def setup_project_path() -> None:
    """Encontra a raiz do projeto e a adiciona ao caminho de busca do Python.

    Esta função resolve o problema comum de `ImportError` em projetos com
    múltiplas pastas. Ela funciona da seguinte maneira:
    1.  Começa a partir da localização deste próprio arquivo (`project_setup.py`).
    2.  "Sobe" na hierarquia de pastas, uma por uma.
    3.  Procura por um arquivo ou pasta que sirva como um "marcador" da raiz
        do projeto (neste caso, o arquivo `.gitignore`).
    4.  Quando encontra a raiz, adiciona o seu caminho ao `sys.path`,
        garantindo que todas as importações a partir da raiz (como
        `from concepts...` ou `from projects...`) funcionem corretamente.

    Esta abordagem torna os scripts autossuficientes e portáteis.
    """
    # Path(__file__) é o caminho para este arquivo (project_setup.py).
    # .resolve() o torna um caminho absoluto e inequívoco.
    current_path = Path(__file__).resolve()
    
    # "Sobe" na árvore de diretórios até encontrar a raiz do projeto.
    while not (current_path / '.gitignore').exists():
        # Se chegarmos à raiz do sistema de arquivos sem encontrar o marcador,
        # algo está errado.
        if current_path.parent == current_path:
            raise FileNotFoundError("Raiz do projeto com .gitignore não encontrada.")
        current_path = current_path.parent

    # Adiciona o caminho da raiz do projeto à lista de busca de módulos do Python.
    # Usamos str() para converter o objeto Path de volta para uma string.
    # sys.path.insert(0, ...) garante que o nosso projeto tenha a maior prioridade.
    if str(current_path) not in sys.path:
        sys.path.insert(0, str(current_path))