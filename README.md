# CRUD com Python e MySQL

<img src="https://irias.com.br/blog/wp-content/uploads/2021/02/python-mysql.png" alt="Python e MySQL" height=400> 

### O que é CRUD?

CRUD é um acrônimo que representa quatro operações básicas realizadas em sistemas de gerenciamento de banco de dados relacionais:
 
1. **Create (Criar)**: Permite a criação de novos registros ou entradas no banco de dados. Em termos simples, é a operação de adicionar informações a um banco de dados.

2. **Read (Ler)**: Permite a leitura ou recuperação de informações existentes do banco de dados. Essa operação é usada para visualizar ou obter dados armazenados.

3. **Update (Atualizar)**: Permite a modificação de registros ou informações existentes no banco de dados. É a operação usada para fazer alterações em dados já armazenados.

4. **Delete (Excluir)**: Permite a remoção de registros ou informações do banco de dados. Essa operação é usada para eliminar dados que não são mais necessários.

### Como aplicar?

O CRUD é uma abordagem fundamental no desenvolvimento de sistemas que envolvem interação com bancos de dados. Ele fornece um conjunto padrão de operações para manipulação de dados, garantindo a integridade e consistência das informações no banco de dados.

Em resumo, o CRUD é utilizado para criar, ler, atualizar e excluir dados em um sistema, representando as operações essenciais para gerenciar informações em um banco de dados. 

 
### Instalação e preparação

Antes de começar é preciso ter o MySQL instalado, os sistemas necessarios são o [MySQL Server](https://dev.mysql.com/downloads/installer/) e o [MySQL Workbench](https://dev.mysql.com/downloads/workbench/). Com eles instalados e tendo em mãos usuario e senha é possivel inico no processo. 

Primeiramete temos que instalar o conector do mysql no notebook. Este comando utiliza a linha de comando **pip install** para instalar o módulo mysql-connector-python. 

O "!" é utilizado para executar comandos do sistema diretamente no ambiente Jupyter Notebook.

~~~

pip install mysql-connector-python

import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Mortadela@24',
    database='crud_python'
)

cursor = conexao.cursor()
~~~

O código acima importa o módulo mysql.connector que fornece funcionalidades para interagir com bancos de dados MySQL usando Python.

Em seguida, ele estabelece uma conexão com um banco de dados MySQL local. Os parâmetros fornecidos são:
    
host: o endereço do servidor do banco de dados (neste caso, 'localhost' indica que o banco de dados está na mesma máquina).
user: o nome de usuário usado para autenticar no banco de dados.
password: a senha associada ao usuário.
database: o nome do banco de dados ao qual se deseja conectar.
    
O código cria um objeto cursor, que é utilizado para executar comandos SQL no banco de dados.

### 1. Criando informações no Banco

~~~

NOME_PRODUTO = "CHOCOLATE"
VALOR = 15

comando = f'INSERT INTO produtos (NOME_PRODUTO, VALOR) VALUES ("{NOME_PRODUTO}", {VALOR})'

cursor.execute(comando)

conexao.commit() 

~~~

Inserindo um segundo produto no banco.

~~~
NOME_PRODUTO = "MOLHO DE TOMATE"
VALOR = 8

comando = f'INSERT INTO produtos (NOME_PRODUTO, VALOR) VALUES ("{NOME_PRODUTO}", {VALOR})'

cursor.execute(comando)

conexao.commit() 
~~~

<img src="/imagens/1. Criando informações no Banco.png">

### 2. Lendo informações do banco de dados

~~~
comando = f'SELECT * FROM produtos'

cursor.execute(comando)
resultado = cursor.fetchall() # ler o banco de dados

print(resultado)
~~~

<img src="" alt="2. Lendo informações do banco de dados" height=300> 


Com este codigo conseguimos ler as informações presentes em nosso banco, e é primordial pois sempre que atuamos no banco seja inserindo, atualizando ou deletando precisamos verificar a situação do banco.

### 3. Atualizando informações no banco de dados

~~~
NOME_PRODUTO = "AGUA C/ GÁS"
VALOR = 4

comando = f'UPDATE produtos SET VALOR = {valor} WHERE NOME_PRODUTO = "{NOME_PRODUTO}"'

cursor.execute(comando)

conexao.commit()
~~~

<img src="" alt="3. Atualizando informações no banco de dados" height=300> 


### 4. Deletando informações do banco de dados

~~~
NOME_PRODUTO = "CHOCOLATE"

comando = f'DELETE FROM produtos WHERE nome_produto = "{NOME_PRODUTO}"'

cursor.execute(comando)

conexao.commit()
~~~

<img src="" alt="4. Deletando informações do banco de dados" height=300> 

Por fim deletar é uma das funções basicas, invariavelmente iremos precisar deletar informações do banco.

Acredito que apesar do comando ser simples e para usuarios mais experientes pode ser até trivial demais, porém o conhecimento em manipulação de bancos de dados é essencial para profissionais da area de dados sejam analistas, engenheiros ou até cientistas. 
E com estas instruções já é possivel realizar a integração entre o MySQL e Jupyter Notebook com python e agora fazer as manipulações CRUD de fora do ambiente do banco. 
