import sqlite3
import os

conexao = sqlite3.connect('python_console_ecommerce')
cursor = conexao.cursor()
is_logged_in = False


def GetUserLogin():
    print("Digite seu nome")
    login = str(input())
    GetUserPassword(login)

def GetUserPassword(login):
    print("Digite sua senha")
    password = input()
    CheckUsernameAndPassword(login,password)

def CheckUsernameAndPassword(login, password):
    novo_login = (f'''SELECT * FROM usuarios''')
    cursor.execute(novo_login)
    my_result = cursor.fetchall()
    for data in my_result:
        if str(login) == str(data[0]):
            if str(password) == str(data[2]):
                WelcomeMessage()
                return
            else:
                print("Login ou senha incorretos")

#def GetUsernameFromDataBase():
#    return 0
#def GetPasswordFromDataBase():
#    return 0

def WelcomeMessage():
    os.system('CLS')
    global is_logged_in
    print("Você chegou ao Python Console Ecommerce")
    is_logged_in = True

def LogOut():
    global is_logged_in
    print("Volte sempre!")
    is_logged_in = False

def GetUserInfo():
    novo_login = (f'''SELECT * FROM usuarios''')
    cursor.execute(novo_login)
    my_result = cursor.fetchall()
    for data in my_result:
        print(data)