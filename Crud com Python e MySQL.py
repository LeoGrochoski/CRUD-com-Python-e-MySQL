#!/usr/bin/env python
# coding: utf-8

# # CRUD com Python e MySQL

# <img src="https://irias.com.br/blog/wp-content/uploads/2021/02/python-mysql.png" alt="Python e MySQL">
# 
# 
# ## O que é CRUD?
# 
# CRUD é um acrônimo que representa quatro operações básicas realizadas em sistemas de gerenciamento de banco de dados relacionais:
# 
# 1. **Create (Criar)**: Permite a criação de novos registros ou entradas no banco de dados. Em termos simples, é a operação de adicionar informações a um banco de dados.
# 
# 2. **Read (Ler)**: Permite a leitura ou recuperação de informações existentes do banco de dados. Essa operação é usada para visualizar ou obter dados armazenados.
# 
# 3. **Update (Atualizar)**: Permite a modificação de registros ou informações existentes no banco de dados. É a operação usada para fazer alterações em dados já armazenados.
# 
# 4. **Delete (Excluir)**: Permite a remoção de registros ou informações do banco de dados. Essa operação é usada para eliminar dados que não são mais necessários.
# 
# ## Como aplicar?
# 
# O CRUD é uma abordagem fundamental no desenvolvimento de sistemas que envolvem interação com bancos de dados. Ele fornece um conjunto padrão de operações para manipulação de dados, garantindo a integridade e consistência das informações no banco de dados.
# 
# Em resumo, o CRUD é utilizado para criar, ler, atualizar e excluir dados em um sistema, representando as operações essenciais para gerenciar informações em um banco de dados. 
# 
# 
# 

# ## Instalação e preparação

# Primeiramete temos que instalar o conector do mysql. Este comando utiliza a linha de comando pip install para instalar o módulo mysql-connector-python. O "!" é utilizado para executar comandos do sistema diretamente no ambiente Jupyter Notebook.

# In[ ]:


get_ipython().system('pip install mysql-connector-python')


# In[16]:


import mysql.connector


# In[17]:


conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='senha_mysql',
    database='crud_python'
)

cursor = conexao.cursor()


# O código acima importa o módulo mysql.connector que fornece funcionalidades para interagir com bancos de dados MySQL usando Python.
# 
# Em seguida, ele estabelece uma conexão com um banco de dados MySQL local. Os parâmetros fornecidos são:
#     
# host: o endereço do servidor do banco de dados (neste caso, 'localhost' indica que o banco de dados está na mesma máquina).
# user: o nome de usuário usado para autenticar no banco de dados.
# password: a senha associada ao usuário.
# database: o nome do banco de dados ao qual se deseja conectar.
#     
# O código cria um objeto cursor, que é utilizado para executar comandos SQL no banco de dados.

# ### Criando informações no Banco

# In[18]:


# CREATE

NOME_PRODUTO = "chocolate"
VALOR = 15

comando = f'INSERT INTO produtos (NOME_PRODUTO, VALOR) VALUES ("{NOME_PRODUTO}", {VALOR})'

cursor.execute(comando)

conexao.commit() # edita o banco de dados


# ### Lendo informações do banco de dados

# In[ ]:




