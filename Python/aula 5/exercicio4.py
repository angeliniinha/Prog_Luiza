class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def apresentar(self):
        print(f"Aluno: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Matrícula: {self.matricula}")
        print()

class Professor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def apresentar(self):
        print(f"Professor: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Salário: R${self.salario:.2f}")
        print()

aluno1 = Aluno("Guilherme", 16, "2025001")
aluno2 = Aluno("Luiza", 17, "2025002")
professor1 = Professor("Angelina", 18, 4500)

pessoas = [aluno1, aluno2, professor1]

for pessoa in pessoas:
    pessoa.apresentar()
