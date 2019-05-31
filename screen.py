import os

BACKGROUND_BLACK = '\033[040m'
mensajes = {
    0: 9,
    14: 6,
    18: 5,
    23: 8,
}


# factura = {
#    0: 0,
#    14: 0,
#    18: 0,
#    23: 0,
# }

def clear_line():
    print("\033[K", end="")


def clear_keepcoding():
    print("\033[2j")


def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")
    print()
    # print(BACKGROUND_BLACK)


def locate(linea, columna):
    print("\033[{};{}H".format(linea, columna), end="")


def imprime_por_pantalla():
    clear()
    locate(1, 24)
    print(" Programa Zoo.\n"
          "--------------\n"
          "\n")
    locate(5, 1)
    print("1.-Entradas baby (0€) (x2).........:   0.00€\n"
          "2.-Entradas niñ@s (14€) (x2).......:  28.00€\n"
          "3.-Entradas jubilados (18€) (x2)...:  36.00€\n"
          "4.-Entradas normales (23€) (x2)....:  46.00€\n"
          "--------------------------------------------\n"
          "                         Total (x8): 120.00€\n")


def prueba():
    diccionario = dict()
    print(len(diccionario))


def muestra_por_pantalla(factura):
    clear()
    locate(1, 25)
    print("Programa Zoo.")
    locate(2, 24)
    print("---------------")
    locate(5, 1)
    print("")

    if len(factura) != 0:
        locate(7, 7)
        if factura[0]:
            print("1.- Entradas de Babys (0€) (x{:2}):..........: {:8.2f}€".format(factura[0], factura[0] * 0))
        else:
            print("1.- Entradas de Babys (0€) (x{:2}):..........: {:8.2f}€".format(0, 0))

        locate(8, 7)
        if factura[14]:
            print("2.- Entradas de menores (14€) (x{:2}):.......: {:8.2f}€".format(factura[14], factura[14] * 14))
        else:
            print("2.- Entradas de menores (14€) (x{:2}):.......: {:8.2f}€".format(0, 0))

        locate(9, 7)
        if factura[23]:
            print("3.- Entradas normales (23€) (x{:2}):.........: {:8.2f}€".format(factura[23], factura[23] * 23))
        else:
            print("3.- Entradas normales (23€) (x{:2}):.........: {:8.2f}€".format(0, 0))

        locate(10, 7)
        if factura[18]:
            print("4.- Entradas jubilad@s (18€) (x{:2}):........: {:8.2f}€".format(factura[18], factura[18] * 18))
        else:
            print("4.- Entradas jubilad@s (18€) (x{:2}):........: {:8.2f}€".format(0, 0))

        locate(11, 7)
        print("------------------------------------------------------")
        locate(12, 11)
        if factura:
            total = 0
            t_total = 0
            for x, y in factura.items():
                total = total + y
                t_total = t_total + (x * y)
            print("Total (x{:3})...........................: {:8.2f}€".format(total, t_total))
        else:
            print("Total (x{:3})...........................: {:8.2f}€".format(0, 0))

    else:
        imprime("1.- Entradas de Babys (0€) (x{:2}):..........: {:8.2f}€".format(0, 0), linea=7, columna=7)
        imprime("2.- Entradas de menores (14€) (x{:2}):.......: {:8.2f}€".format(0, 0), linea=8, columna=7)
        imprime("3.- Entradas normales (23€) (x{:2}):.........: {:8.2f}€".format(0, 0), linea=9, columna=7)
        imprime("4.- Entradas jubilad@s (18€) (x{:2}):........: {:8.2f}€".format(0, 0), linea=10, columna=7)
        imprime("------------------------------------------------------", linea=11, columna=7)
        imprime("Total (x{:3})...........................: {:8.2f}€".format(0, 0), linea=12, columna=11)


def imprime(texto, linea, columna):
    locate(linea, columna)
    print(texto)


locate(5, 4)
print("#")
clear()
muestra_por_pantalla(mensajes)
#print("\nPrueba: {}\n".format(prueba()))
