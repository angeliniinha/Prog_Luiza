class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if nome != "":
            self.__nome = nome
        else:
            print("Nome inválido")

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        if 0 <= idade <= 120:
            self.__idade = idade
        else:
            print("Idade inválida")
          
    def apresentar(self):
        print("Nome:", self.__nome)
        print("Idade:", self.__idade)

pessoa = Pessoa("Guilherme", 17)

pessoa.apresentar()

pessoa.set_idade(130)
pessoa.set_nome("")
