import sqlite3
from datetime import datetime
import os
import login_area

conexao = sqlite3.connect('python_console_ecommerce')
cursor = conexao.cursor()
checar_nome = True

def GetLastUserId():
    cursor.execute('''SELECT id FROM usuarios ORDER BY id DESC''')
    my_result = cursor.fetchall()
    last_index = my_result[0][0]
    GetUserInfo(last_index + 1)

def GetUserInfo(last_index):
    os.system('CLS')
    global checar_nome
    while (checar_nome):
        print ("Digite seu nome:")
        nome = input()
        CheckIfNameIsRegistered(nome)
    checar_nome = True
    print ("Digite seu email:")
    email = input()
    print ("Digite sua senha:")
    senha = input()
    print ("Digite seu endereco:")
    endereco = input()
    print ("Digite a sigla do estado:")
    estado = input()
    data_atual = datetime.now()
    data_cadastro = data_atual.strftime("%d/%m/%Y %H:%M:%S")
    id = last_index
    tipo_usuario = 1
    SetUserData(nome, email, senha, endereco, estado, data_cadastro, id, tipo_usuario)

def SetUserData(nome, email, senha, endereco, estado, data_cadastro, id, tipo_usuario):
    os.system('CLS')
    print(f"Usuário {nome} cadastrado com sucesso")
    cursor.execute('''INSERT INTO usuarios (nome, email, senha, endereco, estado, data_cadastro, id, tipo_usuario)
                        VALUES (?,?,?,?,?,?,?,?)''',
                   (nome, email, senha, endereco, estado, data_cadastro, id, tipo_usuario));
    conexao.commit()

def CheckIfNameIsRegistered(nome):
    global checar_nome
    cursor.execute('''SELECT nome FROM usuarios''')
    my_result = cursor.fetchall()

    if nome == "":
        os.system('CLS')
        login_area.OpenLoginArea()

    for data in my_result:
        if str(data[0]) == str(nome):
            checar_nome = True
            print(f"Nome {nome} já está cadastrado")
            return
    checar_nome = False
    return