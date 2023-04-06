import sqlite3
import os
import login_manager
import new_user_manager
import login_area
import main_menu

app_loop = True

def CheckUserInput(user_input):
    match user_input:
        case 'm':
            os.system('CLS')
            main_menu.OpenMainMenu()
            return True
        case 'e':
            os.system('CLS')
            login_area.OpenLoginArea()
            return True
        case 'l':
            os.system('CLS')
            login_manager.GetUserLogin()
            return True
        case 'c':
            os.system('CLS')
            #new_user_manager.CheckIfNameIsRegistered()
            new_user_manager.GetLastUserId()
            return True
        case 'd':
            os.system('CLS')
            login_manager.LogOut()
            return True
        case 'i':
            os.system('CLS')
            login_manager.GetUserInfo()
            return True
        case 's':
            global app_loop
            os.system('CLS')
            app_loop = QuitApplication()
            return app_loop
        case 'p':
            os.system('CLS')
            return True
        case '':
            os.system('CLS')
            print('Comando inválido')
            return True

def QuitApplication():
    print("Obrigado por utilizar o Python console ecommerce")
    return False