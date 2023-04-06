import sqlite3

conexao = sqlite3.connect('../python_console_ecommerce')

cursor = conexao.cursor()
usuarios = ('''CREATE TABLE usuarios 
                    (nome VARCHAR (100) NOT NULL,
                    email VARCHAR (50) NOT NULL,
                    senha VARCHAR (20) NOT NULL,
                    endereco VARCHAR (150) NOT NULL,
                    estado VARCHAR (2) NOT NULL,
                    data_cadastro VARCHAR (10),
                    id INTEGER UNIQUE,
                    tipo_usuario INTEGER);
''')

produto = ('''CREATE TABLE produto
                (nome_produto VARCHAR (100) NOT NULL UNIQUE,
                marca VARCHAR(100) NOT NULL,
                modelo VARCHAR(100) NOT NULL UNIQUE,
                valor_produto FLOAT NOT NULL,
                quantidade_estoque INTEGER NOT NULL,
                id INTEGER NOT NULL UNIQUE,
                categoria_id INTEGER NOT NULL,
                    FOREIGN KEY (categoria_id) REFERENCES categoria (categoria_id));
''')

categoria = ('''CREATE TABLE categoria
                (nome_categoria VARCHAR (100) NOT NULL,
                categoria_id INTEGER PRIMARY KEY);
''')

carrinho_de_compras = ('''CREATE TABLE carrinho_de_compras
                            (id INTEGER NOT NULL PRIMARY KEY,
                            quantidade INTEGER NOT NULL,
                            valor_produto FLOAT NOT NULL,
                            usuario_id INTEGER NOT NULL,
                            produto_id INTEGER NOT NULL, 
                                FOREIGN KEY (usuario_id) REFERENCES usuarios (id),
                                FOREIGN KEY (produto_id) REFERENCES produto (id));
''')
cursor.execute(usuarios)
cursor.execute(produto)
cursor.execute(categoria)
cursor.execute(carrinho_de_compras)

conexao.commit()
conexao.close()



