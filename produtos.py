class produtos:
    def __init__(self, produto, codigo, preço) -> None:
        self.produto = produto
        self.codigo = codigo
        self.preço = preço



produto = produtos('hamburger', '001', '10,00')
print(produto.preço)
print(produto.produto)
print(produto.codigo)