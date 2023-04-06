import sqlite3
import login_manager
import new_user_manager

conexao = sqlite3.connect('python_console_ecommerce')
cursor = conexao.cursor()
app_loop = True

def CheckUserInput(user_input):
    match user_input:
        case 'l':
            login_manager.GetUserLogin()
        case 'c':
            new_user_manager.GetUserInfo()
        case 'd':
            login_manager.LogOut()
        case 'i':
            login_manager.GetUserInfo()
        case 's':
            QuitApplication()

def QuitApplication():
    global app_loop
    app_loop = False
    print("Obrigado por utilizar o Python console ecommerce")

while app_loop:
    is_logged_in = login_manager.is_logged_in

    print("O que deseja fazer?\n")

    if (is_logged_in == False):
        print("Cadastrar (C), Login (L), Sair (S):")
    else:
        print("Verificar informações (I), Deslogar (D), Sair (S):")

    user_input = str(input()).lower()
    CheckUserInput(user_input)

