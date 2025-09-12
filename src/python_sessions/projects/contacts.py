"""
Agenda de Contatos Simples em Linha de Comando com persistência em JSON.

Este script implementa um sistema de gerenciamento de contatos que permite
ao usuário realizar operações de CRUD (Criar, Ler, Atualizar e Apagar).

Os dados são mantidos em memória como uma lista de dicionários e podem ser
salvos e carregados de um arquivo no formato JSON, garantindo a
integridade de estruturas de dados complexas como os múltiplos telefones.

Funcionalidades:
- Adicionar, alterar, apagar, listar e ordenar contatos.
- Salvar e carregar a agenda em formato JSON.
- Carregamento automático da última agenda utilizada.
- Interface de menu interativa com validação de entrada.
"""

__author__ = 'Enock Silos'
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

from typing import Dict, List, Optional, Any
import json 
from pathlib import Path 

contacts: List[Dict[str, Any]] = []
unsaved_changes: bool = False 
LAST_AGENDA_FILE_CONFIG = Path('last_agenda_file.txt')

def ask_name(default_name: Optional[str] = None) -> str:
    """
    Solicita o nome do contato ao usuário.
    Args:
        default_name (Optional[str], optional): Um valor padrão a ser exibido
            e retornado se o usuário não digitar nada. Padrão é None.
    Returns:
        str: O nome que o usuário digitar ou o valor padrão se a entrada for vazia.
    """
    prompt = f'Nome (padrão: {default_name}): ' if default_name else 'Nome: '
    name_input = input(prompt)
    return name_input or default_name
  
def ask_phones(default_phones: Optional[Dict[str, str]] = None) -> Dict[str, str] :
    """
    Gerencia a coleta interativa de múltiplos telefones para um contato.

    Inicia um laço que permite ao usuário adicionar ou editar telefones
    classificados por tipo (Residencial, Celular, etc.)

    Args:
        default_phones(Optional[Dict[str, str], optional]): Um dicionário de
            telefones existentes para edição. Se None, um novo dicionário é criado.
            Padrão é None.

    Returns:
        Dict[str, str]: Um dicionário final de telefones após a interação com o usuário.

    Side Effects:
        Imprime o menu de tipos de telefone e solicita entradas do usuário no console.
    """
    phones = default_phones.copy() if default_phones else {}

    while True:
        print('\nTelefones Atuais:', phones or 'Nenhum')
        phone_type_input = input('' \
        '\nTipo de Telefone (R-Residencial, C-Celular, T-Trabalho, O-Outro, S-Sair):').lower()

        type_map = {'r': 'Residencial', 'c': 'Celular', 't': 'Trabalho', 'o': 'Outro'}

        if phone_type_input == 's':
            break
        elif phone_type_input in type_map:
            phone_type = type_map[phone_type_input]
            phone_number = ask_phone_number(phones.get(phone_type))
            if phone_number:
                phones[phone_type] = phone_number
            else:
                phones.pop(phone_type, None)
        else:
            print('Opção Inválida')

    return phones 

def ask_phone_number(default_number: Optional[str] = None) -> str:
    """
    Solicita apenas um número de telefone.

    Args:
        default_number (Optional[str], optional): Um valor padrão a ser exibido. Padrão é None.

    Returns:
        str: O telefone informado pelo usuário, ou o valor padrão se a entrada for vazia.
    """
    prompt = f'Telefone (padrão: {default_number}): ' if default_number else 'Telefone: '
    phone_input = input(prompt)
    return phone_input or default_number

def ask_birthdate(default_birthdate: Optional[str] = None) -> str:
    """
    Solicita a data de aniversário ao usuário.

    Args:
        default_birthdate (Optional[str], optional): Um valor padrão a ser exibido.
            Padrão é None.

    Returns:
        str: A data de aniversário informada pelo usuário ou o valor padrão se
             a entrada for vazia.
    """
    prompt = f'Data de aniversário (padrão: {default_birthdate}): ' if default_birthdate else 'Data de Aniversário: '

    birthdate_input = input(prompt)

    return birthdate_input or default_birthdate

def ask_email(default_email: Optional[str] = None) -> str:
    """
    Solicita o email ao usuário.

    Args:
        default_email (Optional[str], optional): Um valor padrão a ser exibido. Padrão
            é None.

    Returns:
        str: O email informado ou o valor padrão.
    """
    prompt = f'Email (padrão: {default_email}): ' if default_email else 'Email: '
        
    email_input = input(prompt)

    return email_input or default_email 

def show_contact_details(
    index: int,
    contact: Dict[str, Any],
) -> None:
    """
    Exibe os detalhes de um único contato de forma formatada.

    Args:
        index (int): A posição (ID) do contato na agenda.
        contact (Dict[str, Any]): O dicionário contendo os dados do contato.

    Side Effects:
        Imprime os detalhes formatados do contato no console.
    """
    print(f'\nID {index} | Nome {contact.get('name', 'N/A')}')
    print(f'    - Aniversário: {contact.get('birthdate', 'N/A')}')
    print(f'    - Email: {contact.get('email', 'N/A')}')
    print(' - Telefones:')
    phones = contact.get('phones', {})
    if phones:
        for p_type, p_number in phones.items():
            print(f'        - {p_type}: {p_number}')
    else:
        print('     - Nenhum telefone cadastrado')

def ask_filename() -> str:
    """
    Solicita ao usuário o nome do arquivo para salvar ou carregar.

    Returns:
        str: O nome do arquivo a ser inserido pelo usuário.
    """
    return input('Nome do arquivo: ')

def search_contact(name:str) -> Optional[int]:
    """
    Procura por um contato na lista pelo nome e retorna seu índice na lista.

    A busca não diferencia maiúsculas de minúsculas.

    Args:
        name (str): O nome digitado pelo usuário para a busca.

    Returns:
        Optional[int]: O índice do contato na lista, se encontrado.
                       Caso contrário, retorna None.
    """
    for index, entry in enumerate(contacts):
        if entry['name'].lower() == name.lower():
            return index
    return None

def add_contact() -> None:
    """
    Adiciona um novo contato à agenda.
    
    Solicita todos os dados do novo contato e o adiciona à lista global
    `contacts`. Impede a adição de contatos com nomes duplicados.

    Side Effects:
        - Modifica a variável global `contacts` adicionando um novo dicionário.
        - Modifica a variável global `unsaved_changes` para True.
        - Imprime mensagens de status ou erro no console.
    """
    global unsaved_changes
    name: str = ask_name()

    if not name:
        print('Nome não pode ser vazio')
        return 
    
    if search_contact(name) is not None:
        print(f'ERRO: Já existe um contato com o nome "{name}".')
        return 
    
    new_contact = {
        'name': name,
        'phones': ask_phones(),
        'birthdate': ask_birthdate(),
        'email': ask_email()
    }
    contacts.append(new_contact)
    unsaved_changes = True 
    print(f'\nContato "{name}" adicionado com sucesso!')

def delete_contact() -> None:
    """
    Apaga um contato da agenda após confirmação.

    Side Effects:
        - Remove um item da lista global `contacts`.
        - Modifica a variável global `unsaved_changes` para True se a exclusão for bem sucedida.
        - Imprime mensagens de status ou erro no console. 
    """
    global unsaved_changes
    name_to_search: str = ask_name()
    if not name_to_search:
        return 
    
    index: Optional[int] = search_contact(name_to_search)
    if index is None:
        print('Nome não encontrado.')
        return
    
    print('\n--- Excluindo Contato ---')
    show_contact_details(index, contacts[index])
    confirmation = input('Tem certeza que deseja excluir este contato? (S/N): ').lower()
    if confirmation == 's':
        del contacts[index]
        unsaved_changes = True
        print('Contato excluído com sucesso.')
    else:
        print('Nenhum registro foi excluído.')

def update_contact() -> None:
    """
    Atualiza os dados de um contato existente.

    Primeiro, busca por um contato. Se encontrado, solicita novos dados para
    cada campo, permitindo que o usuário mantenha os dados antigos ao 
    pressionar Enter.

    Side Effects:
    - Modifica um item na lista global `contacts`.
    - Modifica a variável global `unsaved_changes` para True se houver alteração.
    - Imprime mensagens de status ou erro no console.
    """
    global unsaved_changes
    name_to_search = ask_name()
    if not name_to_search:
        return 

    index = search_contact(name_to_search)
    if index is None:
        print('Nome não encontrado.')
        return 
    
    old_name: str = contacts[index]
    print('\n--- Editando Contato ---')
    show_contact_details(index, old_name)
    print('Digite os novos dados (pressione Enter para manter o atual):')

    new_name = ask_name(default_name=old_name['name'])
    if not new_name:
        print('Nome não pode ser vazio.')
        return 
    
    existing_index = search_contact(new_name)
    if existing_index is not None and existing_index != index:
        print(f'ERRO: Já existe um contato com o nome "{new_name}".')
        return 
    
    updated_contact = {
        'name': new_name,
        'phones': ask_phones(default_phones=old_name['phones']),
        'birthdate': ask_birthdate(default_birthdate=old_name['birthdate']),
        'email': ask_email(default_email=old_name['email'])
    }
    
    contacts[index] = updated_contact
    unsaved_changes = True 
    print('\nContato atualizado com sucesso')

def list_contacts() -> None:
    """
    Exibe todos os contatos da agenda de forma formatada.

    Side Effects:
        Imprime a lista completa de contatos no console, utilizando a 
            função `show_contact_details` para cada um.
    """
    print('\n--- Agenda de Contatos ---')
    if not contacts:
        print('Nenhum contato na agenda.')
    else:
        for index, entry in enumerate(contacts):
            show_contact_details(index, entry)
    print('-----------------------------------\n')

def load_contacts_from_json(filename: Optional[str] = None) -> None:
    """
    Carrega contatos de um arquivo JSON, substituindo a lista atual.

    Args:
        filename (Optional[str], optional): O nome do arquivo a ser carregado.
            Se None, solicita ao usuário. Padrão é None.

    Side Effects:
        - A variável global `contacts` é redefinida e preenchida com o conteúdo do arquivo.
        - Se o carregamento for bem-sucedido, a variável global `unsaved_changes`
          é definida como `False`.
        - Imprime mensagens de status (sucesso, erro, aviso) no console.
    """
    global contacts, unsaved_changes
    
    if filename is None:
        filename = input('Nome do arquivo para carregar: ')

    if not filename: return 

    if unsaved_changes:
        print('Atenção: A agenda atual possui alterações não salvas.')
        confirmation  = input('Deseja continuar e descartar as operações? S / N: ').lower()
        if confirmation != 's':
            print('Operação de carregamento cancelada.')
            return 

    try:
        with Path(filename).open(filename, 'r', encoding='utf-8') as file:
            contacts = json.load(file)
        print(f'\nContatos do arquivo "{filename}" carregados com sucesso!')
        unsaved_changes = False 
    except FileNotFoundError:
        print(f'\nERRO: Arquivo "{filename}" não econtrado.')
    except json.JSONDecodeError:
        print(f'\nERRO: O arquivo "{filename}" está corrompido ou não é um JSON válido. ')
    
def save_contacts_to_json() -> None:
    """
    Salva a lista de contatos atual em um arquivo JSON.

    Side Effects:
        - Cria ou sobrescreve um arquivo no disco.
        - Atualiza o arquivo de configuração `last_agenda_file.txt`.
        - Modifica a variável global `unsaved_changes` para False.
        - Imprime uma mensagem de status (sucesso ou erro) no console.
   """
    global unsaved_changes
    if not unsaved_changes:
        print('A agenda atual não possui alterações. Nenhuma ação foi realizada.')
        return 
    
    filename = input('Nome do arquivo para salvar.')
    if not filename: return 

    try:
        with Path(filename).open('w', encoding='utf-8') as last_file:
            json.dump(contacts, file, indent=4, ensure_ascii=False)

        with LAST_AGENDA_FILE_CONFIG.open('w', encoding='utf-8') as file:
            last_file.write(filename)

        unsaved_changes = False
        print(f'\nContatos salvos com sucesso no arquivo "{filename}"!')
    except IOError as e:
        print(f'ERRO ao salvar o arquivo "{filename}": {e}')

def sort_contacts_by_name()-> None:
    """
    Ordena a lista de contatos em ordem alfabética pelo nome.

    Side Effects:
        - Modifica a ordem da lista global `contacts`.
        - Modifica a variável global `unsaved_changes` para True.
        - Imprime uma mensagem de status e a lista ordenada no console.
    """
    contacts.sort(key=lambda contact: contact['name'].lower())
    unsaved_changes = True 
    print('\nAgenda ordenada por nome.')
    list_contacts()
   
def show_menu() -> int:
    """
    Exibe o menu principal e valida a escolha pelo usuário.

    Returns:
        int: A opção numérica (entre 0 e 7) escolhida pelo usuário.
    
    Side Effects:
        Imprime o menu de opçõe no console e solicita a entrada do usuário.
    """
    print('''
    --- MENU ---
    1 - Adicionar Contato
    2 - Alterar Contato
    3 - Apagar Contato
    4 - Listar Contatos
    5 - Salvar Agenda
    6 - Carregar Agenda
    7 - Ordenar por Nome
    8 - # 

    0 - Sair
''')
    
    while True:
        try:
            option = int(input('Escolha uma opção: '))
            if 0 <= option <= 7:
                return option
            else:
                print('ERRO: Opção inválida. Tente novamente.')
        except ValueError:
            print('ERRO: Por favor, digite um número.')

def main() -> None:
    """
    Ponto de entrada principal do programa.

    Orquestra o carregamento inicial, o laço do menu principal e a
    saída segura do programa.
    """
    if LAST_AGENDA_FILE_CONFIG.is_file():
        last_file_name = LAST_AGENDA_FILE_CONFIG.read_text(enconding='utf-8').strip()
        if last_file_name:
            print(f'Carregando última agenda: {last_file_name}')
            load_contacts_from_json(last_file_name)

    while True:
        option = show_menu()
        if option == 1: add_contact()
        elif option == 2: update_contact()
        elif option == 3: delete_contact()
        elif option == 4: list_contacts()
        elif option == 5: save_contacts_to_json()
        elif option == 6: load_contacts_from_json()
        elif option == 7: sort_contacts_by_name()
        elif option == 0:
            if unsaved_changes:
                confirm_exit = input('Existem alterações não salvas. Deseja realmente sair? (S/N): ').lower()
                if confirm_exit != 's':
                    continue
            break 

    print('\nPrograma Finalizado')

if __name__ == '__main__':
    main()