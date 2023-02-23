class usuario:
    def __init__(self, nome, email, senha) -> None:
        self.nome = nome
        self.email = email
        self.senha = senha

user = usuario('tiago', 'tiagodamasceno@gmai.com', 'senha')
print(user.email)
print(user.nome)
print(user.senha)
