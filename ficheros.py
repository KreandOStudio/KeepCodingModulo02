nombre_fichero = "transacciones.txt"
tipo_acceso = None


def guarda_registros(datos):
    fich = open("transacciones.txt", "a+")
    fich.write(datos)
    fich.close()


def devuelve_linea():
    fich = open(nombre_fichero, "r")
    linea = fich.readline()
    fich.close()
    return linea

