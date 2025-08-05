"""Agenda de Contatos Simples em Linha de Comando.

Este script implementa um sistema de gerenciamento de contatos (uma agenda)
que é executado no terminal. Ele permite ao usuário realizar operações
básicas de CRUD (Criar, Ler, Atualizar e Apagar) sobre uma lista de
contatos que é mantida em memória.

Funcionalidades Principais:
- Adicionar, alterar, apagar e listar contatos.
- Salvar a lista de contatos em um arquivo de texto.
- Carregar contatos de um arquivo de texto para a memória.
- Interface de menu interativa e robusta com validação de entrada.

O estado da agenda é armazenado em uma lista global `contacts`, onde cada
contato é uma sub-lista no formato `[nome, telefone]`. A persistência dos
dados é feita através de arquivos de texto simples, com cada linha
representando um contato no formato 'nome#telefone'.

Este código foi desenvolvido com foco em clareza, robustez e boas práticas
de programação em Python, incluindo anotações de tipo (type hints) e
documentação (docstrings) completas para todas as funções.

Uso:
    Execute o script diretamente em um terminal para iniciar o menu:
        python nome_do_arquivo.py
"""

__author__ = 'Enock Silos'
__version__ = '1.5.0' 
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

from typing import List, Optional 

contacts: List[List[str]] = []

unsaved_changes = False 

def ask_name() -> str:
    """
    Solicita a entrada do nome do usuário.

    Returns:
        str: O nome que o usuário digitar.
    """
    return input('Nome: ')

def ask_phone() -> str:
    """
    Solicita a entrada do telefone do usuário.

    Returns:
        str: O telefone informado pelo usuário.
    """
    return input('Telefone: ')

def show_data(index: int, name: str, phone: str) -> None:
    """
    Exibe o nome e o telefone do usuário no Console.

    Args:
        index (int): A posição que o registro ocupa na lista de contatos
        name (str): O nome do usuário cadastrado na lista de contatos.
        phone (str): O telefone do usuário cadastrado na lista de contatos.

    Side Effects:
        Imprime uma string formatada no console contendo a posição do registro e
        o nome do usuário seguido do seu telefone cadastrado.
    """
    print(f'Posição: {index} Nome: {name} Telefone: {phone}')

def ask_filename() -> str:
    """
    Solicita ao usuário o nome do arquivo para salvar ou carregar.

    Returns:
        str: O nome do arquivo a ser inserido pelo usuário.
    """
    return input('Nome do arquivo: ')

def search(name:str) -> Optional[int]:
    """
    Procura por um contato na lista pelo nome.
    
    A busca é feita comparando o nome com o primeiro elemento ([0]) de
    cada contato na lista. A comparação não diferencia maiúsculas de
    minúsculas.

    Args:
        name (str): O nome digitado pelo usuário para a busca.

    Returns:
        Optional[int]: O índice do contato na lista, se encontrado.
                       Caso contrário, retorna None.
    """
    search_name = name.lower()
    for index, entry in enumerate(contacts):
        if entry[0].lower() == search_name:
            return index
    return None

def add_contact() -> None:
    """
    Acrescenta um nome e um telefone à lista de contatos.

    Side Effects:
        - Adiciona uma nova lista [nome, telefone] à variável global
          'contacts'.
        - Modifica para `True` o status de `unsaved_changes` de modo a informar
          eventuais alterações não salvas na lista.
    """
    global unsaved_changes
    name: str = ask_name()
    phone: str = ask_phone()
    contacts.append([name, phone])
    unsaved_changes = True 


def delete_contact() -> None:
    """
    Apaga um registro [nome, telefone] da lista de contatos, caso este exista.

    Atenção: Esta função remove o item da variável global `contacts` definitivamente.

    Side Effects:
        - Remove o elemento correspondente da lista global `contacts` (caso ele
          exista) após anuência do usuário diante de um prompt de confirmação.
        - Modifica para `True` o status de `unsaved_changes` de modo a informar
          eventuais alterações não salvas na lista.
        - Imprime uma mensagem de erro no console se o nome não for encontrado. 
    """
    global unsaved_changes
    name: str = ask_name()
    index: Optional[int] = search(name)
    if index is not None:
        while True:
            delete_confirmation = input('Confirma a exclusão do registro? S / N: ').lower()
            if delete_confirmation == 's':
                del contacts[index]
                print('1 Registro excluído com sucesso!')
                unsaved_changes = True
                break
            elif delete_confirmation == 'n':
                print('Nenhum registro foi excluído.')
                break
            else:
                print('Digite S para confirmar ou N para nenhuma ação.')
    else:
        print('Nome não encontrado.')

def update_contact() -> None:
    """
    Permite a atualização de um contato existente na lista.

    Atenção: Esta função modifica a lista global `contacts`.

    Side Effects:
        - Se encontrado, exibe os dados antigos, solicita novos dados,
          e antes de efetuar as alterações exibe mensagens de status (confirmação,
          sucesso, erro).
        - Modifica para `True` o status de `unsaved_changes` de modo a informar
          eventuais alterações não salvas na lista.
        - Se não encontrado exibe uma mensagem de erro no console.
    """
    global unsaved_changes
    index: Optional[int] = search(ask_name())
    if index is not None:
        name: str = contacts[index][0]
        phone: str = contacts[index][1]
        print('Encontrado: ')
        show_data(name, phone)

        print('\nDigite os novos dados:')
        name = ask_name()
        phone = ask_phone()

        while True:
            confirmation_prompt = input('Confirma as alterações dos dados? S / N: ').lower()
            
            if confirmation_prompt == 's':
                contacts[index] = [name, phone]
                print('Contato atualizado com sucesso!')
                unsaved_changes = True 
                break
            elif confirmation_prompt == 'n':
                print('Nenhuma alteração foi realizada.')
                break 
            else:
                print('Digite S para confirmar ou N para negar as alterações.')
    else:
        print('Nome não encontrado.')

def list_contacts() -> None:
    """
    Exibe todos os contatos da agenda de forma formatada.

    Side Effects:
        Imprime no console um cabeçalho, a lista de todos os contatos 
        (usando a função show_data) indicando sua posição exata no 
        registro e um rodapé.
    """
    print('\nAgenda\n\n------')
    for index, entry in enumerate(contacts):
        show_data(index, entry[0], entry[1])
    print('------\n')

def load_contacts() -> None:
    """
    Carrega contatos de um arquivo, substituindo a linha atual.

    A função solicita um nome de arquivo ao usuário. Se o arquivo não
    for encontrado, exibe uma mensagem de erro. Se alguma linha no 
    arquivo estiver mal formatada (sem o separador '∴'), ela será
    ignorada e um aviso será exibido.

    Side Effects:
        - A variável global `contacts`é redefinida e preenchida com o
          conteúdo do arquivo.
        - Modifica o status da variável global `unsaved_changes`
          para `False` sinalizando alterações salvas com sucesso.
        - Imprime mensagens de status (sucesso, erro, aviso) no console.
        - A função será interrompida se não houver alterações a serem salvas.
    """
    global contacts, unsaved_changes
    if unsaved_changes:
        print('Atenção: A agenda atual possui alterações não salvas.')
        confirmation  = input('Deseja continuar e descartar as operações? S / N: ').lower()
        if confirmation != 's':
            print('Operação de carregamento cancelada.')
            return 
    filename: str = ask_filename()
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            contacts = []
            for line in file:
                if not line.strip():
                    continue
                try:
                    name, phone = line.strip().split('∴')
                    contacts.append([name, phone])
                except ValueError:
                    print(f'Aviso: Linha mal formatada ignorada: "{line.strip()}"')
        print(f'\nContatos do arquivo "{filename}" carregados com sucesso!')
        unsaved_changes = False 
    except FileNotFoundError:
        print(f'\nERRO: Arquivo "{filename}" não econtrado.')
    
def save_contacts() -> None:
    """
    Salva a lista de contatos atual em um arquivo.

    Atenção: Esta função cria um novo arquivo ou SOBRESCREVE
    completamente um arquivo existente que tenha o mesmo nome.

    Side Effects:
        - Cria ou sobrescreve um arquivo no disco com os dados da
          variável global `contacts`.
        - Modifica o status da variável global `unsaved_changes`
          para `False` sinalizando alterações salvas com sucesso.
        - Imprime uma mensagem de status (sucesso ou erro) no console.
        - A função será interrompida se não houver alterações a serem salvas.
    """
    global unsaved_changes
    if not unsaved_changes:
        print('A agenda atual não possui alterações. Nenhuma ação foi realizada.')
        return 
    
    filename: str = ask_filename()
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for entry in contacts:
                name = str(entry[0]).replace('\n', '')
                phone = str(entry[1]).replace('\n', '')
                file.write(f'{name} ∴ {phone}\n')
        print(f'\nContatos salvos com sucesso no arquivo "{filename}"!')
        unsaved_changes = False 
    except IOError as e:
        print(f'\nErro ao salvar o arquivo "{filename}": {e}')

def validate_integer_range(prompt: str,
                           start: int,
                           end: int
) -> int:
    """
    Solicita uma entrada e valida se é um inteiro em um intervalo.

    A função insiste em um loop até que o usuário forneça um número 
    inteiro válido dentro de um intervalo especificado [start, end].

    Args:
        prompt (str): A mensagem a ser exibida para o usuário.
        start (int): O valor mínimo do intervalo (inclusivo).
        end (int): O valor máximo do intervalo (inclusivo).

    Returns:
        int: O número inteiro validado inserido pelo usuário.

    Side Effects:
        Imprime mensagens de erro no console se a entrada for inválida
        ou estiver fora do intervalo.
    """
    while True:
        try:
            value = int(input(prompt))
            if start <= value <= end:
                return value
            else:
                print(f'ERRO: O valor deve estar entre {start} e {end}.')
        except ValueError:
            print('ERRO: Favor digitar um número inteiro válido')

def show_length() -> None:
    """
    Exibe o total de contatos armazenados na variável global `contacts`.

    Side Effects:
        Exibe uma mensagem no console informando o número de contatos atual
        no arquivo. 
    """
    print(f'{len(contacts)} contatos armazenados.')

def order_names_by_alpha()-> None:
    """
    Ordena e exibe os registros da lista `contacts` em ordem alfabética 
    usando o nome registrado como parâmetro.

    Side Effects:
        Exibe no console uma lista ordenadas pelos nomes em ordem ascendente.
    """
    contacts.sort(key=lambda x: x[0] )
    list_contacts()
   

def show_menu() -> int:
    """
    Exibe o menu principal e retorna a opção escolhida pelo usuário.

    A função utiliza `validate_integer_range`para garantir que a opção
    esteja dentro do intervalo válido de [0, 8].

    Returns:
        int: A opção numérica validada, inserida pelo usuário.

    Side Effects:
        Imprime o menu de opçõe no console.
    """
    print('''

    1 - Novo
    2 - Altera
    3 - Apaga
    4 - Lista
    5 - Grava
    6 - Lê
    7 - Tamanho da agenda
    8 - Ordenar por Nome

    0 - Sai
''')
    return validate_integer_range('Escolha uma opção: ', 0, 8)

while option := show_menu():
    if option == 0:
        break
    elif option == 1:
        add_contact()
    elif option == 2:
        update_contact()
    elif option == 3:
        delete_contact()
    elif option == 4:
        list_contacts()
    elif option == 5:
        save_contacts()
    elif option == 6:
        load_contacts()
    elif option == 7:
        show_length()
    elif option == 8:
        order_names_by_alpha()

print('\nPrograma Finalizado.')
