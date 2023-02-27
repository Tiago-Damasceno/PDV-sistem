import pyodbc



dadosconnect = "Driver={SQL Server}; Server=.; Database=bd_PDV;"
conn = pyodbc.connect(driver='{SQL Server}', host='DESKTOP-L79M8K7', database='db_PDV',
                      )
cursor = connection.cursor()
print("Hello, World!")
cursor.close()
connection.close()






















# 1 criar uma lista de produtos
# 2 colocar preços e codigos a essa lista
# 3 hospedar essa lista em uma classe (SE POSSIVEL A PESSOA
# PODE FAZER A PROPRIA CLASSE)
# 4 fazer um banco de dados atualizavel para essa lista.
# 5 criar uma interface para melhor visualização dessa lista
# 6 criar um sistema de cadastro de usuario.
# criar um banco de imagens (talves fazer um banco de upload)
# 
