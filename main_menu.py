import login_manager
import menu_manager
import os


def OpenMainMenu():
    os.system('CLS')
    print("Você está no menu principal")
    while menu_manager.app_loop:
        is_logged_in = login_manager.is_logged_in

        print("O que deseja fazer?\n")

        if (is_logged_in == False):
            print("Listar Produtos (P), Entrar/Cadastrar (E), Sair (S):")
        else:
            print("Listar Produtos (P), Verificar informações (I), Deslogar (D), Sair (S):")

        user_input = str(input()).lower()
        app_loop = menu_manager.CheckUserInput(user_input)