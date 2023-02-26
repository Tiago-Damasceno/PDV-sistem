import pyodbc

dados_conexão = (
    "Driver={SQL Server};"
    "Server=SQLEXPRESS;"
    "Database=db_PDV;"
)

conexão = pyodbc.connect(dados_conexão)
print("conexão bem sucedida")























# 1 criar uma lista de produtos
# 2 colocar preços e codigos a essa lista
# 3 hospedar essa lista em uma classe (SE POSSIVEL A PESSOA
# PODE FAZER A PROPRIA CLASSE)
# 4 fazer um banco de dados atualizavel para essa lista.
# 5 criar uma interface para melhor visualização dessa lista
# 6 criar um sistema de cadastro de usuario.
# criar um banco de imagens (talves fazer um banco de upload)
# 
