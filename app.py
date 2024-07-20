import os

lista_restaurantes = [{'nome':'PizzaHut', 'categoria':'Pizzaria', 'status':False}, {'nome':'Toshiro Sushi', 'categoria':'Japonesa', 'status':True}]

def exibir_menu_principal():
    '''Exibe o menu principal que é composto do título e das opções disponíveis.'''
    print('===================')
    print('|  SABOR EXPRESS  |')
    print('===================\n')

    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar status restaurantes')
    print('4. Sair')

def escolher_opcao():
    '''Executa a opção escolhida pelo usuário (function).
    
    Inputs:
    - opcao_escolhida (int) : Escolha do usuário
    '''
    try:
        opcao_escolhida = int(input('\nEscolha uma opção: '))
       
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alterar_status_restaurante()
            case 4:
                encerrar_programa()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def voltar_menu_principal():
    input('\nPressione qualquer tecla para voltar ao menu principal')
    main()

def exibir_subtitulo(texto):
    '''Limpa a tela e exibe o subtítulo da página.
    
    Inputs:
    - texto (str) : Texto do subtitulo
    '''
    os.system('cls')
    linha = '=' * (len(texto) + 6)
    print(linha)
    print(f'|  {texto}  |')
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Cadastra um novo restaurante na lista de restaurantes.

     Inputs:
     - nome_restaurante (str) : Nome do restaurante
     - categoria_restaurante (str) : Categoria

     Outputs:
     - Adiciona o novo restaurante à lista de restaurantes
    '''
    exibir_subtitulo('CADASTRO - Novo restaurante')
    nome_restaurante = input('Digite o nome do restaurante:\n')
    categoria_restaurante = input('Digite a categoria do restaurante:\n')
    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria_restaurante, 'status':False}
    lista_restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    voltar_menu_principal()

def listar_restaurantes():
    '''Exibe os restaurantes cadastrados na lista de restaurante.
    
    Outputs:
    - lista_restaurantes (list): Uma lista de restaurantes cadastrados no programa
    '''
    exibir_subtitulo('Lista de restaurantes cadastrados:')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in lista_restaurantes:
        status = '\033[32mAtivo\033[0m' if restaurante['status'] else '\033[31mInativo\033[0m'
        print(f'- {restaurante['nome'].ljust(20)} | {restaurante['categoria'].ljust(20)} | {status}')
    voltar_menu_principal()

def alterar_status_restaurante():
    '''Altera o status de um restaurante.
    
    Inputs:
    - restaurante_escolhido (str) : Nome do resturante
    
    Outputs:
    - Altera o status do restaurante escolhido (bool)
    '''
    exibir_subtitulo('Alterar status restaurante:')
    restaurante_escolhido = input('Digite o nome do restaurante que deseja alterar o status:\n')
    restaurante_encontrado = False

    for restaurante in lista_restaurantes:
        if restaurante_escolhido == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['status'] = not restaurante['status']
            mensagem = f'O restaurante {restaurante_escolhido} foi ativado com sucesso!' if restaurante['status'] else f'O restaurante {restaurante_escolhido} foi desativado com sucesso!'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado!')

    voltar_menu_principal()

def encerrar_programa():
    '''Exibe a mensagem de finalização e encerra o programa.'''
    exibir_subtitulo('Encerrando o programa...')

def opcao_invalida():
    '''Exibe a mensagem de "Opção inválida" e retorna ao menu principal.'''
    print('Opção inválida!')
    voltar_menu_principal()


def main():
    '''Inicia o programa.'''
    os.system('cls')
    exibir_menu_principal()
    escolher_opcao()

if __name__ == '__main__':
    main()