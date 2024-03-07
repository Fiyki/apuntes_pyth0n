class Binario:
    def binario(self, n):
        if n == 0:
            return ''
        else:
            return self.binario(n // 2) + str(n % 2)


print("Ejercicio 9")
print()
n = int(input('Ingrese un número natural: '))
valor = Binario()
print(f'El valor binario de {n} es: {valor.binario(n)}')