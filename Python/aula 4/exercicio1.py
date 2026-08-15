class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    # Getter nome
    def get_nome(self):
        return self.__nome

    # Setter nome
    def set_nome(self, nome):
        self.__nome = nome

    # Getter preço
    def get_preco(self):
        return self.__preco

    # Setter preço
    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco
        else:
            print("Preço inválido")

produto = Produto("Mouse", 100)

print(produto.get_nome())
print(produto.get_preco())

produto.set_preco(150)
print(produto.get_preco())

produto.set_preco(-50)
