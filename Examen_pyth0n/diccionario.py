def main():
    pais_capital = {
        "España": "Madrid",
        "Portugal": "Lisboa",
        "Francia": "París",
        "Reino Unido": "Londres",
        "Irlanda": "Dublín",
        "Italia": "Roma",
        "Grecia": "Atenas",
        "Alemania": "Berlín"
    }

    print("Países:")
    for pais in pais_capital.keys():
        print("-", pais)

    print("\nCapitales:")
    for capital in pais_capital.values():
        print("-", capital)

    pais = input("\n pon el nombre de un país: ")

    if pais in pais_capital:
        capital = pais_capital[pais]
        print(f"La capital de {pais} es {capital}.")
    else:
        print("El país no esta en la lista.")


if __name__ == "__main__":
    main()
