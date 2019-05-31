def suma_todos(limite):
    resultado = 0
    for i in range(0, limite+1):
        resultado += i

    return resultado

def multiplica_todo(limite):
    resultado = 1
    for i in range(1, limite+1):
        resultado = resultado * i

    return resultado


print("Suma todo los numeros: {}".format(suma_todos(100)))
print("Multiplica todo: {}".format(multiplica_todo(10)))
