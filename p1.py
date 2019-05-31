def normal(x):
    return x


def suma_todos(limite, f):
    resultado = 0
    for i in range(limite+1):
        resultado += f(i)

    return resultado


print(suma_todos(100, normal))

