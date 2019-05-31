### DETERMINAR EL PRECIO DE UN CONJUNTO DE ENTRADAS AL ZOO:
# Hacer un programa que muestre el precio total de las entradas
# de un grupo de personas al zoo. Teniendo en cuenta los siguientes
# precios:
# .- niños de 2 o menos años no pagan.
# .- hasta los 12 años: 14€
# .- jubilados de 65 o mas años: 18€
# .- resto: 23€
#
# El programa pedirá la edad de los componentes del grupo, primero
# pedirá una edad, y sucesivamente los demás. En el momento en que
# se introduzca un 0 se considerará el final y el programa devolverá
# lo siguiente:

# 1 entradas de baby (0€):      0.00€
# 2 entradas de menores (14€): 42.00€
# 3 entradas normales (23€):   46.00€
# 4 entradas jubilados (18€):  18.00€
#                           -----------
#                             106.00€
#
import screen
import ficheros


def es_edad_valida(edad):
    ok = False
    try:
        edades = int(edad)
        if edades >= 0 and edades < 180:
            ok = True
        else:
            screen.locate(20, 1)
            print("{} No es válida.".format(edad))
    except ValueError:
        screen.locate(20, 1)
        print("'{}' No es válida.\n".format(edad))
    return ok


def es_menor_dos(edad):
    lo_es = False
    if edad >0 and edad <= 2:
        lo_es = True
    return lo_es


def es_menor_doce(edad):
    lo_es = False
    if edad > 2 and edad <= 12:
        lo_es = True
    return lo_es


def es_jubilado(edad):
    lo_es = False
    if edad >= 65 and edad < 180:
        lo_es = True
    return lo_es


def es_entrada_normal(edad):
    lo_es = False
    if edad > 12 and edad < 65:
        lo_es = True
    return lo_es


def introduccion_edad():
    ok = False
    screen.clear_keepcoding()
    while not ok:
        screen.locate(1, 1)
        print()
        print("Programa Zoo.")
        print("-------------\n")
        screen.clear_line()
        edad = input("Introduzca edad: ")
        if es_edad_valida(edad):
            ok = True
            edad_numero = (int(edad))

    return edad_numero


def intro_edad():
    ok = False
    while not ok:
        #screen.muestra_por_pantalla(factura)
        screen.locate(5, 1)
        screen.clear_line()
        edad = input("Introduzca la edad: ")
        if es_edad_valida(edad):
            ok = True
            edad_num = int(edad)
    return edad_num


def salir_programa(es_salir):
    if es_salir == 0:
        return True
    else:
        return False


def obtener_precio(edad):
    menores = 0
    jovenes = 14
    jubilad = 18
    normal  = 23
    error = -1

    if es_entrada_normal(edad):
        return normal
    elif es_menor_doce(edad):
        return jovenes
    elif es_menor_dos(edad):
        return menores
    elif es_jubilado(edad):
        return jubilad
    else:
        return error


def main():
    fact = dict()
    salir = False
    testigo = False
    while not salir:
        screen.muestra_por_pantalla(fact)
        edad = intro_edad()
        if not salir_programa(edad):
            if not testigo:
                fact = {
                    0: 0,
                    14: 0,
                    18: 0,
                    23: 0,
                 }
                testigo = True
            if obtener_precio(edad) in fact:
                fact[obtener_precio(edad)] += 1
            else:
                fact[obtener_precio(edad)] = 1
        else:
            salir = True

    if len(fact) != 0:
        registros = "{};{};{};{}\n".format(fact[0], fact[14], fact[18], fact[23])
        ficheros.guarda_registros(registros)
        y = 0
        baby = 0
        normal = 0
        joven = 0
        jubi = 0
        f_entradas = open("transacciones.txt", 'r')
        linea = f_entradas.readline()
        while linea != "":
            entradas = linea.split(";")
            for element in entradas:
                if y == 0:
                    baby = baby + int(element)
                    y += 1
                elif y == 1:
                    joven = joven + int(element)
                    y += 1
                elif y == 2:
                    jubi = jubi + int(element)
                    y += 1
                elif y == 3:
                    normal = normal + int(element)
                    y = 0
            linea = f_entradas.readline()

        screen.imprime("Totales: ", linea=17, columna=1)
        screen.imprime("Baby[{}]; Joven[{}]; Jubilad@s[{}]; Normal[{}]".format(baby, joven, jubi, normal), linea=18,
                       columna=1)
        f_entradas.close()
        screen.locate(20, 1)
        screen.clear_line()
        screen.locate(20, 20)
        print("Gracias por usar Zoo.\n")
    else:
        screen.clear()
        screen.locate(1, 25)
        print("Gracias por usar Zoo.\n")


if __name__ == "__main__":
    main()
