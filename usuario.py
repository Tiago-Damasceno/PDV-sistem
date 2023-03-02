class usuario:
    def __init__(self, nome, email, telefone) -> None:
        self.nome = nome
        self.email = email
        self.telefone = telefone

user = usuario('tiago', 'tiagodamasceno@gmai.com', 'senha')
print(user.email)
print(user.nome)
print(user.telefone)
