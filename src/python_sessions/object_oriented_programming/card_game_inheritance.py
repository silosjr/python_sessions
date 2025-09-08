
"""
Este script é um estudo de caso sobre Herança em Programação Orientada a
Objetos (POO), baseado nos exemplos do livro 'Pense em Python'.

Ele define classes para representar cartas de baralho, um baralho completo
e uma mão de jogador, demonstrando como uma subclasee (`Hand`) pode
herdar e especializar o comportamento de uma superclasse (`Deck`).
"""

from __future__ import annotations
import random
from typing import List, Optional, Type

__author__ = 'Enock Silos'
__version__ = '2.3.0' 
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Production'

class Card:
    """
    Representa uma carta de baralho padrão.

    Atributos:
        suit (int): Naipe da carta, representado por um inteiro de 0 a 3.
        rank (int): Valor da carta, representado por um inteiro de 1 a 13.
    """
    suit_names: List[str] = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names: List[Optional[str]] = [
    None, "Ace", "2", "3", "4", "5", "6", "7", 
    "8", "9", "10", "Jack", "Queen", "King"
    ]

    def __init__(self, suit: int = 0, rank: int = 2) -> None:
        """
        Inicializa uma instância de `Card`
        """
        self.suit = suit
        self.rank = rank

    def __str__(self) -> str:
        """
        Retorna a representação da carta em string legível.
        """
        return f'{Card.rank_names[self.rank]} de {Card.suit_names[self.suit]}'

    def __lt__(self, other: Card) -> bool:
        """
        Compara esta carta (self) com outra (other), primeiro por naipe, depois por valor.

        Este método especial sobrecarrega o operador `<`, permitindo que objetos
        `Card` sejam ordenados.

        Args:
            other (Card): O outro objeto Card a ser comparado com este.

        Returns:
            bool: True se `self` for menor que `other`, False, caso contrário.
        """
        t1 = (self.suit, self.rank)
        t2 = (other.suit, other.rank)
        return t1 < t2

class Deck:
    """
    Representa uma coleção de cartas, como um baralho.

    Atributos:
        cards (List[Card]): A lista de objetos `Card` na coleção.
    """
    
    def __init__(self) -> None:
        """
        Inicializa o Deck com 52 cartas padrão.
        """
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self) -> str:
        """
        Retorna uma representação de todas as cartas no baralho.
        """
        # Uma `generator expression` é usada aqui para eficiência de memória
        return '\n'.join(str(card) for card in self.cards)

    def add_card(self, card) -> Card:
        """
        Adiciona uma carta à coleção.
        """
        self.cards.append(card)

    def remove_card(self, card: Card) -> None:
        """
        Remove uma carta específica da coleção.

        Args:
            card (Card): O objeto Card a ser removido.

        Raises:
            ValueError: Se a carta não for encontrada na coleção.
        """
        self.cards.remove(card)

    def pop_card(self, i: int = -1) -> Card:
        """
        Remove e retorna uma carta da coleção.

        Por padrão, remove a última carta, simulando a compra no topo do baralho.
        """
        return self.cards.pop(i)

    def shuffle(self) -> None:
        """
        Embaralha as cartas nesta coleção (operação in-place).
        """
        random.shuffle(self.cards)

    def sort(self) -> None:
        """
        Ordena as cartas em ordem ascendente (operação in-place).
        """
        self.cards.sort()

    def move_cards(self, hand: 'Hand', num: int) -> None:
        """
        Move um número de cartas deste baralho para uma mão.

        Args:
            hand (Hand): O objeto Hand de destino para onde as cartas serão movidas.
            num (int): O número de cartas a serem movidas.
        """
        for _ in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(
            self, num_hands: int,
            cards_per_hand: int,
            hand_class: Optional[Type[Hand]] = None
            ) -> List['Hand']:
        """
        Distribui cartas do baralho para um número de mãos.

        Este método atua como uma "fábrica" flexível, criando e distribuindo
        mãos do tipo especificado em `hand_class`. Se nenhuma classe for
        fornecida, ele usa a classe `Hand` como padrão.

        Args:
            num_hands (int): O número de mãos a serem criadas.
            cards_per_hand (int): O número de cartas a serem distribuídas para cada mão.
            hand_class (Optional[Type[Hand]], optional): A classe a ser usada
                para instanciar as mãos (ex: Hand, PokerHand). O padrão é Hand.

        Returns:
            List[Hand]: Uma lista contendo as instâncias de mão criadas e populadas.
        """
        if hand_class is None:
            hand_class = Hand

        hands = []

        for i in range(num_hands):
            hands.append(hand_class(f'Mão do jogador {i+1}'))
        # Distribui as cartas uma por vez para cada mão
        for i in range(cards_per_hand):
            for hand in hands:
                card = self.pop_card()
                hand.add_card(card)

        return hands

class Hand(Deck):
    """
    Representa uma mão de cartas de um jogador.

    Hand é uma subclasse de Deck. Isso estabelece uma relação 'é um tipo de',
    significando que uma Mão herda todos os métodos públicos de um Baralho
    (como shuffle, sort, pop_card, etc), permitindo a reutilização de código.
    """
    
    def __init__(self, label: str = '') -> None:
        """
        Inicializa uma mão vazia com um rótulo opcional.

        Este método __init__ **sobrescreve (overrides)** o __init__ da superclasse (Deck).
        Quando um objeto Hand é criado, este construtor é executado em vez do construtor de
        Deck, garantindo que a mão comece vazia e não com 52 cartas.
        """
        self.cards: List[Card] = []
        self.label = label

if __name__ == '__main__':

    # 1. Criação e embaralhamento do baralho
    deck = Deck()
    deck.shuffle()

    # 2. Criação da Mão e Prova da Herança
    hand = Hand(label='Mão do Jogador 1')

    # Interação entre Objetos e Uso de Métodos Herdados
    # O método move_cards é chamado no baralho para passar 5 cartas para a mão.
    deck.move_cards(hand, 5)

    # O método sort(), também herdado de Deck, é chamado na mão para ordená-la
    hand.sort()

    # O método __str__, também herdado, é chamado para imprimir a mão.
    print(f'\n--- {hand.label} ---')
    print(hand)

    # Teste do método `deal_hands`
    print('\n--- Testando o método `deal_hands` ---')
    hands_list = deck.deal_hands(num_hands=4, cards_per_hand=5)
    # Exibição das mãos criadas
    for hands in hands_list:
        print(f'\n--- {hand.label} ---')
        print(hand)
    # Verificação do estado final do baralho
    print('\n--- Cartas Restantes do Baralho ---')
    print(f'O baralho agora tem {len(deck.cards)} cartas.')