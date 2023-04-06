import sqlite3
from datetime import datetime

conexao = sqlite3.connect('../python_console_ecommerce')

cursor = conexao.cursor()

nome = 'vinicius'
email = 'email'
senha = '1234'
endereco = 'rua'
estado = 'sp'
data_atual = datetime.now()
data_cadastro = data_atual.strftime("%d/%m/%Y %H:%M:%S")
id = 1
tipo_usuario = 3


cursor.execute('''INSERT INTO usuarios (nome, email, senha, endereco, estado, data_cadastro, id, tipo_usuario)
                    VALUES (?,?,?,?,?,?,?,?)''', (nome, email, senha, endereco, estado, data_cadastro, id, tipo_usuario))
conexao.commit()
conexao.close()