# CRUD com Python e MySQL


pip install mysql-connector-python


import mysql.connector


conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='senha_mysql',
    database='crud_python'
)

cursor = conexao.cursor()

# 1. Criando informações no Banco

NOME_PRODUTO = "chocolate"
VALOR = 15

comando = f'INSERT INTO produtos (NOME_PRODUTO, VALOR) VALUES ("{NOME_PRODUTO}", {VALOR})'

cursor.execute(comando)

conexao.commit()

NOME_PRODUTO = "MOLHO DE TOMATE"
VALOR = 8

comando = f'INSERT INTO produtos (NOME_PRODUTO, VALOR) VALUES ("{NOME_PRODUTO}", {VALOR})'

cursor.execute(comando)

conexao.commit() 

# 2. Lendo informações do banco de dados

comando = f'SELECT * FROM produtos'

cursor.execute(comando)
resultado = cursor.fetchall() # ler o banco de dados

print(resultado)

# 3. Atualizando informações no banco de dados

NOME_PRODUTO = "AGUA C/ GÁS"
VALOR = 4

comando = f'UPDATE produtos SET VALOR = {valor} WHERE NOME_PRODUTO = "{NOME_PRODUTO}"'

cursor.execute(comando)

conexao.commit()

# 4. Deletando informações do banco de dados

NOME_PRODUTO = "CHOCOLATE"

comando = f'DELETE FROM produtos WHERE nome_produto = "{NOME_PRODUTO}"'

cursor.execute(comando)

conexao.commit()


