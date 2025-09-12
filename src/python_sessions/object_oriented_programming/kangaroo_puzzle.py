"""
Este script resolve o "Quebra-Cabeça do Canguru" do livro Pense em Python,
servindo como um estudo de caso sobre um dos erros mais comuns e importantes
de se entender em Python: o uso de argumentos padrão mutáveis.
"""
from __future__ import annotations
from typing import Any, List 

__author__ = 'Enock Silos'
__email__ = 'init.caucasian722@passfwd.com'
__status__ = ''

class Kangaroo:
    """
    Representa um canguru com uma bolsa para carregar itens.

    Esta classe demonstra a forma correta de inicializar atributos mutáveis
    (como listas e dicionários) em um construtor, evitando que todas as
    instâncias compartilhem o mesmo objeto.
    """
    def __init__(self, pouch_contents: List[Any] | None = None) -> None:
        """
        Inicializa uma instância de Kangaroo com uma bolsa vazia.

        Args:
            pouch_contents (List[Any] | None, optional): Uma lista inicial de
                itens para a bolsa. Se None, uma lista vazia é criada. O padrão
                é None para evitar o bug de argumento padrão mutável
        """
        if pouch_contents is None:
            self.pouch_contents = []
        else:
            self.pouch_contents = pouch_contents 

    def put_in_pouch(self, item: Any) -> None:
        """
        Adiciona um item à bolsa do canguru.

        Args:
            item (Any): O objeto a ser adicionado à bolsa.
        """
        self.pouch_contents.append(item)

    def __str__(self) -> str:
        """
        Retorna a representação em string do canguru e do conteúdo da sua bolsa.
        """
        return f'Eu sou um Canguru e na minha bolsa tenho: {self.pouch_contents}'
        
if __name__ == '__main__':

    print('--- O problema: O Canguru com a Implementação Ruim --- ')

    class BadKangaroo:
        """
        Esta é a versão incorreta da classe, para demonstrar o bug.
        NÃO USE ESTE PADRÃO EM CÓDIGO REAL.
        """
        def __init__(self, pouch_contents: List[Any] = []) -> None:
            self.pouch_contents = pouch_contents

        def put_in_pouch(self, item: Any) -> None:
            self.pouch_contents.append(item)

        def __str__(self) -> str:
            return f'Eu sou um Canguru Ruim e na minha bolsa tenho: {self.pouch_contents}'

    # Criando duas instâncias da classe `BadKangaroo`
    kanga_bad = BadKangaroo()
    roo_bad = BadKangaroo()

    kanga_bad.put_in_pouch(roo_bad)

    print(f'Kanga Ruim:     {kanga_bad}')
    print(f'Roo Ruim:       {roo_bad}')
    print(f'\n--> Problema: Ambos os cangurus estão compartilhando a MESMA bolsa!')

    print('\n--- A Solução: O Canguru com a Implementação Correta ---')
    # Criando duas instâncias do Canguru correto
    kanga_bom = Kangaroo()
    roo_bom = Kangaroo()

    # Colocamos roo_bom na bolsa de kanga_bom
    kanga_bom.put_in_pouch(roo_bom)

    print(f"Kanga Bom:      {kanga_bom}")
    print(f"Roo Bom:        {roo_bom}")
    print("\n--> Solução: A bolsa de roo_bom está vazia, como esperado. Cada canguru tem sua própria bolsa.")
        
