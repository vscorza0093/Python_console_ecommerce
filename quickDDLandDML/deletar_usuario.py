import sqlite3

conexao = sqlite3.connect('python_console_ecommerce')
cursor = conexao.cursor()

cursor.execute('''DELETE FROM usuarios WHERE id > 1''')

conexao.commit()
conexao.close()