def suma_todo(limite, f):
    resultado = 0
    for i in range(0, limite+1):
        resultado += f(i)

    return resultado


def multiplica_todo(limite):
    resultado = 1
    for i in range(1, limite+1):
        resultado = resultado * i

    return resultado

