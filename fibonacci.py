# Fibonacci bumber module

def fib(n):     # Escreve a serie Fibonacci até n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


def fib2(n):    # Retorna a serie Fibonacci até n em uma lista
    fibo = []
    a, b = 0, 1
    while a < n:
        fibo.append(a)
        a, b = b, a + b
    return fibo

# fib(100)
# print(fib2(100))
