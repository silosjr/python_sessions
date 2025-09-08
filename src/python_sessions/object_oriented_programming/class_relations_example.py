"""
Módulo para modelagem de estrutura orientada a objetos em Python com fins didáticos,
focado na representação de um esqueleto básico de classes e métodos utilizados para a
geração de diagramas UML (Unified Modeling Language).

Este módulo define uma hierarquia de classes onde `PythonObject` é a superclasse base
para qualquer componente que possa ser representado em um diagrama UML. A classe `ClassDef`
representa uma classe Python, e a classe `Method` representa métodos associados a uma classe.

O objetivo didático deste script é fornecer uma estrutura simples que possa ser utilizada 
para construir ou analisar visualmente a estrutura de código orientado a objetos,
especialmente em ferramentas que geram ou interpretem diagramas UML.
"""

__author__ = 'Enock Silos'
__version__ = '0.3.0'
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

from __future__ import annotations
from typing import Any, List, Optional

class PythonObject:
    """
    Classe base abstrata para qualquer elemento representável em um diagrama de classe UML.

    Esta superclasse existe para facilitar a extensibilidade do modelo, permitindo que
    outras entidades, como atributos, interfaces, ou pacotes, herdem dela.

    A ideia central é que qualquer componente de uma estrutura orientada a objetos que deva
    ser representada visualmente em UML, derive desta classe.
    """
    pass 

class ClassDef(PythonObject):
    """
    Representa uma definição de classe em Python, herdeira de `PythonObject`.

    Esta classe é responsável por armazenar os métodos pertencentes à classe representada,
    o que é essencial para a composição de diagramas UML que exibem as operações de uma classe.

    Attributes:
        methods (List[Any]): Lista de objetos `Method` que representam os métodos da classe.
    """
    def __init__(self, methods: List[Any] | None = None) -> None:
        """
        Inicializa um objeto `ClassDef` com uma lista de métodos `methods` (ou uma lista vazia).

        Args:
            methods (List[Any] | None, optional): Lista contendo instâncias de `Method`, ou outra
                                                  estrutura semelhante. Se não for fornecida, inicializa
                                                  uma lista vazia.

        Notes:
            Embora o tipo aceito aqui seja `List[Any] por flexibilidade, recomenda-se que sejam passadas
            instâncias de `Method` ou seus derivados, a fim de manter a coerência estrutural do modelo UML.
        """
        if methods is None:
            self.methods = []
        else:
            self.methods = methods

class Method(PythonObject):
    """
    Representa um método pertencente a uma classe em Python, herdeira de `PythonObject`.

    Essa classe encapsula a referência à superclasse (`ClassDef`), permitindo identificar
    a qual classe o método pertence. Isso é crucial na construção de diagramas UML, onde 
    os métodos são representados como membros de uma classe.

    Attributes:
        parent_class (ClassDef): Referência à instância `ClassDef` que representa a classe ao qual o método pertence.
    """
    def __init__(self, parent_class: ClassDef) -> None:
        """
        Inicializa um objeto `Method` com a referência ao `ClassDef` ao qual ele pertence.

        Args:
            parent_class (ClassDef): Instância `ClassDef` que representa a classe ao qual o método pertence.
        """
        self.parent_class = parent_class


