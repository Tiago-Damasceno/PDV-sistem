class produtos:
    def __init__(self, nome, codigo, preço, quantidade) -> None:
        self.codigo = codigo
        self.nome = nome
        self.preço = preço
        self.quantidade = quantidade


produto = produtos('hamburger', '001', '10,00', '2')
print(produto.preço)
print(produto.nome)
print(produto.codigo)
print(produto.quantidade)