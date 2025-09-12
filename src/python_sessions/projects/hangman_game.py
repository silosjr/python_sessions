"""
Jogo da Forca para um jogador com cronômetro de partida.
"""

__author__ = 'Enock Silos'
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Release'

import random as r 
import time as t
from typing import List 

def run_hangman_game(secret_word: str) -> None:
    '''
    Executa a lógica principal do jogo da forca.

    A função gerencia as tentativas do jogador, exibe o estado do jogo
    e termina quando a palavra é advinhada ou o limite de erros é atingido.
    Ao final, exibe a duração da partida.

    Args:
        secret_word (str): A palavra a ser advinhada.
    '''
    for _ in range(100):
        print()
    print(secret_word)
    guessed_letters: List[str] = []
    correct_letters: List[str] = []
    errors = 0
    max_errors: int = 6

    start_time: float = t.time()
    while True:
        print(secret_word)
        current_display = ''
        for letter in secret_word:
            current_display += f' {letter} ' if letter in correct_letters else ' _ ' 
        print(f'Palavra: {current_display}\n')

        if ' _ ' not in current_display:
            print('Parabéns, você acertou a palavra!')
            break
        
        print_hangman_stage(errors)

        try:
            attempt = input('\nDigite uma letra:').lower().strip()
            if not attempt.isalpha or len(attempt) != 1:
                print('\nPor favor, digite apenas uma letra válida.')
                t.sleep(1.5)
                continue 
        except KeyboardInterrupt:
            print('\nJogo interrompido pelo usuário.')
            return
        
        if attempt in guessed_letters:
            print('\nVocê já tentou essa letra. Tente outra.')
            t.sleep(1.5)
            continue 

        guessed_letters.append(attempt)

        if attempt in secret_word:
            correct_letters.append(attempt)
        else:
            errors += 1
            print(f'\nA letra "{attempt}" não está na palavra. Você errou!')
            t.sleep(1.5)

        if errors >= max_errors:
            print_hangman_stage(errors)
            print('Você foi enforcado!')
            print(f'A palavra secreta era {secret_word}')
            break 

    end_time: float = t.time()
    duration: float = end_time - start_time
    print(f'\nSua partida durou {duration:.0f} segundos.')

def print_hangman_stage(errors: int) -> None:
        """
        Imprime o estágio atual do desenho da forca com base no número de erros.
        """
        print('  +----+')
        print('  |    |')
        print(f'   O   { '|' if errors > 0 else ''} ')

        body = ''
        if errors == 2: body = '  | '
        elif errors == 3: body = ' /| '
        elif errors >= 4: body = ' /|\\'
        print(f' {body.ljust(4)}  |')

        legs = ''
        if errors == 5: legs = ' /  '
        elif errors >= 6: legs = ' / \\'
        print(f' {legs.ljust(4)}  |')

        print('       |')
        print('=========\n')

def main() -> None:
        """
        Ponto de entrada principal. Carrega as palavras, seleciona uma
        e inicia o jogo.
        """
        try:
            with open('words.txt', 'r', encoding='utf-8') as file_handle:
                 words_list = file_handle.read().split()

                 if not words_list:
                      print('ERRO: O arquivo "words.txt" está vazio ou não pôde ser lido.')
                      return 
                 
                 secret_word = r.choice(words_list).lower()
                 run_hangman_game(secret_word)

        except FileNotFoundError:
             print('ERRO: O arquivo "words.txt" não foi encontrado no diretório.')
        except Exception as e:
             print(f'Ocorreu um erro inesperado: {e}')

if __name__ == '__main__':
  main()