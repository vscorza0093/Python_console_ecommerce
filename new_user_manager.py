import sqlite3
from datetime import datetime

conexao = sqlite3.connect('python_console_ecommerce')
cursor = conexao.cursor()

def GetUserInfo():
    print ("Digite seu nome:")
    nome = input()
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
    id = 2
    tipo_usuario = 1
    SetUserData(nome, email, senha, endereco, estado, data_cadastro, id, tipo_usuario)

def SetUserData(nome, email, senha, endereco, estado, data_cadastro, id, tipo_usuario):
    print(f"Usuário {nome} cadastrado com sucesso")
    cursor.execute('''INSERT INTO usuarios (nome, email, senha, endereco, estado, data_cadastro, id, tipo_usuario)
                        VALUES (?,?,?,?,?,?,?,?)''',
                   (nome, email, senha, endereco, estado, data_cadastro, id, tipo_usuario));
    conexao.commit()
    conexao.close()