"""
Implementação de um Analisador de Cadeias de Markov.

Este script define uma classe `Markov` capaz de ler um texto, aprender a 
estrutura estatística das sequências de palavras e gerar um novo texto 
pseudoaleatório que imita o estilo do original.
"""

from __future__ import print_function, division
import sys
import random
from typing import Dict, List, Tuple 
from text_utils import skip_gutenberg_header, shift
from pathlib import Path

class Markov:
    """
    Encapsula a análise estatística de um texto para geração de texto.

    Esta classe implementa o algoritmo de Cadeia de Markov. Ela funciona
    construindo um mapa de probabilidades de transição entre estados (neste
    caso "estados" são sequências de palavras, ou "prefixos"). Após a análise
    de um texto-fonte, a classe pode usar este mapa para gerar um novo texto
    que imita as características estatísticas do original.
    """

    def __init__(self):
        """
        Inicializa o analisador de Markov.

        O construtor prepara o objeto para a análise, criando os dois atributos
        de estado essenciais: `suffix_map`, que armazenará o conhecimento 
        aprendido do texto, e `prefix`, que atuará como a "memória" de curto
        prazo do analisador enquanto ele lê o texto.
        """
        # Mapeia um prefixo (tupla de palavras) para uma lista de sufixos possíveis.
        self.suffix_map: Dict[Tuple[str, ...], List[str]] = {}
        # A janela "deslizante" atual de palavras.        
        self.prefix: Tuple[str, ...] = ()   

    def process_file(self, filename: str, order: int = 2) -> None:
        """
        Lê um arquivo e realiza a Análise de Markov.

        Este é o método principal para a fase de "treinamento". Ele orquestra
        a abertura do arquivo, a limpeza do cabeçalho e a iteração sobre cada
        palavra, delegando o processamento individual para o método `process_word`.
        A utilização de um gestor de contexto (`with open(...)`) garante que o arquivo
        seja fechado corretamente, mesmo em caso de erros.

        Args:
            filename (str): O caminho para o arquivo de texto a ser analisado.
            order (int, Optional): A ordem da Cadeia de Markov, ou seja, o número
                de palavras no prefixo que o analisador usará como "memória"
                para prever a próxima palavra. Padrão é 2.
        """
        try:
            with open(filename, 'r', encoding='utf-8') as file_pointer:
                skip_gutenberg_header(file_pointer)        
                for line in file_pointer:

                    for word in line.rstrip().split():
                        self.process_word(word, order)
        except FileNotFoundError:
            print(f"ERRO: O arquivo '{filename}' não foi encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro ao processar o arquivo: {e}")

    def process_word(self, word: str, order: int = 2) -> None:
        """
        Processa cada palavra para construir o mapa de sufixos.

        Este método é o cérebro do algoritmo de aprendizado. Para cada palavra
        encontrada no texto, ele atualiza o `suffix_map`. A lógica é dividida
        em duas fases: uma fase inicial de "aquecimento", em que as primeiras
        `order` palavras são acumuladas para formar o primeiro prefixo, e a 
        fase principal, onde cada nova palavra é registrada como um possível
        sufixo para o prefixo atual, antes de a "janela deslizante" do prefixo
        ser movida para a frente.

        Args:
            word (str): A palavra atual a ser processada.
            order (int, Optional): A ordem da análise, necessária para determinar
                o fim da fase de "aquecimento".
        """
        # Fase de "aquecimento": apenas acumula o primeiro prefixo
        if len(self.prefix) < order:
            self.prefix += (word,)
            return
        
        # Tenta adicionar o sufixo à lista existente. Esta abordagem de
        # "tentar primeiro e tratar o erro depois (EAFP)" é comum e eficiente
        # em Python para popular dicionários.
        try:
            self.suffix_map[self.prefix].append(word)
        except KeyError:
            # Se o prefixo é novo, cria uma nova entrada no mapa.
            self.suffix_map[self.prefix] = [word]

        # Move a "janela deslizante" uma palavra para a frente.
        self.prefix = shift(self.prefix, word)        

    def random_text(self, n: int = 100) -> str:
        """
        Gera um texto pseudoaleatório a partir do texto analisado.

        Este método é a fase "criativa". Ele usa o conhecimento armazenado no
        `suffix_map` para construir um novo texto. O processo começa com um 
        prefixo aleatório e, em seguida, itera `n` vezes, a cada passo
        escolhendo aleatoriamente um dos sufixos conhecidos para o prefixo
        atual e atualizando o prefixo para a próxima iteração.

        Args:
            n (int, Optional): O número de palavras a serem geradas. Padrão é 100.

        Returns:
            str: Uma string contendo o texto gerado. Se o mapa de sufixos 
                estiver vazio, retorna uma mensagem de erro.
        """
        if not self.suffix_map:
            return 'ERRO: O mapa de sufixos está vazio. Processe um arquivo primeiro.'
        
        # Escolhe um prefixo aleatoriamente para começar.
        start = random.choice(list(self.suffix_map.keys()))
        generated_words = list(start)

        for _ in range(n - len(start)):
            suffixes = self.suffix_map.get(start)
            if not suffixes:
                # Se chegamos a um "beco sem saída" (um prefixo que estava no
                # final do texto original), recomeçamos com um novo prefixo
                # aleatório para evitar parar a geração.
                start = random.choice(list(self.suffix_map.keys()))
                continue 

            # A escolha aleatória de um sufixo imita a probabilidade
            # estatística do texto original.
            word = random.choice(suffixes)
            generated_words.append(word)
            start = shift(start, word)

        return ' '.join(generated_words)

def main() -> None:
    """
    Função Principal para executar o analisador a partir da linha de comando.

    Esta função lida com a análise de argumentos da linha de comando,
    a instanciação da classe Markov e a orquestração dos métodos
    `process_file` e `random_text` para executar o fluxo completo do programa.

     **Lógica de Caminho de Arquivo Robusta:**
    Para garantir que o script funcione tanto ao ser executado diretamente
    (ex: com o botão "Play" de um editor) quanto a partir do terminal de
    qualquer diretório, a função constrói um caminho absoluto para o arquivo
    de texto padrão (`emma.txt`).

    - `__file__`: É uma variável especial do Python que contém o caminho para o
      arquivo de script atual.
    - `Path(__file__)`: Converte essa string de caminho em um objeto `Path`,
      que é mais poderoso e fácil de manipular.
    - `.parent`: É um atributo do objeto `Path` que nos dá o caminho para a
      pasta que contém o arquivo.
    - `/`: O operador de barra é sobrecarregado pela `pathlib` para juntar
      caminhos de forma inteligente, independentemente do sistema operacional
      (Windows, Linux, etc.).

    Esta abordagem resolve o problema comum do "diretório de trabalho", onde
    o script não consegue encontrar arquivos relativos porque não sabe de
    onde está sendo chamado.
    """
    # Constrói um caminho robusto para o arquivo padrão.
    # Isso garante que o arquivo 'emma.txt' seja encontrado, não importa de onde o script seja executado.
    script_dir = Path(__file__).parent
    default_filename = script_dir / 'emma.txt'
    # Argumentos padrão
    filename: Path | str = default_filename
    n = 100
    order = 2

    # Tenta obter argumentos da linha de comando para permitir a personalização.
    # sys.argv é uma lista contendo o nome do script e os argumentos passados.
    args = sys.argv[1:]
    try:
        if len(args) >= 1:
            filename = args[0]
        if len(args) >= 2:
            n = int(args[1])
        if len(args) >= 3:
            order = int(args[2])
    except ValueError:
        print('ERRO: O número de palavras e a ordem do prefixo devem ser inteiros.')
        sys.exit(1)

    print(f"Analisando '{filename}' com ordem {order} para gerar {n} palavras....\n")

    # Instanciação e execução do analisador.

    markov = Markov()
    markov.process_file(filename, order)
    text = markov.random_text(n)
    print(text)

if __name__ == '__main__':
    main()
