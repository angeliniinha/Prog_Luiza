class Sensor:
    def __init__(self, temperatura):
        self.__temperatura = 0
        self.set_temperatura(temperatura)

    def get_temperatura(self):
        return self.__temperatura

    def set_temperatura(self, temperatura):
        if -50 <= temperatura <= 150:
            self.__temperatura = temperatura
        else:
            print("Temperatura inválida")

    def status(self):
        if -50 <= self.__temperatura <= 80:
            return "Normal"
        elif 81 <= self.__temperatura <= 120:
            return "Alerta"
        else:
            return "Critico"

sensor1 = Sensor(25)
print(sensor1.get_temperatura(), "-", sensor1.status())

sensor2 = Sensor(90)
print(sensor2.get_temperatura(), "-", sensor2.status())

sensor3 = Sensor(130)
print(sensor3.get_temperatura(), "-", sensor3.status())

sensor4 = Sensor(-10)
print(sensor4.get_temperatura(), "-", sensor4.status())
