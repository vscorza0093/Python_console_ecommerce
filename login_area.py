import os
import sqlite3
from user_manager import login_manager
import menu_manager

conexao = sqlite3.connect('python_console_ecommerce')
cursor = conexao.cursor()


def OpenLoginArea():
    os.system('CLS')
    print("Você está na área de Login")
    while menu_manager.app_loop:
        is_logged_in = login_manager.is_logged_in

        print("O que deseja fazer?\n")

        if not is_logged_in:
            print("Menu Principal (M), Cadastrar (C), Login (L), Sair (S):")
        else:
            print("Menu Principal (M), Verificar informações (I), Deslogar (D), Sair (S):")

        user_input = str(input()).lower()
        app_loop = menu_manager.CheckUserInput(user_input)

