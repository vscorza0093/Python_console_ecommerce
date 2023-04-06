import os
from user_manager import login_manager, new_user_manager
import login_area
import main_menu
from user_manager import profile_manager

app_loop = True

def CheckUserInput(user_input):
    os.system('CLS')
    match user_input:
        case 'm':
            main_menu.OpenMainMenu()
            return True
        case 'e':
            login_area.OpenLoginArea()
            return True
        case 'l':
            login_manager.GetUserLogin()
            return True
        case 'c':
            #new_user_manager.CheckIfNameIsRegistered()
            new_user_manager.GetLastUserId()
            return True
        case 'd':
            login_manager.LogOut()
            return True
        case 'i':
            profile_manager.GetUserInfo()
            return True
        case 's':
            global app_loop
            app_loop = QuitApplication()
            return app_loop
        case 'p':
            return True
        case '':
            print('Comando inválido')
            return True

def QuitApplication():
    print("Obrigado por utilizar o Python console ecommerce")
    return False