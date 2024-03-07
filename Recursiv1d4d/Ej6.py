def dimitri(a, b):
    if b == 0:
        return 0
    elif b % 2 == 0:
        return dimitri(a * 2, b // 2)
    else:
        return a + dimitri(a * 2, b // 2)


print(dimitri(5, 3))