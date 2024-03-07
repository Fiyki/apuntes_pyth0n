def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return fib_sequence

# Ejemplo: Imprimir los primeros 10 números de Fibonacci
n = 10
print(fibonacci(n))
