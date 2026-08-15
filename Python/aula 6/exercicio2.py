class Instrumento:
    def tocar(self):
        print("Instrumento tocando")


class Violao(Instrumento):
    def tocar(self):
        print("Violão: strum strum")


class Bateria(Instrumento):
    def tocar(self):
        print("Bateria: tum tum pá")


class Piano(Instrumento):
    def tocar(self):
        print("Piano: plim plim")


instrumentos = [Violao(), Bateria(), Piano()]

for instrumento in instrumentos:
    instrumento.tocar()
