def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return fib_sequence


def main():
    n = int(input("Introduce el numero de veces que quieres fibo: "))
    print(fibonacci(n))


if __name__ == "__main__":
    main()
