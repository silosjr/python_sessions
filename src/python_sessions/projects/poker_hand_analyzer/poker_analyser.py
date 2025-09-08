"""
Este script implementa um analisador de mãos de pôquer e um simulador para
estimar as probabilidades de cada tipo de mão, conforme proposto no livro `Pense em Python`.

O projeto está dividido em duas partes principais:
1.  A classe `PokerHand`, um "motor" de análise que herda de uma `Hand`
    genérica e adiciona a capacidade de se auto-classificar, identificando
    padrões como Pares, Sequências e Flushes.
2.  Uma função de simulação (`simulate_poker`) que utiliza esse motor para
    "jogar" milhares de mãos de Pôquer, recolher estatísticas e calcular 
    as probabilidades de ocorrência de cada tipo de mão.
"""
from __future__ import annotations
from typing import Dict
import sys
from pathlib import Path

# --- Bloco de Configuração de Caminho (Path Bootstrap) ---
# Esta é a solução definitiva para resolver erros de importação (ModuleNotFoundError)
# quando o script é executado de diferentes locais (ex: terminal vs. editor).
try:
    # Obtém o caminho absoluto para a pasta raiz do projeto ('python_sessions')
    # A lógica sobe dois níveis a partir da localização deste arquivo:
    # .../poker_hand_analyzer/ -> .../projects/ -> .../python_sessions/
    project_root = Path(__file__).resolve().parent.parent.parent
    # Adiciona a raiz do projeto ao caminho de busca do Python
    sys.path.insert(0, str(project_root))
except (IndexError, NameError):
    # Fallback caso __file__ não esteja definido (ambientes raros)
    print("AVISO: Não foi possível determinar o caminho raiz do projeto. As importações podem falhar.")
    pass

from concepts.object_oriented_programming.card_game_inheritance import Hand, Deck


__author__ = 'Enock Silos'
__version__ = '3.0.0' 
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

class PokerHand(Hand):
    """
    Representa uma mão de Pôquer, com métodos para se auto-classificar.

    Esta classe herda da classe `Hand`, reutilizando toda a sua funcionalidade
    básica (como adicionar e ordenar cartas), mas adiciona uma camada de
    inteligência específica de Pôquer. A sua principal responsabilidade é 
    analisar o seu próprio conjunto de cartas e determinar a melhor
    classificação de mão que ele representa.
    """
    def make_rank_histogram(self) -> Dict[int, int]:
        """
        Cria um histograma com a contagem de cada valor (rank) na mão.

        Um histograma (ou mapa de frequência) é a estrutura de dados mais
        eficiente para analisar padrões baseados na contagem de itens, como
        Pares, Trincas e Quadras. Este método auxiliar serve como a principal
        "ferramenta de diagnóstico" para esses padrões.

        Returns:
            Dict[int, int]: Um dicionário onde as chaves são os ranks das
                            cartas e os valores são o número de vezes que
                            cada rank aparece na mão.
        """
        rank_cards_dict = {}

        for card in self.cards:
            rank_cards_dict[card.rank] = rank_cards_dict.get(card.rank, 0) + 1
        
        return rank_cards_dict
    
    def make_suit_histogram(self) -> Dict[int, int]:
        """
        Cria um histograma com a contagem de cada naipe (suit) na mão.

        Similar ao histograma de ranks, esta ferramenta é usada para detectar 
        padrões baseados em naipes, como o Flush.

        Returns:
            Dict[int, int]: Um dicionário em que as chaves são os naipes e os
                            os valores são o número de vezes que cada naipe
                            aparece na mão.
        """
        suit_cards_dict = {}

        for card in self.cards:
            suit_cards_dict[card.suit] = suit_cards_dict.get(card.suit, 0) + 1

        return suit_cards_dict

    def has_pair(self) -> bool:
        """
        Verifica se a mão contém pelo menos um par (duas cartas do mesmo valor).
        """
        count_dict = self.make_rank_histogram()

        for values in count_dict.values():
            if values >= 2:
                return True
        return False
    
    def has_twopair(self) -> bool:
        """
        Verifica se a mão contém exatamente dois pares.
        """
        count_dict = self.make_rank_histogram()
        pairs_count = 0

        for pairs in count_dict.values():
            if pairs == 2:
                pairs_count += 1

        return pairs_count == 2
    
    def has_three_of_a_kind(self) -> bool:
        """
        Verifica se a mão contém pelo menos uma trinca (três cartas de um mesmo valor).
        """
        count_dict = self.make_rank_histogram()

        for values in count_dict.values():
            if values >= 3:
                return True
            
        return False 
    
    def has_straight(self) -> bool:
        """
        Verifica se a mão contém uma sequência de 5 cartas.
        """
        ranks = [card.rank for card in self.cards]
        unique_ranks = sorted(list(set(ranks)))
        for i in range(len(unique_ranks) - 4):
            if unique_ranks[i+4] - unique_ranks[i] == 4:
                return True
            
        if unique_ranks == [1, 10, 11, 12, 13]:
            return True   

        return False
    
    def has_flush(self) -> bool:
        """
        Verifica se a mão contém pelo menos 5 cartas do mesmo naipe.
        """
        count_dict = self.make_suit_histogram()

        for values in count_dict.values():
            if values >= 5:
                return True
        
        return False 
    
    def has_full_house(self) -> bool:
        """
        Verifica se a mão contém uma trinca e um par.
        """
        full_house = self.make_rank_histogram().values()

        return 3 in full_house and 2 in full_house
        
    def has_four_of_a_kind(self) -> bool:
        """
        Verifica se a mão contém uma quadra (quatro cartas do mesmo valor).
        """
        four_of_a_kind = self.make_rank_histogram().values()

        return 4 in four_of_a_kind
            
    def has_straight_flush(self) -> bool:
        """
        Verifica se a mão contém um straight flush (sequência do mesmo naipe).

        Este é o teste mais complexo, pois requer que o mesmo conjunto de 5 cartas
        seja, ao mesmo tempo, uma sequência e um flush. A estratégia é:
        1. Encontrar um naipe que tenha 5 ou mais cartas (um flush).
        2. Isolar apenas as cartas desse naipe.
        3. Verificar se esse subconjunto de cartas forma uma sequência.
        """
        suit_histogram = self.make_suit_histogram()
        flush_suit = None 
        for suit, count in suit_histogram.items():
            if count >= 5:
                flush_suit = suit 
                break 
        if flush_suit is None:
            return False
        
        flush_cards = [card for card in self.cards if card.suit == flush_suit]
        flush_hand = PokerHand()
        flush_hand.cards = flush_cards

        return flush_hand.has_straight()
    
    def classify(self):
        """
        Descobre e atribui o rótulo da melhor mão possível.

        Este método atua como um "classificador mestre". Ele invoca os métodos 
        de diagnóstico (`has_*`) numa ordem hierárquica, do padrão mais 
        valioso para o menos valioso. A estrutura `if/elif` garante que, assim
        que a primeira (e, portanto, a melhor) combinação for encontrada, a
        classificação pare e o rótulo seja atribuído.
        """
        if self.has_straight_flush():
            self.label = 'Straight Flush'
        elif self.has_four_of_a_kind():
            self.label = 'Four of a Kind'
        elif self.has_full_house():
            self.label = 'Full House'
        elif self.has_flush():
            self.label = 'Flush'
        elif self.has_straight():
            self.label = 'Straight'
        elif self.has_three_of_a_kind():
            self.label = 'Three of a Kind'
        elif self.has_twopair():
            self.label = 'Two Pairs'
        elif self.has_twopair():
            self.label = 'Pair'
        else:
            self.label = 'High Card'

def simulate_poker(num_simulations: int = 10000) -> Dict[str, int]:
    """
    Executa múltiplas simulações de jogos de Pôquer para estimar probabilidades.

    Esta função é um simulador de "Monte Carlo". Ela repete um processo aleatório
    (embaralhar e distribuir cartas) um grande número de vezes para convergir
    para uma estimativa estatística das probabilidades reais.

    Args:
        num_simulations (int, Optional): O número de vezes que o baralho será 
            embaralhado e distribuído. O padrão é 10000.

    Returns:
        Dict[str, int]: Um dicionário com a contagem total de cada classificação
                        de mão encontrada em todas as simulações.
    """
    
    hand_labels_list = [
        'Straight Flush',
        'Four of a Kind',
        'Full House',
        'Flush',
        'Straight',
        'Three of a Kind',
        'Two Pairs',
        'Pair',
        'High Card'
    ]

    hand_labels_dict = {key: 0 for key in hand_labels_list}


    for i in range(num_simulations):
        if (i + 1) % 1000 == 0:
            print(f'Simulação {i+1}/{num_simulations}...')

        deck = Deck()
        deck.shuffle()

        hands = deck.deal_hands(5, 7, PokerHand)

        for hand in hands:
            hand.classify()
            hand_labels_dict[hand.label] += 1

    return hand_labels_dict

if __name__ == '__main__':
    # Define os parâmetros da simulação
    SIMULATIONS = 10000
    HANDS_PER_SIMULATION = 7
    num_total_hands = HANDS_PER_SIMULATION * SIMULATIONS

    print(f'Executando um total de {num_total_hands} simulações de mãos de Pôquer...')
    counts = simulate_poker(num_simulations=SIMULATIONS)

    # Exibe os resultados numa tabela formatada
    print('\n--- Resultados da Simulação ---')
    print(f'{'Classificação':<20} | {'Contagem':>10} | {'Probabilidade (%)':>20}')
    print('-' * 57)

    for label, count in counts.items():
        probability = (count / num_total_hands) * 100
        print(f'{label:<20} | {count:>10} | {probability:>19.6f}%')







  

        
