class Recursividad:
    def suma(self, n):
        if n < 10:
            return n
        else:
            ultimo = n % 10
            demas = n // 10
            return ultimo + self.suma(demas)

    # b) Escribir un método de clase recursivo que devuelva el número de dígitos
    # de un número natural n ≥ 0 pasado como parámetro.
    def numero(self, n):
        if n < 10:
            return 1
        else:
            resto = n // 10
            return 1 + self.numero(resto)

    def invertir(self, n):
        if n < 10:
            return n
        else:
            ultimo = n % 10
            resto = n // 10
            return int(str(ultimo) + str(self.invertir(resto)))


print("Ejercicio 8, parte 'a'.")
r = Recursividad()
print(r.suma(123))
print()

print("Ejercicio 8, parte 'b'.")
print(r.numero(123))
print()

print("Ejercicio 8, parte 'c'.")
print(r.invertir(123))
