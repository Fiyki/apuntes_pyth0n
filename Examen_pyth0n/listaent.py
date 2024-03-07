def generar_lista(n1, n2):
    if n2 < 0:
        return "¡No puedes poner numeros negativos!"
    elif n2 == 0:
        return "AL poner 0 no genero listas"
    else:
        lista = [n1 + i for i in range(n2)]
        return f"Resultado: {lista}"


def main():
    n1 = int(input("Dame un numero: "))
    n2 = int(input("Dime cuántos numeros quieres: "))

    resultado = generar_lista(n1, n2)
    print(resultado)
    print("------------------------------------------------------------------------")


if __name__ == "__main__":
    main()
