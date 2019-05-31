def retrocontador(e):
    if e > 0:
        print("{}, ".format(e), end="")
        retrocontador(e - 1)
    else:
        print("{}".format(e))


def sumatorio(n):
    if n != 0:
        return n + sumatorio(n-1)
    else:
        return n

retrocontador(10)
print("Sumatorio: \n{}".format(sumatorio(10)))
