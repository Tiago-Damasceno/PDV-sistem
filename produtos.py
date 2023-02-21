class produtos:
    def lista_de_produtos(self, produto, codigo, preço):
        self.produto = produto
        self.codigo = codigo
        self.preço = preço



produto = produtos.lista_de_produtos('hamburger', '001', '10,00')
print(produto.preço)
