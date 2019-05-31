class Termometro():
    def __init__(self):
        self.__centigrados = 0
        self.__fahrenheit = 0

    def pasar_a_centigrados(self, farh):
        return "{} Cº".format((farh - 32) * 5/9)

    def pasar_a_farhenheit(self, centi):
        return "{} Fº".format((centi * 9/5) + 32)


termo = Termometro()
print("{}".format(termo.pasar_a_centigrados(99)))
print("{}".format(termo.pasar_a_farhenheit(35)))
