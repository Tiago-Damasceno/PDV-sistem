import pyodbc



dadosconnect = "Driver={SQL Server};Server=DESKTOP-L79M8K7\SQLEXPRESS;Database=bd_PDV;"
conexão = pyodbc.connect(dadosconnect)
print("conexão bem sucedida")

cursor = conexão.cursor()
comando = """ INSERT INTO tbl_produtos(id_produtos, nome_produto, preço, quantidade)
	 VALUES (0, 'x-burguer', 10, 01)"""

cursor.execute(comando)
cursor.commit #só é usado para mudanças no banco de dados(adicionar ou retrirar)
#conexão.close()





















# 1 criar uma lista de produtos
# 2 colocar preços e codigos a essa lista
# 3 hospedar essa lista em uma classe (SE POSSIVEL A PESSOA
# PODE FAZER A PROPRIA CLASSE)
# 4 fazer um banco de dados atualizavel para essa lista.
# 5 criar uma interface para melhor visualização dessa lista
# 6 criar um sistema de cadastro de usuario.
# criar um banco de imagens (talves fazer um banco de upload)
# 
