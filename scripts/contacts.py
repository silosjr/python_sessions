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
__version__ = '1.10.0' 
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

from typing import List, Optional 
import os.path

contacts: List[List[str]] = []

unsaved_changes = False 

def ask_name(default_name: Optional[str] = None) -> str:
    """
    Solicita a entrada do nome do usuário, exibindo um valor padrão se fornecido.

    Args:
        default_name (Optional[str]): Um valor de nome padrão a ser exibido.
            Se o usuário não fornecer uma entrada, este valor será usado.
    Returns:
        str: O nome que o usuário digitar ou o valor padrão se a entrada for vazia.
    """
    if default_name is not None:
        prompt = f'Nome (padrão: {default_name}):'
    else:
        prompt = 'Nome: '
    
    name_input = input(prompt)
    if name_input:
        return name_input
    return default_name

def ask_phones() -> dict:
    """
    Solicita ao usuário que cadastre um ou mais telefones e seus tipos.

    Returns:
        dict: Um dicionário onde a chave é o tipo do telefone (ex: 'Celular')
              e o valor é o número de telefone correspondente.
    """
    phones = {}
    while True:
        phone_type = input('''\nInforme o tipo de telefone que deseja cadastrar:
                      A - Residencial
                      B - Celular
                      C - Contato
                      D - Comercial
                      E - Outro
                      0 (zero) SAI
''').lower().strip()
        
        if phone_type == '0':
            break
        elif phone_type in ['a', 'b', 'c', 'd', 'e']:
            phone_number = ask_phone()
            
            type_map = {
                'a': 'Residencial',
                'b': 'Celular',
                'c': 'Contato',
                'd': 'Comercial',
                'e': 'Outro'
            }
            phones[type_map[phone_type]] = phone_number

            another = input('Deseja adicionar outro número? (S/N): ').lower().strip()
            if another != 's':
                break
        else:
            print('Opção inválida. Por favor, digite uma opção do menu.')

    return phones

def ask_phone(default_number: Optional[str] = None) -> str:
    """
    Solicita a entrada do telefone do usuário, exibindo um valor padrão se fornecido.

    Args:
        default_number (Optional[str]): Um valor de número de telefone padrão a ser exibido.
            Se o usuário não fornecer uma entrada, este valor será usado.

    Returns:
        str: O telefone informado pelo usuário, ou o valor padrão se a entrada for vazia.
    """
    if default_number is not None:
        prompt = f'Telefone (padrão: {default_number})'
    else:
        prompt = 'Telefone :'

    phone_input = input(prompt)
    if phone_input:
        return phone_input
    return default_number

def ask_birthdate(default_birthdate: Optional[str] = None) -> str:
    """
    Solicita a entrada da data de aniversário do usuário, exibindo um
    valor padrão.

    Args:
        default_birthdate (Optional[str]): Um valor padrão a ser exibido.
            Se o usuário não fornecer uma entrada, este valor será usado.

    Returns:
        str: A data de aniversário informada pelo usuário ou o valor padrão se
             a entrada for vazia.
    """
    if default_birthdate is not None:
        prompt = f'Data de aniversário (padrão: {default_birthdate})'
    else:
        prompt = 'Data de Aniversário: '

    birthdate = input(prompt)
    if birthdate:
        return birthdate
    return default_birthdate

def ask_email(default_email: Optional[str] = None) -> str:
    """
    Solicita a entrada de email para o usuário, exibindo um valor padrão.

    Args:
        default_email (Optional[str]): Um valor padrão a ser exibido. Se 
        o usuário não fornecer uma entrada, este valor será usado.

    Returns:
        str: O email informado pelo usuário ou o valor padrão se a entrada
        for vazia.
    """
    if default_email is not None:
        prompt = f'Email (padrão: {default_email})'
    else:
        prompt = 'Email: '

    email = input(prompt)
    if email:
        return email 
    return default_email

def show_data(
    index: int,
    name: str, 
    phone: str,
    birthdate:str,
    email: str
) -> None:
    """
    Exibe o nome e o telefone do usuário no Console.

    Args:
        index (int): A posição que o registro ocupa na lista de contatos
        name (str): O nome do usuário cadastrado na lista de contatos.
        phone (str): O telefone do usuário cadastrado na lista de contatos.
        birthdate (str): A data de aniversário cadastrada na lista de contatos.
        email (str): O email cadastrado pelo usuário na lista de contatos.

    Side Effects:
        Imprime uma string formatada no console contendo a posição do registro,
        o nome do usuário, seu telefone cadastrado, data de aniversário e email
        cadastrados.
    """
    print(f'Posição: {index} Nome: {name} Telefone: {phone}\
          Data de Aniversário: {birthdate} Email: {email}')

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
    Adiciona um registro composto pelo nome, telefone, data de aniversário e email 
    do usuário à lista `contacts`.

    Side Effects:
        - Adiciona uma nova lista [nome, telefone, data de aniversário, email] à 
          variável global `contacts`.
        - Modifica para `True` o status de `unsaved_changes` de modo a informar
          eventuais alterações não salvas na lista.
        - Exibe uma mensagem de erro ao tentar inserir um nome que já consta na agenda.
    """
    global unsaved_changes
    name: str = ask_name()
    phone: str = ask_phone()
    birthdate: str = ask_birthdate()
    email: str = ask_email()
    if search(name=name):
        print(f'Já existe um contato com o nome {name}')
    else:
        contacts.append([name, phone, birthdate, email])
        unsaved_changes = True 

def delete_contact() -> None:
    """
    Apaga um registro [nome, telefone] da lista de contatos, caso este exista.

    Atenção: Esta função remove o item da variável global `contacts` definitivamente.

    Side Effects:
        - Se o registro a ser apagado for encontrado, todos os seus dados são exibidos
          antes da mensagem de confirmação de exclusão.
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
        contact_data = contacts[index]
        show_data(index, contact_data[0], contact_data[1], contact_data[2], contact_data[3])
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
    Permite a atualização dos seguintes dados de um contato existente na lista:
    1 - Nome.
    2 - Telefone.
    3 - Data de aniversário.
    4 - Email.

    Atenção: Esta função modifica a lista global `contacts`.

    Side Effects:
    - Se encontrado, exibe os dados antigos como padrão, solicita novos dados,
      e antes de efetuar as alterações exibe mensagens de status (confirmação,
      sucesso, erro).
    - Modifica para `True` o status de `unsaved_changes` de modo a informar
      eventuais alterações não salvas na lista.
    - Se não encontrado exibe uma mensagem de erro no console.
    - Ao tentar atualizar um contato com um nome existente é exibida uma mensagem
      de erro interrompendo a operação.
    """
    global unsaved_changes
    index: Optional[int] = search(ask_name())
    if index is not None:
        old_name: str = contacts[index][0]
        old_phone: str = contacts[index][1]
        old_birthdate: str = contacts[index][2]
        old_email: str = contacts[index][3]
        print('Encontrado: ')
        show_data(name=old_name, phone=old_phone, old_birthdate=old_birthdate, old_email=old_email, index=index)

        print('\nDigite os novos dados:')
        name = ask_name(default_name=old_name)
        phone = ask_phone(default_number=old_phone)
        birthdate = ask_birthdate(default_birthdate=old_birthdate)
        email = ask_email(default_email=old_email)

        if name != old_name:
            if search(name) is not None:
                print(f'ERRO: Já existe um contato com o nome {name}.')
                return 

        while True:
            confirmation_prompt = input('Confirma as alterações dos dados? S / N: ').lower()
            if confirmation_prompt == 's':
                contacts[index] = [name, phone, birthdate, email]
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
    Exibe todos os contatos da agenda de forma formatada e no seguinte formato:
        <Posição> <Nome> <Telefone> <Data de Aniversário> <Email>

    Side Effects:
        Imprime no console um cabeçalho, a lista de todos os contatos 
        (usando a função show_data) indicando sua posição exata no 
        registro e um rodapé.
    """
    print('\nAgenda\n\n------')
    for index, entry in enumerate(contacts):
        show_data(index, entry[0], entry[1], entry[2], entry[3])
    print('------\n')

def load_contacts(filename_to_load: Optional[str] = None) -> None:
    """
    Carrega contatos de um arquivo, substituindo a lista atual.

    Se um `filename_to_load` for fornecido, a função o utiliza. Caso contrário,
    solicita o nome do arquivo ao usuário.
    A função verifica se há alterações não salvas antes de carregar um novo arquivo,
    prevenindo a perda de dados.

    Side Effects:
        - A variável global `contacts` é redefinida e preenchida com o conteúdo do arquivo.
        - Se o carregamento for bem-sucedido, a variável global `unsaved_changes`
          é definida como `False`.
        - Imprime mensagens de status (sucesso, erro, aviso) no console.
    """
    global contacts, unsaved_changes
    
    if filename_to_load is not None:
        filename = filename_to_load
    else:
        filename = ask_filename()

    if unsaved_changes:
        print('Atenção: A agenda atual possui alterações não salvas.')
        confirmation  = input('Deseja continuar e descartar as operações? S / N: ').lower()
        if confirmation != 's':
            print('Operação de carregamento cancelada.')
            return 

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
        - Armazena o nome do arquivo da última agenda salva em `last_agenda_file.txt`.
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

        try:
            with open('last_agenda_file.txt', 'w', encoding='utf-8') as last_file_handle:
                last_file_handle.write(filename)
        except IOError as e:
            print(f'Aviso: Não foi possível salvar o nome do último arquivo da agenda: {e}')

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

if os.path.isfile('last_agenda_file.txt'):
    try:
        with open('last_agenda_file.txt', 'r') as last_file_handle:
            last_file_name = last_file_handle.read().strip()
            load_contacts(filename_to_load=last_file_name)
    except IOError as e:
        print(f'Aviso: Não foi possível carregar a última agenda salva: {e}')
    
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
