def es_bisiesto(anyo):
    return (anyo % 4 == 0 and anyo % 100 != 0) or (anyo % 400 == 0)


def numbisiestos(anyo1, anyo2):
    bisiestos = sum(1 for year in range(anyo1, anyo2 + 1) if es_bisiesto(year))
    intervalo_dias = (anyo2 - anyo1 + 1) * 365 + bisiestos

    return bisiestos, intervalo_dias


anyo1 = int(input("Dame un año: "))
anyo2 = int(input("Dame un segundo año: "))

bisiestos, dias_totales = numbisiestos(anyo1, anyo2)
print(
    f"Entre {anyo1} y {anyo2} (ambos incluidos) hubo/hay/habrá {bisiestos} años bisiestos y un total de {dias_totales} días.")
