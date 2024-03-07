def contar(frase, letra):
    cuenta = 0
    for caracter in frase:
        if caracter == letra:
            cuenta += 1
    return cuenta


def main():
    frase = input("Ingrese una frase: ")
    letra = input("Ingrese una letra que este en la frase: ")

    veces = contar(frase, letra)

    print(f"Frase: '{frase}' Letra: '{letra}'")
    print(f"La letra '{letra}' aparece {veces} veces en la frase '{frase}'.")


if __name__ == "__main__":
    main()
