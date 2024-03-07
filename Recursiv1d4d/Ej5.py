def producto(a, b):
    if b == 0:
        return 0
    else:
        print(a, b)
        return a + producto(a, b - 1)


print(producto(7, 4))
