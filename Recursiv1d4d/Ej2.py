print("Ejercicio 2a")


def numerosNaturales(n):
    if n > 0:
        numerosNaturales(n - 1)
        print(n)


numerosNaturales(5)
print()

