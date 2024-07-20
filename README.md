# Sabor Express: Sistema de gerenciamento de restaurantes

Este projeto, desenvolvido no curso "Python: Crie sua primeira aplicação" da Alura durante o processo seletivo "Geração Caldeira",  tem como objetivo apresentar um sistema simples de gerenciamento de restaurantes utilizando a linguagem Python. 

## Funcionalidades:

* **Cadastrar restaurantes:** Permite adicionar novos restaurantes à lista, incluindo nome e categoria.
* **Listar restaurantes:** Exibe os restaurantes cadastrados, incluindo nome, categoria e status (ativo/inativo).
* **Ativar/Desativar restaurantes:** Altera o status de um restaurante, permitindo que ele seja ativado ou desativado.

## Tecnologias utilizadas

* Python

## Como usar:

1. **Executar o código:** Execute o arquivo Python (SaborExpress.py) usando um interpretador Python.
2. **Interagir com o menu:** O menu principal irá apresentar as opções disponíveis:
    * **Cadastrar restaurante:** Opção para adicionar um novo restaurante.
    * **Listar restaurantes:** Opção para visualizar os restaurantes cadastrados.
    * **Ativar restaurante:** Opção para ativar um restaurante.
    * **Sair:** Opção para encerrar o programa.
3. **Selecionar uma opção:** Digite o número correspondente à opção desejada e pressione Enter.
4. **Seguir as instruções:** Siga as instruções para cada opção e forneça os dados necessários.
5. **Voltar ao menu principal:** Após concluir uma operação, você será redirecionado ao menu principal para escolher uma nova opção.

## Estrutura do código:

O código é organizado em diversas funções, cada uma com uma responsabilidade específica:

* **`exibir_menu_principal()`**: Exibe o menu principal do programa.
* **`escolher_opcao()`**: Lê a opção escolhida pelo usuário e executa a função correspondente.
* **`voltar_menu_principal()`**: Retorna o usuário ao menu principal após a execução de uma opção.
* **`exibir_subtitulo()`**: Exibe um subtítulo para cada funcionalidade do programa.
* **`cadastrar_novo_restaurante()`**: Permite cadastrar um novo restaurante.
* **`listar_restaurantes()`**: Lista os restaurantes cadastrados.
* **`alterar_status_restaurante()`**: Altera o status de um restaurante.
* **`encerrar_programa()`**: Exibe a mensagem de encerramento e finaliza o programa.
* **`opcao_invalida()`**: Exibe uma mensagem de erro para opções inválidas.
* **`main()`**: Função principal que inicia o programa.

## Observações:

* O código utiliza uma lista `lista_restaurantes` para armazenar os dados dos restaurantes cadastrados.
* As cores do status "Ativo" e "Inativo" são definidas utilizando escape codes ANSI para melhor visualização.
* O código utiliza o módulo `os` para limpar a tela antes de exibir cada subtítulo.