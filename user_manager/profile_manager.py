import sqlite3

conexao = sqlite3.connect('python_console_ecommerce')
cursor = conexao.cursor()


def GetUserInfo():
    novo_login = (f'''SELECT * FROM usuarios''')
    cursor.execute(novo_login)
    my_result = cursor.fetchall()
    for data in my_result:
        print(data)