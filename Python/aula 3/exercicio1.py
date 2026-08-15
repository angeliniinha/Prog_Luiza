class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


produto1 = Produto("Mouse", 80.0)
produto2 = Produto("Teclado", 150.0)

print("Produto 1:", produto1.nome, "- R$", produto1.preco)
print("Produto 2:", produto2.nome, "- R$", produto2.preco)
