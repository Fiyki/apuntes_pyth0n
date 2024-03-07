def potencia(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b % 2 == 0:
        return potencia(a, b // 2) * potencia(a, b // 2)
    else:
        return potencia(a, b // 2) * potencia(a, b // 2) * a


print(potencia(4, 6))
