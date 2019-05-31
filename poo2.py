class Perro():
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def ladrar(self):
        if self.peso >= 8:
            return "GUAU, GUAU"
        else:
            return "guau, guau"

    def __str__(self):
        return "perro: {}, edad: {}, peso: {}".format(self.nombre, self.edad, self.peso)


class PerroAsistencia(Perro):
    def __init__(self, nombre, edad, peso, amo):
        Perro.__init__(self, nombre, edad, peso)
        self.amo = amo
        self.__trabajando = False

    def __str__(self):
        return "{} y es el perro de asistencia de {}".format(
            Perro.__str__(self), self.amo)

    def pasear(self):
        print("{} ayudo a mi dueño, {} a pasear.".format(self.nombre, self.amo))

    def ladrar(self):
        if self.__trabajando:
            return "shhhh, no puedo ladrar."
        else:
            return Perro.ladrar(self)

    def trabajando(self, valor=None):
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando = valor


def main():
    salchicho = Perro("Salchicho", 3, 12)
    lola = Perro("Lola", 8, 3)
    rantamplan = PerroAsistencia("Rantamplan", 5, 10, "Lucky Luck")

    print("Salchicho ladra así: '{}'".format(salchicho.ladrar()))
    print("y Lola ladra así: '{}'".format(lola.ladrar()))
    print(rantamplan)
    print(salchicho)

    print()
    print(rantamplan.ladrar())
    print("Ahora, {} está trabajando.".format(rantamplan.nombre))
    rantamplan.trabajando(True)
    print(rantamplan.ladrar())


if __name__ == "__main__":
    main()
