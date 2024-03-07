import random

enteros = [random.randint(1, 100) for _ in range(50)]

print("elementos de mi lista: ", enteros)

print("cantidad de elementos: ", len(enteros))

multiplos3_7 = [numero for numero in enteros if numero % 3 == 0 or numero % 7 == 0]

print("elementos multiplos de 3 o 7: ", multiplos3_7)
print("numero de elementos: ", len(multiplos3_7))

repes = set([numero for numero in multiplos3_7 if multiplos3_7.count(numero) > 1])
print("elementos repetidos: ", repes)
