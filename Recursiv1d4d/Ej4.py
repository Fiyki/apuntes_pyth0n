print("Ejercicio 4.")


def division(a, b):
    if a < b:
        return 0
    else:
        print(a, b)
        return 1 + division(a - b, b)


print(division(12, 2))