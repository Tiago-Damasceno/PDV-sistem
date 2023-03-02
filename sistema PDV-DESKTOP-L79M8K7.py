import pyodbc
from produtos import produtos
from usuario import usuario


# Estabelecendo a conexão com o banco de dados
dados_conexao = "Driver={SQL Server};Server=DESKTOP-L79M8K7\SQLEXPRESS;Database=bd_PDV;"
conexão = pyodbc.connect(dados_conexao)
print("Conexão bem sucedida")

# Criando um cursor para executar as consultas SQL
cursor = conexão.cursor()

# Inserindo um registro na tabela "tbl_produtos"
# Os nomes das colunas precisam estar entre parênteses e em ordem correspondente aos valores que estão sendo inseridos
#produto = produtos('xburguer',3 , 12, 2)
#produto3 = produtos('xbacon', '5', '15', '1')
cliente = usuario('paula', '12345', 'paula@gmail.com' )
cursor.execute("INSERT INTO tbl_clientes (nome_cliente, telefone, email_cliente) VALUES (?, ?, ?)", 
                (cliente.nome, cliente.email, cliente.telefone))

# Salvando as mudanças no banco de dados
conexão.commit()

# Fechando o cursor e a conexão
cursor.close()
conexão.close()

#print("conexão bem sucedida")
#cursor.close()
#connection.close()






















# 1 criar uma lista de produtos
# 2 colocar preços e codigos a essa lista
# 3 hospedar essa lista em uma classe (SE POSSIVEL A PESSOA
# PODE FAZER A PROPRIA CLASSE)
# 4 fazer um banco de dados atualizavel para essa lista.
# 5 criar uma interface para melhor visualização dessa lista
# 6 criar um sistema de cadastro de usuario.
# criar um banco de imagens (talves fazer um banco de upload)

